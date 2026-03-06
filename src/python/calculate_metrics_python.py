"""
DHI Feature Extraction Pipeline — Python implementation.

Computes time-series complexity metrics on 5-minute averaged heart rate
data from THEW Holter recordings.  Mirrors the R pipeline in
src/R/calculate_metrics.R.

DESIGN RULE: Every feature function takes a plain numpy array (the time
series) as input, NOT a participant dict.  The loop over participants
happens in a separate wrapper function.  This allows the same feature
function to be called on raw HR or residual series.
"""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import Any

import warnings

import antropy as ant
import nolds
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.signal import periodogram
from scipy.spatial.distance import pdist, squareform
from sklearn.decomposition import PCA
from statsmodels.tsa.stattools import acf

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
_PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = _PROJECT_ROOT / "data_processed" / "thew" / "hr_timeseries_1min" / "panel_24h_wearable5.csv"
META_PATH = _PROJECT_ROOT / "data_processed" / "thew" / "hr_timeseries_1min" / "clinical_metadata_all.csv"

EXPECTED_POINTS = 288        # 24 h at 5-min resolution: 0, 5, …, 1435
TIME_STEP = 5               # minutes
MIN_COVERAGE = 0.90         # require >= 90 % of expected time points
MAX_GAP_POINTS = 12         # max contiguous missing before exclusion (12 × 5 min = 60 min)


# ---------------------------------------------------------------------------
# Data loading & QC
# ---------------------------------------------------------------------------

def _max_contiguous_missing(present: np.ndarray) -> int:
    """Return the length of the longest run of False in a boolean array."""
    if present.all():
        return 0
    missing = ~present
    # Diff trick: find run lengths of consecutive True in `missing`
    changes = np.diff(missing.astype(int))
    starts = np.where(changes == 1)[0] + 1
    ends = np.where(changes == -1)[0] + 1
    # Handle edge cases where the run starts at index 0 or ends at the last index
    if missing[0]:
        starts = np.concatenate([[0], starts])
    if missing[-1]:
        ends = np.concatenate([ends, [len(missing)]])
    if len(starts) == 0:
        return 0
    return int((ends - starts).max())


def load_data(
    path: Path | None = None,
    meta_path: Path | None = None,
) -> dict[str, dict[str, Any]]:
    """Load 5-min HR panel data, apply QC, and return per-participant arrays.

    Parameters
    ----------
    path : Path, optional
        Path to the panel CSV (default: DATA_PATH).
    meta_path : Path, optional
        Path to the clinical metadata CSV (default: META_PATH).

    Returns
    -------
    dict[str, dict]
        Keyed by participant ``id``.  Each value is a dict with keys:
        - ``'time'``  : numpy array of time in minutes (length EXPECTED_POINTS)
        - ``'hr'``    : numpy array of avg_hr values (interpolated where needed)
        - ``'condition'`` : str — one of Healthy, CAD, CAD+DM, ESRD
    """
    path = path or DATA_PATH
    meta_path = meta_path or META_PATH

    # --- read data -----------------------------------------------------------
    panel = pd.read_csv(path)
    meta = pd.read_csv(meta_path, usecols=["id", "DIABETES"])

    # --- derive condition4 (split CAD by diabetes status) --------------------
    panel = panel.merge(meta[["id", "DIABETES"]], on="id", how="left")
    panel["condition4"] = panel["condition"]
    cad_dm_mask = (panel["condition"] == "CAD") & (panel["DIABETES"].isin([1, 2]))
    panel.loc[cad_dm_mask, "condition4"] = "CAD+DM"

    # --- filter to valid rows ------------------------------------------------
    panel["valid"] = panel["valid"].astype(str).str.strip().str.lower() == "true"
    panel_valid = panel.loc[panel["valid"]].copy()

    # --- full expected time grid ---------------------------------------------
    full_time = np.arange(0, EXPECTED_POINTS * TIME_STEP, TIME_STEP)  # 0, 5, …, 1435

    # --- per-participant QC & interpolation -----------------------------------
    participants: dict[str, dict[str, Any]] = {}
    ids = panel["id"].unique()

    n_excluded_coverage = 0
    n_excluded_gap = 0
    excluded_ids_coverage: list[str] = []
    excluded_ids_gap: list[str] = []

    for pid in ids:
        subj = panel_valid.loc[panel_valid["id"] == pid]
        condition = panel.loc[panel["id"] == pid, "condition4"].iat[0]

        # Map valid time points onto the full grid
        valid_times = set(subj["t"].values)
        present = np.array([t in valid_times for t in full_time])
        n_present = present.sum()

        # QC 1: coverage
        if n_present < MIN_COVERAGE * EXPECTED_POINTS:
            n_excluded_coverage += 1
            excluded_ids_coverage.append(pid)
            continue

        # QC 2: max contiguous gap
        max_gap = _max_contiguous_missing(present)
        if max_gap > MAX_GAP_POINTS:
            n_excluded_gap += 1
            excluded_ids_gap.append(pid)
            continue

        # Build HR array on full grid, interpolate missing
        hr_lookup = dict(zip(subj["t"].values, subj["avg_hr"].values))
        hr_observed_times = np.array([t for t in full_time if t in valid_times])
        hr_observed_vals = np.array([hr_lookup[t] for t in hr_observed_times])
        hr_full = np.interp(full_time, hr_observed_times, hr_observed_vals)

        participants[pid] = {
            "time": full_time.copy(),
            "hr": hr_full,
            "condition": condition,
        }

    # --- report exclusions ---------------------------------------------------
    n_total = len(ids)
    n_kept = len(participants)
    print(f"Loaded {n_total} participants from {path.name}")
    print(f"  Excluded {n_excluded_coverage} for < {MIN_COVERAGE*100:.0f}% coverage"
          f" (< {int(MIN_COVERAGE * EXPECTED_POINTS)} of {EXPECTED_POINTS} points)")
    print(f"  Excluded {n_excluded_gap} for contiguous gap > {MAX_GAP_POINTS * TIME_STEP} min"
          f" (> {MAX_GAP_POINTS} consecutive missing)")
    print(f"  Kept {n_kept} participants ({n_kept/n_total*100:.1f}%)")

    return participants


# ---------------------------------------------------------------------------
# Circadian decomposition
# ---------------------------------------------------------------------------

def _cosinor_model(t: np.ndarray, mesor: float, amplitude: float, acrophase: float) -> np.ndarray:
    """Single-harmonic cosinor: HR(t) = M + A * cos(2π * t/1440 - φ)."""
    return mesor + amplitude * np.cos(2 * np.pi * t / 1440 - acrophase)


def _cosinor_model_2h(
    t: np.ndarray,
    mesor: float, amp1: float, acro1: float,
    amp2: float, acro2: float,
) -> np.ndarray:
    """Two-harmonic cosinor: HR(t) = M + A1·cos(2πt/1440 - φ1) + A2·cos(2πt/720 - φ2)."""
    return (mesor
            + amp1 * np.cos(2 * np.pi * t / 1440 - acro1)
            + amp2 * np.cos(2 * np.pi * t / 720 - acro2))


def fit_cosinor_single(
    t: np.ndarray,
    hr: np.ndarray,
    participant_id: str = "unknown",
) -> dict[str, Any]:
    """Fit a single-harmonic cosinor model to one participant's 24h HR series.

    Model: HR(t) = M + A * cos(2π * t/1440 - φ) + ε

    Parameters
    ----------
    t : np.ndarray
        Time in minutes (e.g., 0, 5, 10, ..., 1435).
    hr : np.ndarray
        Heart rate values corresponding to each time point.
    participant_id : str
        Used in warning messages on convergence failure.

    Returns
    -------
    dict with keys:
        - mesor: fitted M (24h mean level)
        - amplitude_24h: fitted A (strength of diurnal swing), constrained >= 0
        - acrophase_24h: fitted φ converted to hours (0-24 scale, time of peak)
        - r_squared_1h: R² goodness-of-fit (1 - SS_res / SS_tot)
        - residuals: np.ndarray of hr - fitted values (for downstream passes)
    """
    nan_result: dict[str, Any] = {
        "mesor": np.nan,
        "amplitude_24h": np.nan,
        "acrophase_24h": np.nan,
        "r_squared_1h": np.nan,
        "residuals": np.full_like(hr, np.nan, dtype=float),
    }

    try:
        p0 = [np.mean(hr), (np.max(hr) - np.min(hr)) / 2, np.pi]
        bounds = ([30, 0, 0], [200, 100, 2 * np.pi])
        popt, _ = curve_fit(_cosinor_model, t, hr, p0=p0, bounds=bounds, maxfev=10000)
    except (RuntimeError, ValueError) as e:
        warnings.warn(f"Cosinor fit failed for {participant_id}: {e}")
        return nan_result

    mesor, amplitude, acrophase_rad = popt
    fitted = _cosinor_model(t, *popt)
    residuals = hr - fitted

    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((hr - np.mean(hr)) ** 2)
    r_squared = float(1 - ss_res / ss_tot) if ss_tot > 0 else np.nan

    # Convert acrophase from radians to hours (0-24)
    acrophase_hours = float((acrophase_rad / (2 * np.pi)) * 24) % 24

    return {
        "mesor": float(mesor),
        "amplitude_24h": float(amplitude),
        "acrophase_24h": acrophase_hours,
        "r_squared_1h": r_squared,
        "residuals": residuals,
    }


def fit_cosinor_two_harmonic(
    t: np.ndarray,
    hr: np.ndarray,
    single_fit: dict[str, Any],
    participant_id: str = "unknown",
) -> dict[str, Any]:
    """Fit a two-harmonic cosinor model to one participant's 24h HR series.

    Model: HR(t) = M + A1·cos(2πt/1440 - φ1) + A2·cos(2πt/720 - φ2) + ε

    Uses single-harmonic fit parameters as initial guesses for shared parameters.

    Parameters
    ----------
    t : np.ndarray
        Time in minutes.
    hr : np.ndarray
        Heart rate values.
    single_fit : dict
        Output from ``fit_cosinor_single`` — used to seed M, A1, φ1 initial guesses
        and to compute r_squared_improvement.
    participant_id : str
        Used in warning messages on convergence failure.

    Returns
    -------
    dict with keys:
        - amplitude_12h: fitted A2 (12h harmonic amplitude)
        - acrophase_12h: fitted φ2 converted to hours (0-12 scale)
        - a2_a1_ratio: A2/A1 (NaN if A1 < 1e-6)
        - r_squared_2h: R² of the two-harmonic model
        - r_squared_improvement: r_squared_2h - r_squared_1h
        - fitted_2h: np.ndarray of fitted values (for downstream residuals)
    """
    nan_result: dict[str, Any] = {
        "amplitude_12h": np.nan,
        "acrophase_12h": np.nan,
        "a2_a1_ratio": np.nan,
        "r_squared_2h": np.nan,
        "r_squared_improvement": np.nan,
        "fitted_2h": np.full_like(hr, np.nan, dtype=float),
    }

    # Seed from single-harmonic fit; fall back to defaults if single fit failed
    m0 = single_fit.get("mesor", np.mean(hr))
    a1_0 = single_fit.get("amplitude_24h", (np.max(hr) - np.min(hr)) / 2)
    # Convert acrophase back to radians for initial guess
    acro_hours = single_fit.get("acrophase_24h", np.nan)
    phi1_0 = (acro_hours / 24 * 2 * np.pi) if np.isfinite(acro_hours) else np.pi
    a2_0 = max(a1_0 / 4, 0.5) if np.isfinite(a1_0) else 1.0
    r_sq_1h = single_fit.get("r_squared_1h", np.nan)

    try:
        p0 = [m0, a1_0, phi1_0, a2_0, np.pi]
        bounds = (
            [30, 0, 0, 0, 0],
            [200, 100, 2 * np.pi, 100, 2 * np.pi],
        )
        popt, _ = curve_fit(_cosinor_model_2h, t, hr, p0=p0, bounds=bounds, maxfev=10000)
    except (RuntimeError, ValueError) as e:
        warnings.warn(f"Two-harmonic cosinor fit failed for {participant_id}: {e}")
        return nan_result

    mesor, amp1, acro1_rad, amp2, acro2_rad = popt
    fitted = _cosinor_model_2h(t, *popt)

    ss_res = np.sum((hr - fitted) ** 2)
    ss_tot = np.sum((hr - np.mean(hr)) ** 2)
    r_squared_2h = float(1 - ss_res / ss_tot) if ss_tot > 0 else np.nan

    # Acrophase of 12h component on 0-12 scale
    acrophase_12h = float((acro2_rad / (2 * np.pi)) * 12) % 12

    a2_a1_ratio = float(amp2 / amp1) if amp1 > 1e-6 else np.nan

    r_sq_improvement = (r_squared_2h - r_sq_1h) if np.isfinite(r_sq_1h) else np.nan

    return {
        "amplitude_12h": float(amp2),
        "acrophase_12h": acrophase_12h,
        "a2_a1_ratio": a2_a1_ratio,
        "r_squared_2h": r_squared_2h,
        "r_squared_improvement": r_sq_improvement,
        "fitted_2h": fitted,
    }


def extract_cosinor_features(
    participants: dict[str, dict[str, Any]],
) -> pd.DataFrame:
    """Fit single- and two-harmonic cosinor models to all participants.

    Stores on each participant's dict:
    - ``'residual_1h'``: residuals from single-harmonic fit
    - ``'fitted_2h'``: fitted values from two-harmonic fit (for downstream residuals)

    Returns
    -------
    pd.DataFrame
        Columns: [id, condition, mesor, amplitude_24h, acrophase_24h, r_squared_1h,
                  amplitude_12h, acrophase_12h, a2_a1_ratio, r_squared_2h,
                  r_squared_improvement]
    """
    rows: list[dict[str, Any]] = []
    for pid, pdata in participants.items():
        t, hr = pdata["time"], pdata["hr"]

        # Single-harmonic fit
        single = fit_cosinor_single(t, hr, participant_id=pid)
        pdata["residual_1h"] = single.pop("residuals")

        # Two-harmonic fit (seeded from single-harmonic results)
        two_h = fit_cosinor_two_harmonic(t, hr, single, participant_id=pid)
        pdata["fitted_2h"] = two_h.pop("fitted_2h")

        rows.append({"id": pid, "condition": pdata["condition"], **single, **two_h})
    return pd.DataFrame(rows)


def compute_residuals(participants: dict[str, dict[str, Any]]) -> None:
    """Compute two-harmonic cosinor residuals and store as 'hr_residual'.

    Must be called AFTER ``extract_cosinor_features``, which stores
    ``fitted_2h`` and ``residual_1h`` on each participant dict.

    Fallback chain:
      1. hr - fitted_2h  (two-harmonic residual)
      2. residual_1h     (single-harmonic residual, if 2h fit failed)
      3. hr - mean(hr)   (mean-centered, if both fits failed; flagged)
    """
    n_2h = n_1h = n_mean = 0
    for pid, pdata in participants.items():
        hr = pdata["hr"]
        fitted_2h = pdata.get("fitted_2h")
        residual_1h = pdata.get("residual_1h")

        if fitted_2h is not None and np.isfinite(fitted_2h).all():
            pdata["hr_residual"] = hr - fitted_2h
            n_2h += 1
        elif residual_1h is not None and np.isfinite(residual_1h).all():
            pdata["hr_residual"] = residual_1h
            n_1h += 1
        else:
            pdata["hr_residual"] = hr - np.nanmean(hr)
            pdata["residual_fallback"] = True
            n_mean += 1

    print(f"\nResidual computation: {n_2h} two-harmonic, "
          f"{n_1h} single-harmonic fallback, {n_mean} mean-centered fallback")
    if n_mean > 0:
        flagged = [pid for pid, p in participants.items()
                   if p.get("residual_fallback")]
        warnings.warn(
            f"{n_mean} participant(s) used mean-centered fallback: {flagged}"
        )


def compute_cv(series: np.ndarray) -> float:
    """Coefficient of variation: std / |mean|. Returns NaN if mean ≈ 0."""
    m = np.nanmean(series)
    if abs(m) < 1e-10:
        return np.nan
    return float(np.nanstd(series) / abs(m))


# ---------------------------------------------------------------------------
# Nonparametric circadian features
# ---------------------------------------------------------------------------

def compute_intradaily_variability(series: np.ndarray) -> float:
    """Intradaily variability (IV) — rhythm fragmentation metric.

    IV = (N * sum_of_squared_first_differences) /
         ((N-1) * sum_of_squared_deviations_from_mean)

    Reference: Van Someren et al., Chronobiology International, 1999.
    """
    n = len(series)
    mean_val = series.mean()
    ss_dev = np.sum((series - mean_val) ** 2)
    if ss_dev == 0:
        return np.nan
    ss_diff = np.sum(np.diff(series) ** 2)
    return float(n * ss_diff / ((n - 1) * ss_dev))


def compute_nonparametric_circadian(
    t: np.ndarray,
    hr: np.ndarray,
) -> dict[str, float]:
    """Nonparametric circadian features from one participant's 24h HR series.

    Parameters
    ----------
    t : np.ndarray
        Time in minutes (e.g., 0, 5, 10, ..., 1435).
    hr : np.ndarray
        Heart rate values corresponding to each time point.

    Returns
    -------
    dict with keys:
        - peak_hr, trough_hr, peak_trough_diff: from 1h-smoothed profile
        - time_of_peak, time_of_trough: hours (0-24) of peak/trough
        - dip_duration: hours where raw HR < 25th percentile
        - dip_sharpness_descent: steepest descent slope (bpm/hour, negative)
        - dip_sharpness_ascent: steepest ascent slope (bpm/hour, positive)
        - iv: intradaily variability (computed on raw series)
    """
    # 1h centered moving average (12 points at 5-min resolution)
    smoothed = pd.Series(hr).rolling(12, center=True, min_periods=1).mean().values

    # Peak and trough from smoothed profile
    peak_idx = int(np.argmax(smoothed))
    trough_idx = int(np.argmin(smoothed))
    peak_hr = float(smoothed[peak_idx])
    trough_hr = float(smoothed[trough_idx])
    peak_trough_diff = peak_hr - trough_hr
    time_of_peak = float(t[peak_idx] / 60)
    time_of_trough = float(t[trough_idx] / 60)

    # Dip duration: hours where raw HR < 25th percentile
    q25 = np.percentile(hr, 25)
    n_below = int(np.sum(hr < q25))
    dip_duration = float(n_below * TIME_STEP / 60)

    # Dip sharpness from first derivative of smoothed profile
    # Convert from bpm/sample to bpm/hour: divide by TIME_STEP (min), multiply by 60
    deriv = np.diff(smoothed) * (60 / TIME_STEP)
    dip_sharpness_descent = float(np.min(deriv))
    dip_sharpness_ascent = float(np.max(deriv))

    # IV on raw series
    iv = compute_intradaily_variability(hr)

    return {
        "peak_hr": peak_hr,
        "trough_hr": trough_hr,
        "peak_trough_diff": peak_trough_diff,
        "time_of_peak": time_of_peak,
        "time_of_trough": time_of_trough,
        "dip_duration": dip_duration,
        "dip_sharpness_descent": dip_sharpness_descent,
        "dip_sharpness_ascent": dip_sharpness_ascent,
        "iv": iv,
    }


def extract_nonparametric_features(
    participants: dict[str, dict[str, Any]],
) -> pd.DataFrame:
    """Compute nonparametric circadian features for all participants.

    Returns
    -------
    pd.DataFrame
        Columns: [id, condition, peak_hr, trough_hr, peak_trough_diff,
                  time_of_peak, time_of_trough, dip_duration,
                  dip_sharpness_descent, dip_sharpness_ascent, iv]
    """
    rows: list[dict[str, Any]] = []
    for pid, pdata in participants.items():
        result = compute_nonparametric_circadian(pdata["time"], pdata["hr"])
        rows.append({"id": pid, "condition": pdata["condition"], **result})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Functional PCA (cross-participant)
# ---------------------------------------------------------------------------

def compute_fpca(
    participants: dict[str, dict[str, Any]],
    n_components: int = 3,
) -> tuple[pd.DataFrame, Any]:
    """Functional PCA of 24h HR curves across all participants.

    This is a cross-participant operation: all curves are analyzed together
    to extract the dominant modes of variation in HR shape.

    Uses scikit-fda for B-spline smoothing and FPCA. If scikit-fda is not
    available, returns NaN columns so the rest of the pipeline still runs.

    Parameters
    ----------
    participants : dict
        Output from ``load_data()``.
    n_components : int
        Number of functional principal components to extract (default 3).

    Returns
    -------
    tuple of (pd.DataFrame, FPCA object or None)
        DataFrame with columns [id, fpca_score_1, ..., fpca_score_{n}].
        FPCA object for later inspection/plotting (None on failure).
    """
    pids = list(participants.keys())
    n_participants = len(pids)

    # NaN fallback
    nan_cols = {f"fpca_score_{j+1}": np.nan for j in range(n_components)}
    nan_df = pd.DataFrame([{"id": pid, **nan_cols} for pid in pids])

    # Assemble HR matrix — all on same 288-point grid from load_data()
    hr_matrix = np.array([participants[pid]["hr"] for pid in pids])
    full_time = participants[pids[0]]["time"]

    try:
        from skfda import FDataGrid
        from skfda.preprocessing.dim_reduction import FPCA
        from skfda.preprocessing.smoothing import BasisSmoother
        from skfda.representation.basis import BSplineBasis

        # Create functional data object
        fd = FDataGrid(hr_matrix, grid_points=full_time)

        # B-spline smoothing (n_basis=48 → ~30-min knot spacing)
        basis = BSplineBasis(domain_range=(float(full_time[0]), float(full_time[-1])),
                             n_basis=48)
        smoother = BasisSmoother(basis)
        fd_smooth = smoother.fit_transform(fd)

        # FPCA
        fpca = FPCA(n_components=n_components)
        scores = fpca.fit_transform(fd_smooth)

        # Print variance explained
        print(f"\n  FPCA variance explained:")
        cumvar = 0.0
        for j, v in enumerate(fpca.explained_variance_ratio_):
            cumvar += v
            print(f"    FPC{j+1}: {v:.4f}  (cumulative: {cumvar:.4f})")

        result = pd.DataFrame(
            scores, columns=[f"fpca_score_{j+1}" for j in range(n_components)]
        )
        result.insert(0, "id", pids)
        return result, fpca

    except ImportError:
        warnings.warn("scikit-fda not installed — skipping FPCA. "
                       "Install with: pip install scikit-fda")
        return nan_df, None
    except Exception as e:
        warnings.warn(f"FPCA failed: {e}")
        return nan_df, None


# ---------------------------------------------------------------------------
# Spectral & rhythm features
# ---------------------------------------------------------------------------

def compute_spectral_features(
    series: np.ndarray,
    fs: float = 1 / 5.0,
) -> dict[str, float]:
    """Spectral features from the periodogram of a HR time series.

    Parameters
    ----------
    series : np.ndarray
        Heart rate time series (e.g., 288 points at 5-min resolution).
    fs : float
        Sampling frequency in cycles per minute (default 1/5).

    Returns
    -------
    dict with keys: power_ulf, power_circ, power_meso, power_hf,
                    spectral_entropy, circadian_power_ratio.
    """
    freqs, psd = periodogram(series, fs=fs)

    # Frequency band boundaries (cycles per minute, defined by period)
    f_ulf_upper = 1 / 360       # period > 6 h
    f_circ_lower = 1 / 480      # period 4–8 h
    f_circ_upper = 1 / 240
    f_meso_lower = 1 / 240      # period 1–4 h
    f_meso_upper = 1 / 60
    f_hf_lower = 1 / 60         # period < 1 h

    # Band masks (exclude DC component at freq == 0)
    mask_ulf = (freqs > 0) & (freqs < f_ulf_upper)
    mask_circ = (freqs >= f_circ_lower) & (freqs <= f_circ_upper)
    mask_meso = (freqs > f_meso_lower) & (freqs <= f_meso_upper)
    mask_hf = (freqs > f_hf_lower)

    def _band_power(mask: np.ndarray) -> float:
        if mask.sum() < 2:
            return float(psd[mask].sum()) if mask.any() else 0.0
        return float(np.trapezoid(psd[mask], freqs[mask]))

    power_ulf = _band_power(mask_ulf)
    power_circ = _band_power(mask_circ)
    power_meso = _band_power(mask_meso)
    power_hf = _band_power(mask_hf)

    # Spectral entropy (normalized Shannon entropy of PSD)
    psd_pos = psd[freqs > 0]  # exclude DC
    total = psd_pos.sum()
    if total > 0:
        p = psd_pos / total
        p = p[p > 0]
        spectral_entropy = float(-np.sum(p * np.log(p)) / np.log(len(psd_pos)))
    else:
        spectral_entropy = np.nan

    # Circadian power ratio
    total_power = power_ulf + power_circ + power_meso + power_hf
    circadian_power_ratio = power_circ / total_power if total_power > 0 else np.nan

    return {
        "power_ulf": power_ulf,
        "power_circ": power_circ,
        "power_meso": power_meso,
        "power_hf": power_hf,
        "spectral_entropy": spectral_entropy,
        "circadian_power_ratio": circadian_power_ratio,
    }


def extract_spectral_and_rhythm_features(
    participants: dict[str, dict[str, Any]],
    series_key: str = "hr",
    col_prefix: str = "",
) -> pd.DataFrame:
    """Compute spectral features for all participants.

    Returns a DataFrame with columns:
        id, condition, power_ulf, power_circ, power_meso, power_hf,
        spectral_entropy, circadian_power_ratio
    """
    rows: list[dict[str, Any]] = []
    for pid, pdata in participants.items():
        spec = compute_spectral_features(pdata[series_key])
        rows.append({"id": pid, "condition": pdata["condition"], **spec})
    df = pd.DataFrame(rows)
    if col_prefix:
        df = df.rename(columns={c: col_prefix + c for c in df.columns
                                if c not in ("id", "condition")})
    return df


# ---------------------------------------------------------------------------
# Complexity features
# ---------------------------------------------------------------------------

def compute_permutation_entropy(
    series: np.ndarray,
    order: int = 3,
    delay: int = 1,
    normalize: bool = True,
) -> float:
    """Permutation entropy of a time series.

    Parameters
    ----------
    series : np.ndarray
        Heart rate time series.
    order : int
        Embedding dimension (default 3).
    delay : int
        Time delay in samples (default 1 = 5-min scale).
    normalize : bool
        If True, normalize to [0, 1].
    """
    return float(ant.perm_entropy(series, order=order, delay=delay, normalize=normalize))


def compute_multidelay_pe(
    series: np.ndarray,
    order: int = 3,
    delays: list[int] | None = None,
) -> dict[str, float]:
    """Permutation entropy at multiple delays + PE slope.

    Delays: τ=1 (5-min), τ=3 (15-min), τ=6 (30-min), τ=12 (1-hour).
    pe_slope: slope of PE vs log(delay), capturing how complexity changes
    across timescales.
    """
    if delays is None:
        delays = [1, 3, 6, 12]
    pe_values = [
        float(ant.perm_entropy(series, order=order, delay=d, normalize=True))
        for d in delays
    ]
    pe_slope = float(np.polyfit(np.log(delays), pe_values, 1)[0])
    result = {f"pe_tau{d}": v for d, v in zip(delays, pe_values)}
    result["pe_slope"] = pe_slope
    return result


def compute_lempel_ziv(series: np.ndarray) -> dict[str, float]:
    """Lempel-Ziv complexity with two binarization strategies.

    - lzc_median: binarize above/below the series median.
    - lzc_running_mean: binarize above/below a 1-hour running mean
      (window=12 for 5-min data).
    """
    # Binarization 1: median threshold
    binary_median = (series > np.median(series)).astype(int)
    lzc_median = float(ant.lziv_complexity(binary_median))

    # Binarization 2: 1-hour running mean threshold
    running_mean = pd.Series(series).rolling(12, center=True, min_periods=1).mean().values
    binary_running = (series > running_mean).astype(int)
    lzc_running_mean = float(ant.lziv_complexity(binary_running))

    return {"lzc_median": lzc_median, "lzc_running_mean": lzc_running_mean}


def compute_sample_entropy(series: np.ndarray, m: int = 2) -> float:
    """Sample entropy (m=2, r=0.2*SD).

    Returns NaN if computation fails (e.g., no template matches).
    """
    try:
        return float(ant.sample_entropy(series, order=m))
    except Exception:
        return np.nan


def compute_mse_slope(
    series: np.ndarray,
    m: int = 2,
    scales: list[int] | None = None,
) -> float:
    """Multiscale entropy slope.

    Coarse-grains the series at each scale factor, computes sample entropy
    with r = 0.2 * SD of the ORIGINAL series (fixed across scales), and
    returns the slope of SampEn vs. scale.

    Returns NaN if fewer than 2 usable scales.
    """
    if scales is None:
        scales = [1, 2, 3]

    r = 0.2 * np.std(series, ddof=1)
    usable_scales: list[int] = []
    sampen_values: list[float] = []

    for s in scales:
        n_coarse = len(series) // s
        if n_coarse < 50:
            continue
        # Coarse-grain: average consecutive non-overlapping windows of size s
        trimmed = series[: n_coarse * s]
        coarse = trimmed.reshape(n_coarse, s).mean(axis=1)
        try:
            se = float(ant.sample_entropy(coarse, order=m, tolerance=r))
            if np.isfinite(se):
                usable_scales.append(s)
                sampen_values.append(se)
        except Exception:
            continue

    if len(usable_scales) < 2:
        return np.nan
    return float(np.polyfit(usable_scales, sampen_values, 1)[0])


def compute_higuchi_fd(series: np.ndarray, kmax: int = 15) -> dict[str, float]:
    """Higuchi fractal dimension with stability check.

    - higuchi_fd: HFD of the full series.
    - hfd_instability: absolute difference of HFD on first half vs second half.
    """
    hfd_full = float(ant.higuchi_fd(series, kmax=kmax))

    mid = len(series) // 2
    hfd_first = float(ant.higuchi_fd(series[:mid], kmax=kmax))
    hfd_second = float(ant.higuchi_fd(series[mid:], kmax=kmax))
    hfd_instability = abs(hfd_first - hfd_second)

    return {"higuchi_fd": hfd_full, "hfd_instability": hfd_instability}


def extract_complexity_features(
    participants: dict[str, dict[str, Any]],
    series_key: str = "hr",
    col_prefix: str = "",
) -> pd.DataFrame:
    """Compute all complexity features for all participants.

    Each feature computation is wrapped in try/except — if any feature
    fails for a participant, that feature is set to NaN and a warning
    is printed.
    """
    feature_funcs = [
        ("perm_entropy", lambda hr: {"perm_entropy": compute_permutation_entropy(hr)}),
        ("multidelay_pe", compute_multidelay_pe),
        ("lempel_ziv", compute_lempel_ziv),
        ("sample_entropy", lambda hr: {"sample_entropy": compute_sample_entropy(hr)}),
        ("mse_slope", lambda hr: {"mse_slope": compute_mse_slope(hr)}),
        ("higuchi_fd", compute_higuchi_fd),
    ]

    rows: list[dict[str, Any]] = []
    for pid, pdata in participants.items():
        hr = pdata[series_key]
        row: dict[str, Any] = {"id": pid, "condition": pdata["condition"]}
        for name, func in feature_funcs:
            try:
                result = func(hr)
                row.update(result)
            except Exception as e:
                warnings.warn(f"{name} failed for {pid}: {e}")
                # Set expected keys to NaN depending on function
                if name == "multidelay_pe":
                    for d in [1, 3, 6, 12]:
                        row[f"pe_tau{d}"] = np.nan
                    row["pe_slope"] = np.nan
                elif name == "lempel_ziv":
                    row["lzc_median"] = np.nan
                    row["lzc_running_mean"] = np.nan
                elif name == "higuchi_fd":
                    row["higuchi_fd"] = np.nan
                    row["hfd_instability"] = np.nan
                else:
                    row[name] = np.nan
        rows.append(row)
    df = pd.DataFrame(rows)
    if col_prefix:
        df = df.rename(columns={c: col_prefix + c for c in df.columns
                                if c not in ("id", "condition")})
    return df


# ---------------------------------------------------------------------------
# Temporal correlation features
# ---------------------------------------------------------------------------

def compute_acf_features(series: np.ndarray) -> dict[str, float]:
    """Autocorrelation-based features from 5-min HR time series.

    Computes ACF out to lag 144 (12 hours at 5-min resolution) and extracts:
    - acf_lag1: short-term persistence (5-min scale)
    - acf_lag12: 1-hour periodicity
    - acf_lag144: 12-hour day-night contrast
    - acf_first_zero: decorrelation time in hours
    - acf_decay_rate: 1/τ from exponential decay fit A*exp(-t/τ)
    """
    max_lag = min(144, len(series) - 1)
    acf_vals = acf(series, nlags=max_lag, fft=True)

    acf_lag1 = float(acf_vals[1])
    acf_lag12 = float(acf_vals[12]) if max_lag >= 12 else np.nan
    acf_lag144 = float(acf_vals[144]) if max_lag >= 144 else np.nan

    # First zero crossing
    acf_first_zero = np.nan
    first_zero_lag = None
    for i in range(1, len(acf_vals)):
        if acf_vals[i] <= 0:
            first_zero_lag = i
            acf_first_zero = float(i * 5 / 60)  # convert to hours
            break

    # Exponential decay fit: A * exp(-t / tau)
    acf_decay_rate = np.nan
    fit_end = first_zero_lag if first_zero_lag is not None else min(50, max_lag)
    if fit_end > 2:
        lags_fit = np.arange(1, fit_end)
        acf_fit = acf_vals[1:fit_end]
        try:
            def _exp_decay(t, a, tau):
                return a * np.exp(-t / tau)
            popt, _ = curve_fit(
                _exp_decay, lags_fit, acf_fit,
                p0=[acf_vals[1], 10.0],
                bounds=([0, 0.1], [2.0, 500.0]),
                maxfev=5000,
            )
            acf_decay_rate = float(1.0 / popt[1])
        except Exception:
            pass

    return {
        "acf_lag1": acf_lag1,
        "acf_lag12": acf_lag12,
        "acf_lag144": acf_lag144,
        "acf_first_zero": acf_first_zero,
        "acf_decay_rate": acf_decay_rate,
    }


def compute_dfa(series: np.ndarray) -> dict[str, float]:
    """Detrended Fluctuation Analysis.

    Box sizes from 4 to 72 (20 min to 6 hours) on a log scale.
    Returns dfa_alpha (scaling exponent) and dfa_r_squared (fit quality).
    """
    try:
        nvals = nolds.logarithmic_n(4, 72, 1.2)
        result = nolds.dfa(series, nvals=nvals, debug_data=True)
        alpha = float(result[0])
        # debug_data: (log_n, log_fluct, poly_coeffs)
        log_n, log_f, _ = result[1]
        predicted = np.polyval(np.polyfit(log_n, log_f, 1), log_n)
        ss_res = np.sum((log_f - predicted) ** 2)
        ss_tot = np.sum((log_f - log_f.mean()) ** 2)
        r_squared = float(1 - ss_res / ss_tot) if ss_tot > 0 else np.nan
        return {"dfa_alpha": alpha, "dfa_r_squared": r_squared}
    except Exception:
        return {"dfa_alpha": np.nan, "dfa_r_squared": np.nan}


def extract_temporal_features(
    participants: dict[str, dict[str, Any]],
    series_key: str = "hr",
    col_prefix: str = "",
) -> pd.DataFrame:
    """Compute ACF and DFA features for all participants."""
    rows: list[dict[str, Any]] = []
    for pid, pdata in participants.items():
        hr = pdata[series_key]
        row: dict[str, Any] = {"id": pid, "condition": pdata["condition"]}
        for name, func in [("acf", compute_acf_features), ("dfa", compute_dfa)]:
            try:
                row.update(func(hr))
            except Exception as e:
                warnings.warn(f"{name} failed for {pid}: {e}")
                if name == "acf":
                    for k in ["acf_lag1", "acf_lag12", "acf_lag144",
                              "acf_first_zero", "acf_decay_rate"]:
                        row[k] = np.nan
                else:
                    row["dfa_alpha"] = np.nan
                    row["dfa_r_squared"] = np.nan
        rows.append(row)
    df = pd.DataFrame(rows)
    if col_prefix:
        df = df.rename(columns={c: col_prefix + c for c in df.columns
                                if c not in ("id", "condition")})
    return df


# ---------------------------------------------------------------------------
# Dynamical features
# ---------------------------------------------------------------------------

def _count_consecutive_runs(binary_seq: np.ndarray) -> list[int]:
    """Return lengths of consecutive runs of 1s in a binary array."""
    runs: list[int] = []
    count = 0
    for val in binary_seq:
        if val:
            count += 1
        else:
            if count > 0:
                runs.append(count)
            count = 0
    if count > 0:
        runs.append(count)
    return runs


def _shannon_entropy_normalized(counts: np.ndarray) -> float:
    """Normalized Shannon entropy of a distribution given as counts."""
    total = counts.sum()
    if total == 0:
        return np.nan
    p = counts / total
    p = p[p > 0]
    n_distinct = len(p)
    if n_distinct <= 1:
        return 0.0
    return float(-np.sum(p * np.log(p)) / np.log(n_distinct))


def compute_rqa_features(
    series: np.ndarray,
    embedding_dim: int = 2,
    time_delay: int = 1,
    recurrence_rate: float = 0.10,
) -> dict[str, float]:
    """Recurrence Quantification Analysis features.

    Manually implements RQA via time-delay embedding and pairwise distances.
    The recurrence threshold is set as the `recurrence_rate` quantile of all
    pairwise distances, giving a fixed recurrence rate across participants.
    """
    nan_result = {
        "rqa_recurrence_rate": np.nan,
        "rqa_determinism": np.nan,
        "rqa_laminarity": np.nan,
        "rqa_trapping_time": np.nan,
        "rqa_entropy": np.nan,
    }
    try:
        # Time-delay embedding
        n_embedded = len(series) - (embedding_dim - 1) * time_delay
        if n_embedded < 10:
            return nan_result
        embedded = np.column_stack([
            series[i * time_delay: i * time_delay + n_embedded]
            for i in range(embedding_dim)
        ])

        # Pairwise distances and recurrence matrix
        dists = squareform(pdist(embedded, metric="euclidean"))
        threshold = np.percentile(dists[np.triu_indices_from(dists, k=1)],
                                  recurrence_rate * 100)
        rec_matrix = (dists <= threshold).astype(int)
        np.fill_diagonal(rec_matrix, 0)  # exclude line of identity

        # Recurrence rate (upper triangle only)
        n_pts = rec_matrix.shape[0]
        upper_tri = rec_matrix[np.triu_indices(n_pts, k=1)]
        total_recurrent = upper_tri.sum()
        n_pairs = len(upper_tri)
        rr = float(total_recurrent / n_pairs) if n_pairs > 0 else 0.0

        # Diagonal lines (parallel to main diagonal, offset >= 1)
        diag_line_lengths: list[int] = []
        for offset in range(1, n_pts):
            diag = np.diag(rec_matrix, k=offset)
            diag_line_lengths.extend(_count_consecutive_runs(diag))

        diag_lines_ge2 = [l for l in diag_line_lengths if l >= 2]
        points_on_diag_ge2 = sum(diag_lines_ge2)
        determinism = float(points_on_diag_ge2 / total_recurrent) if total_recurrent > 0 else np.nan

        # Diagonal line length entropy
        if diag_lines_ge2:
            unique_lengths, length_counts = np.unique(diag_lines_ge2, return_counts=True)
            rqa_entropy = _shannon_entropy_normalized(length_counts)
        else:
            rqa_entropy = np.nan

        # Vertical lines (iterate columns of upper triangle portion)
        vert_line_lengths: list[int] = []
        for col in range(n_pts):
            col_vals = rec_matrix[:, col]
            vert_line_lengths.extend(_count_consecutive_runs(col_vals))

        vert_lines_ge2 = [l for l in vert_line_lengths if l >= 2]
        points_on_vert_ge2 = sum(vert_lines_ge2)
        total_recurrent_full = rec_matrix.sum()
        laminarity = float(points_on_vert_ge2 / total_recurrent_full) if total_recurrent_full > 0 else np.nan
        trapping_time = float(np.mean(vert_lines_ge2)) if vert_lines_ge2 else np.nan

        return {
            "rqa_recurrence_rate": rr,
            "rqa_determinism": determinism,
            "rqa_laminarity": laminarity,
            "rqa_trapping_time": trapping_time,
            "rqa_entropy": rqa_entropy,
        }
    except Exception:
        return nan_result


def compute_transition_features(
    series: np.ndarray,
    n_states: int = 4,
) -> dict[str, float]:
    """Transition matrix features from quartile-discretized HR series.

    Discretizes into quartiles, builds a row-normalized transition matrix,
    and extracts entropy, diagonal dominance, asymmetry, and per-quartile
    transition entropies.
    """
    # Discretize into quartiles
    bin_edges = np.percentile(series, np.linspace(0, 100, n_states + 1))
    # Ensure unique edges by adding small epsilon to duplicates
    bin_edges[-1] += 1e-10
    states = np.digitize(series, bin_edges[1:-1])  # 0-indexed: 0, 1, ..., n_states-1

    # Build transition count matrix
    T_counts = np.zeros((n_states, n_states), dtype=float)
    for t in range(len(states) - 1):
        T_counts[states[t], states[t + 1]] += 1

    # Row-normalize to get transition probabilities
    row_sums = T_counts.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1  # avoid division by zero
    T = T_counts / row_sums

    # Transition entropy (full matrix)
    flat = T.ravel()
    flat_pos = flat[flat > 0]
    if len(flat_pos) > 1:
        trans_entropy = float(-np.sum(flat_pos * np.log(flat_pos)) / np.log(n_states ** 2))
    else:
        trans_entropy = 0.0

    # Diagonal dominance
    trans_diagonal_dominance = float(np.mean(np.diag(T)))

    # Asymmetry
    asym_sum = 0.0
    for i in range(n_states):
        for j in range(i + 1, n_states):
            asym_sum += abs(T[i, j] - T[j, i])
    trans_asymmetry = float(asym_sum / (n_states * (n_states - 1)))

    # Per-row entropies for Q1 (row 0) and Q4 (last row)
    def _row_entropy(row: np.ndarray) -> float:
        p = row[row > 0]
        if len(p) <= 1:
            return 0.0
        return float(-np.sum(p * np.log(p)) / np.log(n_states))

    trans_entropy_q1 = _row_entropy(T[0])
    trans_entropy_q4 = _row_entropy(T[-1])

    return {
        "trans_entropy": trans_entropy,
        "trans_diagonal_dominance": trans_diagonal_dominance,
        "trans_asymmetry": trans_asymmetry,
        "trans_entropy_q1": trans_entropy_q1,
        "trans_entropy_q4": trans_entropy_q4,
    }


def extract_dynamical_features(
    participants: dict[str, dict[str, Any]],
    series_key: str = "hr",
    col_prefix: str = "",
) -> pd.DataFrame:
    """Compute RQA and transition matrix features for all participants."""
    rqa_nan = {
        "rqa_recurrence_rate": np.nan, "rqa_determinism": np.nan,
        "rqa_laminarity": np.nan, "rqa_trapping_time": np.nan,
        "rqa_entropy": np.nan,
    }
    trans_nan = {
        "trans_entropy": np.nan, "trans_diagonal_dominance": np.nan,
        "trans_asymmetry": np.nan, "trans_entropy_q1": np.nan,
        "trans_entropy_q4": np.nan,
    }

    rows: list[dict[str, Any]] = []
    for pid, pdata in participants.items():
        hr = pdata[series_key]
        row: dict[str, Any] = {"id": pid, "condition": pdata["condition"]}
        for name, func, nan_dict in [
            ("rqa", compute_rqa_features, rqa_nan),
            ("transition", compute_transition_features, trans_nan),
        ]:
            try:
                row.update(func(hr))
            except Exception as e:
                warnings.warn(f"{name} failed for {pid}: {e}")
                row.update(nan_dict)
        rows.append(row)
    df = pd.DataFrame(rows)
    if col_prefix:
        df = df.rename(columns={c: col_prefix + c for c in df.columns
                                if c not in ("id", "condition")})
    return df


# ---------------------------------------------------------------------------
# MiniROCKET features
# ---------------------------------------------------------------------------

MINIROCKET_LENGTH = 276  # truncate to first 276 points for MiniRocket


def compute_minirocket_features(
    participants: dict[str, dict[str, Any]],
    n_components: int = 10,
) -> pd.DataFrame:
    """MiniROCKET convolutional features reduced via PCA.

    Truncates each HR series to the first 276 points. If a series has fewer
    than 276 points, it is interpolated onto a 276-point grid.

    Returns a DataFrame with [id, minirocket_pc1, ..., minirocket_pc{n}].
    On failure, returns NaN columns with a warning.
    """
    pids = list(participants.keys())
    n_participants = len(pids)

    # Assemble HR matrix (N × 276)
    hr_matrix = np.empty((n_participants, MINIROCKET_LENGTH))
    for i, pid in enumerate(pids):
        hr = participants[pid]["hr"]
        if len(hr) >= MINIROCKET_LENGTH:
            hr_matrix[i] = hr[:MINIROCKET_LENGTH]
        else:
            # Interpolate onto 276-point grid
            orig_idx = np.arange(len(hr))
            new_idx = np.linspace(0, len(hr) - 1, MINIROCKET_LENGTH)
            hr_matrix[i] = np.interp(new_idx, orig_idx, hr)

    # NaN fallback DataFrame
    nan_cols = {f"minirocket_pc{j+1}": np.nan for j in range(n_components)}
    nan_df = pd.DataFrame([{"id": pid, **nan_cols} for pid in pids])

    try:
        try:
            from sktime.transformations.panel.rocket import MiniRocket
        except ImportError:
            from sktime.transformations.rocket import MiniRocket

        # MiniRocket expects (n_instances, n_channels, n_timepoints)
        X = hr_matrix.reshape(n_participants, 1, MINIROCKET_LENGTH)
        mr = MiniRocket()
        mr.fit(X)
        features = mr.transform(X)

        # PCA reduction
        pca = PCA(n_components=n_components, random_state=42)
        pcs = pca.fit_transform(features)

        print(f"\n  MiniROCKET PCA variance explained:")
        cumvar = 0.0
        for j, v in enumerate(pca.explained_variance_ratio_):
            cumvar += v
            print(f"    PC{j+1:2d}: {v:.4f}  (cumulative: {cumvar:.4f})")

        result = pd.DataFrame(
            pcs, columns=[f"minirocket_pc{j+1}" for j in range(n_components)]
        )
        result.insert(0, "id", pids)
        return result

    except Exception as e:
        warnings.warn(f"MiniROCKET failed: {e}")
        return nan_df


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def _print_condition_summary(
    df: pd.DataFrame,
    cols: list[str],
    title: str,
    cond_counts: dict,
    group_col: str = "condition",
) -> None:
    """Helper to print mean +/- SD of selected columns by condition group."""
    print(f"\n{title}:")
    grouped = df.groupby(group_col)[cols]
    summary = grouped.agg(["mean", "std"])
    for cond in sorted(df[group_col].unique()):
        n = cond_counts.get(cond, df[df[group_col] == cond].shape[0])
        print(f"\n  {cond} (n={n}):")
        for col in cols:
            m = summary.loc[cond, (col, "mean")]
            s = summary.loc[cond, (col, "std")]
            print(f"    {col:28s}  {m:12.4f} +/- {s:.4f}")


if __name__ == "__main__":
    from collections import Counter

    data = load_data()

    # Summary by condition
    cond_counts = Counter(v["condition"] for v in data.values())
    print(f"\nN per condition (total N = {len(data)}):")
    for cond in sorted(cond_counts):
        print(f"  {cond:12s}  {cond_counts[cond]}")

    # --- 0. Circadian decomposition (produces residuals for downstream) ---
    print("\nComputing circadian decomposition (single + two-harmonic cosinor)...")
    cosinor_df = extract_cosinor_features(data)
    print(cosinor_df[["id", "condition", "mesor", "amplitude_24h",
                       "acrophase_24h", "r_squared_1h",
                       "amplitude_12h", "r_squared_2h",
                       "r_squared_improvement"]].head())
    print("\nMean R² (1h / 2h / improvement) per condition:")
    print(cosinor_df.groupby("condition")[
        ["r_squared_1h", "r_squared_2h", "r_squared_improvement"]
    ].mean().to_string())

    # --- 0a. Compute residuals (for Pass 2 downstream use) ---
    print("\nComputing two-harmonic cosinor residuals...")
    compute_residuals(data)

    # Spot-check: residual variance should be lower than raw HR variance
    _spot_ids = list(data.keys())[:3]
    for _sid in _spot_ids:
        _raw_std = np.std(data[_sid]["hr"])
        _res_std = np.std(data[_sid]["hr_residual"])
        print(f"  {_sid}: raw HR std={_raw_std:.2f}, residual std={_res_std:.2f}")

    # --- 0b. Nonparametric circadian features ---
    print("\nComputing nonparametric circadian features...")
    nonparam_df = extract_nonparametric_features(data)
    _print_condition_summary(
        nonparam_df,
        ["peak_trough_diff", "iv"],
        "Nonparametric circadian features — Mean +/- SD by condition",
        cond_counts,
    )

    # --- 1. Spectral & rhythm features ---
    print("\nComputing spectral & rhythm features...")
    spectral_df = extract_spectral_and_rhythm_features(data)
    _print_condition_summary(
        spectral_df,
        ["power_ulf", "power_circ", "power_meso",
         "power_hf", "spectral_entropy", "circadian_power_ratio"],
        "Spectral & rhythm features — Mean +/- SD by condition",
        cond_counts,
    )

    # --- 2. Complexity features ---
    print("\nComputing complexity features...")
    complexity_df = extract_complexity_features(data)
    _print_condition_summary(
        complexity_df,
        ["pe_tau1", "sample_entropy", "higuchi_fd"],
        "Complexity features — Mean +/- SD by condition",
        cond_counts,
    )

    # --- 3. Temporal correlation features ---
    print("\nComputing temporal correlation features...")
    temporal_df = extract_temporal_features(data)
    _print_condition_summary(
        temporal_df,
        ["acf_lag1", "acf_decay_rate", "dfa_alpha"],
        "Temporal correlation features — Mean +/- SD by condition",
        cond_counts,
    )

    # --- 4. Dynamical features ---
    print("\nComputing dynamical features...")
    dynamical_df = extract_dynamical_features(data)
    _print_condition_summary(
        dynamical_df,
        ["rqa_determinism", "rqa_laminarity", "trans_entropy", "trans_diagonal_dominance"],
        "Dynamical features — Mean +/- SD by condition",
        cond_counts,
    )

    # --- 5. MiniROCKET features ---
    print("\nComputing MiniROCKET features...")
    minirocket_df = compute_minirocket_features(data)

    # --- 6. Functional PCA ---
    print("\nComputing Functional PCA...")
    fpca_df, fpca_obj = compute_fpca(data)

    # Validation: correlation between FPC1 and cosinor amplitude
    if "fpca_score_1" in fpca_df.columns and fpca_df["fpca_score_1"].notna().any():
        merged_check = cosinor_df[["id", "amplitude_24h"]].merge(fpca_df[["id", "fpca_score_1"]], on="id")
        r = merged_check["fpca_score_1"].corr(merged_check["amplitude_24h"])
        print(f"\n  Validation: corr(fpca_score_1, amplitude_24h) = {r:.3f}")

    # --- 7. Descriptive stats: CV and SD (raw + residual SD) ---
    print("\nComputing descriptive stats (cv, sd, resid_sd)...")
    desc_rows = [{"id": pid, "condition": pdata["condition"],
                  "cv": compute_cv(pdata["hr"]),
                  "sd": float(np.nanstd(pdata["hr"])),
                  "resid_sd": float(np.nanstd(pdata["hr_residual"]))}
                 for pid, pdata in data.items()]
    cv_df = pd.DataFrame(desc_rows)
    print(f"  Mean CV = {cv_df['cv'].mean():.4f}, "
          f"Mean SD = {cv_df['sd'].mean():.2f}, "
          f"Mean resid_SD = {cv_df['resid_sd'].mean():.2f}")

    # --- 8. Residual features (detrended series) ---
    print("\nComputing residual spectral features...")
    resid_spectral_df = extract_spectral_and_rhythm_features(
        data, series_key="hr_residual", col_prefix="resid_")

    print("Computing residual complexity features...")
    resid_complexity_df = extract_complexity_features(
        data, series_key="hr_residual", col_prefix="resid_")

    print("Computing residual temporal features...")
    resid_temporal_df = extract_temporal_features(
        data, series_key="hr_residual", col_prefix="resid_")

    print("Computing residual dynamical features...")
    resid_dynamical_df = extract_dynamical_features(
        data, series_key="hr_residual", col_prefix="resid_")

    # --- Merge all feature DataFrames ---
    all_features_df = cosinor_df
    for df in [nonparam_df, spectral_df, complexity_df, temporal_df, dynamical_df,
               cv_df, resid_spectral_df, resid_complexity_df,
               resid_temporal_df, resid_dynamical_df]:
        all_features_df = all_features_df.merge(df, on=["id", "condition"])
    all_features_df = all_features_df.merge(minirocket_df, on="id")
    all_features_df = all_features_df.merge(fpca_df, on="id")

    # --- Add condition_3group ---
    all_features_df["condition_3group"] = all_features_df["condition"].map(
        lambda c: "CAD-spectrum" if c in ("CAD", "CAD+DM") else c
    )

    # --- Save CSV ---
    output_dir = _PROJECT_ROOT / "results" / "thew"
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / "thew_metrics_python_5min.csv"
    all_features_df.to_csv(csv_path, index=False)
    print(f"\nSaved to {csv_path}")

    # --- Save participants pickle (with residuals for Pass 2) ---
    pkl_path = _PROJECT_ROOT / "data_processed" / "thew" / "pass1_participants_with_residuals.pkl"
    pkl_path.parent.mkdir(parents=True, exist_ok=True)
    with open(pkl_path, "wb") as f:
        pickle.dump(data, f)
    print(f"Saved participants dict to {pkl_path}")

    # --- Final summary ---
    id_cond_cols = {"id", "condition", "condition_3group"}
    feature_cols_all = [c for c in all_features_df.columns if c not in id_cond_cols]
    _fc = lambda df, excl={"id", "condition"}: len([c for c in df.columns if c not in excl])
    n_cosinor = _fc(cosinor_df)
    n_nonparam = _fc(nonparam_df)
    n_spectral = _fc(spectral_df)
    n_complexity = _fc(complexity_df)
    n_temporal = _fc(temporal_df)
    n_dynamical = _fc(dynamical_df)
    n_cv = _fc(cv_df)
    n_minirocket = _fc(minirocket_df, {"id"})
    n_fpca = _fc(fpca_df, {"id"})
    n_resid_spectral = _fc(resid_spectral_df)
    n_resid_complexity = _fc(resid_complexity_df)
    n_resid_temporal = _fc(resid_temporal_df)
    n_resid_dynamical = _fc(resid_dynamical_df)
    n_resid_total = n_resid_spectral + n_resid_complexity + n_resid_temporal + n_resid_dynamical

    print(f"\n{'='*60}")
    print(f"FINAL SUMMARY")
    print(f"{'='*60}")
    print(f"  Participants:  {len(all_features_df)}")
    print(f"  Total features: {len(feature_cols_all)}")
    print(f"  --- Raw features ---")
    print(f"    Cosinor:          {n_cosinor}")
    print(f"    Nonparametric:    {n_nonparam}")
    print(f"    Spectral/rhythm:  {n_spectral}")
    print(f"    Complexity:       {n_complexity}")
    print(f"    Temporal:         {n_temporal}")
    print(f"    Dynamical:        {n_dynamical}")
    print(f"    Descriptive:      {n_cv}  (cv, sd, resid_sd)")
    print(f"    MiniROCKET PCs:   {n_minirocket}")
    print(f"    FPCA scores:      {n_fpca}")
    print(f"  --- Residual features ---")
    print(f"    resid_Spectral:   {n_resid_spectral}")
    print(f"    resid_Complexity: {n_resid_complexity}")
    print(f"    resid_Temporal:   {n_resid_temporal}")
    print(f"    resid_Dynamical:  {n_resid_dynamical}")
    print(f"    (subtotal):       {n_resid_total}")

    # --- Pass 1 circadian features: group comparison (3-group) ---
    cond3_counts = Counter(all_features_df["condition_3group"])
    circadian_param_cols = [c for c in cosinor_df.columns if c not in {"id", "condition"}]
    circadian_nonparam_cols = [c for c in nonparam_df.columns if c not in {"id", "condition"}]
    fpca_cols = [c for c in fpca_df.columns if c != "id"]
    pass1_cols = circadian_param_cols + circadian_nonparam_cols + fpca_cols

    _print_condition_summary(
        all_features_df,
        pass1_cols,
        "Pass 1 circadian features — Mean +/- SD by 3-group condition",
        cond3_counts,
        group_col="condition_3group",
    )

    # Key raw + residual features by 3-group condition
    key_features = ["cv", "sample_entropy", "dfa_alpha", "rqa_determinism",
                    "resid_sample_entropy", "resid_dfa_alpha",
                    "resid_spectral_entropy", "resid_rqa_determinism"]
    _print_condition_summary(
        all_features_df,
        key_features,
        "Key raw + residual features — Mean +/- SD by 3-group condition",
        cond3_counts,
        group_col="condition_3group",
    )

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
# Spectral & rhythm features
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
) -> pd.DataFrame:
    """Compute IV and spectral features for all participants.

    Returns a DataFrame with columns:
        id, condition, iv, power_ulf, power_circ, power_meso, power_hf,
        spectral_entropy, circadian_power_ratio
    """
    rows: list[dict[str, Any]] = []
    for pid, pdata in participants.items():
        hr = pdata["hr"]
        iv = compute_intradaily_variability(hr)
        spec = compute_spectral_features(hr)
        rows.append({"id": pid, "condition": pdata["condition"], "iv": iv, **spec})
    return pd.DataFrame(rows)


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
        hr = pdata["hr"]
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
    return pd.DataFrame(rows)


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
) -> pd.DataFrame:
    """Compute ACF and DFA features for all participants."""
    rows: list[dict[str, Any]] = []
    for pid, pdata in participants.items():
        hr = pdata["hr"]
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
    return pd.DataFrame(rows)


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
        hr = pdata["hr"]
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
    return pd.DataFrame(rows)


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

    # --- 1. Spectral & rhythm features ---
    print("\nComputing spectral & rhythm features...")
    spectral_df = extract_spectral_and_rhythm_features(data)
    _print_condition_summary(
        spectral_df,
        ["iv", "power_ulf", "power_circ", "power_meso",
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

    # --- Merge all feature DataFrames ---
    all_features_df = spectral_df
    for df in [complexity_df, temporal_df, dynamical_df]:
        all_features_df = all_features_df.merge(df, on=["id", "condition"])
    all_features_df = all_features_df.merge(minirocket_df, on="id")

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

    # --- Save participants pickle ---
    pkl_path = _PROJECT_ROOT / "data_processed" / "thew" / "pass2_participants_raw.pkl"
    pkl_path.parent.mkdir(parents=True, exist_ok=True)
    with open(pkl_path, "wb") as f:
        pickle.dump(data, f)
    print(f"Saved participants dict to {pkl_path}")

    # --- Final summary ---
    id_cond_cols = {"id", "condition", "condition_3group"}
    feature_cols_all = [c for c in all_features_df.columns if c not in id_cond_cols]
    n_spectral = len([c for c in spectral_df.columns if c not in {"id", "condition"}])
    n_complexity = len([c for c in complexity_df.columns if c not in {"id", "condition"}])
    n_temporal = len([c for c in temporal_df.columns if c not in {"id", "condition"}])
    n_dynamical = len([c for c in dynamical_df.columns if c not in {"id", "condition"}])
    n_minirocket = len([c for c in minirocket_df.columns if c != "id"])

    print(f"\n{'='*60}")
    print(f"FINAL SUMMARY")
    print(f"{'='*60}")
    print(f"  Participants:  {len(all_features_df)}")
    print(f"  Total features: {len(feature_cols_all)}")
    print(f"    Spectral/rhythm:  {n_spectral}")
    print(f"    Complexity:       {n_complexity}")
    print(f"    Temporal:         {n_temporal}")
    print(f"    Dynamical:        {n_dynamical}")
    print(f"    MiniROCKET PCs:   {n_minirocket}")

    # Key features by 3-group condition
    cond3_counts = Counter(all_features_df["condition_3group"])
    key_features = ["iv", "pe_tau1", "sample_entropy", "acf_lag1",
                    "dfa_alpha", "rqa_determinism", "trans_entropy"]
    _print_condition_summary(
        all_features_df,
        key_features,
        "Key features — Mean +/- SD by 3-group condition",
        cond3_counts,
        group_col="condition_3group",
    )

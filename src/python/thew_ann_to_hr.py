"""
THEW .ann → 1-minute average HR time series
=============================================

Reads THEW binary annotation files (.ann) in ISHNE annotation format,
extracts beat-to-beat RR intervals, computes instantaneous HR, and
bins into 1-minute average HR time series.

Binary format reference:
  - ECG-Kit read_ishne_ann.m (PhysioNet)
  - Marcus Vollmer HRV toolbox (read_ishne.m)
  - Badilini (1998) ISHNE Holter Standard Output File Format

IMPORTANT: You must know the sampling frequency (fs) for each database.
THEW databases use 180, 200, or 1000 Hz depending on the dataset.
Check your database documentation and set FS below accordingly.

Author: Christine Kuryla
"""

import struct
import os
import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime
import logging
import sys

# ============================================================
# CONFIGURATION — EDIT THESE
# ============================================================
# Define each database with its own path and sampling frequency.
# Add/remove entries as needed.
DATABASES = [
    {
        'name': 't002',
        'ann_dir': Path("/Users/christinekuryla/data_depot/physiological_ts/holter/thew/E-HOL-03-0271-002_ann/"),
        'fs': 200,
        'downsample_to_fs': None,
        'condition': 'CAD',
    },
    {
        'name': 't003',
        'ann_dir': Path("/Users/christinekuryla/data_depot/physiological_ts/holter/thew/E-HOL-03-0202-003_ann/"),
        'fs': 200,
        'downsample_to_fs': None,
        'condition': 'Healthy',
    },
    {
        'name': 't016',
        'ann_dir': Path("/Users/christinekuryla/data_depot/physiological_ts/holter/thew/E-HOL-12-0051-016_ann/"),
        'fs': 1000,
        'downsample_to_fs': 200,
        'condition': 'ESRD',
    },
]

# Root output directory (subfolders created per database)
OUTPUT_ROOT = Path("/Users/christinekuryla/data_depot/physiological_ts/holter/thew/thew_derived/hr_timeseries_1min/")

# Minimum beats in a 1-min window to compute a valid average
# Fewer than this → NaN for that minute
MIN_BEATS_PER_MINUTE = 30

# Physiological HR bounds for artifact rejection
HR_MIN = 20   # bpm
HR_MAX = 250  # bpm

# Whether to also save RR-level data (useful for HRV later)
SAVE_RR_DATA = False

# ============================================================


def setup_logging(output_dir):
    """Configure logging to both console and file."""
    log_file = output_dir / f"processing_log_{datetime.now():%Y%m%d_%H%M%S}.txt"
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger(__name__)


def read_thew_ann(filepath, fs, downsample_to_fs=None):
    """
    Read a THEW .ann binary annotation file.

    Parameters
    ----------
    filepath : path to .ann file
    fs : int, native sampling frequency of this database
    downsample_to_fs : int or None
        If set, quantize beat sample positions to match the resolution
        of a lower sampling rate. This rounds each absolute sample
        position to the nearest sample at downsample_to_fs, then
        recomputes RR intervals from the rounded positions.
        
        This does NOT resample the ECG signal — it degrades the
        *timing precision* of R-peak locations to match what a lower-fs
        system would produce. The result is that RR intervals have the
        same quantization step (1/downsample_to_fs seconds) as data
        natively recorded at downsample_to_fs.
        
        Example: fs=1000, downsample_to_fs=200 → beat times rounded
        to nearest 5 ms (= 1/200), matching the 200 Hz resolution
        of the other databases.

    Returns
    -------
    dict with keys:
        'beat_samples' : np.ndarray of absolute sample positions (normal beats only)
        'beat_times_sec' : np.ndarray of beat times in seconds
        'rr_intervals_sec' : np.ndarray of RR intervals in seconds
        'all_labels' : np.ndarray of all beat type labels (before filtering)
        'n_total_beats' : int, total beats including non-normal
        'n_normal_beats' : int, normal beats retained
        'n_timeouts' : int, number of timeout markers
        'effective_fs' : int, the fs used for time conversion (native or downsampled)
    Or None if file cannot be read.
    """
    filesize = os.path.getsize(filepath)

    with open(filepath, 'rb') as f:
        # --- Magic number (8 bytes) ---
        # Both "ANN  1.0" and "ISHNE1.0" use the same 522-byte header
        # and 4-byte annotation record layout (lab1, lab2, rr_uint16).
        # E-HOL-12-0051-016 (ESRD, 1000 Hz) uses the ISHNE1.0 variant.
        magic = f.read(8)
        if magic not in (b'ANN  1.0', b'ISHNE1.0'):
            return None

        # --- CRC checksum (2 bytes) — skip ---
        f.read(2)

        # --- Variable length block size (4 bytes, int32) ---
        var_length_size = struct.unpack('<i', f.read(4))[0]

        # --- Skip rest of ISHNE header to reach annotations ---
        # Full header is 522 bytes from file start (magic + crc + fixed header)
        # Then var_length_size bytes of variable block
        # Then 4 bytes of init_sample
        # Then annotation data begins

        ann_header_end = 522 + var_length_size

        # Jump to init_sample
        f.seek(ann_header_end)
        init_sample = struct.unpack('<I', f.read(4))[0]

        # Annotation data starts at offset 526 + var_length_size
        ann_data_start = 526 + var_length_size
        ann_data_size = filesize - ann_data_start

        if ann_data_size <= 0 or ann_data_size % 4 != 0:
            return None

        n_annotations = ann_data_size // 4

        # Read all annotation data at once (fast)
        f.seek(ann_data_start)
        raw = f.read(ann_data_size)

    # Parse the 4-byte records
    # Each record: [lab1 (uint8), lab2 (uint8), rr_samples (uint16)]
    # Using numpy for speed on large files
    dt = np.dtype([
        ('lab1', 'u1'),    # beat type character as uint8
        ('lab2', 'u1'),    # subtype character as uint8
        ('rr_samples', '<u2')  # RR interval in samples, little-endian uint16
    ])
    annotations = np.frombuffer(raw, dtype=dt)

    lab1_chars = np.array([chr(c) for c in annotations['lab1']])
    rr_samples = annotations['rr_samples'].astype(np.int64)

    # Identify timeouts ('!' means RR > 65535 samples, i.e., a gap)
    is_timeout = (lab1_chars == '!')
    n_timeouts = np.sum(is_timeout)

    # Compute absolute sample positions via cumulative sum
    abs_samples = init_sample + np.cumsum(rr_samples)

    # Remove timeouts — these represent gaps, not real beats
    valid_mask = ~is_timeout
    abs_samples_clean = abs_samples[valid_mask]
    lab1_clean = lab1_chars[valid_mask]

    # Filter to normal beats only
    # 'N' = normal beat. Some databases may use other conventions.
    # Check your specific database documentation!
    normal_mask = (lab1_clean == 'N')
    beat_samples = abs_samples_clean[normal_mask]

    if len(beat_samples) < 2:
        return None

    # --- Resolution matching (downsampling) ---
    # Quantize beat positions to lower-fs grid to match timing precision
    # of another database. This is the correct way to harmonize RR
    # resolution across databases with different native sampling rates.
    effective_fs = fs
    if downsample_to_fs is not None and downsample_to_fs < fs:
        # Ratio: how many native samples per target sample
        # e.g., 1000/200 = 5 → round to nearest 5 native samples
        ratio = fs / downsample_to_fs
        beat_samples = np.round(beat_samples / ratio).astype(np.int64) * int(ratio)
        effective_fs = fs  # still in native sample units, just quantized
        # Note: we keep fs for sample→second conversion because the
        # sample numbers are still in native units. The quantization
        # just snaps them to the coarser grid.

    # Convert to times and RR intervals
    beat_times_sec = beat_samples / fs
    rr_intervals_sec = np.diff(beat_times_sec)

    # Remove any zero-length RR intervals created by quantization
    # (two beats snapped to same grid point — very rare but possible)
    nonzero = rr_intervals_sec > 0
    if not np.all(nonzero):
        rr_intervals_sec = rr_intervals_sec[nonzero]
        beat_times_sec = np.concatenate([
            beat_times_sec[:1],
            beat_times_sec[1:][nonzero]
        ])
        beat_samples = (beat_times_sec * fs).astype(np.int64)

    return {
        'beat_samples': beat_samples,
        'beat_times_sec': beat_times_sec,
        'rr_intervals_sec': rr_intervals_sec,
        'all_labels': lab1_chars,
        'n_total_beats': len(annotations),
        'n_normal_beats': len(beat_samples),
        'n_timeouts': n_timeouts,
        'effective_fs': effective_fs,
        'downsampled': downsample_to_fs is not None,
    }


def compute_1min_hr(beat_data, fs, min_beats=30, hr_min=20, hr_max=250):
    """
    Compute 1-minute average HR from beat annotations.

    Returns DataFrame with columns: minute, avg_hr, median_hr, sd_hr,
    beat_count, valid (bool), plus optionally SDNN and RMSSD per window.
    """
    beat_times = beat_data['beat_times_sec']
    rr = beat_data['rr_intervals_sec']

    # Instantaneous HR from RR intervals
    hr_inst = 60.0 / rr

    # Physiological plausibility filter
    valid_hr = (hr_inst >= hr_min) & (hr_inst <= hr_max)
    hr_inst_clean = hr_inst[valid_hr]
    # Midpoint times for each HR value (between consecutive beats)
    hr_times = beat_times[1:]
    hr_times_clean = hr_times[valid_hr]

    # Also keep clean RR for HRV metrics
    rr_clean = rr[valid_hr]

    if len(hr_inst_clean) == 0:
        return pd.DataFrame()

    # Bin into 1-minute windows
    total_duration = hr_times_clean[-1]
    n_minutes = int(np.ceil(total_duration / 60))
    bins = np.arange(0, (n_minutes + 1) * 60, 60)
    bin_idx = np.digitize(hr_times_clean, bins)

    records = []
    for i in range(1, len(bins)):
        mask = (bin_idx == i)
        in_bin_hr = hr_inst_clean[mask]
        in_bin_rr = rr_clean[mask]
        n = len(in_bin_hr)

        if n >= min_beats:
            avg_hr = np.mean(in_bin_hr)
            median_hr = np.median(in_bin_hr)
            sd_hr = np.std(in_bin_hr, ddof=1) if n > 1 else np.nan
            # Time-domain HRV metrics (on RR intervals in ms)
            rr_ms = in_bin_rr * 1000
            sdnn = np.std(rr_ms, ddof=1) if n > 1 else np.nan
            rmssd = np.sqrt(np.mean(np.diff(rr_ms)**2)) if n > 2 else np.nan
            valid = True
        else:
            avg_hr = np.nan
            median_hr = np.nan
            sd_hr = np.nan
            sdnn = np.nan
            rmssd = np.nan
            valid = False

        records.append({
            'minute': i - 1,
            'time_start_sec': (i - 1) * 60,
            'avg_hr': round(avg_hr, 2) if not np.isnan(avg_hr) else np.nan,
            'median_hr': round(median_hr, 2) if not np.isnan(median_hr) else np.nan,
            'sd_hr': round(sd_hr, 2) if not np.isnan(sd_hr) else np.nan,
            'sdnn_ms': round(sdnn, 2) if not np.isnan(sdnn) else np.nan,
            'rmssd_ms': round(rmssd, 2) if not np.isnan(rmssd) else np.nan,
            'beat_count': n,
            'valid': valid,
        })

    return pd.DataFrame(records)


def process_all_files(ann_dir, output_dir, fs, min_beats, hr_min, hr_max,
                      save_rr=False, downsample_to_fs=None):
    """
    Loop over all .ann files in ann_dir, process each, save results.
    """
    ann_dir = Path(ann_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logger = setup_logging(output_dir)
    logger.info(f"Starting THEW .ann processing")
    logger.info(f"Input directory: {ann_dir}")
    logger.info(f"Output directory: {output_dir}")
    logger.info(f"Sampling frequency: {fs} Hz")
    if downsample_to_fs:
        logger.info(f"Downsampling RR resolution to match: {downsample_to_fs} Hz")
    logger.info(f"Min beats per minute: {min_beats}")
    logger.info(f"HR range: [{hr_min}, {hr_max}] bpm")

    ann_files = sorted(ann_dir.glob("*.ann"))
    if not ann_files:
        # Also try uppercase
        ann_files = sorted(ann_dir.glob("*.ANN"))

    logger.info(f"Found {len(ann_files)} .ann files")

    summary_records = []
    n_success = 0
    n_fail = 0

    for i, fpath in enumerate(ann_files):
        record_id = fpath.stem
        logger.info(f"[{i+1}/{len(ann_files)}] Processing {record_id}...")

        try:
            beat_data = read_thew_ann(fpath, fs, downsample_to_fs)

            if beat_data is None:
                logger.warning(f"  SKIPPED: Could not parse {record_id}")
                n_fail += 1
                summary_records.append({
                    'record_id': record_id,
                    'status': 'parse_error',
                    'n_total_beats': np.nan,
                    'n_normal_beats': np.nan,
                    'n_timeouts': np.nan,
                    'duration_hours': np.nan,
                    'n_valid_minutes': np.nan,
                    'n_total_minutes': np.nan,
                    'n_valid_wearable_pts': np.nan,
                    'n_total_wearable_pts': np.nan,
                    'mean_hr': np.nan,
                })
                continue

            # Compute 1-min HR
            df_hr = compute_1min_hr(beat_data, fs, min_beats, hr_min, hr_max)

            if df_hr.empty:
                logger.warning(f"  SKIPPED: No valid HR data for {record_id}")
                n_fail += 1
                continue

            # Save 1-min HR time series (continuous)
            out_file = output_dir / f"{record_id}_hr_1min.csv"
            df_hr.to_csv(out_file, index=False)

            # Save wearable-mimicking output: 1-min window every 5 minutes
            # i.e., minutes 0, 5, 10, 15, ... — matches typical wearable
            # spot-check cadence (brief measurement, long gap)
            df_wearable = df_hr[df_hr['minute'] % 5 == 0].copy()
            df_wearable = df_wearable.reset_index(drop=True)
            wearable_file = output_dir / f"{record_id}_hr_wearable5.csv"
            df_wearable.to_csv(wearable_file, index=False)

            # Optionally save beat-level RR data
            if save_rr:
                rr_file = output_dir / f"{record_id}_rr.csv"
                pd.DataFrame({
                    'beat_time_sec': beat_data['beat_times_sec'][1:],
                    'rr_sec': beat_data['rr_intervals_sec'],
                    'hr_bpm': 60.0 / beat_data['rr_intervals_sec'],
                }).to_csv(rr_file, index=False)

            # Summary stats
            duration_hrs = beat_data['beat_times_sec'][-1] / 3600
            n_valid = df_hr['valid'].sum()
            n_valid_wearable = df_wearable['valid'].sum()

            summary_records.append({
                'record_id': record_id,
                'status': 'success',
                'n_total_beats': beat_data['n_total_beats'],
                'n_normal_beats': beat_data['n_normal_beats'],
                'n_timeouts': beat_data['n_timeouts'],
                'duration_hours': round(duration_hrs, 2),
                'n_valid_minutes': int(n_valid),
                'n_total_minutes': len(df_hr),
                'n_valid_wearable_pts': int(n_valid_wearable),
                'n_total_wearable_pts': len(df_wearable),
                'mean_hr': round(df_hr['avg_hr'].mean(), 2),
            })

            n_success += 1
            logger.info(
                f"  OK: {beat_data['n_normal_beats']} normal beats, "
                f"{duration_hrs:.1f} hrs, "
                f"{n_valid}/{len(df_hr)} valid minutes, "
                f"{n_valid_wearable}/{len(df_wearable)} wearable points"
            )

        except Exception as e:
            logger.error(f"  FAILED: {record_id} — {e}")
            n_fail += 1
            summary_records.append({
                'record_id': record_id,
                'status': f'error: {str(e)[:100]}',
                'n_total_beats': np.nan,
                'n_normal_beats': np.nan,
                'n_timeouts': np.nan,
                'duration_hours': np.nan,
                'n_valid_minutes': np.nan,
                'n_total_minutes': np.nan,
                'n_valid_wearable_pts': np.nan,
                'n_total_wearable_pts': np.nan,
                'mean_hr': np.nan,
            })

    # Save processing summary
    df_summary = pd.DataFrame(summary_records)
    df_summary.to_csv(output_dir / "processing_summary.csv", index=False)

    logger.info(f"\n{'='*60}")
    logger.info(f"DONE: {n_success} succeeded, {n_fail} failed out of {len(ann_files)}")
    logger.info(f"Summary saved to: {output_dir / 'processing_summary.csv'}")
    logger.info(f"{'='*60}")

    return df_summary


MINUTES_24H = 1440  # 24 hours × 60 minutes


def build_aligned_panel(databases, output_root):
    """
    Build a single long-format DataFrame with the last 24 hours of
    1-min HR data for every subject across all databases, aligned
    at the minute level (t = 0..1439).

    For recordings > 24 hrs (e.g., ESRD 48-hr): takes the LAST 24 hrs.
    For recordings < 24 hrs: includes all data starting at t=0 and
    pads the remaining minutes with NaN.

    Also produces a modulo-5 wearable-resolution version.
    """
    all_rows = []

    for db in databases:
        db_name = db['name']
        condition = db['condition']
        db_output_dir = output_root / db_name

        # Find all per-subject 1-min CSVs
        hr_files = sorted(db_output_dir.glob("*_hr_1min.csv"))
        print(f"  {db_name} ({condition}): {len(hr_files)} subjects")

        for fpath in hr_files:
            # Extract original subject ID from filename
            # Filename pattern: {orig_id}_hr_1min.csv
            orig_id = fpath.stem.replace("_hr_1min", "")
            subject_id = f"{db_name}_{orig_id}"

            df = pd.read_csv(fpath)

            if df.empty:
                continue

            n_minutes_available = len(df)

            if n_minutes_available >= MINUTES_24H:
                # Take the LAST 24 hours
                df_24h = df.iloc[-MINUTES_24H:].copy()
                df_24h = df_24h.reset_index(drop=True)
                df_24h['t'] = np.arange(MINUTES_24H)
                truncated = False
                recording_hrs = n_minutes_available / 60
            else:
                # Shorter than 24 hrs: keep all, pad with NaN
                df_short = df.copy()
                df_short = df_short.reset_index(drop=True)
                df_short['t'] = np.arange(n_minutes_available)

                # Create padding rows
                n_pad = MINUTES_24H - n_minutes_available
                pad = pd.DataFrame({
                    't': np.arange(n_minutes_available, MINUTES_24H),
                    'avg_hr': np.nan,
                    'median_hr': np.nan,
                    'sd_hr': np.nan,
                    'sdnn_ms': np.nan,
                    'rmssd_ms': np.nan,
                    'beat_count': 0,
                    'valid': False,
                })
                # Carry forward any columns from df not in pad
                for col in df_short.columns:
                    if col not in pad.columns and col != 't':
                        pad[col] = np.nan

                df_24h = pd.concat([df_short, pad], ignore_index=True)
                truncated = True
                recording_hrs = n_minutes_available / 60

            # Add identifying columns
            df_24h['id'] = subject_id
            df_24h['orig_id'] = orig_id
            df_24h['dataset'] = db_name
            df_24h['condition'] = condition
            df_24h['recording_hours'] = round(recording_hrs, 2)
            df_24h['used_last_24h'] = not truncated

            all_rows.append(df_24h)

    if not all_rows:
        print("WARNING: No data found to combine.")
        return pd.DataFrame(), pd.DataFrame()

    # Combine into single long-format panel
    col_order = [
        'id', 'orig_id', 'dataset', 'condition',
        't', 'avg_hr', 'median_hr', 'sd_hr',
        'sdnn_ms', 'rmssd_ms', 'beat_count', 'valid',
        'recording_hours', 'used_last_24h',
    ]
    panel = pd.concat(all_rows, ignore_index=True)

    # Reorder columns: known columns first, then any extras
    known = [c for c in col_order if c in panel.columns]
    extra = [c for c in panel.columns if c not in col_order]
    panel = panel[known + extra]

    # Sort by dataset, subject, time
    panel = panel.sort_values(['dataset', 'id', 't']).reset_index(drop=True)

    # Wearable version: every 5th minute
    panel_wearable = panel[panel['t'] % 5 == 0].copy().reset_index(drop=True)

    # Save
    out_full = output_root / "panel_24h_1min.csv"
    out_wear = output_root / "panel_24h_wearable5.csv"
    panel.to_csv(out_full, index=False)
    panel_wearable.to_csv(out_wear, index=False)

    # Summary
    n_subjects = panel['id'].nunique()
    n_rows = len(panel)
    print(f"\n  Combined panel: {n_subjects} subjects × {MINUTES_24H} minutes = {n_rows} rows")
    print(f"  Wearable panel: {len(panel_wearable)} rows")

    by_condition = panel.groupby('condition')['id'].nunique()
    print(f"  By condition: {dict(by_condition)}")

    short = panel.groupby('id')['used_last_24h'].first()
    n_short = (~short).sum()
    if n_short > 0:
        short_ids = short[~short].index.tolist()
        print(f"  WARNING: {n_short} subjects had < 24 hrs (padded with NaN):")
        for sid in short_ids[:10]:  # show first 10
            hrs = panel.loc[panel['id'] == sid, 'recording_hours'].iloc[0]
            print(f"    {sid}: {hrs} hrs")
        if n_short > 10:
            print(f"    ... and {n_short - 10} more")

    print(f"\n  Saved: {out_full}")
    print(f"  Saved: {out_wear}")

    return panel, panel_wearable


# ============================================================
# RUN
# ============================================================
if __name__ == "__main__":
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    # --- Phase 1: Process each database → per-subject CSVs ---
    all_summaries = []
    for db in DATABASES:
        ds_info = f" → downsampled to {db['downsample_to_fs']} Hz" if db.get('downsample_to_fs') else ""
        print(f"\n{'='*60}")
        print(f"Processing database: {db['name']} — {db['condition']} (fs={db['fs']} Hz{ds_info})")
        print(f"{'='*60}")
        output_dir = OUTPUT_ROOT / db['name']
        summary = process_all_files(
            ann_dir=db['ann_dir'],
            output_dir=output_dir,
            fs=db['fs'],
            min_beats=MIN_BEATS_PER_MINUTE,
            hr_min=HR_MIN,
            hr_max=HR_MAX,
            save_rr=SAVE_RR_DATA,
            downsample_to_fs=db.get('downsample_to_fs'),
        )
        summary['database'] = db['name']
        summary['condition'] = db['condition']
        summary['fs'] = db['fs']
        summary['downsampled_to'] = db.get('downsample_to_fs', None)
        all_summaries.append(summary)

    # Combined per-database summary
    df_all = pd.concat(all_summaries, ignore_index=True)
    df_all.to_csv(OUTPUT_ROOT / "combined_processing_summary.csv", index=False)
    print(f"\nPer-subject summary: {OUTPUT_ROOT / 'combined_processing_summary.csv'}")

    # --- Phase 2: Build aligned 24-hr panels ---
    print(f"\n{'='*60}")
    print("Building aligned 24-hr panels...")
    print(f"{'='*60}")
    panel, panel_wearable = build_aligned_panel(DATABASES, OUTPUT_ROOT)
    print(f"\nDone.")

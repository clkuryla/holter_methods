# CLAUDE.md — holter_methods

## Project Overview

Research project analyzing 24-hour Holter ECG recordings. Extracts time series metrics and complexity features (catch22, approximate/sample/permutation entropy) across multiple databases:

- **SHAREE** (PhysioNet): hypertension study with BP metadata
- **PhysioNet CHAOS**: AF, CHF, Normal sinus rhythm
- **THEW** (E-HOL databases): CAD, ESRD, Healthy controls

Project is in progress and evolving.

Goal: compare heart rate complexity metrics to quantify health using statistical methods. Very focused on downsampled HR data to eventually compare to wearables.

## Architecture & Data Flow

Three-stage pipeline:

1. **Raw ECG → Beat extraction**: `holter_sharee_1.R` (RHRV/WFDB for SHAREE), `thew_ann_to_hr.py` (binary .ann parsing for THEW)
2. **Windowed aggregation**: Downsample beat-level RR intervals into 1-minute and 5-minute average HR time series (stored as CSVs in `data_processed/`)
3. **Feature extraction & analysis**: `hr_metric_calc_1.R` computes catch22 + entropy features per subject; `cross_apply_pca.R` trains PCA on one dataset and projects others
4. Project is evolving, more to come.

### Key Dependencies

- **R**: tidyverse, RHRV, Rcatch22, pracma (approx/sample entropy), statcomp (permutation entropy)
- **Python**: numpy, pandas, struct, pathlib, logging

## Key Files

| File | Purpose |
|------|---------|
| `code/holter_sharee_1.R` | Load SHAREE ECG data via RHRV, classify hypertension, downsample to 1min/5min |
| `code/hr_metric_calc_1.R` | `calculate_metrics()` function: catch22 + descriptive stats + entropy per subject |
| `code/feature_extraction_20250328.R` | Feature extraction with catch22 and entropy (earlier version) |
| `code/cross_apply_pca.R` | `project_pca_loadings()`: train PCA on one dataset, project onto another |
| `src/python/thew_ann_to_hr.py` | Parse THEW binary .ann files → RR intervals → 1-min HR time series |

## Conventions

- **Windowing**: Standard aggregation windows are 1-minute averages and 5 minute samples of the 1 minute average (1 minute averages modulo 5).
- **R style**: Tidyverse piping (`%>%`), `group_by`/`summarize` patterns. Uses `Rcatch22::catch22_all()` with `catch24 = TRUE`.
- **Python style**: pathlib for paths, logging module for output, struct for binary parsing.

## Coding expectations
- Prefer minimal diffs over rewrites.
- If in R, Prefer tidyverse unless base R is clearer.
- Be explicit about NA handling. Do not introduce broad `drop_na()`/`complete.cases()` changes or equivalent.
- When refactoring, preserve output column names, units, and grouping level unless explicitly told otherwise.
- Add small guardrail checks for required columns, ranges, and dataset identifiers rather than silently coercing.


# Scientific project instructions

- If uncertain, ask in the response instead of guessing.
- Never change statistical intent without being explicitly asked.
  If a requested code change could alter the estimator, test, or model meaning, ask for clarification in the response.
- Write code to be reproducible:
  - use set.seed() or equivalent when randomness is involved
  - avoid absolute paths; prefer here::here() or data_depot or derived_path from R/paths.R if possible
  - keep functions pure where possible (no hidden global state)
- Be explicit about NA handling (na.rm=, drop_na vs replace_na, etc).
- When refactoring, preserve outputs: same columns, same units, same grouping.
  If you must change them, explain the change and why.
- When doing analyses (not final paper Figure generation) Add minimal checks (stopifnot/assertthat) around assumptions that could silently break.
- Encourage small functions, explicit inputs/outputs, informative errors, and reproducible scripts.

# Instructions — Scientific workflow

- This is a scientific analysis repo.
- Never change statistical intent, estimators, contrasts, or inclusion/exclusion rules unless explicitly requested. If there is something better, suggest it.
- Preserve output shape: column names, types, units, row counts (unless asked), NA handling.
- Be explicit about NA handling and grouping behavior.
- Prefer minimal diffs over rewrites.
- If uncertain, ask questions in the response instead of guessing.
- If a change could alter results, ask instead of guessing.
- Refactors must preserve outputs unless explicitly told otherwise.
- During exploratory and sensitivity analyses, add small checks (rlang::abort/stopifnot) around fragile assumptions.

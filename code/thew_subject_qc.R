# code/thew_subject_qc.R
# THEW Subject Quality Control — filter subjects by data completeness
#
# Reads 1-min panel and processing summary (read-only), computes per-subject
# quality metrics, applies configurable filters, and saves filtered ID lists.
#
# Outputs (to data_processed/thew/qc/):
#   thew_qc_summary.csv            — full per-subject quality table (all subjects)
#   thew_ids_miss10.csv             — IDs passing all filters at 10% missingness
#   thew_ids_miss15.csv             — IDs passing all filters at 15% missingness
#   thew_ids_miss20.csv             — IDs passing all filters at 20% missingness

library(tidyverse)
library(here)

# --- Parameters ---------------------------------------------------------------
MISS_THRESHOLDS  <- c(10, 15, 20)       # % missing allowed
MIN_RECORDING_HR <- 20                   # minimum recording hours
HR_MEAN_RANGE    <- c(40, 150)           # plausible mean HR range (bpm)
EXPECTED_MINUTES <- 1440L                # 24h at 1-min resolution

# --- Load data ----------------------------------------------------------------
panel <- read_csv(
  here("data_processed/thew/hr_timeseries_1min/panel_24h_1min.csv"),
  show_col_types = FALSE
)

proc <- read_csv(
  here("data_processed/thew/hr_timeseries_1min/combined_processing_summary.csv"),
  show_col_types = FALSE
)

# --- Guardrail checks ---------------------------------------------------------
stopifnot(
  "Panel must have columns: id, orig_id, dataset, condition, avg_hr, valid" =
    all(c("id", "orig_id", "dataset", "condition", "avg_hr", "valid") %in% names(panel)),
  "Processing summary must have columns: record_id, database, duration_hours, n_normal_beats, n_total_beats, mean_hr" =
    all(c("record_id", "database", "duration_hours", "n_normal_beats",
          "n_total_beats", "mean_hr") %in% names(proc))
)

# Ensure valid column is logical (it comes in as "True"/"False" strings)
if (is.character(panel$valid)) {
  panel <- panel %>%
    mutate(valid = tolower(valid) == "true")
}

# Check each subject has exactly EXPECTED_MINUTES rows
rows_per_subject <- panel %>% count(id) %>% pull(n)
if (!all(rows_per_subject == EXPECTED_MINUTES)) {
  bad <- panel %>% count(id) %>% filter(n != EXPECTED_MINUTES)
  warning(
    sprintf(
      "%d subject(s) do not have exactly %d rows: %s",
      nrow(bad), EXPECTED_MINUTES,
      paste(head(bad$id, 5), collapse = ", ")
    )
  )
}

# --- Compute per-subject quality metrics from panel ---------------------------

# Helper: longest run of consecutive TRUE values in a logical vector
max_consecutive_true <- function(x) {
  if (!any(x, na.rm = TRUE)) return(0L)
  r <- rle(x)
  max(r$lengths[r$values], na.rm = TRUE)
}

panel_qc <- panel %>%
  group_by(id, orig_id, dataset, condition) %>%
  summarize(
    n_total_min   = n(),
    n_invalid     = sum(is.na(avg_hr) | !valid, na.rm = FALSE),
    n_valid_min   = sum(valid & !is.na(avg_hr), na.rm = FALSE),
    pct_missing   = n_invalid / EXPECTED_MINUTES * 100,
    mean_hr_panel = mean(avg_hr[valid & !is.na(avg_hr)], na.rm = TRUE),
    max_consec_missing = max_consecutive_true(is.na(avg_hr) | !valid),
    .groups = "drop"
  )

# --- Merge with processing summary -------------------------------------------
proc_selected <- proc %>%
  select(
    record_id, database, duration_hours,
    n_normal_beats, n_total_beats,
    mean_hr_proc = mean_hr
  ) %>%
  mutate(
    pct_normal_beats = ifelse(
      n_total_beats > 0,
      n_normal_beats / n_total_beats * 100,
      NA_real_
    )
  )

qc <- panel_qc %>%
  left_join(
    proc_selected,
    by = c("orig_id" = "record_id", "dataset" = "database")
  )

# Use processing summary mean_hr if available, else fall back to panel
qc <- qc %>%
  mutate(
    recording_hours = duration_hours,
    mean_hr = coalesce(mean_hr_proc, mean_hr_panel)
  )

# Check join completeness
n_no_proc <- sum(is.na(qc$recording_hours))
if (n_no_proc > 0) {
  warning(sprintf("%d subject(s) had no match in processing summary.", n_no_proc))
}

# --- Apply filters & build pass flags ----------------------------------------

# Fixed filters (applied at all thresholds)
qc <- qc %>%
  mutate(
    pass_duration = recording_hours >= MIN_RECORDING_HR,
    pass_hr_range = mean_hr >= HR_MEAN_RANGE[1] & mean_hr <= HR_MEAN_RANGE[2]
  )

# Add a pass flag for each missingness threshold
for (thr in MISS_THRESHOLDS) {
  col_name <- paste0("pass_", thr, "pct")
  qc <- qc %>%
    mutate(
      !!col_name := pass_duration & pass_hr_range & (pct_missing <= thr)
    )
}

# --- Select and order output columns -----------------------------------------
output_cols <- c(
  "id", "orig_id", "dataset", "condition",
  "n_valid_min", "n_total_min", "pct_missing", "max_consec_missing",
  "recording_hours", "mean_hr", "pct_normal_beats",
  "pass_duration", "pass_hr_range",
  paste0("pass_", MISS_THRESHOLDS, "pct")
)

qc_out <- qc %>% select(all_of(output_cols))

# --- Save outputs -------------------------------------------------------------
out_dir <- here("data_processed/thew/qc")
dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)

# Full QC summary
write_csv(qc_out, file.path(out_dir, "thew_qc_summary.csv"))
cat(sprintf("Wrote QC summary: %d subjects\n", nrow(qc_out)))

# Filtered ID lists for each threshold
id_cols <- c("id", "orig_id", "dataset", "condition")

for (thr in MISS_THRESHOLDS) {
  flag_col <- paste0("pass_", thr, "pct")
  ids <- qc_out %>%
    filter(.data[[flag_col]]) %>%
    select(all_of(id_cols))
  fname <- sprintf("thew_ids_miss%d.csv", thr)
  write_csv(ids, file.path(out_dir, fname))
  cat(sprintf("Wrote %s: %d subjects\n", fname, nrow(ids)))
}

# --- Print diagnostic summary ------------------------------------------------
cat("\n=== THEW Subject QC Diagnostic Summary ===\n\n")
cat(sprintf("Total subjects: %d\n", nrow(qc_out)))
cat(sprintf("Excluded by recording duration (< %d h): %d\n",
            MIN_RECORDING_HR, sum(!qc_out$pass_duration, na.rm = TRUE)))
cat(sprintf("Excluded by mean HR outside [%d, %d] bpm: %d\n",
            HR_MEAN_RANGE[1], HR_MEAN_RANGE[2],
            sum(!qc_out$pass_hr_range, na.rm = TRUE)))

cat("\nSubjects retained per condition per threshold:\n")
for (thr in MISS_THRESHOLDS) {
  flag_col <- paste0("pass_", thr, "pct")
  tbl <- qc_out %>%
    filter(.data[[flag_col]]) %>%
    count(condition, name = "n")
  total <- sum(tbl$n)
  cat(sprintf("\n  Missingness <= %d%%  (total: %d)\n", thr, total))
  for (i in seq_len(nrow(tbl))) {
    cat(sprintf("    %-10s %d\n", tbl$condition[i], tbl$n[i]))
  }
}

cat("\nMissingness distribution (all subjects):\n")
cat(sprintf("  Median: %.1f%%\n", median(qc_out$pct_missing, na.rm = TRUE)))
cat(sprintf("  Mean:   %.1f%%\n", mean(qc_out$pct_missing, na.rm = TRUE)))
cat(sprintf("  Max:    %.1f%%\n", max(qc_out$pct_missing, na.rm = TRUE)))
cat(sprintf("  Subjects with 0%% missing: %d\n",
            sum(qc_out$pct_missing == 0, na.rm = TRUE)))

cat("\nDone.\n")

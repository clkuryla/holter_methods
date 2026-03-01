# thew_metric_calc.R
#
# Calculate heart rate complexity metrics (catch22/24, descriptive stats, entropy)
# for THEW Holter data across three cohorts: CAD (t002), Healthy (t003), ESRD (t016).
#
# Inputs:
#   - 1-min and 5-min (wearable) HR panels from data_processed/thew/
#   - QC-filtered subject IDs (<=10% missing)
#   - Clinical metadata
#
# Filtering: all valid minutes for CAD/Healthy; ESRD restricted to last 24h
#   (ESRD recordings are 48h, we use only the final day)
#
# Outputs:
#   - results/thew/thew_metrics_1min.csv
#   - results/thew/thew_metrics_5min.csv

library(tidyverse)
library(here)

source(here::here("src/R/calculate_metrics.R"))

# ---------------------------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------------------------

panel_1min <- read_csv(
  here("data_processed/thew/hr_timeseries_1min/panel_24h_1min.csv"),
  show_col_types = FALSE
)

panel_5min <- read_csv(
  here("data_processed/thew/hr_timeseries_1min/panel_24h_wearable5.csv"),
  show_col_types = FALSE
)

qc_ids <- read_csv(
  here("data_processed/thew/qc/thew_ids_miss10.csv"),
  show_col_types = FALSE
)

clinical_meta <- read_csv(
  here("data_processed/thew/hr_timeseries_1min/clinical_metadata_all.csv"),
  show_col_types = FALSE
)

cat("Loaded panel_1min:", nrow(panel_1min), "rows,",
    n_distinct(panel_1min$id), "subjects\n")
cat("Loaded panel_5min:", nrow(panel_5min), "rows,",
    n_distinct(panel_5min$id), "subjects\n")
cat("QC-passing subjects:", nrow(qc_ids), "\n")
cat("Clinical metadata:", nrow(clinical_meta), "subjects,",
    ncol(clinical_meta), "columns\n")

# ---------------------------------------------------------------------------
# 2. Filter to QC-passing, valid, last-24h rows
# ---------------------------------------------------------------------------

filter_panel <- function(panel, qc_ids) {
  panel %>%
    filter(
      id %in% qc_ids$id,
      valid == TRUE
    ) %>%
    # ESRD (t016) recordings are 48h; keep only the last 24h
    group_by(id) %>%
    filter(!(dataset == "t016" & used_last_24h == FALSE)) %>%
    ungroup()
}

panel_1min_filt <- filter_panel(panel_1min, qc_ids)
panel_5min_filt <- filter_panel(panel_5min, qc_ids)

cat("\nAfter filtering:\n")
cat("  1-min:", nrow(panel_1min_filt), "rows,",
    n_distinct(panel_1min_filt$id), "subjects\n")
cat("  5-min:", nrow(panel_5min_filt), "rows,",
    n_distinct(panel_5min_filt$id), "subjects\n")

# ---------------------------------------------------------------------------
# 3. Calculate HR metrics using calculate_hr_metrics()
# ---------------------------------------------------------------------------

group_cols <- c("id", "dataset", "condition")

cat("\nCalculating 1-min metrics...\n")
metrics_1min <- calculate_hr_metrics(
  df        = panel_1min_filt,
  hr_col    = "avg_hr",
  group_cols = group_cols,
  prefix    = "avg_hr"
)
cat("  Done:", nrow(metrics_1min), "subjects\n")

cat("Calculating 5-min metrics...\n")
metrics_5min <- calculate_hr_metrics(
  df        = panel_5min_filt,
  hr_col    = "avg_hr",
  group_cols = group_cols,
  prefix    = "avg_hr"
)
cat("  Done:", nrow(metrics_5min), "subjects\n")

# ---------------------------------------------------------------------------
# 4. Per-subject mean HRV columns (simple means of windowed values)
# ---------------------------------------------------------------------------

compute_mean_hrv <- function(panel) {
  panel %>%
    group_by(id) %>%
    summarize(
      mean_sdnn_ms   = mean(sdnn_ms,   na.rm = TRUE),
      mean_rmssd_ms  = mean(rmssd_ms,  na.rm = TRUE),
      mean_median_hr = mean(median_hr, na.rm = TRUE),
      mean_sd_hr     = mean(sd_hr,     na.rm = TRUE),
      mean_beat_count = mean(beat_count, na.rm = TRUE),
      .groups = "drop"
    )
}

hrv_means_1min <- compute_mean_hrv(panel_1min_filt)
hrv_means_5min <- compute_mean_hrv(panel_5min_filt)

metrics_1min <- metrics_1min %>% left_join(hrv_means_1min, by = "id")
metrics_5min <- metrics_5min %>% left_join(hrv_means_5min, by = "id")

# ---------------------------------------------------------------------------
# 5. Join with clinical metadata
# ---------------------------------------------------------------------------

# Drop dataset/condition from metadata to avoid .x/.y duplication on join
meta_join <- clinical_meta %>%
  select(-any_of(c("orig_id", "dataset", "condition")))

metrics_1min <- metrics_1min %>% left_join(meta_join, by = "id")
metrics_5min <- metrics_5min %>% left_join(meta_join, by = "id")

# ---------------------------------------------------------------------------
# 6. Create condition4 column (CAD split by diabetes status)
# ---------------------------------------------------------------------------

add_condition4 <- function(df) {
  df %>%
    mutate(
      condition4 = case_when(
        condition == "CAD" & DIABETES %in% c(1, 2) ~ "CAD_Diabetes",
        condition == "CAD"                          ~ "CAD",
        TRUE                                        ~ condition
      )
    )
}

metrics_1min <- add_condition4(metrics_1min)
metrics_5min <- add_condition4(metrics_5min)

# ---------------------------------------------------------------------------
# 7. Sanity checks
# ---------------------------------------------------------------------------

cat("\n--- Sanity Checks ---\n")

cat("\n1-min metrics: condition counts\n")
print(count(metrics_1min, dataset, condition, condition4))

cat("\n5-min metrics: condition counts\n")
print(count(metrics_5min, dataset, condition, condition4))

# Check key metric columns for NAs
key_metric_cols <- c("avg_hr_mean", "avg_hr_sd", "avg_hr_apen",
                     "avg_hr_sampen", "avg_hr_permen")
existing_key_cols <- intersect(key_metric_cols, colnames(metrics_1min))

cat("\nNA counts in key 1-min metric columns:\n")
print(colSums(is.na(metrics_1min[existing_key_cols])))

cat("\nInf counts in 1-min metric columns:\n")
metric_cols_1min <- grep("^avg_hr_|^mean_", colnames(metrics_1min), value = TRUE)
inf_counts <- sapply(metrics_1min[metric_cols_1min], function(x) sum(is.infinite(x)))
if (any(inf_counts > 0)) {
  print(inf_counts[inf_counts > 0])
} else {
  cat("  None\n")
}

# ---------------------------------------------------------------------------
# 8. Write results
# ---------------------------------------------------------------------------

write_csv(metrics_1min, here("results/thew/thew_metrics_1min.csv"))
write_csv(metrics_5min, here("results/thew/thew_metrics_5min.csv"))

cat("\nResults written to:\n")
cat("  results/thew/thew_metrics_1min.csv (", nrow(metrics_1min), "rows)\n")
cat("  results/thew/thew_metrics_5min.csv (", nrow(metrics_5min), "rows)\n")

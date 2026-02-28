# combine_thew_metadata_all.R
#
# Combine t016 (ESRD) harmonized metadata with t002/t003 (CAD/Healthy) metadata
# into a unified CSV for all THEW datasets.
#
# Inputs:
#   data_processed/thew/hr_timeseries_1min/clinical_metadata_t002_t003.csv  (473 rows)
#   data_processed/thew/hr_timeseries_1min/clinical_metadata_t016.csv       (56 rows)
#
# Output:
#   data_processed/thew/hr_timeseries_1min/clinical_metadata_all.csv

library(dplyr)
library(here)

# ---- paths ----
base_dir <- here("data_processed", "thew", "hr_timeseries_1min")

t002_t003_path <- file.path(base_dir, "clinical_metadata_t002_t003.csv")
t016_path      <- file.path(base_dir, "clinical_metadata_t016.csv")
out_path       <- file.path(base_dir, "clinical_metadata_all.csv")

stopifnot(file.exists(t002_t003_path), file.exists(t016_path))

# ---- read ----
t002_t003 <- read.csv(t002_t003_path, stringsAsFactors = FALSE)
t016      <- read.csv(t016_path, stringsAsFactors = FALSE)

cat("t002/t003:", nrow(t002_t003), "rows,", ncol(t002_t003), "cols\n")
cat("t016:     ", nrow(t016), "rows,", ncol(t016), "cols\n")

stopifnot(nrow(t002_t003) == 473, nrow(t016) == 56)

# ---- drop t016 raw source columns before combining ----
# Keep only harmonized columns from t016 (drop C_F* and raw-only cols).
# The raw columns are preserved in clinical_metadata_t016.csv and
# clinical_metadata_t016_raw.csv for reference.
t016_raw_cols <- grep("^C_F|^Age$", names(t016), value = TRUE)
t016_clean <- t016 %>% select(-all_of(t016_raw_cols))

cat("t016 after dropping raw cols:", ncol(t016_clean), "cols\n")

# ---- identify shared vs dataset-specific columns ----
shared_cols   <- intersect(names(t002_t003), names(t016_clean))
only_t002_t003 <- setdiff(names(t002_t003), names(t016_clean))
only_t016      <- setdiff(names(t016_clean), names(t002_t003))

cat("\nShared columns (", length(shared_cols), "):", paste(sort(shared_cols), collapse = ", "), "\n")
cat("t002/t003-only (", length(only_t002_t003), "):", paste(sort(only_t002_t003), collapse = ", "), "\n")
cat("t016-only (", length(only_t016), "):", paste(sort(only_t016), collapse = ", "), "\n")

# ---- combine with bind_rows (non-shared columns filled with NA) ----
combined <- bind_rows(t002_t003, t016_clean)

# ---- column ordering: id cols, shared harmonized, dataset-specific alphabetically ----
id_cols <- c("id", "orig_id", "dataset", "condition")
harmonized_core <- sort(setdiff(shared_cols, id_cols))
extra_cols <- sort(c(only_t002_t003, only_t016))

combined <- combined %>%
  select(all_of(id_cols), all_of(harmonized_core), all_of(extra_cols))

# ---- checks ----
stopifnot(nrow(combined) == 473 + 56)
stopifnot(!anyDuplicated(combined$id))
stopifnot(all(combined$dataset %in% c("t002", "t003", "t016")))

# ---- write ----
write.csv(combined, out_path, row.names = FALSE)

# ---- summary ----
cat("\n--- Summary ---\n")
cat("Output:", out_path, "\n")
cat("Total rows:", nrow(combined), "\n")
cat("Total cols:", ncol(combined), "\n")
cat("\nRows per dataset/condition:\n")
print(table(combined$dataset, combined$condition))

cat("\nHarmonized variable coverage (non-NA counts by dataset):\n")
coverage <- combined %>%
  group_by(dataset) %>%
  summarise(
    n         = n(),
    AGE       = sum(!is.na(AGE)),
    GENDER    = sum(!is.na(GENDER)),
    RACE      = sum(!is.na(RACE)),
    SMOKING   = sum(!is.na(SMOKING)),
    BP_SYST   = sum(!is.na(BP_SYST)),
    BP_DIAST  = sum(!is.na(BP_DIAST)),
    HEIGHT    = sum(!is.na(HEIGHT)),
    WEIGHT    = sum(!is.na(WEIGHT)),
    BMI       = sum(!is.na(BMI)),
    DIABETES  = sum(!is.na(DIABETES)),
    HYPERTEN  = sum(!is.na(HYPERTEN)),
    CHF       = sum(!is.na(CHF)),
    .groups   = "drop"
  )
print(as.data.frame(coverage))

cat("\nFirst few IDs per dataset:\n")
for (ds in c("t002", "t003", "t016")) {
  ids <- head(combined$id[combined$dataset == ds], 3)
  cat(ds, ":", paste(ids, collapse = ", "), "\n")
}

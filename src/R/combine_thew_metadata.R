# combine_thew_metadata.R
#
# Harmonize THEW t002 (CAD) and t003 (Healthy) clinical metadata into a single
# CSV that can be joined to the panel HR time-series data.
#
# Inputs:
#   data_processed/thew/hr_timeseries_1min/clinicalData_t002/E-HOL-03-0271-002.xls
#   data_processed/thew/hr_timeseries_1min/clinicalData_t003/E-HOL-03-0202-003.xls
#
# Output:
#   data_processed/thew/hr_timeseries_1min/clinical_metadata_t002_t003.csv

library(readxl)
library(dplyr)
library(here)

# ---- paths ----
base_dir <- here("data_processed", "thew", "hr_timeseries_1min")

t002_path <- file.path(base_dir, "clinicalData_t002", "E-HOL-03-0271-002.xls")
t003_path <- file.path(base_dir, "clinicalData_t003", "E-HOL-03-0202-003.xls")
out_path  <- file.path(base_dir, "clinical_metadata_t002_t003.csv")

stopifnot(file.exists(t002_path), file.exists(t003_path))

# ---- read ----
t002 <- read_xls(t002_path, sheet = "ANALYSIS")
t003 <- read_xls(t003_path, sheet = "ANALYSIS")

cat("t002:", nrow(t002), "rows,", ncol(t002), "cols\n")
cat("t003:", nrow(t003), "rows,", ncol(t003), "cols\n")

stopifnot(nrow(t002) == 271, nrow(t003) == 202)

# ---- add panel-compatible ID columns ----
t002 <- t002 %>%
  mutate(
    orig_id   = as.character(ID),
    dataset   = "t002",
    id        = paste0(dataset, "_", orig_id),
    condition = "CAD"
  ) %>%
  select(-ID)

t003 <- t003 %>%
  mutate(
    orig_id   = as.character(ID),
    dataset   = "t003",
    id        = paste0(dataset, "_", orig_id),
    condition = "Healthy"
  ) %>%
  select(-ID)

# ---- standardize REG_DATE before binding ----
# t002 REG_DATE is all-NA logical; t003 REG_DATE is POSIXct.
# Coerce both to character so bind_rows doesn't error.
t002 <- t002 %>% mutate(REG_DATE = as.character(REG_DATE))
t003 <- t003 %>% mutate(REG_DATE = as.character(REG_DATE))

# ---- combine ----
combined <- bind_rows(t002, t003)

# ---- column ordering: id columns first, then clinical alphabetically ----
id_cols      <- c("id", "orig_id", "dataset", "condition")
clinical_cols <- sort(setdiff(names(combined), id_cols))
combined <- combined %>% select(all_of(id_cols), all_of(clinical_cols))

stopifnot(nrow(combined) == 473)
stopifnot(!anyDuplicated(combined$id))

# ---- write ----
write.csv(combined, out_path, row.names = FALSE)

# ---- summary ----
cat("\n--- Summary ---\n")
cat("Output:", out_path, "\n")
cat("Total rows:", nrow(combined), "\n")
cat("Total cols:", ncol(combined), "\n")
cat("Rows per dataset:\n")
print(table(combined$dataset, combined$condition))
cat("\nFirst few IDs:\n")
cat(head(combined$id, 5), sep = "\n")
cat("\n")

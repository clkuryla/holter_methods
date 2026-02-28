# combine_thew_metadata_t016.R
#
# Extract and harmonize THEW t016 (ESRD) clinical metadata from 3 Excel files
# into a single CSV with column names matching the t002/t003 convention.
#
# Inputs (all in data_processed/thew/hr_timeseries_1min/clinicalData_t016/):
#   Enrollment_Confirmation.xls  — demographics (age, gender, diabetes, hypertension)
#   Baseline Med Eval.xls        — race, smoking, CHF/NYHA class
#   Dialysis_Treatment.xls       — vitals (BP, height, weight)
#
# Outputs:
#   data_processed/thew/hr_timeseries_1min/clinical_metadata_t016_raw.csv
#   data_processed/thew/hr_timeseries_1min/clinical_metadata_t016.csv

library(readxl)
library(dplyr)
library(here)

# ---- paths ----
base_dir    <- here("data_processed", "thew", "hr_timeseries_1min")
clinic_dir  <- file.path(base_dir, "clinicalData_t016")

enroll_path  <- file.path(clinic_dir, "Enrollment_Confirmation.xls")
baseline_path <- file.path(clinic_dir, "Baseline Med Eval.xls")
dialysis_path <- file.path(clinic_dir, "Dialysis_Treatment.xls")

out_raw_path  <- file.path(base_dir, "clinical_metadata_t016_raw.csv")
out_path      <- file.path(base_dir, "clinical_metadata_t016.csv")

stopifnot(
  file.exists(enroll_path),
  file.exists(baseline_path),
  file.exists(dialysis_path)
)

# ---- Step 1: Read the 3 Excel files and select variables of interest ----

enroll <- read_xls(enroll_path, sheet = "ClinicalPreview", skip = 4) %>%
  select(PATNO, Age, C_F1_4, C_F1_5, C_F1_6)

baseline <- read_xls(baseline_path, sheet = "ClinicalPreview", skip = 4) %>%
  select(PATNO, C_F2A21, C_F2A5A, C_F2A5B, C_F2A6)

dialysis <- read_xls(dialysis_path, sheet = "ClinicalPreview", skip = 4) %>%
  select(PATNO, C_F7_4A_SY, C_F7_4A_DI, C_F7_4C, C_F7_4D, C_F7_4E, C_F7_4F, C_F7_4G)

cat("Enrollment:", nrow(enroll), "rows\n")
cat("Baseline Med Eval:", nrow(baseline), "rows\n")
cat("Dialysis Treatment:", nrow(dialysis), "rows\n")

# ---- Step 2: Merge by PATNO (full join to keep all subjects) ----

master <- enroll %>%
  full_join(baseline, by = "PATNO") %>%
  full_join(dialysis, by = "PATNO") %>%
  arrange(PATNO)

cat("Master (full join):", nrow(master), "rows\n")

# ---- Step 3: Write raw master CSV ----

write.csv(master, out_raw_path, row.names = FALSE)
cat("Wrote raw master:", out_raw_path, "\n")

# ---- Step 4: Add harmonized columns ----

harmonized <- master %>%
  mutate(
    # ID columns
    id        = paste0("t016_", PATNO),
    orig_id   = as.character(PATNO),
    dataset   = "t016",
    condition = "ESRD",

    # Demographics
    AGE    = Age,
    GENDER = C_F1_4,                          # already 1=M, 2=F
    RACE   = case_when(
      C_F2A21 == 1 ~ 1L,                     # White
      C_F2A21 == 2 ~ 2L,                     # Black
      C_F2A21 == 9 ~ NA_integer_,            # Unknown → NA
      TRUE         ~ NA_integer_
    ),
    RACE_ORIG = C_F2A21,                      # preserve original coding

    # Smoking
    SMOKING      = C_F2A5B,                   # 0=No, 1=Yes (current)
    SMOKING_EVER = C_F2A5A,                   # 0=No, 1=Yes (ever)

    # Vitals
    BP_SYST  = C_F7_4A_SY,
    BP_DIAST = C_F7_4A_DI,
    HEIGHT   = C_F7_4C,                       # cm
    WEIGHT   = C_F7_4D,                       # kg (primary weight)
    WEIGHT_E = C_F7_4E,
    WEIGHT_F = C_F7_4F,
    WEIGHT_G = C_F7_4G,
    BMI      = C_F7_4D / (C_F7_4C / 100)^2,  # kg / m^2

    # Conditions
    DIABETES = case_when(
      C_F1_5 == 0            ~ 0L,           # No
      C_F1_5 %in% c(1, 2, 3) ~ 1L,          # Yes (any type)
      C_F1_5 == 9            ~ NA_integer_,  # Unknown → NA
      TRUE                   ~ NA_integer_
    ),
    DIABETES_TYPE = case_when(
      C_F1_5 == 0 ~ 0L,                      # No
      C_F1_5 == 1 ~ 1L,                      # Type I
      C_F1_5 == 2 ~ 2L,                      # Type II
      C_F1_5 == 3 ~ 3L,                      # Other
      C_F1_5 == 9 ~ NA_integer_,
      TRUE        ~ NA_integer_
    ),
    HYPERTEN = case_when(
      C_F1_6 == 1 ~ 1L,                      # Yes
      C_F1_6 == 2 ~ 0L,                      # No
      TRUE        ~ NA_integer_
    ),
    CHF = case_when(
      C_F2A6 == 0            ~ NA_integer_,  # No CHF → NA (matches t002/t003)
      C_F2A6 %in% c(1, 2, 3, 4) ~ as.integer(C_F2A6),  # NYHA class 1-4
      TRUE                   ~ NA_integer_
    )
  )

# ---- Step 5: Write harmonized CSV ----

# Column ordering: id columns first, harmonized, then raw alphabetically
id_cols        <- c("id", "orig_id", "dataset", "condition")
harmonized_cols <- c("AGE", "GENDER", "RACE", "RACE_ORIG",
                     "SMOKING", "SMOKING_EVER",
                     "BP_SYST", "BP_DIAST", "HEIGHT",
                     "WEIGHT", "WEIGHT_E", "WEIGHT_F", "WEIGHT_G", "BMI",
                     "DIABETES", "DIABETES_TYPE", "HYPERTEN", "CHF")
raw_cols       <- sort(setdiff(names(master), "PATNO"))  # raw cols alphabetically, drop PATNO (replaced by id)

harmonized <- harmonized %>%
  select(all_of(id_cols), all_of(harmonized_cols), all_of(raw_cols))

write.csv(harmonized, out_path, row.names = FALSE)
cat("Wrote harmonized:", out_path, "\n")

# ---- Step 6: Summary and checks ----

stopifnot(nrow(harmonized) == 56)
stopifnot(!anyDuplicated(harmonized$id))
stopifnot(all(grepl("^t016_", harmonized$id)))

cat("\n--- Summary ---\n")
cat("Output:", out_path, "\n")
cat("Total rows:", nrow(harmonized), "\n")
cat("Total cols:", ncol(harmonized), "\n")

cat("\nHarmonized variable distributions:\n")
cat("\nGENDER (1=M, 2=F):\n"); print(table(harmonized$GENDER, useNA = "ifany"))
cat("\nRACE (1=White, 2=Black):\n"); print(table(harmonized$RACE, useNA = "ifany"))
cat("\nSMOKING (0=No, 1=Yes current):\n"); print(table(harmonized$SMOKING, useNA = "ifany"))
cat("\nSMOKING_EVER (0=No, 1=Yes):\n"); print(table(harmonized$SMOKING_EVER, useNA = "ifany"))
cat("\nDIABETES (0=No, 1=Yes):\n"); print(table(harmonized$DIABETES, useNA = "ifany"))
cat("\nDIABETES_TYPE (0=No, 1=I, 2=II, 3=Other):\n"); print(table(harmonized$DIABETES_TYPE, useNA = "ifany"))
cat("\nHYPERTEN (0=No, 1=Yes):\n"); print(table(harmonized$HYPERTEN, useNA = "ifany"))
cat("\nCHF (1-4 NYHA):\n"); print(table(harmonized$CHF, useNA = "ifany"))
cat("\nAGE range:", range(harmonized$AGE, na.rm = TRUE), "\n")
cat("BMI range:", range(harmonized$BMI, na.rm = TRUE), "\n")
cat("BP_SYST range:", range(harmonized$BP_SYST, na.rm = TRUE), "\n")
cat("BP_DIAST range:", range(harmonized$BP_DIAST, na.rm = TRUE), "\n")

cat("\nFirst few IDs:\n")
cat(head(harmonized$id, 5), sep = "\n")
cat("\n")

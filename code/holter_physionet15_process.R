# holter_physionet15_process.R
#
# Process PhysioNet CHAOS dataset (15 subjects: 5 Normal, 5 CHF, 5 AF)
# into standardized 1-minute and 5-minute downsampled CSVs.
#
# Input:  *nn.txt files from data_big/physionet_15/is-the-normal-heart-rate-chaotic-1.0.0/
# Output: data_processed/physionet_15/physionet15_1min.csv
#         data_processed/physionet_15/physionet15_5min.csv

library(here)
library(tidyverse)

# --- Paths ----------------------------------------------------------------

data_dir <- here("data_big/physionet_15/is-the-normal-heart-rate-chaotic-1.0.0")
out_dir  <- here("data_processed/physionet_15")

if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)

# --- Read metadata from RECORDS.txt ----------------------------------------

records_raw <- read_lines(file.path(data_dir, "RECORDS.txt"))

# Parse the tab-delimited metadata (skip header, skip blanks and footer note)
records_meta <- read_tsv(
  file.path(data_dir, "RECORDS.txt"),
  col_names = c("file", "source_record", "sex", "age", "start_time"),
  skip = 1,               # skip header line
  na = c("", "NA"),
  col_types = cols(
    file         = col_character(),
    source_record = col_character(),
    sex          = col_character(),
    age          = col_integer(),
    start_time   = col_character()
  )
) %>%
  filter(!is.na(file), file != "") %>%
  # Map rr filenames to nn ids: n1rr.txt -> n1nn
  mutate(
    id = str_replace(tools::file_path_sans_ext(file), "rr$", "nn")
  ) %>%
  select(id, source_record, sex, age)

stopifnot("Expected 15 metadata rows" = nrow(records_meta) == 15)

# --- Read all *nn.txt files ------------------------------------------------

file_list <- list.files(data_dir, pattern = "nn\\.txt$", full.names = TRUE)
stopifnot("Expected 15 nn.txt files" = length(file_list) == 15)

combined_df <- file_list %>%
  set_names() %>%
  map_dfr(
    .f = ~ read_table(.x, col_names = c("ibi", "marker", "time_sec"),
                       col_types = cols(
                         ibi      = col_double(),
                         marker   = col_character(),
                         time_sec = col_double()
                       )),
    .id = "filename"
  ) %>%
  mutate(id = tools::file_path_sans_ext(basename(filename))) %>%
  select(id, time_sec, ibi)

# Assign condition based on filename prefix
combined_df <- combined_df %>%
  mutate(
    condition = case_when(
      str_starts(id, "n") ~ "Normal",
      str_starts(id, "c") ~ "CHF",
      str_starts(id, "a") ~ "AF",
      TRUE                ~ "Unknown"
    )
  )

stopifnot("No Unknown conditions" = !any(combined_df$condition == "Unknown"))

# Join metadata
combined_df <- combined_df %>%
  left_join(records_meta, by = "id")

stopifnot("All rows have source_record" = !any(is.na(combined_df$source_record)))

# --- 1-minute aggregation --------------------------------------------------

data_1min <- combined_df %>%
  arrange(id, time_sec) %>%
  mutate(
    minute_index = floor(time_sec / 60) + 1L   # 1-indexed to match SHAREE
  ) %>%
  group_by(id, condition, sex, age, source_record, minute_index) %>%
  summarize(
    mean_hr = mean(60 / ibi, na.rm = TRUE),
    sdnn    = sd(ibi, na.rm = TRUE),
    rmssd   = {
      diffs <- diff(ibi)
      sqrt(mean(diffs^2, na.rm = TRUE))
    },
    n_beats = n(),
    .groups = "drop"
  ) %>%
  mutate(minute_start_sec = (minute_index - 1L) * 60) %>%
  arrange(id, minute_index)

cat(sprintf("1-min data: %d rows, %d subjects\n", nrow(data_1min), n_distinct(data_1min$id)))

# --- 5-minute downsampling -------------------------------------------------

data_5min <- data_1min %>%
  filter(minute_index %% 5 == 0) %>%
  mutate(time_5min = minute_index / 5)

cat(sprintf("5-min data: %d rows, %d subjects\n", nrow(data_5min), n_distinct(data_5min$id)))

# --- Sanity checks ----------------------------------------------------------

stopifnot("15 unique subjects in 1min" = n_distinct(data_1min$id) == 15)
stopifnot("15 unique subjects in 5min" = n_distinct(data_5min$id) == 15)

# Check HR values are physiologically plausible
hr_range <- range(data_1min$mean_hr, na.rm = TRUE)
cat(sprintf("HR range: %.1f - %.1f bpm\n", hr_range[1], hr_range[2]))
if (hr_range[1] < 20 || hr_range[2] > 300) {
  warning("HR values outside expected physiological range (20-300 bpm)")
}

# --- Write output -----------------------------------------------------------

write_csv(data_1min, file.path(out_dir, "physionet15_1min.csv"))
write_csv(data_5min, file.path(out_dir, "physionet15_5min.csv"))

cat(sprintf("\nWrote:\n  %s\n  %s\n",
            file.path(out_dir, "physionet15_1min.csv"),
            file.path(out_dir, "physionet15_5min.csv")))

library(Rcatch22)


one_interval <- metrics_5_minute %>% 
  filter(id == "a1nn") %>% 
  pull(avg_hr)

metric_catch22 <- catch22_all(one_interval, catch24 = TRUE)


metric_catch22[1,1]


# --- Load required libraries ---
library(tidyverse)
library(catch22)
library(pracma)

results <- data_holter_downsampled %>%
  mutate(avg_hr = mean_hr) %>% 
  group_by(id, condition, status) %>%
  
  # Summarize to produce a list-column that stores:
  # 1) The catch22/catch24 features
  # 2) The descriptive stats in the same "names"/"values" format
  summarize(
    combined_stats = list(
      catch22_all(data = avg_hr, catch24 = TRUE) %>% 
        bind_rows(
          tibble(
            names = c("mean", "sd", "max", "min", "cv", "iqr", "median", "apen", "sampen"),
            values = c(
              mean(avg_hr, na.rm = TRUE),
              sd(avg_hr, na.rm = TRUE),
              max(avg_hr, na.rm = TRUE),
              min(avg_hr, na.rm = TRUE),
              # For coefficient of variation, check mean!=0 to avoid Inf/NaN
              sd(avg_hr, na.rm = TRUE) / mean(avg_hr, na.rm = TRUE),
              IQR(avg_hr, na.rm = TRUE),
              median(avg_hr, na.rm = TRUE),
              approx_entropy(mean_hr, edim = 2, r = 0.2 * sd(mean_hr, na.rm = TRUE)),
              sample_entropy(mean_hr, edim = 2, r = 0.2 * sd(mean_hr, na.rm = TRUE))
            )
          )
        )
    ),
    .groups = "drop"   # Ungroup after summarizing
  ) %>%
  
  # Unnest to convert your list-column into a long data frame
  unnest(cols = combined_stats) %>%
  
  # Pivot wide: each feature gets its own column
  pivot_wider(
    names_from = names,
    values_from = values
  )

# --- Example check of the resulting data ---
head(results)


# --- Optional: Look at the first few rows ---
head(results)

# --- Sanity checks ---
# 1) Ensure you have as many rows as you expect, i.e. one row per group
#    plus any expansions if you pivoted wide.
# 2) Check for missing or Inf values in your features 
#    (common for time-series feature extraction if the data has zeros, NAs, etc.).
# 3) Confirm that catch22/catch24 transformations make sense for your domain.


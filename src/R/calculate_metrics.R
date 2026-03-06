# calculate_metrics.R
#
# Reusable functions for computing time-series complexity metrics
# on heart rate data (or any numeric time series).
#
# Dependencies: Rcatch22, pracma, statcomp, dplyr, tidyr
#
# Usage:
#   source(here::here("src/R/calculate_metrics.R"))
#
#   # Single vector
#   calculate_metrics(some_numeric_vector)
#
#   # Full pipeline on a dataframe
#   hr_features <- calculate_hr_metrics(
#     df = data_sharee_5min,
#     hr_col = "mean_hr",
#     group_cols = c("id", "Gender", "Age", "HTN"),
#     prefix = "avg_hr"
#   )

library(Rcatch22)
library(pracma)
library(statcomp)
library(dplyr)
library(tidyr)

#' Calculate time-series metrics for a single numeric vector
#'
#' Returns a long tibble with columns `names` and `values` containing:
#'   - 24 catch22/catch24 features
#'   - 7 descriptive stats (mean, sd, max, min, cv, iqr, median)
#'   - 5 asymmetry/range/circadian metrics (max_minus_mean, mean_minus_min,
#'       max_minus_mean_rel, mean_minus_min_rel, iv)
#'   - 3 entropy measures (apen, sampen, permen)
#'
#' Entropy measures require at least 10 non-NA values; otherwise they return NA.
#'
#' @param data_vector Numeric vector (e.g., 1-min or 5-min average HR)
#' @return A tibble with columns `names` (character) and `values` (numeric)
calculate_metrics <- function(data_vector) {

  n_valid <- sum(!is.na(data_vector))
  vec_clean <- data_vector[!is.na(data_vector)]

  # Entropy measures need a reasonable number of observations
  if (n_valid >= 10) {
    sd_val <- sd(vec_clean, na.rm = TRUE)
    apen   <- pracma::approx_entropy(vec_clean, edim = 2, r = 0.2 * sd_val)
    sampen <- pracma::sample_entropy(vec_clean, edim = 2, r = 0.2 * sd_val)
    permen <- statcomp::permutation_entropy(vec_clean)
  } else {
    apen   <- NA_real_
    sampen <- NA_real_
    permen <- NA_real_
  }

  catch22_all(data = data_vector, catch24 = TRUE) %>%
    bind_rows(
      tibble(
        names = c("mean", "sd", "max", "min", "cv", "iqr", "median",
                   "max_minus_mean", "mean_minus_min",
                   "max_minus_mean_rel", "mean_minus_min_rel", "iv",
                   "apen", "sampen", "permen"),
        values = c(
          mean(data_vector, na.rm = TRUE),
          sd(data_vector, na.rm = TRUE),
          max(data_vector, na.rm = TRUE),
          min(data_vector, na.rm = TRUE),
          sd(data_vector, na.rm = TRUE) / mean(data_vector, na.rm = TRUE),
          IQR(data_vector, na.rm = TRUE),
          median(data_vector, na.rm = TRUE),
          max(data_vector, na.rm = TRUE) - mean(data_vector, na.rm = TRUE),
          mean(data_vector, na.rm = TRUE) - min(data_vector, na.rm = TRUE),
          (max(data_vector, na.rm = TRUE) - mean(data_vector, na.rm = TRUE)) / mean(data_vector, na.rm = TRUE),
          (mean(data_vector, na.rm = TRUE) - min(data_vector, na.rm = TRUE)) / mean(data_vector, na.rm = TRUE),
          if (n_valid >= 2) {
            v <- var(vec_clean)
            if (is.na(v) || v == 0) NA_real_ else mean(diff(vec_clean)^2) / v
          } else NA_real_,
          apen,
          sampen,
          permen
        )
      )
    )
}


#' Calculate HR metrics grouped by subject (wide-format output)
#'
#' Groups `df` by `group_cols`, applies `calculate_metrics()` to the
#' specified HR column within each group, and pivots to wide format
#' with column names prefixed by `prefix`.
#'
#' @param df        Dataframe with one row per subject per time point
#' @param hr_col    Name of the HR column (default "mean_hr")
#' @param group_cols Character vector of columns to group by
#'                   (e.g., c("id", "condition", "status"))
#' @param prefix    String prefix for output metric columns (default "avg_hr")
#' @return Wide dataframe: one row per group, with grouping columns +
#'         prefixed metric columns (e.g., avg_hr_mean, avg_hr_sd, ...)
calculate_hr_metrics <- function(df, hr_col = "mean_hr", group_cols, prefix = "avg_hr") {

  stopifnot(
    is.data.frame(df),
    hr_col %in% colnames(df),
    all(group_cols %in% colnames(df))
  )

  df %>%
    group_by(across(all_of(group_cols))) %>%
    summarize(
      .metrics = list(calculate_metrics(.data[[hr_col]])),
      .groups = "drop"
    ) %>%
    unnest(cols = .metrics) %>%
    pivot_wider(
      names_from  = names,
      values_from = values,
      names_prefix = paste0(prefix, "_")
    )
}

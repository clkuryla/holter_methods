library(Rcatch22)
library(pracma)
library(statcomp)

# Function to calculate all metrics for a single variable
calculate_metrics <- function(data_vector) {
  catch22_all(data = data_vector, catch24 = TRUE) %>% 
    bind_rows(
      tibble(
        names = c("mean", "sd", "max", "min", "cv", "iqr", "median", #),
        "apen", 
        "sampen", 
        "permen"), # "permenq", "permenrenyi"),
        values = c(
          mean(data_vector, na.rm = TRUE),
          sd(data_vector, na.rm = TRUE),
          max(data_vector, na.rm = TRUE),
          min(data_vector, na.rm = TRUE),
          # For coefficient of variation, check mean!=0 to avoid Inf/NaN
          sd(data_vector, na.rm = TRUE) / mean(data_vector, na.rm = TRUE),
          IQR(data_vector, na.rm = TRUE),
          median(data_vector, na.rm = TRUE),
          pracma::approx_entropy(data_vector, edim = 2, r = 0.2 * sd(data_vector, na.rm = TRUE)),
          pracma::sample_entropy(data_vector, edim = 2, r = 0.2 * sd(data_vector, na.rm = TRUE)),
          statcomp::permutation_entropy(data_vector)#, #permutation entropy
          #   statcomp::permutation_entropy_qlog(data_vector, q = 1.2), #This is a generalization of permutation entropy using the q-logarithm from non-extensive statistical mechanics: When q=1, it reduces to standard permutation entropy, When q<1, it emphasizes rare patterns, When q>1, it emphasizes common patterns
          #   statcomp::permutation_entropy_Renyi(data_vector, alpha = 2) #, #When α=1, it's equivalent to standard permutation entropy, Lower α values give more weight to rare patterns, Higher α values focus on dominant patterns
          #   statcomp::global_complexity(data_vector),
          #    statcomp::Abbe(data_vector)
        )
      )
    )
}

library(pracma)
pracma::sample_entropy(data_holter_downsampled_s %>% 
                         filter(id %in% c(2315)) %>% pull(mean_hr) %>% head(n=3000),
                       edim = 2, r = 0.2 * sd(data_holter_downsampled_s %>% 
                                                filter(id %in% c(2315)) %>% pull(mean_hr) %>% head(n=3000), na.rm = TRUE))



############### SHAREE

data_holter_downsampled_s <- data_sharee_5min

# data_holter_downsampled_clean_s <- data_sharee_5min %>%
#   filter(is.finite(sdnn), is.finite(rmssd), 
#          is.finite(mean_hr))

# Just apply to avg HR
new_method_hr_results_long_s <- data_holter_downsampled_s %>% 
# new_method_hr_results_long_s <- data_holter_downsampled_s %>%
  mutate(avg_hr = mean_hr) %>% 
  #  group_by(id, condition, status) %>% 
  select(id, Gender, Age, Smoker, SBP, DBP, vascular_event, HTN, Hypertension, avg_hr) %>%
  group_by(id, Gender, Age, Smoker, SBP, DBP, vascular_event, HTN, Hypertension) %>%
  summarize(
    avg_hr_stats = list(calculate_metrics(avg_hr)),
   # sdnn_stats   = list(calculate_metrics(sdnn)),
  #  rmssd_stats  = list(calculate_metrics(rmssd)),
    .groups = "drop"
  ) %>% 
  unnest(cols = avg_hr_stats) #%>%
  # pivot_wider(
  #   names_from = names,
  #   values_from = values,
  #   names_prefix = "avg_hr_"
  # )

df_long_s <- df_long_s %>% 
  rename(value = values) %>% 
  mutate(metric = str_c("avg_hr_", names))

############################
  
# If you want all of the metrics applied to avg_hr, sdnn, and rmssd
results_s <- data_holter_downsampled_s %>%
  mutate(avg_hr = mean_hr) %>% 
#  group_by(id, condition, status) %>% 
  select(id, Gender, Age, Smoker, SBP, DBP, vascular_event, HTN, Hypertension, avg_hr) %>%
  group_by(id, Gender, Age, Smoker, SBP, DBP, vascular_event, HTN, Hypertension) %>%
  summarize(
    avg_hr_stats = list(calculate_metrics(avg_hr)),
    sdnn_stats   = list(calculate_metrics(sdnn)),
    rmssd_stats  = list(calculate_metrics(rmssd)),
    .groups = "drop"
  )

# Process avg_hr metrics
avg_hr_results_s <- results_s %>%
 # select(id, condition, status, avg_hr_stats) %>% 
  select(id, Gender, Age, Smoker, SBP, DBP, vascular_event, HTN, Hypertension, avg_hr_stats) %>%
  unnest(cols = avg_hr_stats) %>%
  pivot_wider(
    names_from = names,
    values_from = values,
    names_prefix = "avg_hr_"
  )

# Process sdnn metrics
sdnn_results <- results %>%
  select(id, Gender, Age, Smoker, SBP, DBP, vascular_event, HTN, Hypertension, sdnn_stats) %>%
  unnest(cols = sdnn_stats) %>%
  pivot_wider(
    names_from = names,
    values_from = values,
    names_prefix = "sdnn_"
  )

# Process rmssd metrics
rmssd_results <- results %>%
  select(id, Gender, Age, Smoker, SBP, DBP, vascular_event, HTN, Hypertension, rmssd_stats) %>%
  unnest(cols = rmssd_stats) %>%
  pivot_wider(
    names_from = names,
    values_from = values,
    names_prefix = "rmssd_"
  )

# Join all results together
final_results <- avg_hr_results %>%
  left_join(sdnn_results, by = c("id", "Gender", "Age", "Smoker", "SBP", "DBP", "vascular_event", "HTN", "Hypertension" )) %>%
  left_join(rmssd_results, by = c("id", "Gender", "Age", "Smoker", "SBP", "DBP", "vascular_event", "HTN", "Hypertension" ))

# --- Example check of the resulting data ---
head(final_results)

# --- Sanity checks ---
# Check for missing values in key metrics
colSums(is.na(final_results))

# Check for infinite values
colSums(sapply(final_results, is.infinite))






##################

data_holter_downsampled_clean <- data_holter_downsampled %>%
  filter(is.finite(sdnn), is.finite(rmssd), is.finite(mean_hr))

results <- data_holter_downsampled_clean %>%
  mutate(avg_hr = mean_hr) %>% 
  group_by(id, Gender, Age, Smoker, SBP, DBP, vascular_event, HTN, Hypertension) %>%
  summarize(
    avg_hr_stats = list(calculate_metrics(avg_hr)),
    sdnn_stats   = list(calculate_metrics(sdnn)),
    rmssd_stats  = list(calculate_metrics(rmssd)),
    .groups = "drop"
  )


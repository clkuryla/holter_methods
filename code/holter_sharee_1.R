# SHAREE
# https://physionet.org/content/shareedb/1.0.0/ 


path_to_metadata <- file.path("/Users/christinekuryla/Giant_Data/sharee/info.txt")
#path_to_sharee_raw_data <- file.path("/Users/christinekuryla/Downloads/")
path_to_sharee_raw_data <- file.path("/Users/christinekuryla/Giant_Data/sharee/")

########################## Participant info ###############################

library(tidyverse)

# Participant info

metadata <- read_tsv("/Users/christinekuryla/Downloads/info.txt") %>% 
  rename(SBP = SBP...9,
         DBP = SBP...10) 

glimpse(metadata)

metadata <- metadata %>% 
  mutate(HTN = case_when(
                  SBP < 120 & DBP < 80 ~ "Normal",
                  SBP == 120 & DBP < 80 ~ "Sys120",
                  SBP > 120 & SBP <= 129 & DBP < 80 ~ "PreHTN",
                  SBP >= 130 & SBP <= 139 ~ "HTN_1",
                  DBP >= 80 & DBP <= 89 ~ "HTN_1",
                  SBP >= 140 ~ "HTN_2",
                  DBP >= 90 ~ "HTN_2"
         )) %>% 
 # mutate(HTN = relevel(as_factor((HTN, levels = c("Normal", "Sys120", "PreHTN", "HTN_1", "HTN_2"))))) %>% 
  mutate(Hypertension = case_when(
                  SBP <= 129 & DBP <= 80 ~ "Normal",
                  SBP >= 130 & SBP <= 139 ~ "HTN_1",
                  DBP >= 80 & DBP <= 89 ~ "HTN_1",
                  SBP >= 140 ~ "HTN_2",
                  DBP >= 90 ~ "HTN_2"
                )) %>% 
  mutate(Smoker = as_factor(Smoker)) %>% 
  mutate(vascular_event = as_factor(`Vascular event`))

table(metadata$HTN)
table(metadata$Hypertension)
table(metadata$vascular_event)
table(metadata$Smoker)

######################## ECG Data Test ################################

library(RHRV)

# Test

# Create HRV data object
hrv_data <- CreateHRVData()

# Load with CORRECT annotator type
hrv_data <- LoadBeatWFDB(hrv_data, 
                         RecordName = "01911",
                  #       RecordPath = path_to_sharee_raw_data, #"~/Downloads",
                         annotator = "qrs")  # ← KEY: use "qrs" not "atr"!

# Check it loaded
cat("Number of beats detected:", length(hrv_data$Beat$Time), "\n")

# Build NN intervals
hrv_data <- BuildNIHR(hrv_data)

# Filter artifacts
hrv_data <- FilterNIHR(hrv_data)
hrv_data <- FilterNIHR(hrv_data)

# Plot the RR intervals
PlotNIHR(hrv_data)

# Calculate time-domain metrics
hrv_data <- CreateTimeAnalysis(hrv_data, size = 300, interval = 7.8125)

# View results
hrv_data$TimeAnalysis

hrv_data$Beat



######################## ECG Data Bulk ################################

record_ids <- metadata %>% 
  pull(Record) %>% 
  head(139)

##### RHRV is finicky and you need to manually set the working directory via the GUI*****

str_c("0", 1234)

library(RHRV)

# path_to_sharee_raw_data <- file.path("/Users/christinekuryla/Giant_Data/sharee/")

for(id in record_ids) {      #[1:139]) {

# Create HRV data object
hrv_data <- CreateHRVData()

# Load with CORRECT annotator type
hrv_data <- LoadBeatWFDB(hrv_data, 
                    RecordName = str_c("0", id),
               #     RecordPath = "/Users/christinekuryla/Giant_Data/sharee", # 
                    annotator = "qrs") 

# Build NN intervals
hrv_data <- BuildNIHR(hrv_data)

# Filter artifacts
hrv_data <- FilterNIHR(hrv_data)
hrv_data <- FilterNIHR(hrv_data)

#hrv_data <- CreateTimeAnalysis(hrv_data, size = 300, interval = 7.8125)
#hrv_data$TimeAnalysis

cat("Number of beats detected:", length(hrv_data$Beat$Time), "\n")
glimpse(hrv_data$Beat)

subj_data <- metadata %>% filter(Record == id)

subj_data_complete <- hrv_data$Beat %>% 
  cross_join(subj_data) %>% 
  mutate(ibi = RR / 1000) %>% 
  rename(time_sec = Time) %>% 
  rename(id = Record) %>% 
  select(-RR) #%>% 
 # select(-niHR)



write_csv(subj_data_complete, file = file.path("/Users/christinekuryla/Documents/Giant_Data/sharee_processed", "beats_20251116", str_c(id, "_beats.csv")))



# data_holter_sharee <- bind_rows(data_holter_sharee, subj_data_complete)

}


######################### Calculate and downsample #######################


# record_ids <- metadata %>% 
#   pull(Record) %>% 
#   head(139)

for(Record in record_ids) {   
  data_holter_minute <- read_csv(str_c("/Users/christinekuryla/Documents/Giant_Data/sharee_processed/beats_20251116/", Record, "_beats.csv")) %>%
    # Ensure data is ordered by time before we take diffs
   # select(-niHR) %>% 
    arrange(id, time_sec) %>%
    filter(ibi != 1.000000) %>% 
    mutate(time_sec = time_sec - min(time_sec)) %>%  # Reset to start at 0
    mutate(
      minute_index = floor(time_sec / 60)
    ) %>%
    group_by(across(c(-time_sec, -ibi, -niHR))) %>%
    summarize(
      mean_hr = mean(niHR),
      mean_hr_ibi60 = mean(60 / ibi, na.rm = TRUE),
      # SDNN: standard deviation of the IBIs in that minute
      sdnn = sd(ibi, na.rm = TRUE),
      # RMSSD: square root of mean of squared differences of successive IBI
      rmssd = {
        # We compute consecutive differences of ibi within the group
        diffs <- diff(ibi)
        sqrt(mean(diffs^2, na.rm = TRUE))
      },
      n_beats = n(),
      .groups = "drop"
    ) %>%
    # If desired, a time stamp for each minute
    mutate(minute_start_sec = minute_index * 60) %>%
    arrange(id, minute_index) %>% 
    mutate(minute_index = minute_index - min(minute_index) + 1)
  
  write_csv(data_holter_minute, file = file.path("/Users/christinekuryla/Documents/Giant_Data/sharee_processed", "beats_20251116", str_c(Record, "_1min.csv")))  
  

}




# # Calculate downsampled HR
# colnames(subj_data_complete %>% select(-c(id, time_sec)))
# 
# 
# 
# # calculate heart rate, rmssd, sdnn every minute
# 
# data_holter_minute <- subj_data_complete %>%
#   # Ensure data is ordered by time before we take diffs
#   select(-niHR) %>% 
#   arrange(id, time_sec) %>%
#   filter(ibi != 1.000000) %>% 
#   mutate(
#     minute_index = floor(time_sec / 60)
#   ) %>%
#   group_by(across(c(-time_sec, -ibi))) %>%
#   summarize(
#     mean_hr = mean(60 / ibi, na.rm = TRUE),
#     # SDNN: standard deviation of the IBIs in that minute
#     sdnn = sd(ibi, na.rm = TRUE),
#     # RMSSD: square root of mean of squared differences of successive IBI
#     rmssd = {
#       # We compute consecutive differences of ibi within the group
#       diffs <- diff(ibi)
#       sqrt(mean(diffs^2, na.rm = TRUE))
#     },
#     n_beats = n(),
#     .groups = "drop"
#   ) %>%
#   # If desired, a time stamp for each minute
#   mutate(minute_start_sec = minute_index * 60) %>%
#   arrange(id, minute_index) %>% 
#   mutate(minute_index = minute_index - min(minute_index) + 1)
# 
# data_holter_minute <- subj_data_complete %>%
#   # Ensure data is ordered by time before we take diffs
#   select(-niHR) %>% 
#   arrange(id, time_sec) %>%
#   filter(ibi != 1.000000) %>% 
#   mutate(
#     minute_index = floor(time_sec / 60)
#   ) %>%
#   group_by(across(c(-time_sec, -ibi))) %>%
#   summarize(
#     mean_hr = mean(60 / ibi, na.rm = TRUE),
#     # SDNN: standard deviation of the IBIs in that minute
#     sdnn = sd(ibi, na.rm = TRUE),
#     # RMSSD: square root of mean of squared differences of successive IBI
#     rmssd = {
#       # We compute consecutive differences of ibi within the group
#       diffs <- diff(ibi)
#       sqrt(mean(diffs^2, na.rm = TRUE))
#     },
#     n_beats = n(),
#     .groups = "drop"
#   ) %>%
#   # If desired, a time stamp for each minute
#   mutate(minute_start_sec = minute_index * 60) %>%
#   arrange(id, minute_index) %>% 
#   mutate(minute_index = minute_index - min(minute_index) + 1)


# # downsample to every 5 minutes
# data_holter_downsampled <- data_holter_minute %>%
#   filter(minute_index %% 5 == 1) %>% 
#   mutate(time_5min = minute_index/5)

# If you need a different offset (e.g., 1, 6, 11, etc.), you can adjust accordingly:
# filter(minute_index %% 5 == 1)


### This
library(tidyverse)

# Get the first 5 record IDs
record_ids <- metadata %>% 
  pull(Record) %>% 
  head(139)

# Define the expected column types
col_types <- cols(
  id = col_double(),
  Gender = col_character(),  # Force as character
  Age = col_double(),
  Weight = col_double(),
  Height = col_double(),
  BSA = col_double(),
  BMI = col_double(),
  SBP = col_double(),
  DBP = col_double(),
  `IMT MAX` = col_character(),  # Force as character (can convert later)
  Smoker = col_character(),
  `Vascular event` = col_character(),
  HTN = col_character(),
  Hypertension = col_character(),
  vascular_event = col_character(),
  LVMi = col_double(),
  EF = col_double(),
  minute_index = col_double(),
  mean_hr = col_double(),
  sdnn = col_double(),
  rmssd = col_double(),
  pnn50 = col_double(),
  lf_hf_ratio = col_double()
)

# Read and combine all files with specified column types
data_sharee_1min <- map_dfr(record_ids, function(id) {
  file_path <- file.path("/Users/christinekuryla/Documents/Giant_Data/sharee_processed", 
                         "beats_20251116", 
                         str_c(id, "_1min.csv"))
  
  read_csv(file_path, col_types = col_types) %>%
    mutate(record_id = id)
})

# Convert IMT MAX to numeric if needed
data_sharee_1min <- data_sharee_1min %>%
  mutate(`IMT MAX` = as.numeric(`IMT MAX`))

# downsample to every 5 minutes
data_sharee_5min <- data_sharee_1min %>%
  filter(minute_index %% 5 == 0) %>% 
  mutate(time_5min = minute_index/5)


write_csv(data_sharee_1min, file = file.path("/Users/christinekuryla/Documents/Giant_Data/sharee_processed", "beats_20251116", "sharee_1min.csv"))  
write_csv(data_sharee_5min, file = file.path("/Users/christinekuryla/Documents/Giant_Data/sharee_processed", "beats_20251116", "sharee_5min.csv"))

write_csv(data_sharee_1min, file = "/Users/christinekuryla/Documents/_Research/Holter/holter_methods/data_processed/sharee_20251118/sharee_1min.csv")
write_csv(data_sharee_5min, file = "/Users/christinekuryla/Documents/_Research/Holter/holter_methods/data_processed/sharee_20251118/sharee_5min.csv")

# SHAREE
# https://physionet.org/content/shareedb/1.0.0/ 


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
                         RecordPath = "~/Downloads",
                         annotator = "qrs")  # ← KEY: use "qrs" not "atr"!

# Check it loaded
cat("Number of beats detected:", length(hrv_data$Beat$Time), "\n")

# Build NN intervals
hrv_data <- BuildNIHR(hrv_data)

# Filter artifacts
hrv_data <- FilterNIHR(hrv_data)

# Plot the RR intervals
PlotNIHR(hrv_data)

# Calculate time-domain metrics
hrv_data <- CreateTimeAnalysis(hrv_data, size = 300, interval = 7.8125)

# View results
hrv_data$TimeAnalysis

hrv_data$Beat



######################## ECG Data Bulk ################################

str_c("0", 1234)

data_holter_sharee <- data_frame()

for(Record in metadata %>% pull(Record)) {

# Create HRV data object
hrv_data <- CreateHRVData()

# Load with CORRECT annotator type
hrv_data <- LoadBeatWFDB(hrv_data, 
                    RecordName = str_c("0", Record),
                    RecordPath = "~/Downloads",
                    annotator = "qrs") 

# Build NN intervals
hrv_data <- BuildNIHR(hrv_data)

# Filter artifacts
hrv_data <- FilterNIHR(hrv_data)

#hrv_data <- CreateTimeAnalysis(hrv_data, size = 300, interval = 7.8125)
#hrv_data$TimeAnalysis

glimpse(hrv_data$Beat)

subj_data <- metadata %>% filter(Record == Record)

subj_data_complete <- hrv_data$Beat %>% 
  cross_join(subj_data) %>% 
  mutate(ibi = RR / 1000) %>% 
  rename(time_sec = Time) %>% 
  rename(id = Record) %>% 
  select(-RR) %>% 
  select(-niHR)

bind_rows(data_holter_sharee, subj_data_complete)

}


######################### Calculate and downsample #######################

# Calculate downsampled HR
colnames(subj_data_complete %>% select(-c(id, time_sec)))

# calculate heart rate, rmssd, sdnn every minute

data_holter_minute <- subj_data_complete %>%
  # Ensure data is ordered by time before we take diffs
  arrange(id, time_sec) %>%
  mutate(
    minute_index = floor(time_sec / 60)
  ) %>%
  group_by(across(c(-time_sec, -ibi)), minute_index) %>%
  summarize(
    mean_hr = mean(60 / ibi, na.rm = TRUE),
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
  arrange(id, minute_index)

# downsample to every 5 minutes
data_holter_downsampled <- data_holter_minute %>%
  filter(minute_index %% 5 == 1) %>% 
  mutate(time_5min = minute_index/5)

# If you need a different offset (e.g., 1, 6, 11, etc.), you can adjust accordingly:
# filter(minute_index %% 5 == 1)





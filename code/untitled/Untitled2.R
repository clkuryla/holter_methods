b <- readMat("../../../../Downloads/19070921.mat")

# Required packages
library(R.matlab)  # For reading .mat files
library(RHRV)      # For HRV analysis
library(signal)    # For filtering
library(pracma)    # For peak detection

# Step 1: Load the .mat file and examine its structure
file_path <- "path_to_your_file.mat"  # Replace with your file path
ecg_data <- readMat(file_path)


ecg_data <- b
print(names(ecg_data))  # View available variables

# Step 2: Process a single dataset (e.g., sleep data)
# Choose which dataset to analyze
raw_ecg <- ecg_data$sleep[1, ]  # Replace with your variable of interest
sampling_rate <- 250  # Adjust based on your data collection settings

# Step 3: R-peak detection function
detect_r_peaks <- function(ecg_data, sampling_rate = 250) {
  # Apply bandpass filter to enhance QRS complexes
  bf <- butter(3, c(5/(sampling_rate/2), 15/(sampling_rate/2)), type="pass")
  filtered_ecg <- filtfilt(bf, ecg_data)
  
  # Find peaks
  peaks <- findpeaks(filtered_ecg, 
                     minpeakheight = mean(filtered_ecg) + 2*sd(filtered_ecg),
                     minpeakdistance = 0.4 * sampling_rate)  # Minimum distance between peaks
  
  if(is.matrix(peaks)) {
    return(peaks[,2])  # Return indices
  } else {
    return(integer(0))
  }
}

# Step 4: Extract R-peaks and calculate RR intervals
# Process in chunks if data is large
chunk_size <- 100000
num_chunks <- ceiling(length(raw_ecg) / chunk_size)
all_r_peaks <- numeric(0)

for(i in 1:num_chunks) {
  start_idx <- (i-1) * chunk_size + 1
  end_idx <- min(i * chunk_size, length(raw_ecg))
  
  chunk_data <- raw_ecg[start_idx:end_idx]
  chunk_peaks <- detect_r_peaks(chunk_data, sampling_rate)
  
  # Adjust peak indices to account for chunking
  if(length(chunk_peaks) > 0) {
    chunk_peaks <- chunk_peaks + start_idx - 1
    all_r_peaks <- c(all_r_peaks, chunk_peaks)
  }
}

# Calculate RR intervals in milliseconds
rr_intervals <- diff(all_r_peaks) * (1000/sampling_rate)

# Step 5: Clean RR intervals
# Remove physiologically implausible values (typical heart rates 30-200 BPM)
valid_rr <- rr_intervals[rr_intervals >= 300 & rr_intervals <= 2000]

# Remove outliers (values beyond ±2 SD from mean)
mean_rr <- mean(valid_rr)
sd_rr <- sd(valid_rr)
clean_rr <- valid_rr[abs(valid_rr - mean_rr) <= 2*sd_rr]

# Step 6: Create HRV data structure
hrv_data <- CreateHRVData()
hrv_data$Beat$RR <- clean_rr
hrv_data$Beat$Time <- cumsum(c(0, head(clean_rr, -1)/1000))  # Convert to seconds
hrv_data$Beat$Index <- 1:length(clean_rr)

# Step 7: Build heart rate time series
hrv_data <- BuildNIHR(hrv_data)

# Step 8: HRV analysis (skipping filtering to avoid data loss)
# Time domain analysis
hrv_data <- CreateTimeAnalysis(hrv_data)
print(hrv_data$TimeAnalysis)

# Frequency domain analysis
hrv_data <- CreateFreqAnalysis(hrv_data)
hrv_data <- CalculatePSD(hrv_data, method = "ar")  # Use autoregressive method
hrv_data <- CalculatePowerBand(hrv_data, 
                               ULFmin = 0, ULFmax = 0.03,
                               VLFmin = 0.03, VLFmax = 0.05,
                               LFmin = 0.05, LFmax = 0.15,
                               HFmin = 0.15, HFmax = 0.4)
print(hrv_data$FreqAnalysis)

# Nonlinear analysis
hrv_data <- CreateNonLinearAnalysis(hrv_data)
print(hrv_data$NonLinearAnalysis)

# Step 9: Visualize results
PlotNIHR(hrv_data)
PlotPowerBand(hrv_data)
PoincarePlot(hrv_data)

# Step 10: Save results
WriteToFile(hrv_data, "hrv_results.txt")   
                   
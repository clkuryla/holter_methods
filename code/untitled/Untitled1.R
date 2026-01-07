# Create HRV data object
hrv_data <- CreateHRVData()

# Set RR intervals
rr_intervals <- as.numeric(t(a$RS)/1000)  # Convert to seconds
rr_intervals <- rr_intervals[!is.na(rr_intervals) & rr_intervals > 0]

# Set the RR values and create time series
hrv_data$Beat$RR <- rr_intervals
hrv_data$Beat$Time <- cumsum(c(0, head(rr_intervals, -1)))
hrv_data$Beat$Index <- 1:length(rr_intervals)

# Build NIHR data
hrv_data <- BuildNIHR(hrv_data)

# Filter and interpolate
hrv_data <- FilterNIHR(hrv_data)
hrv_data <- InterpolateNIHR(hrv_data, freqhr = 4)

# Time domain analysis
hrv_data <- CreateTimeAnalysis(hrv_data)

# Create basic frequency analysis structure
hrv_data <- CreateFreqAnalysis(hrv_data)

# Now calculate PSD using specific method
# The parameters should be passed to CalculatePSD, not CreateFreqAnalysis
hrv_data <- CalculatePSD(hrv_data, 
                         method = "ar",         # Autoregressive method
                         size = 300,            # Window size
                         shift = 30)            # Window shift

# Calculate the power in different frequency bands
hrv_data <- CalculatePowerBand(hrv_data,
                               size = 300,       # Window size
                               shift = 30,       # Window shift
                               type = "ar",      # Autoregressive
                               ULFmin = 0,       # ULF band min
                               ULFmax = 0.03,    # ULF band max
                               VLFmin = 0.03,    # VLF band min
                               VLFmax = 0.05,    # VLF band max
                               LFmin = 0.05,     # LF band min
                               LFmax = 0.15,     # LF band max
                               HFmin = 0.15,     # HF band min
                               HFmax = 0.4)      # HF band max

# For nonlinear analysis
hrv_data <- CreateNonLinearAnalysis(hrv_data)

# Calculate specific nonlinear metrics
# Poincaré plot is automatically done in CreateNonLinearAnalysis
# For DFA
hrv_data <- CalculateDFA(hrv_data)

# Corr Dim
hrv_data <- CalculateCorrDim(hrv_data)

# For Sample Entropy
hrv_data <- CalculateSampleEntropy(hrv_data)

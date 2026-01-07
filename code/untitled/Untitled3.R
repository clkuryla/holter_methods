# Enhanced function to calculate heart rate with improved detection and handling of missing values
analyze_hr_by_minute_improved <- function(signal, sampling_rate = 250) {
  # Calculate the number of complete minutes in the dataset
  samples_per_minute <- sampling_rate * 60
  total_minutes <- floor(length(signal) / samples_per_minute)
  
  # Storage for results
  minute_hrs <- numeric(total_minutes)
  valid_minute_flags <- logical(total_minutes)
  
  # Process each minute
  for(minute in 1:total_minutes) {
    # Calculate window indices
    start_idx <- (minute-1) * samples_per_minute + 1
    end_idx <- minute * samples_per_minute
    
    # Extract window
    window_signal <- signal[start_idx:end_idx]
    
    # Apply simple bandpass filter to reduce noise
    window_smooth <- stats::filter(window_signal, rep(1/5, 5), sides=2)
    # Handle NAs at edges from filtering
    window_smooth[is.na(window_smooth)] <- window_signal[is.na(window_smooth)]
    
    # Try different thresholds for peak detection
    for(sd_multiplier in c(3, 4, 5)) {
      # Find peaks with current threshold
      threshold <- mean(window_smooth, na.rm=TRUE) + sd_multiplier*sd(window_smooth, na.rm=TRUE)
      above_thresh <- which(window_smooth > threshold)
      
      # Group consecutive points and find peaks
      peaks <- c()
      if(length(above_thresh) > 0) {
        # Find gaps between consecutive indices
        gaps <- diff(above_thresh)
        # Start a new group when gap > 1
        group_starts <- c(1, which(gaps > 1) + 1)
        group_ends <- c(group_starts[-1] - 1, length(above_thresh))
        
        # For each group, find the maximum value
        for(i in 1:length(group_starts)) {
          group_indices <- above_thresh[group_starts[i]:group_ends[i]]
          max_idx <- group_indices[which.max(window_smooth[group_indices])]
          peaks <- c(peaks, max_idx)
        }
      }
      
      # Calculate heart rate for this minute
      heart_rate <- length(peaks)  # Beats per minute directly
      
      # Check if heart rate is physiologically plausible
      is_valid <- heart_rate >= 30 && heart_rate <= 200
      
      # If we found a valid heart rate with this threshold, use it and break
      if(is_valid) {
        minute_hrs[minute] <- heart_rate
        valid_minute_flags[minute] <- TRUE
        break
      }
      
      # If this was the last attempt, store the result even if invalid
      if(sd_multiplier == 5) {
        minute_hrs[minute] <- heart_rate
        valid_minute_flags[minute] <- is_valid
      }
    }
  }
  
  # Create time stamps (minute markers)
  minutes <- 1:total_minutes
  
  # Mark invalid heart rates as NA
  minute_hrs[!valid_minute_flags] <- NA
  
  # Return results as a data frame
  result <- data.frame(
    minute = minutes,
    heart_rate = minute_hrs,
    is_valid = valid_minute_flags
  )
  
  return(result)
}

# Process day data in chunks with improved function
process_day_data_improved <- function(day_data, chunk_size = 1000000, sampling_rate = 250) {
  # Calculate total length and required chunks
  total_length <- length(day_data)
  num_chunks <- ceiling(total_length / chunk_size)
  
  # Calculate minutes per chunk
  samples_per_minute <- sampling_rate * 60
  minutes_per_chunk <- floor(chunk_size / samples_per_minute)
  
  # Initialize results
  all_results <- NULL
  
  # Process each chunk
  for(chunk in 1:num_chunks) {
    # Calculate chunk indices
    start_idx <- (chunk-1) * chunk_size + 1
    end_idx <- min(chunk * chunk_size, total_length)
    
    # Extract chunk
    chunk_data <- day_data[start_idx:end_idx]
    
    # Analyze this chunk with improved function
    chunk_results <- analyze_hr_by_minute_improved(chunk_data, sampling_rate)
    
    # Adjust minute numbers
    chunk_results$minute <- chunk_results$minute + (chunk-1) * minutes_per_chunk
    
    # Append to overall results
    if(is.null(all_results)) {
      all_results <- chunk_results
    } else {
      all_results <- rbind(all_results, chunk_results)
    }
    
    # Report progress
    cat(sprintf("Processed chunk %d of %d (%.1f%%)\n", 
                chunk, num_chunks, 100 * chunk/num_chunks))
  }
  
  return(all_results)
}

# Interpolate missing values
interpolate_missing_hr <- function(hr_data) {
  # Create a copy of the data
  interpolated <- hr_data
  
  # Find indices of valid and NA heart rates
  valid_indices <- which(!is.na(hr_data$heart_rate))
  
  # Skip if there are too few valid points
  if(length(valid_indices) < 2) return(hr_data)
  
  # Create interpolation function
  interp_fun <- approxfun(hr_data$minute[valid_indices], 
                          hr_data$heart_rate[valid_indices],
                          method = "linear", 
                          rule = 2)  # rule=2 means extrapolate
  
  # Apply interpolation to all minutes
  all_minutes <- hr_data$minute
  interpolated$heart_rate <- interp_fun(all_minutes)
  interpolated$interpolated <- is.na(hr_data$heart_rate)
  
  return(interpolated)
}

# Main processing pipeline
library(R.matlab)  # For reading .mat files
library(ggplot2)   # For plotting

# Process the day data with improved detection
day_hr_by_minute <- process_day_data_improved(ecg_data$day[1,], sampling_rate = 250)

# Count valid and invalid minutes before interpolation
valid_count <- sum(day_hr_by_minute$is_valid)
invalid_count <- sum(!day_hr_by_minute$is_valid)
percent_valid <- 100 * valid_count / nrow(day_hr_by_minute)

cat(sprintf("Before interpolation: %d valid minutes (%.1f%%), %d invalid minutes\n",
            valid_count, percent_valid, invalid_count))

# Apply interpolation to fill missing values
day_hr_interpolated <- interpolate_missing_hr(day_hr_by_minute)

# Calculate additional statistics for more robust heart rate metrics
# Use 5-minute moving averages
library(zoo)  # For rolling window calculations
day_hr_interpolated$hr_smooth <- rollmean(day_hr_interpolated$heart_rate, 
                                          k = 5, 
                                          fill = NA, 
                                          align = "center")

# Save results to CSV files
write.csv(day_hr_by_minute, "day_heart_rate_raw.csv", row.names = FALSE)
write.csv(day_hr_interpolated, "day_heart_rate_interpolated.csv", row.names = FALSE)

# Create improved visualizations
# Raw data with valid/invalid points
p1 <- ggplot(day_hr_by_minute, aes(x = minute, y = heart_rate)) +
  geom_point(aes(color = is_valid), alpha = 0.6) +
  scale_color_manual(values = c("TRUE" = "blue", "FALSE" = "red")) +
  labs(title = "Heart Rate Throughout the Day (Raw Data)",
       subtitle = sprintf("%.1f%% valid data points", percent_valid),
       x = "Minute",
       y = "Heart Rate (BPM)",
       color = "Valid") +
  theme_minimal()

# Interpolated data with trend
p2 <- ggplot(day_hr_interpolated, aes(x = minute, y = heart_rate)) +
  geom_line(alpha = 0.4) +
  geom_line(aes(y = hr_smooth), color = "blue", size = 1) +
  labs(title = "Heart Rate Throughout the Day (Interpolated)",
       subtitle = "Blue line shows 5-minute moving average",
       x = "Minute",
       y = "Heart Rate (BPM)") +
  theme_minimal()

# Save plots
ggsave("heart_rate_raw.png", p1, width = 12, height = 6)
ggsave("heart_rate_interpolated.png", p2, width = 12, height = 6)

# Calculate hourly heart rate metrics from the interpolated data
calculate_hourly_metrics <- function(hr_data) {
  # Determine total hours
  total_hours <- ceiling(max(hr_data$minute) / 60)
  
  # Initialize results
  hourly_results <- data.frame(
    hour = 1:total_hours,
    mean_hr = numeric(total_hours),
    median_hr = numeric(total_hours),
    sd_hr = numeric(total_hours),
    min_hr = numeric(total_hours),
    max_hr = numeric(total_hours)
  )
  
  # Calculate metrics for each hour
  for(hour in 1:total_hours) {
    # Get data for this hour
    start_minute <- (hour-1) * 60 + 1
    end_minute <- hour * 60
    hour_data <- subset(hr_data, minute >= start_minute & minute <= end_minute)
    
    # Calculate metrics
    hourly_results$mean_hr[hour] <- mean(hour_data$heart_rate, na.rm = TRUE)
    hourly_results$median_hr[hour] <- median(hour_data$heart_rate, na.rm = TRUE)
    hourly_results$sd_hr[hour] <- sd(hour_data$heart_rate, na.rm = TRUE)
    hourly_results$min_hr[hour] <- min(hour_data$heart_rate, na.rm = TRUE)
    hourly_results$max_hr[hour] <- max(hour_data$heart_rate, na.rm = TRUE)
  }
  
  return(hourly_results)
}

# Calculate and save hourly metrics
hourly_metrics <- calculate_hourly_metrics(day_hr_interpolated)
write.csv(hourly_metrics, "hourly_heart_rate_metrics.csv", row.names = FALSE)

# Plot hourly metrics
p3 <- ggplot(hourly_metrics, aes(x = hour)) +
  geom_ribbon(aes(ymin = min_hr, ymax = max_hr), fill = "lightblue", alpha = 0.3) +
  geom_line(aes(y = mean_hr), color = "blue", size = 1) +
  geom_line(aes(y = median_hr), color = "darkblue", linetype = "dashed") +
  labs(title = "Hourly Heart Rate Metrics",
       subtitle = "Blue line = mean, dashed = median, ribbon = min-max range",
       x = "Hour of Day",
       y = "Heart Rate (BPM)") +
  theme_minimal()

ggsave("hourly_heart_rate_metrics.png", p3, width = 12, height = 6)

# Print summary statistics
cat("\nOverall Heart Rate Summary:\n")
print(summary(day_hr_interpolated$heart_rate))
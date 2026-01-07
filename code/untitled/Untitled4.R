library(ggplot2)
library(dplyr)
library(ggpubr)
library(gridExtra)

# Create a plot for each metric
create_plot <- function(metric_name) {
  # Filter data for the specific metric
  plot_data <- df_long %>% filter(metric == metric_name)
  
  # Get the unique status groups
  status_groups <- unique(plot_data$status)
  
  # Get test results
  t_test_results <- df_status_tests %>% 
    filter(metric == metric_name, test == "t-test") %>%
    head(1)
  
  wilcox_results <- df_status_tests %>% 
    filter(metric == metric_name, test == "wilcoxon-rank-sum") %>%
    head(1)
  
  # Calculate means for each group
  means <- plot_data %>% 
    group_by(status) %>% 
    summarize(mean_value = mean(value, na.rm = TRUE))
  
  # Create the base plot
  p <- ggplot(plot_data, aes(x = status, y = value, fill = status)) +
    geom_boxplot(alpha = 0.7) +
    # Add mean points with labels
    geom_point(data = means, aes(y = mean_value), shape = 18, size = 4, color = "black") +
    geom_text(data = means, aes(y = mean_value, label = round(mean_value, 2)), 
              vjust = -1, color = "black", size = 3) +
    labs(
      title = metric_name,
      x = "Status",
      y = "Value"
    ) +
    theme_minimal() +
    theme(legend.position = "none")
  
  # Extract group names from the test results if available
  if (nrow(t_test_results) > 0) {
    t_stat <- round(t_test_results$statistic, 3)
    t_p <- round(t_test_results$p.value, 4)
    p_text <- paste0("t-test: stat=", t_stat, ", p=", t_p)
    
    # If we have group names, add them to the annotation
    if (!is.na(t_test_results$estimate1) && !is.na(t_test_results$estimate2)) {
      group1_mean <- round(t_test_results$estimate1, 2)
      group2_mean <- round(t_test_results$estimate2, 2)
      p_text <- paste0(p_text, "\n(", group1_mean, " vs ", group2_mean, ")")
    }
    
    p <- p + annotate("text", x = Inf, y = Inf, label = p_text,
                      hjust = 1.1, vjust = 2, size = 3)
  }
  
  if (nrow(wilcox_results) > 0) {
    w_stat <- round(wilcox_results$statistic, 3)
    w_p <- round(wilcox_results$p.value, 4)
    
    p <- p + annotate("text", x = Inf, y = Inf, 
                      label = paste0("Wilcoxon: stat=", w_stat, ", p=", w_p),
                      hjust = 1.1, vjust = 4, size = 3)
  }
  
  # Add significance markers based on p-value
  if (nrow(t_test_results) > 0 && length(status_groups) == 2) {
    max_y <- max(plot_data$value, na.rm = TRUE)
    sig_level <- ""
    
    if (t_test_results$p.value < 0.001) sig_level <- "***"
    else if (t_test_results$p.value < 0.01) sig_level <- "**"
    else if (t_test_results$p.value < 0.05) sig_level <- "*"
    else sig_level <- "ns"
    
    # Only add significance bracket if we have exactly 2 groups
    if (sig_level != "ns") {
      p <- p + annotate("text", x = 1.5, y = max_y * 1.1, 
                        label = sig_level, size = 5)
    }
  }
  
  return(p)
}

# For multiple metrics, create plots and arrange them in a grid
# metrics_to_plot <- unique(df_long$metric) 
metrics_to_plot <- c("avg_hr_DN_HistogramMode_5", "avg_hr_cv", "avg_hr_SB_BinaryStats_diff_longstretch0", "avg_hr_PD_PeriodicityWang_th0_01", "avg_hr_IN_AutoMutualInfoStats_40_gaussian_fmmi", "avg_hr_CO_FirstMin_ac")



plots <- lapply(metrics_to_plot, create_plot)

# Determine a reasonable grid layout based on the number of plots
n_plots <- length(plots)
n_cols <- min(3, n_plots)  # Maximum 3 columns
n_rows <- ceiling(n_plots / n_cols)

# Arrange plots in a grid
grid_plot <- grid.arrange(grobs = plots, ncol = n_cols)

# Save the plot (optional)
# ggsave("metric_comparisons.png", grid_plot, width = n_cols * 5, height = n_rows * 4)
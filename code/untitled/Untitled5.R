library(ggplot2)
library(dplyr)
library(ggpubr)
library(gridExtra)

# Create a plot for each metric
create_plot <- function(metric_name, custom_title = NULL) {
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
  
  # Determine y-axis limits with extra padding to prevent overlapping
  y_min <- min(plot_data$value, na.rm = TRUE)
  y_max <- max(plot_data$value, na.rm = TRUE)
  y_range <- y_max - y_min
  y_padding <- y_range * 0.2  # 20% padding
  
  # Use custom title if provided, otherwise use metric name
  plot_title <- ifelse(!is.null(custom_title), custom_title, metric_name)
  
  # Create the base plot with expanded limits
  p <- ggplot(plot_data, aes(x = status, y = value, fill = status)) +
    geom_boxplot(alpha = 0.7, outlier.size = 2) +
    # Add mean points with better-positioned labels
    geom_point(data = means, aes(y = mean_value), shape = 18, size = 4, color = "black") +
    geom_text(data = means, aes(y = mean_value, label = round(mean_value, 1)), 
              vjust = -1.5, color = "black", size = 3) +
    scale_fill_manual(values = c("CHF" = "#F8AFA8", "Healthy" = "#7FCDBB")) + # Custom colors for consistency
    labs(
      title = plot_title,
      x = "Status",
      y = "Value"
    ) +
    theme_minimal() +
    theme(
      plot.title = element_text(size = 11, face = "bold", hjust = 0.5),
      axis.title.x = element_text(size = 10, margin = margin(t = 10)),
      axis.title.y = element_text(size = 10, margin = margin(r = 10)),
      legend.position = "none",
      panel.grid.minor = element_blank()
    ) +
    # Expand y limits to make room for annotations and prevent overlapping
    coord_cartesian(ylim = c(y_min - y_padding, y_max + y_padding * 2), clip = "off")
  
  # Position for annotations - at the top but with better spacing
  annotation_y_position <- y_max + (y_padding * 0.5)
  comparison_y_position <- y_max + (y_padding * 1.3)
  
  # Add test statistics with improved positioning
  if (nrow(t_test_results) > 0) {
    t_stat <- round(t_test_results$statistic, 2)
    t_p <- formatC(t_test_results$p.value, format = "f", digits = 4)
    
    # Format p-value for display (add leading zero if necessary)
    if (t_test_results$p.value < 0.0001) {
      t_p_display <- "p<0.0001"
    } else {
      t_p_display <- paste0("p=", t_p)
    }
    
    p_text <- paste0("t-test: stat=", t_stat, ", ", t_p_display)
    
    p <- p + annotate("text", x = 1.5, y = annotation_y_position, 
                      label = p_text, size = 3.5, hjust = 0.5)
  }
  
  if (nrow(wilcox_results) > 0) {
    w_stat <- round(wilcox_results$statistic, 0)  # Integer for Wilcoxon
    w_p <- formatC(wilcox_results$p.value, format = "f", digits = 4)
    
    # Format p-value for display
    if (wilcox_results$p.value < 0.0001) {
      w_p_display <- "p<0.0001"
    } else {
      w_p_display <- paste0("p=", w_p)
    }
    
    p <- p + annotate("text", x = 1.5, y = annotation_y_position - (y_padding * 0.25),
                      label = paste0("Wilcox: stat=", w_stat, ", ", w_p_display), 
                      size = 3.5, hjust = 0.5)
  }
  
  # Add comparison of means
  if (!is.na(t_test_results$estimate1[1]) && !is.na(t_test_results$estimate2[1])) {
    group1_mean <- round(t_test_results$estimate1, 1)
    group2_mean <- round(t_test_results$estimate2, 1)
    
    p <- p + annotate("text", x = 1.5, y = comparison_y_position,
                      label = paste0("(", group1_mean, " vs ", group2_mean, ")"),
                      size = 3.5, hjust = 0.5)
  }
  
  # Add significance markers based on p-value
  if (nrow(wilcox_results) > 0 && length(status_groups) == 2) {
    sig_level <- ""
    
    if (wilcox_results$p.value < 0.001) sig_level <- "***"
    else if (wilcox_results$p.value < 0.01) sig_level <- "**" 
    else if (wilcox_results$p.value < 0.05) sig_level <- "*"
    
    # Only add significance marker if significant
    if (sig_level != "") {
      p <- p + annotate("text", x = 1.5, y = y_max + (y_padding * 1.7), 
                        label = sig_level, size = 6)
    }
  }
  
  return(p)
}

# Custom titles mapping - you can modify these titles
metric_titles <- list(
  "avg_hr_DN_HistogramMode_5" = "Histogram Mode 5",
  "avg_hr_cv" = "Coefficient of Variation",
  "avg_hr_SB_BinaryStats_mean" = "Binary Stats Mean",
  "avg_hr_PD_PeriodicityWang_th0_01" = "Periodicity Wang",
  "avg_hr_IN_AutoMutualInfoStats_40_gaussian" = "Auto Mutual Info",
  "avg_hr_CO_FirstMin_ac" = "First Min AC"
  # Add more metrics and their custom titles as needed
)

# For multiple metrics, create plots and arrange them in a grid
# metrics_to_plot <- unique(df_long$metric)
metrics_to_plot <- c("avg_hr_DN_HistogramMode_5", "avg_hr_cv", "avg_hr_SB_BinaryStats_diff_longstretch0", "avg_hr_PD_PeriodicityWang_th0_01", "avg_hr_IN_AutoMutualInfoStats_40_gaussian_fmmi", "avg_hr_CO_FirstMin_ac")
plots <- list()

# Create plots with custom titles where available
for (i in seq_along(metrics_to_plot)) {
  metric <- metrics_to_plot[i]
  custom_title <- NULL
  
  # Use custom title if available
  if (metric %in% names(metric_titles)) {
    custom_title <- metric_titles[[metric]]
  }
  
  plots[[i]] <- create_plot(metric, custom_title)
}

# Determine a reasonable grid layout based on the number of plots
n_plots <- length(plots)
n_cols <- min(3, n_plots)  # Maximum 3 columns
n_rows <- ceiling(n_plots / n_cols)

# Custom theme for better-looking grid
grid_theme <- gridExtra::ttheme_minimal(
  core = list(fg_params = list(hjust = 0.5, x = 0.5)),
  colhead = list(fg_params = list(hjust = 0.5, x = 0.5))
)

# Arrange plots in a grid with appropriate spacing for better fit
grid_plot <- gridExtra::grid.arrange(
  grobs = plots, 
  ncol = n_cols,
  widths = rep(1, n_cols),
  heights = rep(1, n_rows),
  padding = unit(0.5, "cm")
)

# Save the plot with appropriate dimensions (uncomment to use)
# width and height automatically calculated based on number of plots
# ggsave("metric_comparisons.png", grid_plot, 
#        width = min(n_cols * 4, 12),  # Limit max width
#        height = min(n_rows * 3.5, 10),  # Limit max height
#        dpi = 300)
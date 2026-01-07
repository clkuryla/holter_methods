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
  
  # Determine y-axis limits
  y_min <- min(plot_data$value, na.rm = TRUE)
  y_max <- max(plot_data$value, na.rm = TRUE)
  y_range <- y_max - y_min
  y_padding <- y_range * 0.1  # Just a little padding for the plot
  
  # Use custom title if provided, otherwise use metric name
  plot_title <- ifelse(!is.null(custom_title), custom_title, metric_name)
  
  # Prepare subtitle with test statistics (will be placed below the plot)
  subtitle <- ""
  
  # Add significance markers based on p-value
  if (nrow(wilcox_results) > 0 && length(status_groups) == 2) {
    sig_level <- ""
    
    if (wilcox_results$p.value < 0.001) sig_level <- "***"
    else if (wilcox_results$p.value < 0.01) sig_level <- "**" 
    else if (wilcox_results$p.value < 0.05) sig_level <- "*"
    
    # Only add significance marker if significant
    if (sig_level != "") {
      # Place significance star at top of plot
      p_mark <- sig_level
    } else {
      p_mark <- ""
    }
  } else {
    p_mark <- ""
  }
  
  # Create the base plot
  p <- ggplot(plot_data, aes(x = status, y = value, fill = status)) +
    geom_boxplot(alpha = 0.7, outlier.size = 2) +
    # Add mean points with labels
    geom_point(data = means, aes(y = mean_value), shape = 18, size = 4, color = "black") +
    geom_text(data = means, aes(y = mean_value, label = round(mean_value, 1)), 
              vjust = -1.5, color = "black", size = 3.5) +
    scale_fill_manual(values = c("CHF" = "#F8AFA8", "Healthy" = "#7FCDBB")) +
    # Add significance marker at top
    annotate("text", x = 1.5, y = y_max + (y_padding * 0.8), 
             label = p_mark, size = 8, hjust = 0.5) +
    labs(
      title = plot_title,
      x = NULL,  # Remove x-axis label as it's redundant
      y = "Value"
    ) +
    theme_minimal() +
    theme(
      plot.title = element_text(size = 12, face = "bold", hjust = 0.5),
      axis.title.y = element_text(size = 11, margin = margin(r = 10)),
      axis.text = element_text(size = 10),
      legend.position = "none",
      panel.grid.minor = element_blank(),
      plot.margin = margin(b = 0, t = 5, r = 5, l = 5)  # Minimal bottom margin
    ) +
    coord_cartesian(ylim = c(y_min - y_padding, y_max + y_padding * 1.1), clip = "off")
  
  # Create text for below the plot
  plot_text <- NULL
  
  # Get test statistics
  if (nrow(t_test_results) > 0) {
    t_stat <- round(t_test_results$statistic, 2)
    t_p <- formatC(t_test_results$p.value, format = "f", digits = 4)
    
    # Format p-value for display
    if (t_test_results$p.value < 0.0001) {
      t_p_display <- "p<0.0001"
    } else {
      t_p_display <- paste0("p=", t_p)
    }
    
    t_text <- paste0("t-test: stat=", t_stat, ", ", t_p_display)
  } else {
    t_text <- NULL
  }
  
  if (nrow(wilcox_results) > 0) {
    w_stat <- round(wilcox_results$statistic, 0)
    w_p <- formatC(wilcox_results$p.value, format = "f", digits = 4)
    
    # Format p-value for display
    if (wilcox_results$p.value < 0.0001) {
      w_p_display <- "p<0.0001"
    } else {
      w_p_display <- paste0("p=", w_p)
    }
    
    w_text <- paste0("Wilcox: stat=", w_stat, ", ", w_p_display)
  } else {
    w_text <- NULL
  }
  
  # Add comparison of means
  if (!is.na(t_test_results$estimate1[1]) && !is.na(t_test_results$estimate2[1])) {
    group1_mean <- round(t_test_results$estimate1, 1)
    group2_mean <- round(t_test_results$estimate2, 1)
    comp_text <- paste0("(", group1_mean, " vs ", group2_mean, ")")
  } else {
    comp_text <- NULL
  }
  
  # Return the plot and annotation text for below
  return(list(
    plot = p,
    text = list(
      t_test = t_text,
      wilcox = w_text,
      comparison = comp_text
    )
  ))
}

# Custom titles mapping - you can modify these titles
metric_titles <- list(
  "avg_hr_DN_HistogramMode_5" = "HR Histogram Mode (5 Bins)",
  "avg_hr_cv" = "HR Coefficient of Variation",
  "avg_hr_SB_BinaryStats_diff_longstretch0" = "HR Longest Consecutive Decrease", # Longest Run of Zeros in Binary-Differenced Series
  "avg_hr_PD_PeriodicityWang_th0_01" = "HR Periodicity Index (Wang)",
  "avg_hr_IN_AutoMutualInfoStats_40_gaussian_fmmi" = "HR Auto Mutual Information",
  "avg_hr_CO_FirstMin_ac" = "HR First Autocorrelation Minimum"
  # Add more metrics and their custom titles as needed
)

# Comment out automatic metric detection and use the specified list
# metrics_to_plot <- unique(df_long$metric)
metrics_to_plot <- c("avg_hr_DN_HistogramMode_5", "avg_hr_cv", "avg_hr_SB_BinaryStats_diff_longstretch0", 
                     "avg_hr_PD_PeriodicityWang_th0_01", "avg_hr_IN_AutoMutualInfoStats_40_gaussian_fmmi", 
                     "avg_hr_CO_FirstMin_ac")

plot_list <- list()
text_list <- list()

# Create plots with custom titles where available
for (i in seq_along(metrics_to_plot)) {
  metric <- metrics_to_plot[i]
  custom_title <- NULL
  
  # Use custom title if available
  if (metric %in% names(metric_titles)) {
    custom_title <- metric_titles[[metric]]
  }
  
  result <- create_plot(metric, custom_title)
  plot_list[[i]] <- result$plot
  text_list[[i]] <- result$text
}

# Determine a reasonable grid layout based on the number of plots
n_plots <- length(plot_list)
n_cols <- min(3, n_plots)  # Maximum 3 columns
n_rows <- ceiling(n_plots / n_cols)

# Create a combined plot with text below each graph
library(grid)
library(gridExtra)

# Function to create a combined plot with text placed immediately below the graph
create_combined_plot <- function(plot_obj, text_obj, plot_index) {
  # Create text grob with all information
  text_lines <- c()
  
  if (!is.null(text_obj$wilcox)) {
    text_lines <- c(text_lines, text_obj$wilcox)
  }
  
  if (!is.null(text_obj$t_test)) {
    text_lines <- c(text_lines, text_obj$t_test)
  }
  
  if (!is.null(text_obj$comparison)) {
    text_lines <- c(text_lines, text_obj$comparison)
  }
  
  # Join text lines
  text_content <- paste(text_lines, collapse = "\n")
  
  # Create a text grob with larger font size and minimal margins
  text_grob <- textGrob(
    text_content,
    gp = gpar(fontsize = 11),
    just = "center",
    vp = viewport(height = unit(0.9, "npc"))  # Reduces internal padding
  )
  
  # Arrange plot and text with minimal space between
  combined <- arrangeGrob(
    plot_obj,
    text_grob,
    heights = c(4, 0.9),  # Reduced text area height
    padding = unit(0, "line")  # No padding
  )
  
  return(combined)
}

# Create combined plots
combined_plots <- list()
for (i in seq_along(plot_list)) {
  combined_plots[[i]] <- create_combined_plot(plot_list[[i]], text_list[[i]], i)
}

# Layout all plots in a grid with absolutely minimal spacing
grid_plot <- arrangeGrob(
  grobs = combined_plots,
  ncol = n_cols,
  padding = unit(0, "line"),  # No padding at all between panels
  widths = unit(rep(1, n_cols), "null"),
  heights = unit(rep(1, ceiling(n_plots/n_cols)), "null")
)

# Display the plot
grid.newpage()
grid.draw(grid_plot)

# Save the plot with appropriate dimensions (uncomment to use)
# ggsave("metric_comparisons.png", grid_plot, 
#        width = min(n_cols * 3.5, 12),  # Reduced width
#        height = min(n_rows * 3.5, 12),  # Reduced height
#        dpi = 300)
# Once I get both working...

# The selected variables from the original development in Physionet Chaos
# Test with other variables in the future
selected_vars <- c("avg_hr_DN_HistogramMode_5", "avg_hr_cv", "avg_hr_SB_BinaryStats_diff_longstretch0",
                   "avg_hr_PD_PeriodicityWang_th0_01", "avg_hr_IN_AutoMutualInfoStats_40_gaussian_fmmi",
                   "avg_hr_CO_FirstMin_ac", "avg_hr_permen")


project_pca_loadings <- function(
    train_data,
    test_data,
    vars = NULL,        
    n_comp = 4,              # number of PCs to compute/store (must be >= max(plot_pcs))
    center = TRUE,
    scale. = TRUE,
    id_col = NULL,           
    color_var = NULL,
    plot_pcs = c(1, 2)       # 👉 NEW: choose which two PCs to plot
) {
  
  require(dplyr)
  require(ggplot2)
  require(rlang)
  require(tibble)
  
  # -------------------------
  # 1. Variables to use
  # -------------------------
  if (is.null(vars)) {
    num_train <- train_data %>%
      select(where(is.numeric)) %>% names()
    num_test <- test_data %>%
      select(where(is.numeric)) %>% names()
    vars <- intersect(num_train, num_test)
  }
  if (length(vars) == 0) stop("No common numeric variables.")
  
  # -------------------------
  # 2. PCA on training data
  # -------------------------
  train_mat <- train_data %>%
    select(all_of(vars)) %>% as.matrix()
  
  pca_fit <- prcomp(train_mat, center = center, scale. = scale.)
  
  # Validate requested PCs for plotting
  if (max(plot_pcs) > ncol(pca_fit$rotation)) {
    stop("plot_pcs requests PCs not present in the PCA fit.")
  }
  
  # Adjust n_comp to be at least as large as requested PCs
  n_comp <- max(n_comp, max(plot_pcs))
  
  # -------------------------
  # 3. Project test data into training PCA space
  # -------------------------
  test_mat <- test_data %>%
    select(all_of(vars)) %>% as.matrix()
  
  test_scaled <- sweep(test_mat, 2, pca_fit$center, "-")
  if (!is.null(pca_fit$scale)) {
    test_scaled <- sweep(test_scaled, 2, pca_fit$scale, "/")
  }
  
  test_scores_mat <- test_scaled %*% pca_fit$rotation[, seq_len(n_comp), drop = FALSE]
  
  scores_tbl <- as_tibble(test_scores_mat)
  colnames(scores_tbl) <- paste0("PC", seq_len(n_comp))
  
  test_aug <- bind_cols(test_data, scores_tbl)
  
  # -------------------------
  # 4. Plot user-chosen PCs
  # -------------------------
  plot_obj <- NULL
  if (length(plot_pcs) == 2) {
    
    pcx <- paste0("PC", plot_pcs[1])
    pcy <- paste0("PC", plot_pcs[2])
    
    aes_args <- aes(x = .data[[pcx]], y = .data[[pcy]])
    
    if (!is.null(color_var)) {
      aes_args <- modifyList(aes_args, aes(color = !!sym(color_var)))
    }
    if (!is.null(id_col)) {
      aes_args <- modifyList(aes_args, aes(label = !!sym(id_col)))
    }
    
    plot_title <- paste0("Projection of Test Data into Training PCA Space (",
                         pcx, " vs ", pcy, ")")
    
    plot_obj <- ggplot(test_aug, aes_args) +
      geom_point(alpha = 0.7) +
      { if (!is.null(id_col)) ggrepel::geom_text_repel(size = 3, max.overlaps = 20) else NULL } +
      labs(title = plot_title, x = pcx, y = pcy) +
      theme_minimal()
  }
  
  # -------------------------
  # 5. Return list
  # -------------------------
  list(
    pca_fit   = pca_fit,
    test_aug  = test_aug,
    plot      = plot_obj
  )
}



selected_vars <- c("avg_hr_DN_HistogramMode_5", "avg_hr_cv", "avg_hr_SB_BinaryStats_diff_longstretch0",
                   "avg_hr_PD_PeriodicityWang_th0_01", "avg_hr_IN_AutoMutualInfoStats_40_gaussian_fmmi",
                   "avg_hr_CO_FirstMin_ac", "avg_hr_permen")

a <- project_pca_loadings(
    train_data = df_long_s %>% filter(Hypertension %in% c("HTN_2", "Normal")) %>% 
      select(-names) %>% pivot_wider(names_from = metric, values_from = value),
    test_data = df_long_s %>% filter(Hypertension %in% c("HTN_2", "Normal")) %>% 
      select(-names) %>% pivot_wider(names_from = metric, values_from = value),
    vars = metrics_x,        
    n_comp = 4,              # number of PCs to compute/store (must be >= max(plot_pcs))
    center = TRUE,
    scale. = TRUE,
   # id_col = "id",           
    color_var = "Hypertension",
    plot_pcs = c(1, 2)       # choose which two PCs to plot
)

a$plot

b <- project_pca_loadings(
  train_data = df_long_c %>% pivot_wider(names_from = metric, values_from = value),
  test_data = df_long_c %>% pivot_wider(names_from = metric, values_from = value),
  vars = selected_vars,        
  n_comp = 4,              # number of PCs to compute/store (must be >= max(plot_pcs))
  center = TRUE,
  scale. = TRUE,
  # id_col = "id",           
  color_var = "condition",
  plot_pcs = c(1, 2)       # choose which two PCs to plot
)

b$plot + 
  ggtitle("PCA of Heart Rate Time Series Metrics") +
  scale_color_manual(values = c("AF" = "orange", "CHF" = "violetred", "Normal" = "mediumpurple"),
                     labels = c("AF", "CHF", "Control")) +
  geom_point(size = 3) +
  labs(color = "Condition",
       x = "PC1 (41.47%)",
       y = "PC2 (32.72%)") 

# PhysioNet CHAOS Holter Metrics: Group Comparisons by Health Status

2026-03-05

- [1 Setup & Data Loading](#1-setup--data-loading)
- [2 Data Overview & Demographics](#2-data-overview--demographics)
- [3 Boxplots by Condition](#3-boxplots-by-condition)
  - [avg_hr Metrics (catch22 + descriptive +
    entropy)](#avg_hr-metrics-catch22--descriptive--entropy)
  - [HRV Metrics](#hrv-metrics)
- [3.5 Correlation Heatmap](#35-correlation-heatmap)
  - [3.6 Permutation Entropy vs CV
    Scatter](#36-permutation-entropy-vs-cv-scatter)
  - [3.7 SDNN & RMSSD by Condition](#37-sdnn--rmssd-by-condition)
- [4 Omnibus Significance Tests (ANOVA &
  Kruskal-Wallis)](#4-omnibus-significance-tests-anova--kruskal-wallis)
- [5 Pairwise Significance Tests](#5-pairwise-significance-tests)
- [6 PCA Analysis](#6-pca-analysis)
  - [6.1 All Metrics (36)](#61-all-metrics-36)
  - [6.2 avg_hr Metrics Only (34)](#62-avg_hr-metrics-only-34)
  - [6.2.1 HRV vs avg_hr PCA Scores](#621-hrv-vs-avg_hr-pca-scores)
  - [6.2.2 SDNN vs -PC3: Sign-Flipped
    Agreement](#622-sdnn-vs--pc3-sign-flipped-agreement)
  - [6.3 Top Significant avg_hr
    Metrics](#63-top-significant-avg_hr-metrics)
- [7 Summary](#7-summary)
  - [Key Findings](#key-findings)
- [8 Metric Discriminability: PCA Composite vs SD of avg
  HR](#8-metric-discriminability-pca-composite-vs-sd-of-avg-hr)
  - [Recommendation](#recommendation)

## 1 Setup & Data Loading

## 2 Data Overview & Demographics

| condition | 5-min | 1-min |
|:----------|------:|------:|
| Normal    |     5 |     5 |
| CHF       |     5 |     5 |
| AF        |     5 |     5 |

Subjects by condition group

| condition |   F |   M |  NA |
|:----------|----:|----:|----:|
| Normal    |   3 |   2 |   0 |
| CHF       |   0 |   5 |   0 |
| AF        |   0 |   0 |   5 |

Sex distribution by condition

    No missing values in any metric column.

## 3 Boxplots by Condition

### avg_hr Metrics (catch22 + descriptive + entropy)

<div class="panel-tabset">

#### 5-min

![](physionet15_analysis_1_files/figure-commonmark/boxplots-avghr-5min-1.png)

#### 1-min

![](physionet15_analysis_1_files/figure-commonmark/boxplots-avghr-1min-1.png)

</div>

### HRV Metrics

<div class="panel-tabset">

#### 5-min

![](physionet15_analysis_1_files/figure-commonmark/boxplots-hrv-5min-1.png)

#### 1-min

![](physionet15_analysis_1_files/figure-commonmark/boxplots-hrv-1min-1.png)

</div>

## 3.5 Correlation Heatmap

<div class="panel-tabset">

### 5-min

![](physionet15_analysis_1_files/figure-commonmark/corr-heatmap-5min-1.png)

### 1-min

![](physionet15_analysis_1_files/figure-commonmark/corr-heatmap-1min-1.png)

</div>

### 3.6 Permutation Entropy vs CV Scatter

<div class="panel-tabset">

#### 5-min

![](physionet15_analysis_1_files/figure-commonmark/permen-cv-scatter-5min-1.png)

#### 1-min

![](physionet15_analysis_1_files/figure-commonmark/permen-cv-scatter-1min-1.png)

</div>

### 3.7 SDNN & RMSSD by Condition

<div class="panel-tabset">

#### 5-min

![](physionet15_analysis_1_files/figure-commonmark/sdnn-jitter-5min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/rmssd-jitter-5min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/permen-jitter-5min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/sd-jitter-5min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/cv-jitter-5min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/mean-hr-jitter-5min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/median-hr-jitter-5min-1.png)

#### 1-min

![](physionet15_analysis_1_files/figure-commonmark/sdnn-jitter-1min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/rmssd-jitter-1min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/permen-jitter-1min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/sd-jitter-1min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/cv-jitter-1min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/mean-hr-jitter-1min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/median-hr-jitter-1min-1.png)

</div>

## 4 Omnibus Significance Tests (ANOVA & Kruskal-Wallis)

<div class="panel-tabset">

### 5-min

| Metric | Test | Statistic | p-value | p (BH-adj) | Sig |
|:---|:---|---:|---:|---:|:---|
| mean_rmssd | ANOVA | 64.21 | 4.00e-07 | 1.40e-05 | \*\*\* |
| mean_sdnn | ANOVA | 45.38 | 2.50e-06 | 4.57e-05 | \*\*\* |
| mean_rmssd | Kruskal-Wallis | 12.50 | 1.93e-03 | 3.47e-02 | \* |
| mean_sdnn | Kruskal-Wallis | 12.50 | 1.93e-03 | 3.47e-02 | \* |
| cv | ANOVA | 4.96 | 2.69e-02 | 2.61e-01 |  |
| CO_trev_1_num | Kruskal-Wallis | 7.22 | 2.71e-02 | 2.82e-01 |  |
| DN_HistogramMode_5 | ANOVA | 4.78 | 2.98e-02 | 2.61e-01 |  |
| DN_HistogramMode_10 | Kruskal-Wallis | 6.62 | 3.65e-02 | 2.82e-01 |  |
| DN_HistogramMode_5 | Kruskal-Wallis | 6.48 | 3.92e-02 | 2.82e-01 |  |
| CO_trev_1_num | ANOVA | 4.00 | 4.66e-02 | 2.61e-01 |  |
| DN_HistogramMode_10 | ANOVA | 3.97 | 4.75e-02 | 2.61e-01 |  |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | ANOVA | 3.75 | 5.42e-02 | 2.61e-01 |  |
| permen | ANOVA | 3.65 | 5.79e-02 | 2.61e-01 |  |
| cv | Kruskal-Wallis | 5.36 | 6.86e-02 | 2.88e-01 |  |
| min | Kruskal-Wallis | 5.18 | 7.50e-02 | 2.88e-01 |  |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Kruskal-Wallis | 5.04 | 8.06e-02 | 2.88e-01 |  |
| permen | Kruskal-Wallis | 4.94 | 8.46e-02 | 2.88e-01 |  |
| min | ANOVA | 3.02 | 8.67e-02 | 3.47e-01 |  |
| DN_Spread_Std | Kruskal-Wallis | 4.86 | 8.80e-02 | 2.88e-01 |  |
| sd | Kruskal-Wallis | 4.86 | 8.80e-02 | 2.88e-01 |  |
| iqr | Kruskal-Wallis | 4.56 | 1.02e-01 | 3.07e-01 |  |
| DN_Spread_Std | ANOVA | 2.23 | 1.50e-01 | 4.21e-01 |  |
| sd | ANOVA | 2.23 | 1.50e-01 | 4.21e-01 |  |
| DN_Mean | ANOVA | 2.21 | 1.52e-01 | 4.21e-01 |  |
| mean | ANOVA | 2.21 | 1.52e-01 | 4.21e-01 |  |
| median | ANOVA | 1.99 | 1.80e-01 | 4.35e-01 |  |
| max | ANOVA | 1.98 | 1.81e-01 | 4.35e-01 |  |
| max | Kruskal-Wallis | 2.94 | 2.30e-01 | 5.95e-01 |  |
| iqr | ANOVA | 1.61 | 2.39e-01 | 5.21e-01 |  |
| DN_OutlierInclude_n_001_mdrmd | ANOVA | 1.58 | 2.46e-01 | 5.21e-01 |  |
| DN_Mean | Kruskal-Wallis | 2.78 | 2.49e-01 | 5.95e-01 |  |
| mean | Kruskal-Wallis | 2.78 | 2.49e-01 | 5.95e-01 |  |
| SB_BinaryStats_mean_longstretch1 | ANOVA | 1.51 | 2.60e-01 | 5.21e-01 |  |
| DN_OutlierInclude_n_001_mdrmd | Kruskal-Wallis | 2.66 | 2.64e-01 | 5.95e-01 |  |
| FC_LocalSimple_mean1_tauresrat | Kruskal-Wallis | 2.54 | 2.81e-01 | 5.95e-01 |  |
| median | Kruskal-Wallis | 2.42 | 2.98e-01 | 5.96e-01 |  |
| DN_OutlierInclude_p_001_mdrmd | ANOVA | 1.20 | 3.34e-01 | 5.88e-01 |  |
| CO_f1ecac | ANOVA | 1.20 | 3.35e-01 | 5.88e-01 |  |
| FC_LocalSimple_mean1_tauresrat | ANOVA | 1.17 | 3.43e-01 | 5.88e-01 |  |
| PD_PeriodicityWang_th0_01 | ANOVA | 1.12 | 3.59e-01 | 5.88e-01 |  |
| SB_BinaryStats_mean_longstretch1 | Kruskal-Wallis | 2.00 | 3.68e-01 | 6.94e-01 |  |
| apen | Kruskal-Wallis | 1.82 | 4.03e-01 | 6.94e-01 |  |
| PD_PeriodicityWang_th0_01 | Kruskal-Wallis | 1.81 | 4.05e-01 | 6.94e-01 |  |
| CO_f1ecac | Kruskal-Wallis | 1.50 | 4.72e-01 | 7.73e-01 |  |
| apen | ANOVA | 0.80 | 4.73e-01 | 7.20e-01 |  |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | ANOVA | 0.78 | 4.80e-01 | 7.20e-01 |  |
| DN_OutlierInclude_p_001_mdrmd | Kruskal-Wallis | 1.34 | 5.12e-01 | 8.01e-01 |  |
| SP_Summaries_welch_rect_centroid | ANOVA | 0.67 | 5.28e-01 | 7.60e-01 |  |
| SP_Summaries_welch_rect_centroid | Kruskal-Wallis | 1.15 | 5.64e-01 | 8.23e-01 |  |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Kruskal-Wallis | 1.10 | 5.77e-01 | 8.23e-01 |  |
| sampen | Kruskal-Wallis | 1.04 | 5.95e-01 | 8.23e-01 |  |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | ANOVA | 0.48 | 6.30e-01 | 8.24e-01 |  |
| MD_hrv_classic_pnn40 | ANOVA | 0.47 | 6.36e-01 | 8.24e-01 |  |
| sampen | ANOVA | 0.46 | 6.45e-01 | 8.24e-01 |  |
| SP_Summaries_welch_rect_area_5_1 | ANOVA | 0.39 | 6.83e-01 | 8.24e-01 |  |
| MD_hrv_classic_pnn40 | Kruskal-Wallis | 0.76 | 6.85e-01 | 9.13e-01 |  |
| SB_TransitionMatrix_3ac_sumdiagcov | ANOVA | 0.37 | 6.96e-01 | 8.24e-01 |  |
| CO_HistogramAMI_even_2_5 | ANOVA | 0.35 | 7.09e-01 | 8.24e-01 |  |
| SB_TransitionMatrix_3ac_sumdiagcov | Kruskal-Wallis | 0.58 | 7.48e-01 | 9.41e-01 |  |
| SB_MotifThree_quantile_hh | ANOVA | 0.29 | 7.51e-01 | 8.45e-01 |  |
| CO_HistogramAMI_even_2_5 | Kruskal-Wallis | 0.50 | 7.79e-01 | 9.41e-01 |  |
| CO_FirstMin_ac | ANOVA | 0.24 | 7.93e-01 | 8.47e-01 |  |
| FC_LocalSimple_mean3_stderr | ANOVA | 0.23 | 8.00e-01 | 8.47e-01 |  |
| SB_BinaryStats_diff_longstretch0 | Kruskal-Wallis | 0.43 | 8.08e-01 | 9.41e-01 |  |
| SB_MotifThree_quantile_hh | Kruskal-Wallis | 0.42 | 8.11e-01 | 9.41e-01 |  |
| CO_FirstMin_ac | Kruskal-Wallis | 0.25 | 8.84e-01 | 9.66e-01 |  |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Kruskal-Wallis | 0.24 | 8.85e-01 | 9.66e-01 |  |
| SB_BinaryStats_diff_longstretch0 | ANOVA | 0.12 | 8.88e-01 | 9.14e-01 |  |
| FC_LocalSimple_mean3_stderr | Kruskal-Wallis | 0.06 | 9.70e-01 | 9.90e-01 |  |
| CO_Embed2_Dist_tau_d_expfit_meandiff | ANOVA | 0.01 | 9.87e-01 | 9.87e-01 |  |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Kruskal-Wallis | 0.02 | 9.90e-01 | 9.90e-01 |  |
| SP_Summaries_welch_rect_area_5_1 | Kruskal-Wallis | 0.02 | 9.90e-01 | 9.90e-01 |  |

### 1-min

| Metric | Test | Statistic | p-value | p (BH-adj) | Sig |
|:---|:---|---:|---:|---:|:---|
| mean_rmssd | ANOVA | 63.05 | 4.00e-07 | 1.55e-05 | \*\*\* |
| mean_sdnn | ANOVA | 45.42 | 2.50e-06 | 4.54e-05 | \*\*\* |
| mean_rmssd | Kruskal-Wallis | 12.50 | 1.93e-03 | 3.47e-02 | \* |
| mean_sdnn | Kruskal-Wallis | 12.50 | 1.93e-03 | 3.47e-02 | \* |
| MD_hrv_classic_pnn40 | ANOVA | 7.01 | 9.64e-03 | 1.16e-01 |  |
| cv | ANOVA | 5.02 | 2.61e-02 | 2.01e-01 |  |
| DN_HistogramMode_5 | ANOVA | 4.79 | 2.96e-02 | 2.01e-01 |  |
| PD_PeriodicityWang_th0_01 | ANOVA | 4.57 | 3.35e-02 | 2.01e-01 |  |
| DN_HistogramMode_5 | Kruskal-Wallis | 6.74 | 3.44e-02 | 2.61e-01 |  |
| MD_hrv_classic_pnn40 | Kruskal-Wallis | 6.74 | 3.44e-02 | 2.61e-01 |  |
| cv | Kruskal-Wallis | 6.54 | 3.80e-02 | 2.61e-01 |  |
| permen | ANOVA | 3.83 | 5.17e-02 | 2.38e-01 |  |
| apen | Kruskal-Wallis | 5.78 | 5.56e-02 | 2.61e-01 |  |
| DN_Spread_Std | Kruskal-Wallis | 5.66 | 5.90e-02 | 2.61e-01 |  |
| sd | Kruskal-Wallis | 5.66 | 5.90e-02 | 2.61e-01 |  |
| apen | ANOVA | 3.55 | 6.16e-02 | 2.38e-01 |  |
| permen | Kruskal-Wallis | 5.46 | 6.52e-02 | 2.61e-01 |  |
| sampen | ANOVA | 3.46 | 6.52e-02 | 2.38e-01 |  |
| min | ANOVA | 3.43 | 6.62e-02 | 2.38e-01 |  |
| min | Kruskal-Wallis | 5.18 | 7.50e-02 | 2.70e-01 |  |
| sampen | Kruskal-Wallis | 4.86 | 8.80e-02 | 2.88e-01 |  |
| DN_HistogramMode_10 | ANOVA | 2.78 | 1.02e-01 | 3.33e-01 |  |
| PD_PeriodicityWang_th0_01 | Kruskal-Wallis | 4.47 | 1.07e-01 | 3.21e-01 |  |
| DN_HistogramMode_10 | Kruskal-Wallis | 4.22 | 1.21e-01 | 3.36e-01 |  |
| iqr | Kruskal-Wallis | 3.98 | 1.37e-01 | 3.38e-01 |  |
| CO_trev_1_num | Kruskal-Wallis | 3.92 | 1.41e-01 | 3.38e-01 |  |
| DN_Spread_Std | ANOVA | 2.25 | 1.48e-01 | 3.47e-01 |  |
| sd | ANOVA | 2.25 | 1.48e-01 | 3.47e-01 |  |
| DN_Mean | ANOVA | 2.18 | 1.56e-01 | 3.47e-01 |  |
| mean | ANOVA | 2.18 | 1.56e-01 | 3.47e-01 |  |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Kruskal-Wallis | 3.69 | 1.58e-01 | 3.42e-01 |  |
| CO_FirstMin_ac | Kruskal-Wallis | 3.65 | 1.61e-01 | 3.42e-01 |  |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | ANOVA | 2.07 | 1.69e-01 | 3.47e-01 |  |
| SB_BinaryStats_diff_longstretch0 | ANOVA | 2.07 | 1.69e-01 | 3.47e-01 |  |
| median | ANOVA | 2.01 | 1.77e-01 | 3.47e-01 |  |
| DN_OutlierInclude_n_001_mdrmd | Kruskal-Wallis | 3.44 | 1.79e-01 | 3.50e-01 |  |
| DN_OutlierInclude_n_001_mdrmd | ANOVA | 1.96 | 1.83e-01 | 3.47e-01 |  |
| FC_LocalSimple_mean1_tauresrat | Kruskal-Wallis | 3.38 | 1.85e-01 | 3.50e-01 |  |
| FC_LocalSimple_mean1_tauresrat | ANOVA | 1.78 | 2.10e-01 | 3.63e-01 |  |
| CO_trev_1_num | ANOVA | 1.77 | 2.11e-01 | 3.63e-01 |  |
| DN_Mean | Kruskal-Wallis | 2.78 | 2.49e-01 | 4.27e-01 |  |
| mean | Kruskal-Wallis | 2.78 | 2.49e-01 | 4.27e-01 |  |
| iqr | ANOVA | 1.54 | 2.54e-01 | 3.98e-01 |  |
| max | ANOVA | 1.54 | 2.54e-01 | 3.98e-01 |  |
| SP_Summaries_welch_rect_centroid | Kruskal-Wallis | 2.57 | 2.77e-01 | 4.53e-01 |  |
| median | Kruskal-Wallis | 2.42 | 2.98e-01 | 4.67e-01 |  |
| DN_OutlierInclude_p_001_mdrmd | ANOVA | 1.31 | 3.06e-01 | 4.59e-01 |  |
| SB_BinaryStats_diff_longstretch0 | Kruskal-Wallis | 2.22 | 3.29e-01 | 4.70e-01 |  |
| CO_f1ecac | ANOVA | 1.21 | 3.33e-01 | 4.78e-01 |  |
| max | Kruskal-Wallis | 2.18 | 3.36e-01 | 4.70e-01 |  |
| SP_Summaries_welch_rect_area_5_1 | Kruskal-Wallis | 2.16 | 3.40e-01 | 4.70e-01 |  |
| SB_BinaryStats_mean_longstretch1 | ANOVA | 1.16 | 3.45e-01 | 4.78e-01 |  |
| SP_Summaries_welch_rect_area_5_1 | ANOVA | 1.03 | 3.85e-01 | 5.14e-01 |  |
| CO_f1ecac | Kruskal-Wallis | 1.82 | 4.03e-01 | 5.37e-01 |  |
| SB_MotifThree_quantile_hh | ANOVA | 0.95 | 4.16e-01 | 5.34e-01 |  |
| DN_OutlierInclude_p_001_mdrmd | Kruskal-Wallis | 1.58 | 4.54e-01 | 5.63e-01 |  |
| SB_BinaryStats_mean_longstretch1 | Kruskal-Wallis | 1.58 | 4.54e-01 | 5.63e-01 |  |
| SP_Summaries_welch_rect_centroid | ANOVA | 0.77 | 4.85e-01 | 5.98e-01 |  |
| CO_FirstMin_ac | ANOVA | 0.74 | 4.98e-01 | 5.98e-01 |  |
| FC_LocalSimple_mean3_stderr | ANOVA | 0.67 | 5.31e-01 | 6.17e-01 |  |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | ANOVA | 0.51 | 6.11e-01 | 6.87e-01 |  |
| SB_MotifThree_quantile_hh | Kruskal-Wallis | 0.98 | 6.13e-01 | 7.35e-01 |  |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | ANOVA | 0.46 | 6.43e-01 | 7.01e-01 |  |
| FC_LocalSimple_mean3_stderr | Kruskal-Wallis | 0.74 | 6.91e-01 | 7.77e-01 |  |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Kruskal-Wallis | 0.74 | 6.91e-01 | 7.77e-01 |  |
| CO_HistogramAMI_even_2_5 | ANOVA | 0.35 | 7.09e-01 | 7.50e-01 |  |
| CO_Embed2_Dist_tau_d_expfit_meandiff | ANOVA | 0.32 | 7.33e-01 | 7.54e-01 |  |
| CO_HistogramAMI_even_2_5 | Kruskal-Wallis | 0.62 | 7.33e-01 | 8.00e-01 |  |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Kruskal-Wallis | 0.39 | 8.24e-01 | 8.51e-01 |  |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Kruskal-Wallis | 0.38 | 8.27e-01 | 8.51e-01 |  |
| SB_TransitionMatrix_3ac_sumdiagcov | ANOVA | 0.08 | 9.22e-01 | 9.22e-01 |  |
| SB_TransitionMatrix_3ac_sumdiagcov | Kruskal-Wallis | 0.06 | 9.69e-01 | 9.69e-01 |  |

</div>

## 5 Pairwise Significance Tests

<div class="panel-tabset">

### 5-min

**Summary — most significant pair per metric:**

| Metric | Most Sig. Pair | W stat | Wilcox p | Wilcox p (BH) | t-test p | Sig |
|:---|:---|---:|---:|---:|---:|:---|
| mean_rmssd | Normal vs CHF | 25.0 | 0.00794 | 0.143 | 0.0348 |  |
| mean_sdnn | Normal vs CHF | 25.0 | 0.00794 | 0.143 | 0.0015 |  |
| CO_trev_1_num | Normal vs AF | 1.0 | 0.01590 | 0.245 | 0.0562 |  |
| DN_HistogramMode_10 | Normal vs CHF | 2.0 | 0.03170 | 0.333 | 0.0325 |  |
| DN_HistogramMode_5 | Normal vs CHF | 2.0 | 0.03170 | 0.333 | 0.0130 |  |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Normal vs CHF | 2.5 | 0.04520 | 0.333 | 0.0536 |  |
| DN_Spread_Std | CHF vs AF | 3.0 | 0.05560 | 0.333 | 0.1290 |  |
| cv | Normal vs CHF | 22.0 | 0.05560 | 0.333 | 0.0262 |  |
| iqr | Normal vs CHF | 22.0 | 0.05560 | 0.333 | 0.1410 |  |
| min | Normal vs CHF | 3.0 | 0.05560 | 0.333 | 0.0457 |  |
| permen | Normal vs CHF | 3.0 | 0.05560 | 0.333 | 0.0626 |  |
| sd | CHF vs AF | 3.0 | 0.05560 | 0.333 | 0.1290 |  |
| DN_Mean | Normal vs AF | 5.0 | 0.15100 | 0.494 | 0.0878 |  |
| DN_OutlierInclude_n_001_mdrmd | CHF vs AF | 20.0 | 0.15100 | 0.494 | 0.1420 |  |
| FC_LocalSimple_mean1_tauresrat | CHF vs AF | 20.0 | 0.15100 | 0.494 | 0.2740 |  |
| PD_PeriodicityWang_th0_01 | Normal vs CHF | 5.0 | 0.15100 | 0.494 | 0.1800 |  |
| max | Normal vs CHF | 20.0 | 0.15100 | 0.494 | 0.3950 |  |
| mean | Normal vs AF | 5.0 | 0.15100 | 0.494 | 0.0878 |  |
| median | Normal vs AF | 5.0 | 0.15100 | 0.494 | 0.0832 |  |
| SB_BinaryStats_mean_longstretch1 | Normal vs CHF | 19.0 | 0.22200 | 0.667 | 0.1900 |  |
| apen | CHF vs AF | 6.0 | 0.22200 | 0.667 | 0.2680 |  |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Normal vs CHF | 7.0 | 0.29000 | 0.727 | 0.2500 |  |
| CO_f1ecac | Normal vs CHF | 18.0 | 0.31000 | 0.727 | 0.2680 |  |
| DN_OutlierInclude_p_001_mdrmd | Normal vs AF | 7.0 | 0.31000 | 0.727 | 0.2380 |  |
| SP_Summaries_welch_rect_centroid | Normal vs CHF | 7.5 | 0.34000 | 0.778 | 0.3530 |  |
| CO_HistogramAMI_even_2_5 | Normal vs AF | 17.0 | 0.42100 | 0.797 | 0.4630 |  |
| MD_hrv_classic_pnn40 | Normal vs AF | 8.0 | 0.42100 | 0.797 | 0.4730 |  |
| sampen | CHF vs AF | 8.0 | 0.42100 | 0.797 | 0.3970 |  |
| SB_TransitionMatrix_3ac_sumdiagcov | Normal vs AF | 16.0 | 0.51500 | 0.910 | 0.9170 |  |
| SB_BinaryStats_diff_longstretch0 | Normal vs CHF | 9.5 | 0.58400 | 0.940 | 0.7000 |  |
| CO_FirstMin_ac | Normal vs CHF | 9.5 | 0.59800 | 0.940 | 1.0000 |  |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Normal vs CHF | 15.5 | 0.59900 | 0.940 | 0.3410 |  |
| SB_MotifThree_quantile_hh | Normal vs CHF | 10.0 | 0.69000 | 0.968 | 0.5600 |  |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Normal vs CHF | 11.0 | 0.84100 | 1.000 | 0.8900 |  |
| FC_LocalSimple_mean3_stderr | CHF vs AF | 11.0 | 0.84100 | 1.000 | 0.5950 |  |
| SP_Summaries_welch_rect_area_5_1 | Normal vs CHF | 11.0 | 0.84100 | 1.000 | 0.6930 |  |

Most significant pairwise comparison per metric (Wilcoxon)

<details>

<summary>

Full pairwise results (click to expand)
</summary>

| Metric | Pair | t stat | t p | t p (BH) | W stat | W p | W p (BH) |
|:---|:---|---:|---:|---:|---:|---:|---:|
| mean_rmssd | Normal vs CHF | 2.88 | 0.034800 | 0.4180 | 25.0 | 0.00794 | 0.143 |
| mean_sdnn | Normal vs CHF | 5.90 | 0.001500 | 0.0405 | 25.0 | 0.00794 | 0.143 |
| mean_rmssd | Normal vs AF | -7.54 | 0.000728 | 0.0405 | 0.0 | 0.00794 | 0.143 |
| mean_sdnn | Normal vs AF | -5.67 | 0.002860 | 0.0618 | 0.0 | 0.00794 | 0.143 |
| mean_rmssd | CHF vs AF | -8.90 | 0.000780 | 0.0405 | 0.0 | 0.00794 | 0.143 |
| mean_sdnn | CHF vs AF | -7.79 | 0.001280 | 0.0405 | 0.0 | 0.00794 | 0.143 |
| CO_trev_1_num | Normal vs AF | -2.38 | 0.056200 | 0.4670 | 1.0 | 0.01590 | 0.245 |
| DN_HistogramMode_10 | Normal vs CHF | -2.62 | 0.032500 | 0.4180 | 2.0 | 0.03170 | 0.333 |
| DN_HistogramMode_5 | Normal vs CHF | -3.18 | 0.013000 | 0.2340 | 2.0 | 0.03170 | 0.333 |
| DN_HistogramMode_10 | Normal vs AF | -2.48 | 0.040600 | 0.4380 | 2.0 | 0.03170 | 0.333 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Normal vs CHF | -2.43 | 0.053600 | 0.4670 | 2.5 | 0.04520 | 0.333 |
| cv | Normal vs CHF | 2.76 | 0.026200 | 0.4040 | 22.0 | 0.05560 | 0.333 |
| iqr | Normal vs CHF | 1.64 | 0.141000 | 0.5550 | 22.0 | 0.05560 | 0.333 |
| min | Normal vs CHF | -2.37 | 0.045700 | 0.4490 | 3.0 | 0.05560 | 0.333 |
| permen | Normal vs CHF | -2.28 | 0.062600 | 0.4740 | 3.0 | 0.05560 | 0.333 |
| CO_trev_1_num | CHF vs AF | -1.88 | 0.112000 | 0.5270 | 3.0 | 0.05560 | 0.333 |
| DN_Spread_Std | CHF vs AF | -1.70 | 0.129000 | 0.5550 | 3.0 | 0.05560 | 0.333 |
| sd | CHF vs AF | -1.70 | 0.129000 | 0.5550 | 3.0 | 0.05560 | 0.333 |
| DN_Spread_Std | Normal vs CHF | 1.82 | 0.108000 | 0.5270 | 21.0 | 0.09520 | 0.490 |
| sd | Normal vs CHF | 1.82 | 0.108000 | 0.5270 | 21.0 | 0.09520 | 0.490 |
| cv | CHF vs AF | -2.10 | 0.075700 | 0.4740 | 4.0 | 0.09520 | 0.490 |
| PD_PeriodicityWang_th0_01 | Normal vs CHF | -1.54 | 0.180000 | 0.6220 | 5.0 | 0.15100 | 0.494 |
| max | Normal vs CHF | 0.92 | 0.395000 | 0.7150 | 20.0 | 0.15100 | 0.494 |
| DN_HistogramMode_5 | Normal vs AF | -0.97 | 0.360000 | 0.7150 | 5.0 | 0.15100 | 0.494 |
| DN_Mean | Normal vs AF | -2.19 | 0.087800 | 0.4740 | 5.0 | 0.15100 | 0.494 |
| mean | Normal vs AF | -2.19 | 0.087800 | 0.4740 | 5.0 | 0.15100 | 0.494 |
| median | Normal vs AF | -2.22 | 0.083200 | 0.4740 | 5.0 | 0.15100 | 0.494 |
| min | Normal vs AF | -2.13 | 0.087800 | 0.4740 | 5.0 | 0.15100 | 0.494 |
| DN_HistogramMode_5 | CHF vs AF | 2.01 | 0.080600 | 0.4740 | 20.0 | 0.15100 | 0.494 |
| DN_OutlierInclude_n_001_mdrmd | CHF vs AF | 1.63 | 0.142000 | 0.5550 | 20.0 | 0.15100 | 0.494 |
| FC_LocalSimple_mean1_tauresrat | CHF vs AF | 1.26 | 0.274000 | 0.6320 | 20.0 | 0.15100 | 0.494 |
| min | CHF vs AF | -0.98 | 0.369000 | 0.7150 | 5.0 | 0.15100 | 0.494 |
| permen | CHF vs AF | 1.63 | 0.149000 | 0.5550 | 20.0 | 0.15100 | 0.494 |
| SB_BinaryStats_mean_longstretch1 | Normal vs CHF | 1.50 | 0.190000 | 0.6220 | 19.0 | 0.22200 | 0.667 |
| apen | CHF vs AF | -1.19 | 0.268000 | 0.6320 | 6.0 | 0.22200 | 0.667 |
| iqr | CHF vs AF | -1.04 | 0.332000 | 0.7150 | 6.0 | 0.22200 | 0.667 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Normal vs AF | -1.48 | 0.189000 | 0.6220 | 6.5 | 0.24800 | 0.723 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | CHF vs AF | 1.50 | 0.172000 | 0.6190 | 18.0 | 0.28700 | 0.727 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Normal vs CHF | -1.25 | 0.250000 | 0.6320 | 7.0 | 0.29000 | 0.727 |
| CO_f1ecac | Normal vs CHF | 1.19 | 0.268000 | 0.6320 | 18.0 | 0.31000 | 0.727 |
| FC_LocalSimple_mean1_tauresrat | Normal vs CHF | -0.95 | 0.384000 | 0.7150 | 7.0 | 0.31000 | 0.727 |
| DN_OutlierInclude_p_001_mdrmd | Normal vs AF | -1.36 | 0.238000 | 0.6320 | 7.0 | 0.31000 | 0.727 |
| max | Normal vs AF | -1.25 | 0.272000 | 0.6320 | 7.0 | 0.31000 | 0.727 |
| DN_Mean | CHF vs AF | -1.17 | 0.275000 | 0.6320 | 7.0 | 0.31000 | 0.727 |
| max | CHF vs AF | -1.64 | 0.149000 | 0.5550 | 7.0 | 0.31000 | 0.727 |
| mean | CHF vs AF | -1.17 | 0.275000 | 0.6320 | 7.0 | 0.31000 | 0.727 |
| SP_Summaries_welch_rect_centroid | Normal vs CHF | -1.00 | 0.353000 | 0.7150 | 7.5 | 0.34000 | 0.778 |
| SB_BinaryStats_mean_longstretch1 | Normal vs AF | 1.27 | 0.243000 | 0.6320 | 17.5 | 0.34600 | 0.778 |
| CO_trev_1_num | Normal vs CHF | -0.85 | 0.419000 | 0.7190 | 8.0 | 0.42100 | 0.797 |
| CO_HistogramAMI_even_2_5 | Normal vs AF | 0.78 | 0.463000 | 0.7190 | 17.0 | 0.42100 | 0.797 |
| CO_f1ecac | Normal vs AF | 1.39 | 0.205000 | 0.6320 | 17.0 | 0.42100 | 0.797 |
| DN_OutlierInclude_n_001_mdrmd | Normal vs AF | 1.14 | 0.291000 | 0.6540 | 17.0 | 0.42100 | 0.797 |
| MD_hrv_classic_pnn40 | Normal vs AF | -0.76 | 0.473000 | 0.7190 | 8.0 | 0.42100 | 0.797 |
| cv | Normal vs AF | 1.40 | 0.214000 | 0.6320 | 17.0 | 0.42100 | 0.797 |
| iqr | Normal vs AF | 0.84 | 0.429000 | 0.7190 | 17.0 | 0.42100 | 0.797 |
| permen | Normal vs AF | -1.49 | 0.199000 | 0.6320 | 8.0 | 0.42100 | 0.797 |
| sampen | CHF vs AF | -0.90 | 0.397000 | 0.7150 | 8.0 | 0.42100 | 0.797 |
| SB_TransitionMatrix_3ac_sumdiagcov | Normal vs AF | 0.11 | 0.917000 | 0.9920 | 16.0 | 0.51500 | 0.910 |
| SP_Summaries_welch_rect_centroid | Normal vs AF | -0.99 | 0.376000 | 0.7150 | 9.0 | 0.52300 | 0.910 |
| DN_OutlierInclude_n_001_mdrmd | Normal vs CHF | -0.66 | 0.525000 | 0.7470 | 9.0 | 0.54800 | 0.910 |
| DN_OutlierInclude_p_001_mdrmd | Normal vs CHF | -1.22 | 0.264000 | 0.6320 | 9.0 | 0.54800 | 0.910 |
| median | Normal vs CHF | -1.00 | 0.368000 | 0.7150 | 9.0 | 0.54800 | 0.910 |
| apen | Normal vs AF | -0.84 | 0.426000 | 0.7190 | 9.0 | 0.54800 | 0.910 |
| sampen | Normal vs AF | -0.70 | 0.504000 | 0.7330 | 9.0 | 0.54800 | 0.910 |
| median | CHF vs AF | -0.93 | 0.378000 | 0.7150 | 9.0 | 0.54800 | 0.910 |
| SB_BinaryStats_diff_longstretch0 | Normal vs CHF | -0.40 | 0.700000 | 0.8580 | 9.5 | 0.58400 | 0.940 |
| CO_FirstMin_ac | Normal vs CHF | 0.00 | 1.000000 | 1.0000 | 9.5 | 0.59800 | 0.940 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Normal vs CHF | 1.02 | 0.341000 | 0.7150 | 15.5 | 0.59900 | 0.940 |
| PD_PeriodicityWang_th0_01 | Normal vs AF | -1.28 | 0.253000 | 0.6320 | 9.5 | 0.60000 | 0.940 |
| SB_TransitionMatrix_3ac_sumdiagcov | Normal vs CHF | 0.69 | 0.509000 | 0.7330 | 15.0 | 0.66200 | 0.968 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Normal vs AF | -1.12 | 0.315000 | 0.6940 | 10.0 | 0.67300 | 0.968 |
| DN_Mean | Normal vs CHF | -0.79 | 0.470000 | 0.7190 | 10.0 | 0.69000 | 0.968 |
| MD_hrv_classic_pnn40 | Normal vs CHF | -0.77 | 0.473000 | 0.7190 | 10.0 | 0.69000 | 0.968 |
| SB_MotifThree_quantile_hh | Normal vs CHF | -0.61 | 0.560000 | 0.7760 | 10.0 | 0.69000 | 0.968 |
| apen | Normal vs CHF | 0.39 | 0.707000 | 0.8580 | 15.0 | 0.69000 | 0.968 |
| mean | Normal vs CHF | -0.79 | 0.470000 | 0.7190 | 10.0 | 0.69000 | 0.968 |
| SB_MotifThree_quantile_hh | Normal vs AF | -0.76 | 0.469000 | 0.7190 | 10.0 | 0.69000 | 0.968 |
| SB_BinaryStats_diff_longstretch0 | CHF vs AF | 0.45 | 0.667000 | 0.8370 | 14.5 | 0.74700 | 1.000 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Normal vs CHF | -0.14 | 0.890000 | 0.9920 | 11.0 | 0.84100 | 1.000 |
| SP_Summaries_welch_rect_area_5_1 | Normal vs CHF | -0.41 | 0.693000 | 0.8580 | 11.0 | 0.84100 | 1.000 |
| sampen | Normal vs CHF | 0.15 | 0.888000 | 0.9920 | 14.0 | 0.84100 | 1.000 |
| SP_Summaries_welch_rect_area_5_1 | Normal vs AF | 0.52 | 0.622000 | 0.8000 | 14.0 | 0.84100 | 1.000 |
| DN_OutlierInclude_p_001_mdrmd | CHF vs AF | -0.75 | 0.486000 | 0.7190 | 11.0 | 0.84100 | 1.000 |
| FC_LocalSimple_mean3_stderr | CHF vs AF | -0.56 | 0.595000 | 0.7920 | 11.0 | 0.84100 | 1.000 |
| SB_BinaryStats_mean_longstretch1 | CHF vs AF | -0.08 | 0.941000 | 1.0000 | 14.0 | 0.84100 | 1.000 |
| SB_MotifThree_quantile_hh | CHF vs AF | -0.04 | 0.970000 | 1.0000 | 14.0 | 0.84100 | 1.000 |
| SB_TransitionMatrix_3ac_sumdiagcov | CHF vs AF | -0.75 | 0.479000 | 0.7190 | 11.5 | 0.91400 | 1.000 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Normal vs AF | 0.58 | 0.581000 | 0.7840 | 13.5 | 0.91600 | 1.000 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | CHF vs AF | -0.35 | 0.739000 | 0.8770 | 13.5 | 0.91600 | 1.000 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | CHF vs AF | -0.37 | 0.724000 | 0.8690 | 13.5 | 0.91600 | 1.000 |
| CO_HistogramAMI_even_2_5 | Normal vs CHF | 0.01 | 0.990000 | 1.0000 | 13.0 | 1.00000 | 1.000 |
| FC_LocalSimple_mean3_stderr | Normal vs CHF | 0.03 | 0.979000 | 1.0000 | 12.0 | 1.00000 | 1.000 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Normal vs AF | -0.14 | 0.893000 | 0.9920 | 13.0 | 1.00000 | 1.000 |
| CO_FirstMin_ac | Normal vs AF | -0.50 | 0.632000 | 0.8030 | 12.0 | 1.00000 | 1.000 |
| DN_Spread_Std | Normal vs AF | 0.12 | 0.905000 | 0.9920 | 13.0 | 1.00000 | 1.000 |
| FC_LocalSimple_mean1_tauresrat | Normal vs AF | 0.64 | 0.555000 | 0.7760 | 12.0 | 1.00000 | 1.000 |
| FC_LocalSimple_mean3_stderr | Normal vs AF | -0.53 | 0.610000 | 0.7940 | 12.0 | 1.00000 | 1.000 |
| SB_BinaryStats_diff_longstretch0 | Normal vs AF | 0.00 | 1.000000 | 1.0000 | 12.0 | 1.00000 | 1.000 |
| sd | Normal vs AF | 0.12 | 0.905000 | 0.9920 | 13.0 | 1.00000 | 1.000 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | CHF vs AF | -0.04 | 0.966000 | 1.0000 | 12.0 | 1.00000 | 1.000 |
| CO_FirstMin_ac | CHF vs AF | -0.56 | 0.602000 | 0.7920 | 13.0 | 1.00000 | 1.000 |
| CO_HistogramAMI_even_2_5 | CHF vs AF | 0.77 | 0.466000 | 0.7190 | 13.0 | 1.00000 | 1.000 |
| CO_f1ecac | CHF vs AF | 0.15 | 0.882000 | 0.9920 | 13.0 | 1.00000 | 1.000 |
| DN_HistogramMode_10 | CHF vs AF | 0.11 | 0.918000 | 0.9920 | 12.0 | 1.00000 | 1.000 |
| MD_hrv_classic_pnn40 | CHF vs AF | -0.07 | 0.947000 | 1.0000 | 12.5 | 1.00000 | 1.000 |
| PD_PeriodicityWang_th0_01 | CHF vs AF | 0.23 | 0.820000 | 0.9630 | 13.0 | 1.00000 | 1.000 |
| SP_Summaries_welch_rect_area_5_1 | CHF vs AF | 0.77 | 0.476000 | 0.7190 | 12.0 | 1.00000 | 1.000 |
| SP_Summaries_welch_rect_centroid | CHF vs AF | -0.59 | 0.578000 | 0.7840 | 13.0 | 1.00000 | 1.000 |

</details>

### 1-min

**Summary — most significant pair per metric:**

| Metric | Most Sig. Pair | W stat | Wilcox p | Wilcox p (BH) | t-test p | Sig |
|:---|:---|---:|---:|---:|---:|:---|
| mean_rmssd | Normal vs CHF | 25.0 | 0.00794 | 0.143 | 0.03440 |  |
| mean_sdnn | Normal vs CHF | 25.0 | 0.00794 | 0.143 | 0.00216 |  |
| DN_HistogramMode_5 | CHF vs AF | 24.0 | 0.01590 | 0.214 | 0.01770 |  |
| apen | CHF vs AF | 1.0 | 0.01590 | 0.214 | 0.04550 |  |
| MD_hrv_classic_pnn40 | Normal vs AF | 2.0 | 0.03170 | 0.300 | 0.01530 |  |
| cv | Normal vs CHF | 23.0 | 0.03170 | 0.300 | 0.02670 |  |
| DN_HistogramMode_10 | Normal vs CHF | 3.0 | 0.05560 | 0.300 | 0.04750 |  |
| DN_Spread_Std | Normal vs CHF | 22.0 | 0.05560 | 0.300 | 0.10500 |  |
| min | Normal vs CHF | 3.0 | 0.05560 | 0.300 | 0.05030 |  |
| permen | Normal vs CHF | 3.0 | 0.05560 | 0.300 | 0.05960 |  |
| sampen | Normal vs AF | 3.0 | 0.05560 | 0.300 | 0.09210 |  |
| sd | Normal vs CHF | 22.0 | 0.05560 | 0.300 | 0.10500 |  |
| PD_PeriodicityWang_th0_01 | Normal vs CHF | 3.0 | 0.05930 | 0.305 | 0.02910 |  |
| CO_FirstMin_ac | Normal vs CHF | 4.0 | 0.09520 | 0.367 | 0.10600 |  |
| CO_trev_1_num | Normal vs AF | 4.0 | 0.09520 | 0.367 | 0.16100 |  |
| DN_OutlierInclude_n_001_mdrmd | CHF vs AF | 21.0 | 0.09520 | 0.367 | 0.10400 |  |
| FC_LocalSimple_mean1_tauresrat | CHF vs AF | 21.0 | 0.09520 | 0.367 | 0.20400 |  |
| iqr | Normal vs CHF | 21.0 | 0.09520 | 0.367 | 0.15100 |  |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Normal vs CHF | 4.5 | 0.11500 | 0.428 | 0.07360 |  |
| DN_Mean | Normal vs AF | 5.0 | 0.15100 | 0.429 | 0.08890 |  |
| mean | Normal vs AF | 5.0 | 0.15100 | 0.429 | 0.08890 |  |
| median | Normal vs AF | 5.0 | 0.15100 | 0.429 | 0.08310 |  |
| SP_Summaries_welch_rect_centroid | Normal vs CHF | 5.5 | 0.16100 | 0.447 | 0.28300 |  |
| SB_BinaryStats_diff_longstretch0 | CHF vs AF | 19.0 | 0.20600 | 0.500 | 0.14300 |  |
| CO_f1ecac | Normal vs CHF | 19.0 | 0.22200 | 0.500 | 0.24000 |  |
| SP_Summaries_welch_rect_area_5_1 | Normal vs CHF | 6.0 | 0.22200 | 0.500 | 0.18400 |  |
| max | Normal vs CHF | 19.0 | 0.22200 | 0.500 | 0.28800 |  |
| DN_OutlierInclude_p_001_mdrmd | Normal vs AF | 7.0 | 0.31000 | 0.548 | 0.22000 |  |
| SB_BinaryStats_mean_longstretch1 | Normal vs AF | 18.0 | 0.31000 | 0.548 | 0.27600 |  |
| SB_MotifThree_quantile_hh | Normal vs AF | 7.0 | 0.31000 | 0.548 | 0.27700 |  |
| CO_HistogramAMI_even_2_5 | Normal vs AF | 17.0 | 0.42100 | 0.668 | 0.42600 |  |
| FC_LocalSimple_mean3_stderr | Normal vs CHF | 17.0 | 0.42100 | 0.668 | 0.32300 |  |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Normal vs CHF | 16.5 | 0.45200 | 0.708 | 0.35600 |  |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Normal vs CHF | 10.0 | 0.67300 | 0.898 | 0.67300 |  |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Normal vs CHF | 10.0 | 0.69000 | 0.898 | 0.47600 |  |
| SB_TransitionMatrix_3ac_sumdiagcov | Normal vs AF | 14.0 | 0.83000 | 0.937 | 0.91100 |  |

Most significant pairwise comparison per metric (Wilcoxon)

<details>

<summary>

Full pairwise results (click to expand)
</summary>

| Metric | Pair | t stat | t p | t p (BH) | W stat | W p | W p (BH) |
|:---|:---|---:|---:|---:|---:|---:|---:|
| mean_rmssd | Normal vs CHF | 2.88 | 0.034400 | 0.3380 | 25.0 | 0.00794 | 0.143 |
| mean_sdnn | Normal vs CHF | 5.53 | 0.002160 | 0.0567 | 25.0 | 0.00794 | 0.143 |
| mean_rmssd | Normal vs AF | -7.48 | 0.000793 | 0.0441 | 0.0 | 0.00794 | 0.143 |
| mean_sdnn | Normal vs AF | -5.67 | 0.002630 | 0.0567 | 0.0 | 0.00794 | 0.143 |
| mean_rmssd | CHF vs AF | -8.78 | 0.000821 | 0.0441 | 0.0 | 0.00794 | 0.143 |
| mean_sdnn | CHF vs AF | -7.85 | 0.001230 | 0.0441 | 0.0 | 0.00794 | 0.143 |
| DN_HistogramMode_5 | CHF vs AF | 3.06 | 0.017700 | 0.2520 | 24.0 | 0.01590 | 0.214 |
| apen | CHF vs AF | -2.53 | 0.045500 | 0.3820 | 1.0 | 0.01590 | 0.214 |
| cv | Normal vs CHF | 2.75 | 0.026700 | 0.3140 | 23.0 | 0.03170 | 0.300 |
| MD_hrv_classic_pnn40 | Normal vs AF | -3.07 | 0.015300 | 0.2520 | 2.0 | 0.03170 | 0.300 |
| MD_hrv_classic_pnn40 | CHF vs AF | -3.13 | 0.018700 | 0.2520 | 2.0 | 0.03170 | 0.300 |
| DN_HistogramMode_10 | Normal vs CHF | -2.36 | 0.047500 | 0.3820 | 3.0 | 0.05560 | 0.300 |
| DN_HistogramMode_5 | Normal vs CHF | -2.17 | 0.061400 | 0.3820 | 3.0 | 0.05560 | 0.300 |
| DN_Spread_Std | Normal vs CHF | 1.84 | 0.105000 | 0.3820 | 22.0 | 0.05560 | 0.300 |
| min | Normal vs CHF | -2.31 | 0.050300 | 0.3820 | 3.0 | 0.05560 | 0.300 |
| permen | Normal vs CHF | -2.33 | 0.059600 | 0.3820 | 3.0 | 0.05560 | 0.300 |
| sd | Normal vs CHF | 1.84 | 0.105000 | 0.3820 | 22.0 | 0.05560 | 0.300 |
| sampen | Normal vs AF | -2.00 | 0.092100 | 0.3820 | 3.0 | 0.05560 | 0.300 |
| DN_Spread_Std | CHF vs AF | -1.69 | 0.132000 | 0.4450 | 3.0 | 0.05560 | 0.300 |
| sd | CHF vs AF | -1.69 | 0.132000 | 0.4450 | 3.0 | 0.05560 | 0.300 |
| PD_PeriodicityWang_th0_01 | Normal vs CHF | -3.29 | 0.029100 | 0.3140 | 3.0 | 0.05930 | 0.305 |
| CO_FirstMin_ac | Normal vs CHF | -2.04 | 0.106000 | 0.3820 | 4.0 | 0.09520 | 0.367 |
| iqr | Normal vs CHF | 1.60 | 0.151000 | 0.4640 | 21.0 | 0.09520 | 0.367 |
| CO_trev_1_num | Normal vs AF | -1.60 | 0.161000 | 0.4820 | 4.0 | 0.09520 | 0.367 |
| DN_OutlierInclude_n_001_mdrmd | CHF vs AF | 1.84 | 0.104000 | 0.3820 | 21.0 | 0.09520 | 0.367 |
| FC_LocalSimple_mean1_tauresrat | CHF vs AF | 1.51 | 0.204000 | 0.4860 | 21.0 | 0.09520 | 0.367 |
| cv | CHF vs AF | -2.08 | 0.078400 | 0.3820 | 4.0 | 0.09520 | 0.367 |
| sampen | CHF vs AF | -2.06 | 0.087700 | 0.3820 | 4.0 | 0.09520 | 0.367 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Normal vs CHF | -2.26 | 0.073600 | 0.3820 | 4.5 | 0.11500 | 0.428 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | CHF vs AF | 1.35 | 0.215000 | 0.4860 | 20.0 | 0.13800 | 0.429 |
| PD_PeriodicityWang_th0_01 | Normal vs AF | -2.68 | 0.053700 | 0.3820 | 5.0 | 0.14200 | 0.429 |
| CO_trev_1_num | Normal vs CHF | -1.93 | 0.089900 | 0.3820 | 5.0 | 0.15100 | 0.429 |
| DN_Mean | Normal vs AF | -2.17 | 0.088900 | 0.3820 | 5.0 | 0.15100 | 0.429 |
| mean | Normal vs AF | -2.17 | 0.088900 | 0.3820 | 5.0 | 0.15100 | 0.429 |
| median | Normal vs AF | -2.22 | 0.083100 | 0.3820 | 5.0 | 0.15100 | 0.429 |
| min | Normal vs AF | -2.30 | 0.067400 | 0.3820 | 5.0 | 0.15100 | 0.429 |
| min | CHF vs AF | -1.04 | 0.344000 | 0.5650 | 5.0 | 0.15100 | 0.429 |
| permen | CHF vs AF | 1.64 | 0.146000 | 0.4640 | 20.0 | 0.15100 | 0.429 |
| SP_Summaries_welch_rect_centroid | Normal vs CHF | -1.18 | 0.283000 | 0.5100 | 5.5 | 0.16100 | 0.447 |
| CO_FirstMin_ac | CHF vs AF | 0.27 | 0.798000 | 0.8530 | 19.5 | 0.17200 | 0.464 |
| SB_BinaryStats_diff_longstretch0 | CHF vs AF | 1.75 | 0.143000 | 0.4640 | 19.0 | 0.20600 | 0.500 |
| CO_f1ecac | Normal vs CHF | 1.27 | 0.240000 | 0.5100 | 19.0 | 0.22200 | 0.500 |
| FC_LocalSimple_mean1_tauresrat | Normal vs CHF | -1.23 | 0.275000 | 0.5100 | 6.0 | 0.22200 | 0.500 |
| SP_Summaries_welch_rect_area_5_1 | Normal vs CHF | -1.49 | 0.184000 | 0.4860 | 6.0 | 0.22200 | 0.500 |
| max | Normal vs CHF | 1.16 | 0.288000 | 0.5100 | 19.0 | 0.22200 | 0.500 |
| cv | Normal vs AF | 1.46 | 0.197000 | 0.4860 | 19.0 | 0.22200 | 0.500 |
| permen | Normal vs AF | -1.55 | 0.184000 | 0.4860 | 6.0 | 0.22200 | 0.500 |
| iqr | CHF vs AF | -0.99 | 0.355000 | 0.5650 | 6.0 | 0.22200 | 0.500 |
| SP_Summaries_welch_rect_centroid | Normal vs AF | -1.04 | 0.354000 | 0.5650 | 7.0 | 0.26500 | 0.548 |
| SB_BinaryStats_diff_longstretch0 | Normal vs CHF | -1.38 | 0.212000 | 0.4860 | 7.0 | 0.29200 | 0.548 |
| apen | Normal vs CHF | 1.44 | 0.191000 | 0.4860 | 18.0 | 0.31000 | 0.548 |
| DN_OutlierInclude_n_001_mdrmd | Normal vs AF | 1.20 | 0.267000 | 0.5100 | 18.0 | 0.31000 | 0.548 |
| DN_OutlierInclude_p_001_mdrmd | Normal vs AF | -1.43 | 0.220000 | 0.4860 | 7.0 | 0.31000 | 0.548 |
| SB_BinaryStats_mean_longstretch1 | Normal vs AF | 1.17 | 0.276000 | 0.5100 | 18.0 | 0.31000 | 0.548 |
| SB_MotifThree_quantile_hh | Normal vs AF | -1.19 | 0.277000 | 0.5100 | 7.0 | 0.31000 | 0.548 |
| apen | Normal vs AF | -1.35 | 0.220000 | 0.4860 | 7.0 | 0.31000 | 0.548 |
| DN_HistogramMode_10 | CHF vs AF | 1.23 | 0.255000 | 0.5100 | 18.0 | 0.31000 | 0.548 |
| DN_Mean | CHF vs AF | -1.16 | 0.279000 | 0.5100 | 7.0 | 0.31000 | 0.548 |
| SP_Summaries_welch_rect_area_5_1 | CHF vs AF | 1.29 | 0.258000 | 0.5100 | 18.0 | 0.31000 | 0.548 |
| max | CHF vs AF | -1.49 | 0.181000 | 0.4860 | 7.0 | 0.31000 | 0.548 |
| mean | CHF vs AF | -1.16 | 0.279000 | 0.5100 | 7.0 | 0.31000 | 0.548 |
| DN_OutlierInclude_p_001_mdrmd | Normal vs CHF | -1.47 | 0.191000 | 0.4860 | 8.0 | 0.42100 | 0.668 |
| FC_LocalSimple_mean3_stderr | Normal vs CHF | 1.06 | 0.323000 | 0.5610 | 17.0 | 0.42100 | 0.668 |
| SB_BinaryStats_mean_longstretch1 | Normal vs CHF | 1.40 | 0.213000 | 0.4860 | 17.0 | 0.42100 | 0.668 |
| CO_HistogramAMI_even_2_5 | Normal vs AF | 0.84 | 0.426000 | 0.6220 | 17.0 | 0.42100 | 0.668 |
| CO_f1ecac | Normal vs AF | 1.37 | 0.208000 | 0.4860 | 17.0 | 0.42100 | 0.668 |
| DN_HistogramMode_10 | Normal vs AF | -1.14 | 0.288000 | 0.5100 | 8.0 | 0.42100 | 0.668 |
| iqr | Normal vs AF | 0.85 | 0.422000 | 0.6220 | 17.0 | 0.42100 | 0.668 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Normal vs CHF | 0.98 | 0.356000 | 0.5650 | 16.5 | 0.45200 | 0.708 |
| DN_OutlierInclude_n_001_mdrmd | Normal vs CHF | -0.80 | 0.446000 | 0.6420 | 9.0 | 0.54800 | 0.799 |
| median | Normal vs CHF | -0.99 | 0.372000 | 0.5660 | 9.0 | 0.54800 | 0.799 |
| DN_Spread_Std | Normal vs AF | 0.20 | 0.845000 | 0.8780 | 16.0 | 0.54800 | 0.799 |
| sd | Normal vs AF | 0.20 | 0.845000 | 0.8780 | 16.0 | 0.54800 | 0.799 |
| median | CHF vs AF | -0.95 | 0.370000 | 0.5660 | 9.0 | 0.54800 | 0.799 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | CHF vs AF | -0.44 | 0.673000 | 0.8060 | 10.0 | 0.67000 | 0.898 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Normal vs CHF | -0.44 | 0.673000 | 0.8060 | 10.0 | 0.67300 | 0.898 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | CHF vs AF | 1.10 | 0.327000 | 0.5610 | 15.0 | 0.67400 | 0.898 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Normal vs CHF | -0.75 | 0.476000 | 0.6510 | 10.0 | 0.69000 | 0.898 |
| DN_Mean | Normal vs CHF | -0.78 | 0.472000 | 0.6510 | 10.0 | 0.69000 | 0.898 |
| MD_hrv_classic_pnn40 | Normal vs CHF | -0.58 | 0.583000 | 0.7560 | 10.0 | 0.69000 | 0.898 |
| mean | Normal vs CHF | -0.78 | 0.472000 | 0.6510 | 10.0 | 0.69000 | 0.898 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Normal vs AF | -0.52 | 0.620000 | 0.7750 | 10.0 | 0.69000 | 0.898 |
| FC_LocalSimple_mean3_stderr | CHF vs AF | -1.05 | 0.337000 | 0.5650 | 10.0 | 0.69000 | 0.898 |
| SB_TransitionMatrix_3ac_sumdiagcov | Normal vs AF | 0.12 | 0.911000 | 0.9370 | 14.0 | 0.83000 | 0.937 |
| CO_FirstMin_ac | Normal vs AF | -0.78 | 0.476000 | 0.6510 | 14.0 | 0.83300 | 0.937 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Normal vs AF | -0.29 | 0.783000 | 0.8470 | 14.0 | 0.83300 | 0.937 |
| CO_HistogramAMI_even_2_5 | Normal vs CHF | 0.42 | 0.686000 | 0.8060 | 14.0 | 0.84100 | 0.937 |
| SB_MotifThree_quantile_hh | Normal vs CHF | -0.24 | 0.815000 | 0.8630 | 11.0 | 0.84100 | 0.937 |
| DN_HistogramMode_5 | Normal vs AF | 0.54 | 0.606000 | 0.7700 | 14.0 | 0.84100 | 0.937 |
| FC_LocalSimple_mean1_tauresrat | Normal vs AF | 0.60 | 0.577000 | 0.7560 | 11.0 | 0.84100 | 0.937 |
| FC_LocalSimple_mean3_stderr | Normal vs AF | -0.32 | 0.760000 | 0.8370 | 11.0 | 0.84100 | 0.937 |
| max | Normal vs AF | -0.88 | 0.420000 | 0.6220 | 11.0 | 0.84100 | 0.937 |
| CO_trev_1_num | CHF vs AF | -0.43 | 0.683000 | 0.8060 | 11.0 | 0.84100 | 0.937 |
| DN_OutlierInclude_p_001_mdrmd | CHF vs AF | -0.70 | 0.514000 | 0.6930 | 11.0 | 0.84100 | 0.937 |
| PD_PeriodicityWang_th0_01 | CHF vs AF | 0.36 | 0.728000 | 0.8340 | 14.0 | 0.84100 | 0.937 |
| SB_BinaryStats_mean_longstretch1 | CHF vs AF | 0.08 | 0.938000 | 0.9550 | 14.0 | 0.84100 | 0.937 |
| SB_MotifThree_quantile_hh | CHF vs AF | -0.98 | 0.361000 | 0.5650 | 11.0 | 0.84100 | 0.937 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Normal vs AF | 0.51 | 0.624000 | 0.7750 | 13.5 | 0.91300 | 0.999 |
| SP_Summaries_welch_rect_centroid | CHF vs AF | -0.64 | 0.552000 | 0.7360 | 13.5 | 0.91600 | 0.999 |
| SB_TransitionMatrix_3ac_sumdiagcov | Normal vs CHF | 0.33 | 0.749000 | 0.8340 | 13.0 | 1.00000 | 1.000 |
| sampen | Normal vs CHF | 0.03 | 0.976000 | 0.9760 | 13.0 | 1.00000 | 1.000 |
| SB_BinaryStats_diff_longstretch0 | Normal vs AF | 0.34 | 0.743000 | 0.8340 | 13.0 | 1.00000 | 1.000 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Normal vs AF | 0.58 | 0.588000 | 0.7560 | 12.0 | 1.00000 | 1.000 |
| SP_Summaries_welch_rect_area_5_1 | Normal vs AF | 0.41 | 0.694000 | 0.8060 | 13.0 | 1.00000 | 1.000 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | CHF vs AF | 0.33 | 0.748000 | 0.8340 | 13.0 | 1.00000 | 1.000 |
| CO_HistogramAMI_even_2_5 | CHF vs AF | 0.42 | 0.682000 | 0.8060 | 13.0 | 1.00000 | 1.000 |
| CO_f1ecac | CHF vs AF | 0.03 | 0.973000 | 0.9760 | 13.0 | 1.00000 | 1.000 |
| SB_TransitionMatrix_3ac_sumdiagcov | CHF vs AF | -0.29 | 0.785000 | 0.8470 | 12.0 | 1.00000 | 1.000 |

</details>

</div>

## 6 PCA Analysis

### 6.1 All Metrics (36)

<div class="panel-tabset">

#### 5-min

![](physionet15_analysis_1_files/figure-commonmark/pca-all-5min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-all-5min-13-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-all-5min-34-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-all-5min-load-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-all-5min-var-1.png)

#### 1-min

![](physionet15_analysis_1_files/figure-commonmark/pca-all-1min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-all-1min-13-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-all-1min-34-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-all-1min-load-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-all-1min-var-1.png)

</div>

### 6.2 avg_hr Metrics Only (34)

<div class="panel-tabset">

#### 5-min

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-3d-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-dist-1.png)

| Variable                                    | Coefficient |
|:--------------------------------------------|------------:|
| DN_OutlierInclude_p_001_mdrmd               |     -0.5499 |
| CO_f1ecac                                   |      0.4836 |
| min                                         |     -0.4483 |
| DN_HistogramMode_10                         |     -0.4478 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi     |     -0.4071 |
| permen                                      |     -0.3994 |
| SB_BinaryStats_mean_longstretch1            |      0.3904 |
| DN_OutlierInclude_n_001_mdrmd               |      0.3858 |
| cv                                          |      0.3510 |
| DN_Mean                                     |     -0.3048 |
| mean                                        |     -0.3048 |
| PD_PeriodicityWang_th0_01                   |     -0.3013 |
| median                                      |     -0.2968 |
| iqr                                         |      0.2898 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1      |     -0.2860 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 |      0.2847 |
| MD_hrv_classic_pnn40                        |     -0.2754 |
| SB_MotifThree_quantile_hh                   |     -0.2679 |
| CO_HistogramAMI_even_2_5                    |      0.2647 |
| CO_FirstMin_ac                              |     -0.2443 |
| DN_HistogramMode_5                          |     -0.2408 |
| apen                                        |     -0.2345 |
| SP_Summaries_welch_rect_centroid            |     -0.2119 |
| FC_LocalSimple_mean1_tauresrat              |     -0.2042 |
| SB_TransitionMatrix_3ac_sumdiagcov          |      0.1921 |
| max                                         |     -0.1919 |
| sampen                                      |     -0.1856 |
| FC_LocalSimple_mean3_stderr                 |     -0.1670 |
| DN_Spread_Std                               |      0.1577 |
| sd                                          |      0.1577 |
| CO_Embed2_Dist_tau_d_expfit_meandiff        |      0.1346 |
| SP_Summaries_welch_rect_area_5_1            |      0.1211 |
| CO_trev_1_num                               |     -0.0730 |
| SB_BinaryStats_diff_longstretch0            |      0.0175 |

Composite Index (PC1 - PC2 - PC3): variable coefficients sorted by
\|coefficient\| (5-min)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-pc1-jitter-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-pc2-jitter-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-pc3-jitter-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-dist-line-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-pc1-line-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-pc2-line-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-pc3-line-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-13-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-34-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-42-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-45-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-46-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-47-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-load-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-5min-var-1.png)

<details>

<summary>

<b>PC1 — Sorted Loadings</b>
</summary>

<table style="border-collapse:collapse; font-size:12px;">

<tr>

<th style="padding:4px 8px;">

Rank
</th>

<th style="padding:4px 8px;">

Variable
</th>

<th style="padding:4px 8px;">

Loading
</th>

</tr>

<tr>

<td style="padding:2px 8px;">

1
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(214,216,225); color:black; text-align:right;">

+0.27
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(213,219,227); color:black; text-align:right;">

+0.25
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(212,221,228); color:black; text-align:right;">

+0.24
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(212,221,228); color:black; text-align:right;">

+0.24
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(212,221,228); color:black; text-align:right;">

+0.24
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(218,229,251); color:black; text-align:right;">

-0.24
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(218,229,251); color:black; text-align:right;">

-0.24
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(212,221,228); color:black; text-align:right;">

+0.24
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(219,230,251); color:black; text-align:right;">

-0.23
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(219,230,251); color:black; text-align:right;">

-0.23
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(221,231,251); color:black; text-align:right;">

-0.22
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(211,225,231); color:black; text-align:right;">

+0.21
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(224,234,251); color:black; text-align:right;">

-0.20
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(224,234,251); color:black; text-align:right;">

-0.20
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(209,229,235); color:black; text-align:right;">

+0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(209,229,235); color:black; text-align:right;">

+0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(229,237,252); color:black; text-align:right;">

-0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(230,238,252); color:black; text-align:right;">

-0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(208,232,237); color:black; text-align:right;">

+0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(207,235,239); color:black; text-align:right;">

+0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(239,244,253); color:black; text-align:right;">

-0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(241,245,253); color:black; text-align:right;">

-0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(241,245,253); color:black; text-align:right;">

-0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(204,242,245); color:black; text-align:right;">

+0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(244,248,254); color:black; text-align:right;">

-0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(202,246,248); color:black; text-align:right;">

+0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

-0.00
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

+0.00
</td>

</tr>

</table>

</details>

<details>

<summary>

<b>PC2 — Sorted Loadings</b>
</summary>

<table style="border-collapse:collapse; font-size:12px;">

<tr>

<th style="padding:4px 8px;">

Rank
</th>

<th style="padding:4px 8px;">

Variable
</th>

<th style="padding:4px 8px;">

Loading
</th>

</tr>

<tr>

<td style="padding:2px 8px;">

1
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(219,204,215); color:black; text-align:right;">

+0.36
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(219,204,215); color:black; text-align:right;">

+0.36
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(219,204,215); color:black; text-align:right;">

+0.36
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(219,205,216); color:black; text-align:right;">

+0.35
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(216,211,220); color:black; text-align:right;">

+0.31
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(211,224,230); color:black; text-align:right;">

+0.22
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(224,234,251); color:black; text-align:right;">

-0.20
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(210,228,234); color:black; text-align:right;">

+0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(210,228,234); color:black; text-align:right;">

+0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(225,235,252); color:black; text-align:right;">

-0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(225,235,252); color:black; text-align:right;">

-0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(208,231,236); color:black; text-align:right;">

+0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(238,243,253); color:black; text-align:right;">

-0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(239,244,253); color:black; text-align:right;">

-0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(241,245,253); color:black; text-align:right;">

-0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(246,249,254); color:black; text-align:right;">

-0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(201,249,251); color:black; text-align:right;">

+0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(249,251,254); color:black; text-align:right;">

-0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(201,249,251); color:black; text-align:right;">

+0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(200,252,253); color:black; text-align:right;">

+0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

+0.00
</td>

</tr>

</table>

</details>

<details>

<summary>

<b>PC3 — Sorted Loadings</b>
</summary>

<table style="border-collapse:collapse; font-size:12px;">

<tr>

<th style="padding:4px 8px;">

Rank
</th>

<th style="padding:4px 8px;">

Variable
</th>

<th style="padding:4px 8px;">

Loading
</th>

</tr>

<tr>

<td style="padding:2px 8px;">

1
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(220,202,213); color:black; text-align:right;">

+0.37
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(219,205,216); color:black; text-align:right;">

+0.35
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(219,205,216); color:black; text-align:right;">

+0.35
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(204,220,249); color:black; text-align:right;">

-0.33
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(215,214,222); color:black; text-align:right;">

+0.29
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(213,219,227); color:black; text-align:right;">

+0.25
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(213,219,227); color:black; text-align:right;">

+0.25
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(219,230,251); color:black; text-align:right;">

-0.23
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(224,234,251); color:black; text-align:right;">

-0.20
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(225,235,252); color:black; text-align:right;">

-0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(210,228,234); color:black; text-align:right;">

+0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(229,237,252); color:black; text-align:right;">

-0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(206,236,240); color:black; text-align:right;">

+0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(236,242,253); color:black; text-align:right;">

-0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(239,244,253); color:black; text-align:right;">

-0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(244,248,254); color:black; text-align:right;">

-0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(244,248,254); color:black; text-align:right;">

-0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(202,246,248); color:black; text-align:right;">

+0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(202,246,248); color:black; text-align:right;">

+0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(202,246,248); color:black; text-align:right;">

+0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(202,246,248); color:black; text-align:right;">

+0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(201,249,251); color:black; text-align:right;">

+0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(201,249,251); color:black; text-align:right;">

+0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

+0.00
</td>

</tr>

</table>

</details>

<details>

<summary>

<b>PC4 — Sorted Loadings</b>
</summary>

<table style="border-collapse:collapse; font-size:12px;">

<tr>

<th style="padding:4px 8px;">

Rank
</th>

<th style="padding:4px 8px;">

Variable
</th>

<th style="padding:4px 8px;">

Loading
</th>

</tr>

<tr>

<td style="padding:2px 8px;">

1
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(191,211,248); color:black; text-align:right;">

-0.41
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(217,209,219); color:black; text-align:right;">

+0.32
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(213,219,227); color:black; text-align:right;">

+0.25
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(218,229,251); color:black; text-align:right;">

-0.24
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(219,230,251); color:black; text-align:right;">

-0.23
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(212,222,229); color:black; text-align:right;">

+0.23
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(222,233,251); color:black; text-align:right;">

-0.21
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(222,233,251); color:black; text-align:right;">

-0.21
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(210,226,233); color:black; text-align:right;">

+0.20
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(224,234,251); color:black; text-align:right;">

-0.20
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(210,228,234); color:black; text-align:right;">

+0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(208,231,236); color:black; text-align:right;">

+0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(208,232,237); color:black; text-align:right;">

+0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(230,238,252); color:black; text-align:right;">

-0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(233,240,253); color:black; text-align:right;">

-0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(236,242,253); color:black; text-align:right;">

-0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(236,242,253); color:black; text-align:right;">

-0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(206,238,242); color:black; text-align:right;">

+0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(206,238,242); color:black; text-align:right;">

+0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(239,244,253); color:black; text-align:right;">

-0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(241,245,253); color:black; text-align:right;">

-0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(241,245,253); color:black; text-align:right;">

-0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(244,248,254); color:black; text-align:right;">

-0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(202,246,248); color:black; text-align:right;">

+0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

</table>

</details>

<details>

<summary>

<b>PC5 — Sorted Loadings</b>
</summary>

<table style="border-collapse:collapse; font-size:12px;">

<tr>

<th style="padding:4px 8px;">

Rank
</th>

<th style="padding:4px 8px;">

Variable
</th>

<th style="padding:4px 8px;">

Loading
</th>

</tr>

<tr>

<td style="padding:2px 8px;">

1
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(225,188,202); color:black; text-align:right;">

+0.47
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(222,195,208); color:black; text-align:right;">

+0.42
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(221,199,211); color:black; text-align:right;">

+0.39
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(216,212,221); color:black; text-align:right;">

+0.30
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(215,214,222); color:black; text-align:right;">

+0.29
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(218,229,251); color:black; text-align:right;">

-0.24
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(212,222,229); color:black; text-align:right;">

+0.23
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(230,238,252); color:black; text-align:right;">

-0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(206,236,240); color:black; text-align:right;">

+0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(236,242,253); color:black; text-align:right;">

-0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(236,242,253); color:black; text-align:right;">

-0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(241,245,253); color:black; text-align:right;">

-0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(241,245,253); color:black; text-align:right;">

-0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(241,245,253); color:black; text-align:right;">

-0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(202,246,248); color:black; text-align:right;">

+0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(202,246,248); color:black; text-align:right;">

+0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(246,249,254); color:black; text-align:right;">

-0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(246,249,254); color:black; text-align:right;">

-0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(249,251,254); color:black; text-align:right;">

-0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(201,249,251); color:black; text-align:right;">

+0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(201,249,251); color:black; text-align:right;">

+0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(200,252,253); color:black; text-align:right;">

+0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

+0.00
</td>

</tr>

</table>

</details>

<details>

<summary>

<b>PC6 — Sorted Loadings</b>
</summary>

<table style="border-collapse:collapse; font-size:12px;">

<tr>

<th style="padding:4px 8px;">

Rank
</th>

<th style="padding:4px 8px;">

Variable
</th>

<th style="padding:4px 8px;">

Loading
</th>

</tr>

<tr>

<td style="padding:2px 8px;">

1
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(188,209,247); color:black; text-align:right;">

-0.43
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(222,195,208); color:black; text-align:right;">

+0.42
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(197,215,248); color:black; text-align:right;">

-0.37
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(218,206,217); color:black; text-align:right;">

+0.34
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(213,219,227); color:black; text-align:right;">

+0.25
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(212,221,228); color:black; text-align:right;">

+0.24
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(212,222,229); color:black; text-align:right;">

+0.23
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(227,236,252); color:black; text-align:right;">

-0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(208,231,236); color:black; text-align:right;">

+0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(235,241,253); color:black; text-align:right;">

-0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(236,242,253); color:black; text-align:right;">

-0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(239,244,253); color:black; text-align:right;">

-0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(204,242,245); color:black; text-align:right;">

+0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(204,242,245); color:black; text-align:right;">

+0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(244,248,254); color:black; text-align:right;">

-0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(202,246,248); color:black; text-align:right;">

+0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(249,251,254); color:black; text-align:right;">

-0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

</table>

</details>

<details>

<summary>

<b>PC7 — Sorted Loadings</b>
</summary>

<table style="border-collapse:collapse; font-size:12px;">

<tr>

<th style="padding:4px 8px;">

Rank
</th>

<th style="padding:4px 8px;">

Variable
</th>

<th style="padding:4px 8px;">

Loading
</th>

</tr>

<tr>

<td style="padding:2px 8px;">

1
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(229,179,196); color:black; text-align:right;">

+0.53
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(222,195,208); color:black; text-align:right;">

+0.42
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(216,211,220); color:black; text-align:right;">

+0.31
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(215,214,222); color:black; text-align:right;">

+0.29
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(214,216,225); color:black; text-align:right;">

+0.27
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(212,222,229); color:black; text-align:right;">

+0.23
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(225,235,252); color:black; text-align:right;">

-0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(229,237,252); color:black; text-align:right;">

-0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(232,239,252); color:black; text-align:right;">

-0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(233,240,253); color:black; text-align:right;">

-0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(233,240,253); color:black; text-align:right;">

-0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(206,236,240); color:black; text-align:right;">

+0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(236,242,253); color:black; text-align:right;">

-0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(236,242,253); color:black; text-align:right;">

-0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(202,246,248); color:black; text-align:right;">

+0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(246,249,254); color:black; text-align:right;">

-0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(246,249,254); color:black; text-align:right;">

-0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(201,249,251); color:black; text-align:right;">

+0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(249,251,254); color:black; text-align:right;">

-0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(200,252,253); color:black; text-align:right;">

+0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(200,252,253); color:black; text-align:right;">

+0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(200,252,253); color:black; text-align:right;">

+0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(200,252,253); color:black; text-align:right;">

+0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

-0.00
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

+0.00
</td>

</tr>

</table>

</details>

<details>

<summary>

<b>PC8 — Sorted Loadings</b>
</summary>

<table style="border-collapse:collapse; font-size:12px;">

<tr>

<th style="padding:4px 8px;">

Rank
</th>

<th style="padding:4px 8px;">

Variable
</th>

<th style="padding:4px 8px;">

Loading
</th>

</tr>

<tr>

<td style="padding:2px 8px;">

1
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(223,194,207); color:black; text-align:right;">

+0.43
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(201,218,249); color:black; text-align:right;">

-0.35
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(202,219,249); color:black; text-align:right;">

-0.34
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(216,211,220); color:black; text-align:right;">

+0.31
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(210,224,250); color:black; text-align:right;">

-0.29
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(214,216,225); color:black; text-align:right;">

+0.27
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(218,229,251); color:black; text-align:right;">

-0.24
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(225,235,252); color:black; text-align:right;">

-0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(227,236,252); color:black; text-align:right;">

-0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(233,240,253); color:black; text-align:right;">

-0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(235,241,253); color:black; text-align:right;">

-0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(236,242,253); color:black; text-align:right;">

-0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(206,238,242); color:black; text-align:right;">

+0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(238,243,253); color:black; text-align:right;">

-0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(238,243,253); color:black; text-align:right;">

-0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(238,243,253); color:black; text-align:right;">

-0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(239,244,253); color:black; text-align:right;">

-0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(241,245,253); color:black; text-align:right;">

-0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(241,245,253); color:black; text-align:right;">

-0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(241,245,253); color:black; text-align:right;">

-0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(204,242,245); color:black; text-align:right;">

+0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(246,249,254); color:black; text-align:right;">

-0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(201,249,251); color:black; text-align:right;">

+0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(249,251,254); color:black; text-align:right;">

-0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(200,252,253); color:black; text-align:right;">

+0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

</table>

</details>

#### 1-min

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-3d-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-dist-1.png)

| Variable                                    | Coefficient |
|:--------------------------------------------|------------:|
| SP_Summaries_welch_rect_area_5_1            |      0.6113 |
| FC_LocalSimple_mean3_stderr                 |     -0.5979 |
| apen                                        |     -0.5754 |
| sampen                                      |     -0.5418 |
| SB_MotifThree_quantile_hh                   |     -0.5391 |
| SP_Summaries_welch_rect_centroid            |     -0.4814 |
| MD_hrv_classic_pnn40                        |     -0.4124 |
| CO_HistogramAMI_even_2_5                    |      0.4024 |
| CO_Embed2_Dist_tau_d_expfit_meandiff        |      0.3961 |
| CO_trev_1_num                               |     -0.3331 |
| SB_BinaryStats_mean_longstretch1            |      0.2935 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi     |      0.2891 |
| CO_f1ecac                                   |      0.2599 |
| PD_PeriodicityWang_th0_01                   |      0.2518 |
| CO_FirstMin_ac                              |      0.2432 |
| max                                         |     -0.1372 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 |      0.1301 |
| DN_HistogramMode_5                          |      0.1293 |
| DN_Mean                                     |     -0.1233 |
| mean                                        |     -0.1233 |
| SB_BinaryStats_diff_longstretch0            |      0.1215 |
| min                                         |     -0.1165 |
| SB_TransitionMatrix_3ac_sumdiagcov          |      0.1012 |
| median                                      |     -0.0989 |
| FC_LocalSimple_mean1_tauresrat              |      0.0937 |
| DN_OutlierInclude_p_001_mdrmd               |      0.0854 |
| DN_Spread_Std                               |     -0.0613 |
| sd                                          |     -0.0613 |
| iqr                                         |      0.0520 |
| DN_HistogramMode_10                         |      0.0477 |
| cv                                          |     -0.0353 |
| DN_OutlierInclude_n_001_mdrmd               |      0.0242 |
| permen                                      |     -0.0212 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1      |     -0.0150 |

Composite Index (PC1 - PC2 - PC3): variable coefficients sorted by
\|coefficient\| (1-min)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-pc1-jitter-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-pc2-jitter-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-pc3-jitter-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-dist-line-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-pc1-line-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-pc2-line-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-pc3-line-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-13-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-34-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-42-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-45-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-46-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-47-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-load-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-avghr-1min-var-1.png)

<details>

<summary>

<b>PC1 — Sorted Loadings</b>
</summary>

<table style="border-collapse:collapse; font-size:12px;">

<tr>

<th style="padding:4px 8px;">

Rank
</th>

<th style="padding:4px 8px;">

Variable
</th>

<th style="padding:4px 8px;">

Loading
</th>

</tr>

<tr>

<td style="padding:2px 8px;">

1
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(215,215,224); color:black; text-align:right;">

+0.28
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(214,216,225); color:black; text-align:right;">

+0.27
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(214,216,225); color:black; text-align:right;">

+0.27
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(216,228,251); color:black; text-align:right;">

-0.25
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(212,221,228); color:black; text-align:right;">

+0.24
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(212,221,228); color:black; text-align:right;">

+0.24
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(212,222,229); color:black; text-align:right;">

+0.23
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(219,230,251); color:black; text-align:right;">

-0.23
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(211,224,230); color:black; text-align:right;">

+0.22
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(221,231,251); color:black; text-align:right;">

-0.22
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(222,233,251); color:black; text-align:right;">

-0.21
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(222,233,251); color:black; text-align:right;">

-0.21
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(224,234,251); color:black; text-align:right;">

-0.20
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(225,235,252); color:black; text-align:right;">

-0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(209,229,235); color:black; text-align:right;">

+0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(227,236,252); color:black; text-align:right;">

-0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(229,237,252); color:black; text-align:right;">

-0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(208,232,237); color:black; text-align:right;">

+0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(230,238,252); color:black; text-align:right;">

-0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(238,243,253); color:black; text-align:right;">

-0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(239,244,253); color:black; text-align:right;">

-0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(244,248,254); color:black; text-align:right;">

-0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(244,248,254); color:black; text-align:right;">

-0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(202,246,248); color:black; text-align:right;">

+0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(201,249,251); color:black; text-align:right;">

+0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

+0.00
</td>

</tr>

</table>

</details>

<details>

<summary>

<b>PC2 — Sorted Loadings</b>
</summary>

<table style="border-collapse:collapse; font-size:12px;">

<tr>

<th style="padding:4px 8px;">

Rank
</th>

<th style="padding:4px 8px;">

Variable
</th>

<th style="padding:4px 8px;">

Loading
</th>

</tr>

<tr>

<td style="padding:2px 8px;">

1
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(218,206,217); color:black; text-align:right;">

+0.34
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(218,206,217); color:black; text-align:right;">

+0.34
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(217,208,218); color:black; text-align:right;">

+0.33
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(216,211,220); color:black; text-align:right;">

+0.31
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(216,211,220); color:black; text-align:right;">

+0.31
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(210,228,234); color:black; text-align:right;">

+0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(210,228,234); color:black; text-align:right;">

+0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(227,236,252); color:black; text-align:right;">

-0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(209,229,235); color:black; text-align:right;">

+0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(209,229,235); color:black; text-align:right;">

+0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(229,237,252); color:black; text-align:right;">

-0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(208,231,236); color:black; text-align:right;">

+0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(208,231,236); color:black; text-align:right;">

+0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(208,231,236); color:black; text-align:right;">

+0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(208,232,237); color:black; text-align:right;">

+0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(208,232,237); color:black; text-align:right;">

+0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(230,238,252); color:black; text-align:right;">

-0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(207,235,239); color:black; text-align:right;">

+0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(233,240,253); color:black; text-align:right;">

-0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(239,244,253); color:black; text-align:right;">

-0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(239,244,253); color:black; text-align:right;">

-0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(204,242,245); color:black; text-align:right;">

+0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(244,248,254); color:black; text-align:right;">

-0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(246,249,254); color:black; text-align:right;">

-0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

-0.00
</td>

</tr>

</table>

</details>

<details>

<summary>

<b>PC3 — Sorted Loadings</b>
</summary>

<table style="border-collapse:collapse; font-size:12px;">

<tr>

<th style="padding:4px 8px;">

Rank
</th>

<th style="padding:4px 8px;">

Variable
</th>

<th style="padding:4px 8px;">

Loading
</th>

</tr>

<tr>

<td style="padding:2px 8px;">

1
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(202,219,249); color:black; text-align:right;">

-0.34
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(207,222,249); color:black; text-align:right;">

-0.31
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(210,224,250); color:black; text-align:right;">

-0.29
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(215,227,250); color:black; text-align:right;">

-0.26
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(216,228,251); color:black; text-align:right;">

-0.25
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(212,221,228); color:black; text-align:right;">

+0.24
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(212,222,229); color:black; text-align:right;">

+0.23
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(221,231,251); color:black; text-align:right;">

-0.22
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(222,233,251); color:black; text-align:right;">

-0.21
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(224,234,251); color:black; text-align:right;">

-0.20
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(210,226,233); color:black; text-align:right;">

+0.20
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(225,235,252); color:black; text-align:right;">

-0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(230,238,252); color:black; text-align:right;">

-0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(208,232,237); color:black; text-align:right;">

+0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(232,239,252); color:black; text-align:right;">

-0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(235,241,253); color:black; text-align:right;">

-0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(206,238,242); color:black; text-align:right;">

+0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(236,242,253); color:black; text-align:right;">

-0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(236,242,253); color:black; text-align:right;">

-0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(206,238,242); color:black; text-align:right;">

+0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(238,243,253); color:black; text-align:right;">

-0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(204,242,245); color:black; text-align:right;">

+0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(204,242,245); color:black; text-align:right;">

+0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(246,249,254); color:black; text-align:right;">

-0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(201,249,251); color:black; text-align:right;">

+0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

</table>

</details>

<details>

<summary>

<b>PC4 — Sorted Loadings</b>
</summary>

<table style="border-collapse:collapse; font-size:12px;">

<tr>

<th style="padding:4px 8px;">

Rank
</th>

<th style="padding:4px 8px;">

Variable
</th>

<th style="padding:4px 8px;">

Loading
</th>

</tr>

<tr>

<td style="padding:2px 8px;">

1
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(194,213,248); color:black; text-align:right;">

-0.39
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(217,208,218); color:black; text-align:right;">

+0.33
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(217,208,218); color:black; text-align:right;">

+0.33
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(210,224,250); color:black; text-align:right;">

-0.29
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(213,226,250); color:black; text-align:right;">

-0.27
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(212,221,228); color:black; text-align:right;">

+0.24
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(212,222,229); color:black; text-align:right;">

+0.23
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(221,231,251); color:black; text-align:right;">

-0.22
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(225,235,252); color:black; text-align:right;">

-0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(225,235,252); color:black; text-align:right;">

-0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(209,229,235); color:black; text-align:right;">

+0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(208,232,237); color:black; text-align:right;">

+0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(230,238,252); color:black; text-align:right;">

-0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(232,239,252); color:black; text-align:right;">

-0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(232,239,252); color:black; text-align:right;">

-0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(235,241,253); color:black; text-align:right;">

-0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(206,238,242); color:black; text-align:right;">

+0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(206,238,242); color:black; text-align:right;">

+0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(249,251,254); color:black; text-align:right;">

-0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(249,251,254); color:black; text-align:right;">

-0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

-0.00
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

+0.00
</td>

</tr>

</table>

</details>

<details>

<summary>

<b>PC5 — Sorted Loadings</b>
</summary>

<table style="border-collapse:collapse; font-size:12px;">

<tr>

<th style="padding:4px 8px;">

Rank
</th>

<th style="padding:4px 8px;">

Variable
</th>

<th style="padding:4px 8px;">

Loading
</th>

</tr>

<tr>

<td style="padding:2px 8px;">

1
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(222,196,209); color:black; text-align:right;">

+0.41
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(221,199,211); color:black; text-align:right;">

+0.39
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(217,208,218); color:black; text-align:right;">

+0.33
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(217,209,219); color:black; text-align:right;">

+0.32
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(216,228,251); color:black; text-align:right;">

-0.25
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(219,230,251); color:black; text-align:right;">

-0.23
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(211,224,230); color:black; text-align:right;">

+0.22
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(209,229,235); color:black; text-align:right;">

+0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(209,229,235); color:black; text-align:right;">

+0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(227,236,252); color:black; text-align:right;">

-0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(229,237,252); color:black; text-align:right;">

-0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(208,232,237); color:black; text-align:right;">

+0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(207,235,239); color:black; text-align:right;">

+0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(207,235,239); color:black; text-align:right;">

+0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(236,242,253); color:black; text-align:right;">

-0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(206,238,242); color:black; text-align:right;">

+0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(246,249,254); color:black; text-align:right;">

-0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(249,251,254); color:black; text-align:right;">

-0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(249,251,254); color:black; text-align:right;">

-0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(200,252,253); color:black; text-align:right;">

+0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

+0.00
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

-0.00
</td>

</tr>

</table>

</details>

<details>

<summary>

<b>PC6 — Sorted Loadings</b>
</summary>

<table style="border-collapse:collapse; font-size:12px;">

<tr>

<th style="padding:4px 8px;">

Rank
</th>

<th style="padding:4px 8px;">

Variable
</th>

<th style="padding:4px 8px;">

Loading
</th>

</tr>

<tr>

<td style="padding:2px 8px;">

1
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(173,198,246); color:black; text-align:right;">

-0.53
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(194,213,248); color:black; text-align:right;">

-0.39
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(220,201,212); color:black; text-align:right;">

+0.38
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(213,226,250); color:black; text-align:right;">

-0.27
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(213,226,250); color:black; text-align:right;">

-0.27
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(215,227,250); color:black; text-align:right;">

-0.26
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(216,228,251); color:black; text-align:right;">

-0.25
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(208,231,236); color:black; text-align:right;">

+0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(235,241,253); color:black; text-align:right;">

-0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(235,241,253); color:black; text-align:right;">

-0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(239,244,253); color:black; text-align:right;">

-0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(239,244,253); color:black; text-align:right;">

-0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(239,244,253); color:black; text-align:right;">

-0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(239,244,253); color:black; text-align:right;">

-0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(241,245,253); color:black; text-align:right;">

-0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(241,245,253); color:black; text-align:right;">

-0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(244,248,254); color:black; text-align:right;">

-0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(244,248,254); color:black; text-align:right;">

-0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(249,251,254); color:black; text-align:right;">

-0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(249,251,254); color:black; text-align:right;">

-0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(249,251,254); color:black; text-align:right;">

-0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

</table>

</details>

<details>

<summary>

<b>PC7 — Sorted Loadings</b>
</summary>

<table style="border-collapse:collapse; font-size:12px;">

<tr>

<th style="padding:4px 8px;">

Rank
</th>

<th style="padding:4px 8px;">

Variable
</th>

<th style="padding:4px 8px;">

Loading
</th>

</tr>

<tr>

<td style="padding:2px 8px;">

1
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(191,211,248); color:black; text-align:right;">

-0.41
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(218,206,217); color:black; text-align:right;">

+0.34
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(205,221,249); color:black; text-align:right;">

-0.32
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(217,209,219); color:black; text-align:right;">

+0.32
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(213,226,250); color:black; text-align:right;">

-0.27
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(215,227,250); color:black; text-align:right;">

-0.26
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(212,222,229); color:black; text-align:right;">

+0.23
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(221,231,251); color:black; text-align:right;">

-0.22
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(210,228,234); color:black; text-align:right;">

+0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(227,236,252); color:black; text-align:right;">

-0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(229,237,252); color:black; text-align:right;">

-0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(208,231,236); color:black; text-align:right;">

+0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(232,239,252); color:black; text-align:right;">

-0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(206,236,240); color:black; text-align:right;">

+0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(206,238,242); color:black; text-align:right;">

+0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(239,244,253); color:black; text-align:right;">

-0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(204,242,245); color:black; text-align:right;">

+0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(241,245,253); color:black; text-align:right;">

-0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(246,249,254); color:black; text-align:right;">

-0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(246,249,254); color:black; text-align:right;">

-0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(202,246,248); color:black; text-align:right;">

+0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(246,249,254); color:black; text-align:right;">

-0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(202,246,248); color:black; text-align:right;">

+0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(249,251,254); color:black; text-align:right;">

-0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

+0.00
</td>

</tr>

</table>

</details>

<details>

<summary>

<b>PC8 — Sorted Loadings</b>
</summary>

<table style="border-collapse:collapse; font-size:12px;">

<tr>

<th style="padding:4px 8px;">

Rank
</th>

<th style="padding:4px 8px;">

Variable
</th>

<th style="padding:4px 8px;">

Loading
</th>

</tr>

<tr>

<td style="padding:2px 8px;">

1
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(228,181,197); color:black; text-align:right;">

+0.52
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(222,196,209); color:black; text-align:right;">

+0.41
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(208,223,250); color:black; text-align:right;">

-0.30
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(218,229,251); color:black; text-align:right;">

-0.24
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(210,226,233); color:black; text-align:right;">

+0.20
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(209,229,235); color:black; text-align:right;">

+0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(208,231,236); color:black; text-align:right;">

+0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(229,237,252); color:black; text-align:right;">

-0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(230,238,252); color:black; text-align:right;">

-0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(232,239,252); color:black; text-align:right;">

-0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(235,241,253); color:black; text-align:right;">

-0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(235,241,253); color:black; text-align:right;">

-0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(235,241,253); color:black; text-align:right;">

-0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(206,236,240); color:black; text-align:right;">

+0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(236,242,253); color:black; text-align:right;">

-0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(238,243,253); color:black; text-align:right;">

-0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(239,244,253); color:black; text-align:right;">

-0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(204,242,245); color:black; text-align:right;">

+0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(246,249,254); color:black; text-align:right;">

-0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(201,249,251); color:black; text-align:right;">

+0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(201,249,251); color:black; text-align:right;">

+0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

</table>

</details>

</div>

### 6.2.1 HRV vs avg_hr PCA Scores

Do traditional HRV measures (RMSSD, SDNN) agree with the principal
components derived from the 34-metric avg_hr PCA? We assess this via
correlation heatmap, scatter plots with identity line (z-scored),
Bland-Altman agreement plots, and ICC (two-way, agreement).

<div class="panel-tabset">

#### 5-min

![](physionet15_analysis_1_files/figure-commonmark/hrv-pca-corr-5min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/hrv-pca-scatter-5min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/hrv-pca-ba-5min-1.png)

| HRV Metric | PC  |    ICC | 95% CI Lower | 95% CI Upper |
|:-----------|:----|-------:|-------------:|-------------:|
| mean_rmssd | PC1 | -0.058 |       -0.598 |        0.473 |
| mean_rmssd | PC2 |  0.399 |       -0.153 |        0.752 |
| mean_rmssd | PC3 |  0.045 |       -0.515 |        0.546 |
| mean_rmssd | PC4 |  0.143 |       -0.428 |        0.609 |
| mean_rmssd | PC5 |  0.241 |       -0.332 |        0.668 |
| mean_rmssd | PC6 |  0.671 |        0.247 |        0.877 |
| mean_rmssd | PC7 |  0.109 |       -0.459 |        0.587 |
| mean_rmssd | PC8 |  0.061 |       -0.501 |        0.556 |
| mean_sdnn  | PC1 | -0.035 |       -0.580 |        0.490 |
| mean_sdnn  | PC2 |  0.371 |       -0.188 |        0.738 |
| mean_sdnn  | PC3 | -0.054 |       -0.595 |        0.476 |
| mean_sdnn  | PC4 |  0.204 |       -0.370 |        0.646 |
| mean_sdnn  | PC5 |  0.195 |       -0.379 |        0.640 |
| mean_sdnn  | PC6 |  0.727 |        0.350 |        0.900 |
| mean_sdnn  | PC7 |  0.108 |       -0.460 |        0.587 |
| mean_sdnn  | PC8 |  0.013 |       -0.542 |        0.524 |

ICC (two-way, agreement) between z-scored HRV metrics and PC scores
(5-min)

#### 1-min

![](physionet15_analysis_1_files/figure-commonmark/hrv-pca-corr-1min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/hrv-pca-scatter-1min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/hrv-pca-ba-1min-1.png)

| HRV Metric | PC  |    ICC | 95% CI Lower | 95% CI Upper |
|:-----------|:----|-------:|-------------:|-------------:|
| mean_rmssd | PC1 | -0.174 |       -0.683 |        0.382 |
| mean_rmssd | PC2 |  0.558 |        0.064 |        0.828 |
| mean_rmssd | PC3 |  0.296 |       -0.273 |        0.698 |
| mean_rmssd | PC4 | -0.445 |       -0.849 |        0.125 |
| mean_rmssd | PC5 | -0.114 |       -0.640 |        0.430 |
| mean_rmssd | PC6 | -0.033 |       -0.579 |        0.491 |
| mean_rmssd | PC7 | -0.019 |       -0.568 |        0.501 |
| mean_rmssd | PC8 |  0.180 |       -0.393 |        0.632 |
| mean_sdnn  | PC1 | -0.147 |       -0.664 |        0.404 |
| mean_sdnn  | PC2 |  0.556 |        0.061 |        0.827 |
| mean_sdnn  | PC3 |  0.418 |       -0.130 |        0.762 |
| mean_sdnn  | PC4 | -0.419 |       -0.835 |        0.153 |
| mean_sdnn  | PC5 | -0.156 |       -0.670 |        0.397 |
| mean_sdnn  | PC6 | -0.079 |       -0.614 |        0.457 |
| mean_sdnn  | PC7 |  0.015 |       -0.540 |        0.525 |
| mean_sdnn  | PC8 |  0.202 |       -0.371 |        0.645 |

ICC (two-way, agreement) between z-scored HRV metrics and PC scores
(1-min)

</div>

### 6.2.2 SDNN vs -PC3: Sign-Flipped Agreement

SDNN and PC3 appear anticorrelated. Flipping the sign of PC3 and
comparing z-scored SDNN vs z(-PC3) via scatter (identity line) and
Bland-Altman.

<div class="panel-tabset">

#### 5-min

![](physionet15_analysis_1_files/figure-commonmark/sdnn-pc3-scatter-5min-1.png)

    r = 0.050, p = 8.58e-01

![](physionet15_analysis_1_files/figure-commonmark/sdnn-pc3-ba-5min-1.png)

    Mean diff = -0.000, 95% LoA = [-2.701, 2.701]

    ICC = 0.054 [-0.508, 0.551]

#### 1-min

![](physionet15_analysis_1_files/figure-commonmark/sdnn-pc3-scatter-1min-1.png)

    r = -0.401, p = 1.39e-01

![](physionet15_analysis_1_files/figure-commonmark/sdnn-pc3-ba-1min-1.png)

    Mean diff = -0.000, 95% LoA = [-3.281, 3.281]

    ICC = -0.442 [-0.848, 0.128]

</div>

### 6.3 Top Significant avg_hr Metrics

    Fewer than 3 metrics pass KW p_adj < 0.05 — using top 10 by raw p-value.

    Using 10 significant avg_hr metrics for PCA:

    - CO_trev_1_num
    - DN_HistogramMode_10
    - DN_HistogramMode_5
    - cv
    - min
    - SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
    - permen
    - DN_Spread_Std
    - sd
    - iqr

<div class="panel-tabset">

#### 5-min

![](physionet15_analysis_1_files/figure-commonmark/pca-top-5min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-top-5min-13-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-top-5min-34-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-top-5min-load-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-top-5min-var-1.png)

#### 1-min

![](physionet15_analysis_1_files/figure-commonmark/pca-top-1min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-top-1min-13-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-top-1min-34-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-top-1min-load-1.png)

![](physionet15_analysis_1_files/figure-commonmark/pca-top-1min-var-1.png)

</div>

## 7 Summary

### Key Findings

**Omnibus tests**: 2 of 36 metrics show significant group differences
(KW p_adj \< 0.05, 5-min resolution).

**Top 5 most discriminating metrics** (Kruskal-Wallis, 5-min,
BH-adjusted):

1.  **mean_rmssd** — p_adj = 3.47e-02 \*
2.  **mean_sdnn** — p_adj = 3.47e-02 \*
3.  **CO_trev_1_num** — p_adj = 2.82e-01
4.  **DN_HistogramMode_10** — p_adj = 2.82e-01
5.  **DN_HistogramMode_5** — p_adj = 2.82e-01

**Most significant pairwise comparison**: Normal vs CHF on metric
mean_rmssd (Wilcoxon p = 7.94e-03).

**Note**: With only n = 5 per group (15 total), statistical power is
very limited. Non-parametric tests (Kruskal-Wallis, Wilcoxon) are
preferred but p-values should be interpreted cautiously. These results
are exploratory.

## 8 Metric Discriminability: PCA Composite vs SD of avg HR

This section formally compares two candidate scalar summaries of 24-hour
heart-rate complexity for their ability to discriminate among the three
clinical groups along the hypothesised severity gradient **Normal \> CHF
\> AF**:

- **PCA Composite** (`pca_dist = PC1 - PC2 - PC3`) — a data-driven
  linear combination of all 34 avg-HR features.
- **SD of avg HR** (`avg_hr_sd`) — a single, clinically interpretable
  variability measure.

Five analyses are applied to each metric: pairwise AUCs, Kruskal-Wallis
with effect size, Jonckheere-Terpstra trend test, Bhattacharyya
distance, and overlap coefficient.

<div class="panel-tabset">

### 5-min

![](physionet15_analysis_1_files/figure-commonmark/s8-dist-plot-5min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/s8-roc-5min-1.png)

| metric | pair | AUC_CI | interpretation |
|:---|:---|:---|:---|
| PCA Composite (PC1-PC2-PC3) | Normal vs CHF | 0.760 \[0.414, 1.000\] | Fair |
| PCA Composite (PC1-PC2-PC3) | Normal vs AF | 0.840 \[0.568, 1.000\] | Good |
| PCA Composite (PC1-PC2-PC3) | CHF vs AF | 0.600 \[0.189, 1.000\] |  |
| SD of avg HR | Normal vs CHF | 0.840 \[0.517, 1.000\] | Good |
| SD of avg HR | Normal vs AF | 0.480 \[0.065, 0.895\] | Fail |
| SD of avg HR | CHF vs AF | 0.880 \[0.626, 1.000\] |  |

Pairwise AUCs with 95% DeLong CIs — 5-min

| Metric | Mean AUC (N vs D) | KW H | KW p | e2 | JT stat | JT p | Bhatt (N vs CHF) | Bhatt (N vs AF) | OVL (N vs CHF) | OVL (N vs AF) |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| PCA Composite (PC1-PC2-PC3) | 0.800 | 3.6 | 1.64e-01 | 0.135 | 20 | 3.59e-02 | 0.283 | 0.344 | 0.574 | 0.523 |
| SD of avg HR | 0.660 | 4.9 | 8.80e-02 | 0.238 | 38 | 5.41e-01 | 0.178 | 0.001 | 0.399 | 0.675 |

Discriminability comparison — 5-min resolution

> **Normality caveat (5-min):** Shapiro-Wilk p \< 0.05 detected for the
> following, meaning the Gaussian-approximation Bhattacharyya distances
> should be interpreted with caution:
>
> - SD of avg HR, Normal vs CHF (Shapiro p: Normal=0.404, Disease=0.004)

### 1-min

![](physionet15_analysis_1_files/figure-commonmark/s8-dist-plot-1min-1.png)

![](physionet15_analysis_1_files/figure-commonmark/s8-roc-1min-1.png)

| metric | pair | AUC_CI | interpretation |
|:---|:---|:---|:---|
| PCA Composite (PC1-PC2-PC3) | Normal vs CHF | 0.440 \[0.014, 0.866\] | Fail |
| PCA Composite (PC1-PC2-PC3) | Normal vs AF | 0.680 \[0.304, 1.000\] | Poor |
| PCA Composite (PC1-PC2-PC3) | CHF vs AF | 0.880 \[0.626, 1.000\] |  |
| SD of avg HR | Normal vs CHF | 0.880 \[0.626, 1.000\] | Good |
| SD of avg HR | Normal vs AF | 0.640 \[0.252, 1.000\] | Poor |
| SD of avg HR | CHF vs AF | 0.880 \[0.626, 1.000\] |  |

Pairwise AUCs with 95% DeLong CIs — 1-min

| Metric | Mean AUC (N vs D) | KW H | KW p | e2 | JT stat | JT p | Bhatt (N vs CHF) | Bhatt (N vs AF) | OVL (N vs CHF) | OVL (N vs AF) |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| PCA Composite (PC1-PC2-PC3) | 0.560 | 3.3 | 1.96e-01 | 0.105 | 25 | 1.05e-01 | 0.045 | 0.176 | 0.708 | 0.664 |
| SD of avg HR | 0.760 | 5.7 | 5.90e-02 | 0.305 | 34 | 3.78e-01 | 0.178 | 0.002 | 0.406 | 0.672 |

Discriminability comparison — 1-min resolution

> **Normality caveat (1-min):** Shapiro-Wilk p \< 0.05 detected for the
> following, meaning the Gaussian-approximation Bhattacharyya distances
> should be interpreted with caution:
>
> - SD of avg HR, Normal vs CHF (Shapiro p: Normal=0.459, Disease=0.005)

</div>

### Recommendation

**Mean Normal-vs-Disease AUC**: PCA Composite = 0.800 (5-min) / 0.560
(1-min); SD of avg HR = 0.660 (5-min) / 0.760 (1-min).

**Jonckheere-Terpstra trend test** (decreasing across Normal \> CHF \>
AF): PCA p = 3.59e-02 (5-min) / 1.05e-01 (1-min); SD p = 5.41e-01
(5-min) / 3.78e-01 (1-min).

**Mean overlap coefficient** (Normal vs Disease; lower = better
separation): PCA = 0.548 (5-min) / 0.686 (1-min); SD = 0.537 (5-min) /
0.539 (1-min).

**Overall**: neither metric clearly dominates appears to better satisfy
both separation and ordering criteria (the two metrics show mixed
advantages across criteria and resolutions).

**Caveats**:

1.  Each group has only n = 5, leading to very wide AUC confidence
    intervals and limited statistical power for all comparisons.
2.  Shapiro-Wilk violations (see normality flags above) mean that the
    Gaussian-approximation Bhattacharyya distances are approximate.
3.  The PCA composite was evaluated on the same data used to derive the
    PCA loadings; its AUCs are therefore **optimistic** relative to
    out-of-sample performance.
4.  Superior discriminability does not imply causality — a metric that
    separates groups may reflect confounders (e.g., age, medication)
    rather than disease per se.

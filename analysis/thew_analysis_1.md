# THEW Holter Metrics: Group Comparisons by Health Status

2026-03-04

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
  - [6.1 All Metrics (38)](#61-all-metrics-38)
  - [6.2 avg_hr Metrics Only (34)](#62-avg_hr-metrics-only-34)
  - [6.2.1 HRV vs avg_hr PCA Scores](#621-hrv-vs-avg_hr-pca-scores)
  - [6.2.2 SDNN vs −PC3: Sign-Flipped
    Agreement](#622-sdnn-vs-pc3-sign-flipped-agreement)
  - [6.3 Top Significant avg_hr
    Metrics](#63-top-significant-avg_hr-metrics)
- [7 Summary](#7-summary)
  - [Key Findings](#key-findings)

## 1 Setup & Data Loading

## 2 Data Overview & Demographics

| condition4   | 5-min | 1-min |
|:-------------|------:|------:|
| Healthy      |   159 |   159 |
| CAD          |   217 |   217 |
| CAD_Diabetes |    29 |    29 |
| ESRD         |    41 |    41 |

Subjects by condition4 group

| condition4   |   1 |   2 |
|:-------------|----:|----:|
| Healthy      |  78 |  81 |
| CAD          | 180 |  37 |
| CAD_Diabetes |  23 |   6 |
| ESRD         |  24 |  17 |

Gender distribution by condition4

    No missing values in any metric column.

## 3 Boxplots by Condition

### avg_hr Metrics (catch22 + descriptive + entropy)

<div class="panel-tabset">

#### 5-min

![](thew_analysis_1_files/figure-commonmark/boxplots-avghr-5min-1.png)

#### 1-min

![](thew_analysis_1_files/figure-commonmark/boxplots-avghr-1min-1.png)

</div>

### HRV Metrics

<div class="panel-tabset">

#### 5-min

![](thew_analysis_1_files/figure-commonmark/boxplots-hrv-5min-1.png)

#### 1-min

![](thew_analysis_1_files/figure-commonmark/boxplots-hrv-1min-1.png)

</div>

## 3.5 Correlation Heatmap

<div class="panel-tabset">

### 5-min

![](thew_analysis_1_files/figure-commonmark/corr-heatmap-5min-1.png)

### 1-min

![](thew_analysis_1_files/figure-commonmark/corr-heatmap-1min-1.png)

</div>

### 3.6 Permutation Entropy vs CV Scatter

<div class="panel-tabset">

#### 5-min

![](thew_analysis_1_files/figure-commonmark/permen-cv-scatter-5min-1.png)

#### 1-min

![](thew_analysis_1_files/figure-commonmark/permen-cv-scatter-1min-1.png)

</div>

### 3.7 SDNN & RMSSD by Condition

<div class="panel-tabset">

#### 5-min

![](thew_analysis_1_files/figure-commonmark/sdnn-jitter-5min-1.png)

![](thew_analysis_1_files/figure-commonmark/rmssd-jitter-5min-1.png)

![](thew_analysis_1_files/figure-commonmark/permen-jitter-5min-1.png)

![](thew_analysis_1_files/figure-commonmark/sd-jitter-5min-1.png)

![](thew_analysis_1_files/figure-commonmark/cv-jitter-5min-1.png)

![](thew_analysis_1_files/figure-commonmark/mean-hr-jitter-5min-1.png)

![](thew_analysis_1_files/figure-commonmark/median-hr-jitter-5min-1.png)

#### 1-min

![](thew_analysis_1_files/figure-commonmark/sdnn-jitter-1min-1.png)

![](thew_analysis_1_files/figure-commonmark/rmssd-jitter-1min-1.png)

![](thew_analysis_1_files/figure-commonmark/permen-jitter-1min-1.png)

![](thew_analysis_1_files/figure-commonmark/sd-jitter-1min-1.png)

![](thew_analysis_1_files/figure-commonmark/cv-jitter-1min-1.png)

![](thew_analysis_1_files/figure-commonmark/mean-hr-jitter-1min-1.png)

![](thew_analysis_1_files/figure-commonmark/median-hr-jitter-1min-1.png)

</div>

## 4 Omnibus Significance Tests (ANOVA & Kruskal-Wallis)

<div class="panel-tabset">

### 5-min

| Metric | Test | Statistic | p-value | p (BH-adj) | Sig |
|:---|:---|---:|---:|---:|:---|
| max | ANOVA | 103.73 | 0.00e+00 | 0.00e+00 | \*\*\* |
| DN_Spread_Std | ANOVA | 96.76 | 0.00e+00 | 0.00e+00 | \*\*\* |
| sd | ANOVA | 96.76 | 0.00e+00 | 0.00e+00 | \*\*\* |
| iqr | ANOVA | 91.98 | 0.00e+00 | 0.00e+00 | \*\*\* |
| max | Kruskal-Wallis | 193.47 | 0.00e+00 | 0.00e+00 | \*\*\* |
| DN_Spread_Std | Kruskal-Wallis | 192.03 | 0.00e+00 | 0.00e+00 | \*\*\* |
| sd | Kruskal-Wallis | 192.03 | 0.00e+00 | 0.00e+00 | \*\*\* |
| iqr | Kruskal-Wallis | 184.50 | 0.00e+00 | 0.00e+00 | \*\*\* |
| cv | ANOVA | 70.84 | 0.00e+00 | 0.00e+00 | \*\*\* |
| permen | Kruskal-Wallis | 158.43 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean_sd_hr | Kruskal-Wallis | 156.90 | 0.00e+00 | 0.00e+00 | \*\*\* |
| cv | Kruskal-Wallis | 156.34 | 0.00e+00 | 0.00e+00 | \*\*\* |
| permen | ANOVA | 57.81 | 0.00e+00 | 0.00e+00 | \*\*\* |
| DN_Mean | ANOVA | 42.03 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean | ANOVA | 42.03 | 0.00e+00 | 0.00e+00 | \*\*\* |
| median | ANOVA | 41.82 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean_sd_hr | ANOVA | 40.94 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean_median_hr | ANOVA | 40.34 | 0.00e+00 | 0.00e+00 | \*\*\* |
| DN_Mean | Kruskal-Wallis | 103.06 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean | Kruskal-Wallis | 103.06 | 0.00e+00 | 0.00e+00 | \*\*\* |
| median | Kruskal-Wallis | 102.99 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean_median_hr | Kruskal-Wallis | 98.84 | 0.00e+00 | 0.00e+00 | \*\*\* |
| min | ANOVA | 16.35 | 0.00e+00 | 0.00e+00 | \*\*\* |
| min | Kruskal-Wallis | 45.92 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean_sdnn_ms | Kruskal-Wallis | 38.88 | 0.00e+00 | 1.00e-07 | \*\*\* |
| FC_LocalSimple_mean1_tauresrat | ANOVA | 10.02 | 2.10e-06 | 6.20e-06 | \*\*\* |
| sampen | Kruskal-Wallis | 28.88 | 2.40e-06 | 6.50e-06 | \*\*\* |
| sampen | ANOVA | 9.66 | 3.50e-06 | 9.40e-06 | \*\*\* |
| FC_LocalSimple_mean1_tauresrat | Kruskal-Wallis | 24.95 | 1.58e-05 | 4.00e-05 | \*\*\* |
| CO_f1ecac | Kruskal-Wallis | 22.14 | 6.10e-05 | 1.37e-04 | \*\*\* |
| SB_TransitionMatrix_3ac_sumdiagcov | Kruskal-Wallis | 22.13 | 6.13e-05 | 1.37e-04 | \*\*\* |
| SB_TransitionMatrix_3ac_sumdiagcov | ANOVA | 7.22 | 9.74e-05 | 2.47e-04 | \*\*\* |
| SP_Summaries_welch_rect_centroid | Kruskal-Wallis | 20.26 | 1.50e-04 | 3.16e-04 | \*\*\* |
| DN_OutlierInclude_n_001_mdrmd | ANOVA | 6.49 | 2.64e-04 | 6.28e-04 | \*\*\* |
| CO_f1ecac | ANOVA | 6.20 | 3.93e-04 | 8.78e-04 | \*\*\* |
| SB_MotifThree_quantile_hh | Kruskal-Wallis | 18.22 | 3.96e-04 | 7.91e-04 | \*\*\* |
| SP_Summaries_welch_rect_centroid | ANOVA | 5.78 | 6.94e-04 | 1.47e-03 | \*\* |
| CO_HistogramAMI_even_2_5 | Kruskal-Wallis | 16.06 | 1.10e-03 | 2.09e-03 | \*\* |
| DN_OutlierInclude_n_001_mdrmd | Kruskal-Wallis | 15.15 | 1.69e-03 | 3.07e-03 | \*\* |
| SB_MotifThree_quantile_hh | ANOVA | 5.12 | 1.72e-03 | 3.44e-03 | \*\* |
| MD_hrv_classic_pnn40 | ANOVA | 4.76 | 2.80e-03 | 5.32e-03 | \*\* |
| MD_hrv_classic_pnn40 | Kruskal-Wallis | 13.42 | 3.80e-03 | 6.57e-03 | \*\* |
| FC_LocalSimple_mean3_stderr | Kruskal-Wallis | 13.25 | 4.13e-03 | 6.82e-03 | \*\* |
| CO_HistogramAMI_even_2_5 | ANOVA | 4.25 | 5.63e-03 | 1.02e-02 | \* |
| SB_BinaryStats_diff_longstretch0 | ANOVA | 4.12 | 6.75e-03 | 1.17e-02 | \* |
| FC_LocalSimple_mean3_stderr | ANOVA | 3.70 | 1.19e-02 | 1.97e-02 | \* |
| apen | Kruskal-Wallis | 10.31 | 1.61e-02 | 2.55e-02 | \* |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | ANOVA | 3.02 | 2.95e-02 | 4.68e-02 | \* |
| apen | ANOVA | 2.79 | 3.99e-02 | 6.07e-02 |  |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Kruskal-Wallis | 8.04 | 4.51e-02 | 6.86e-02 |  |
| SB_BinaryStats_diff_longstretch0 | Kruskal-Wallis | 7.90 | 4.81e-02 | 7.02e-02 |  |
| SP_Summaries_welch_rect_area_5_1 | ANOVA | 2.43 | 6.48e-02 | 9.47e-02 |  |
| CO_trev_1_num | ANOVA | 2.36 | 7.05e-02 | 9.92e-02 |  |
| SP_Summaries_welch_rect_area_5_1 | Kruskal-Wallis | 6.99 | 7.21e-02 | 1.02e-01 |  |
| mean_sdnn_ms | ANOVA | 2.15 | 9.30e-02 | 1.25e-01 |  |
| CO_FirstMin_ac | ANOVA | 2.13 | 9.52e-02 | 1.25e-01 |  |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Kruskal-Wallis | 5.97 | 1.13e-01 | 1.53e-01 |  |
| CO_trev_1_num | Kruskal-Wallis | 5.41 | 1.44e-01 | 1.87e-01 |  |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Kruskal-Wallis | 5.36 | 1.47e-01 | 1.87e-01 |  |
| CO_FirstMin_ac | Kruskal-Wallis | 4.79 | 1.88e-01 | 2.30e-01 |  |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | ANOVA | 1.47 | 2.22e-01 | 2.81e-01 |  |
| mean_rmssd_ms | Kruskal-Wallis | 4.25 | 2.36e-01 | 2.80e-01 |  |
| PD_PeriodicityWang_th0_01 | ANOVA | 1.40 | 2.42e-01 | 2.95e-01 |  |
| DN_HistogramMode_10 | Kruskal-Wallis | 4.13 | 2.47e-01 | 2.85e-01 |  |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | ANOVA | 1.38 | 2.48e-01 | 2.95e-01 |  |
| SB_BinaryStats_mean_longstretch1 | ANOVA | 1.12 | 3.39e-01 | 3.90e-01 |  |
| SB_BinaryStats_mean_longstretch1 | Kruskal-Wallis | 3.14 | 3.70e-01 | 4.14e-01 |  |
| DN_HistogramMode_10 | ANOVA | 0.95 | 4.16e-01 | 4.65e-01 |  |
| mean_rmssd_ms | ANOVA | 0.90 | 4.39e-01 | 4.77e-01 |  |
| PD_PeriodicityWang_th0_01 | Kruskal-Wallis | 2.17 | 5.38e-01 | 5.84e-01 |  |
| DN_OutlierInclude_p_001_mdrmd | ANOVA | 0.71 | 5.48e-01 | 5.69e-01 |  |
| DN_HistogramMode_5 | ANOVA | 0.70 | 5.54e-01 | 5.69e-01 |  |
| DN_HistogramMode_5 | Kruskal-Wallis | 1.97 | 5.79e-01 | 6.11e-01 |  |
| DN_OutlierInclude_p_001_mdrmd | Kruskal-Wallis | 1.68 | 6.41e-01 | 6.59e-01 |  |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Kruskal-Wallis | 1.56 | 6.69e-01 | 6.69e-01 |  |
| CO_Embed2_Dist_tau_d_expfit_meandiff | ANOVA | 0.52 | 6.70e-01 | 6.70e-01 |  |

### 1-min

| Metric | Test | Statistic | p-value | p (BH-adj) | Sig |
|:---|:---|---:|---:|---:|:---|
| max | ANOVA | 129.03 | 0.00e+00 | 0.00e+00 | \*\*\* |
| DN_Spread_Std | ANOVA | 98.30 | 0.00e+00 | 0.00e+00 | \*\*\* |
| sd | ANOVA | 98.30 | 0.00e+00 | 0.00e+00 | \*\*\* |
| iqr | ANOVA | 94.48 | 0.00e+00 | 0.00e+00 | \*\*\* |
| max | Kruskal-Wallis | 215.49 | 0.00e+00 | 0.00e+00 | \*\*\* |
| DN_Spread_Std | Kruskal-Wallis | 193.37 | 0.00e+00 | 0.00e+00 | \*\*\* |
| sd | Kruskal-Wallis | 193.37 | 0.00e+00 | 0.00e+00 | \*\*\* |
| iqr | Kruskal-Wallis | 187.51 | 0.00e+00 | 0.00e+00 | \*\*\* |
| cv | ANOVA | 71.97 | 0.00e+00 | 0.00e+00 | \*\*\* |
| permen | Kruskal-Wallis | 160.05 | 0.00e+00 | 0.00e+00 | \*\*\* |
| cv | Kruskal-Wallis | 159.05 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean_sd_hr | Kruskal-Wallis | 156.18 | 0.00e+00 | 0.00e+00 | \*\*\* |
| permen | ANOVA | 58.45 | 0.00e+00 | 0.00e+00 | \*\*\* |
| DN_Mean | ANOVA | 42.01 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean | ANOVA | 42.01 | 0.00e+00 | 0.00e+00 | \*\*\* |
| median | ANOVA | 41.43 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean_sd_hr | ANOVA | 40.72 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean_median_hr | ANOVA | 40.48 | 0.00e+00 | 0.00e+00 | \*\*\* |
| DN_Mean | Kruskal-Wallis | 103.17 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean | Kruskal-Wallis | 103.17 | 0.00e+00 | 0.00e+00 | \*\*\* |
| median | Kruskal-Wallis | 101.48 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean_median_hr | Kruskal-Wallis | 99.02 | 0.00e+00 | 0.00e+00 | \*\*\* |
| FC_LocalSimple_mean1_tauresrat | ANOVA | 26.45 | 0.00e+00 | 0.00e+00 | \*\*\* |
| min | ANOVA | 16.15 | 0.00e+00 | 0.00e+00 | \*\*\* |
| min | Kruskal-Wallis | 45.57 | 0.00e+00 | 0.00e+00 | \*\*\* |
| FC_LocalSimple_mean1_tauresrat | Kruskal-Wallis | 40.73 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean_sdnn_ms | Kruskal-Wallis | 37.72 | 0.00e+00 | 1.00e-07 | \*\*\* |
| MD_hrv_classic_pnn40 | ANOVA | 8.90 | 9.80e-06 | 2.65e-05 | \*\*\* |
| SP_Summaries_welch_rect_centroid | Kruskal-Wallis | 25.04 | 1.51e-05 | 3.83e-05 | \*\*\* |
| CO_f1ecac | Kruskal-Wallis | 23.45 | 3.25e-05 | 7.71e-05 | \*\*\* |
| SB_BinaryStats_diff_longstretch0 | ANOVA | 7.68 | 5.20e-05 | 1.32e-04 | \*\*\* |
| apen | ANOVA | 6.95 | 1.40e-04 | 3.32e-04 | \*\*\* |
| CO_f1ecac | ANOVA | 6.66 | 2.08e-04 | 4.66e-04 | \*\*\* |
| sampen | ANOVA | 6.58 | 2.32e-04 | 4.90e-04 | \*\*\* |
| MD_hrv_classic_pnn40 | Kruskal-Wallis | 19.29 | 2.38e-04 | 5.32e-04 | \*\*\* |
| SB_TransitionMatrix_3ac_sumdiagcov | Kruskal-Wallis | 18.59 | 3.33e-04 | 7.02e-04 | \*\*\* |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | ANOVA | 6.29 | 3.47e-04 | 6.93e-04 | \*\*\* |
| CO_trev_1_num | Kruskal-Wallis | 18.18 | 4.04e-04 | 7.81e-04 | \*\*\* |
| sampen | Kruskal-Wallis | 18.14 | 4.11e-04 | 7.81e-04 | \*\*\* |
| SB_TransitionMatrix_3ac_sumdiagcov | ANOVA | 6.13 | 4.32e-04 | 8.21e-04 | \*\*\* |
| DN_OutlierInclude_n_001_mdrmd | ANOVA | 5.55 | 9.59e-04 | 1.74e-03 | \*\* |
| apen | Kruskal-Wallis | 15.07 | 1.76e-03 | 3.18e-03 | \*\* |
| SB_BinaryStats_diff_longstretch0 | Kruskal-Wallis | 14.00 | 2.90e-03 | 5.01e-03 | \*\* |
| SB_MotifThree_quantile_hh | ANOVA | 4.66 | 3.22e-03 | 5.57e-03 | \*\* |
| DN_OutlierInclude_n_001_mdrmd | Kruskal-Wallis | 13.20 | 4.22e-03 | 6.90e-03 | \*\* |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Kruskal-Wallis | 13.13 | 4.36e-03 | 6.90e-03 | \*\* |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | ANOVA | 4.36 | 4.85e-03 | 8.01e-03 | \*\* |
| CO_FirstMin_ac | Kruskal-Wallis | 12.81 | 5.06e-03 | 7.48e-03 | \*\* |
| SB_MotifThree_quantile_hh | Kruskal-Wallis | 12.79 | 5.12e-03 | 7.48e-03 | \*\* |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Kruskal-Wallis | 12.51 | 5.82e-03 | 8.19e-03 | \*\* |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Kruskal-Wallis | 12.11 | 7.01e-03 | 9.51e-03 | \*\* |
| SP_Summaries_welch_rect_centroid | ANOVA | 3.91 | 8.89e-03 | 1.41e-02 | \* |
| SP_Summaries_welch_rect_area_5_1 | Kruskal-Wallis | 11.04 | 1.15e-02 | 1.51e-02 | \* |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | ANOVA | 3.71 | 1.17e-02 | 1.75e-02 | \* |
| SP_Summaries_welch_rect_area_5_1 | ANOVA | 3.69 | 1.20e-02 | 1.75e-02 | \* |
| CO_Embed2_Dist_tau_d_expfit_meandiff | ANOVA | 3.37 | 1.85e-02 | 2.60e-02 | \* |
| FC_LocalSimple_mean3_stderr | ANOVA | 2.61 | 5.07e-02 | 6.89e-02 |  |
| FC_LocalSimple_mean3_stderr | Kruskal-Wallis | 7.49 | 5.79e-02 | 7.33e-02 |  |
| SB_BinaryStats_mean_longstretch1 | ANOVA | 2.36 | 7.08e-02 | 9.27e-02 |  |
| SB_BinaryStats_mean_longstretch1 | Kruskal-Wallis | 6.86 | 7.64e-02 | 9.36e-02 |  |
| mean_sdnn_ms | ANOVA | 2.15 | 9.32e-02 | 1.18e-01 |  |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Kruskal-Wallis | 6.40 | 9.38e-02 | 1.11e-01 |  |
| CO_FirstMin_ac | ANOVA | 2.02 | 1.11e-01 | 1.36e-01 |  |
| CO_HistogramAMI_even_2_5 | ANOVA | 1.81 | 1.45e-01 | 1.72e-01 |  |
| DN_HistogramMode_10 | Kruskal-Wallis | 4.99 | 1.73e-01 | 1.99e-01 |  |
| CO_HistogramAMI_even_2_5 | Kruskal-Wallis | 4.89 | 1.80e-01 | 2.01e-01 |  |
| DN_HistogramMode_10 | ANOVA | 1.56 | 1.98e-01 | 2.28e-01 |  |
| mean_rmssd_ms | Kruskal-Wallis | 4.40 | 2.22e-01 | 2.41e-01 |  |
| CO_trev_1_num | ANOVA | 1.46 | 2.25e-01 | 2.51e-01 |  |
| mean_rmssd_ms | ANOVA | 0.93 | 4.27e-01 | 4.64e-01 |  |
| PD_PeriodicityWang_th0_01 | ANOVA | 0.65 | 5.81e-01 | 6.13e-01 |  |
| PD_PeriodicityWang_th0_01 | Kruskal-Wallis | 1.87 | 5.99e-01 | 6.32e-01 |  |
| DN_OutlierInclude_p_001_mdrmd | ANOVA | 0.44 | 7.25e-01 | 7.45e-01 |  |
| DN_HistogramMode_5 | Kruskal-Wallis | 1.20 | 7.54e-01 | 7.74e-01 |  |
| DN_HistogramMode_5 | ANOVA | 0.33 | 8.01e-01 | 8.01e-01 |  |
| DN_OutlierInclude_p_001_mdrmd | Kruskal-Wallis | 0.85 | 8.37e-01 | 8.37e-01 |  |

</div>

## 5 Pairwise Significance Tests

<div class="panel-tabset">

### 5-min

**Summary — most significant pair per metric:**

| Metric | Most Sig. Pair | W stat | Wilcox p | Wilcox p (BH) | t-test p | Sig |
|:---|:---|---:|---:|---:|---:|:---|
| max | Healthy vs CAD | 31073.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| DN_Spread_Std | Healthy vs CAD | 30456.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| sd | Healthy vs CAD | 30456.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| iqr | Healthy vs CAD | 29736.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean_sd_hr | Healthy vs CAD | 28639.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| permen | Healthy vs CAD | 6092.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| cv | Healthy vs CAD | 28301.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| DN_Mean | Healthy vs CAD | 27353.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean | Healthy vs CAD | 27353.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| median | Healthy vs CAD | 27295.5 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean_median_hr | Healthy vs CAD | 27080.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| min | CAD vs ESRD | 1795.5 | 0.00e+00 | 0.00e+00 | 6.00e-07 | \*\*\* |
| sampen | Healthy vs CAD | 11860.0 | 2.00e-07 | 1.80e-06 | 1.00e-07 | \*\*\* |
| mean_sdnn_ms | Healthy vs ESRD | 4850.0 | 1.50e-06 | 1.07e-05 | 5.50e-02 | \*\*\* |
| SB_MotifThree_quantile_hh | Healthy vs CAD | 12748.0 | 1.52e-05 | 9.66e-05 | 3.83e-05 | \*\*\* |
| FC_LocalSimple_mean1_tauresrat | Healthy vs ESRD | 1875.5 | 2.82e-05 | 1.74e-04 | 1.10e-03 | \*\*\* |
| CO_f1ecac | Healthy vs CAD | 21378.0 | 7.40e-05 | 4.02e-04 | 1.78e-04 | \*\*\* |
| SB_TransitionMatrix_3ac_sumdiagcov | Healthy vs ESRD | 4533.5 | 1.07e-04 | 5.43e-04 | 1.29e-04 | \*\*\* |
| CO_HistogramAMI_even_2_5 | Healthy vs CAD | 21211.0 | 1.43e-04 | 6.95e-04 | 4.01e-04 | \*\*\* |
| SP_Summaries_welch_rect_centroid | Healthy vs CAD | 13353.5 | 1.67e-04 | 7.94e-04 | 2.19e-04 | \*\*\* |
| MD_hrv_classic_pnn40 | Healthy vs CAD | 13514.0 | 3.31e-04 | 1.43e-03 | 2.37e-04 | \*\* |
| FC_LocalSimple_mean3_stderr | Healthy vs CAD | 13731.0 | 7.22e-04 | 2.94e-03 | 8.50e-04 | \*\* |
| apen | Healthy vs CAD | 13901.0 | 1.29e-03 | 4.91e-03 | 3.38e-03 | \*\* |
| DN_OutlierInclude_n_001_mdrmd | Healthy vs CAD | 20522.0 | 1.68e-03 | 6.30e-03 | 5.79e-03 | \*\* |
| SB_BinaryStats_diff_longstretch0 | Healthy vs ESRD | 2377.0 | 5.99e-03 | 1.98e-02 | 8.92e-03 | \* |
| SP_Summaries_welch_rect_area_5_1 | Healthy vs CAD | 19922.0 | 1.03e-02 | 3.27e-02 | 5.66e-03 | \* |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | CAD vs CAD_Diabetes | 2310.5 | 1.59e-02 | 4.64e-02 | 1.88e-02 | \* |
| CO_trev_1_num | CAD vs ESRD | 3471.0 | 2.58e-02 | 7.00e-02 | 1.89e-02 |  |
| CO_FirstMin_ac | Healthy vs ESRD | 2542.5 | 2.98e-02 | 7.81e-02 | 8.74e-02 |  |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Healthy vs ESRD | 2551.5 | 3.18e-02 | 8.23e-02 | 8.40e-02 |  |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Healthy vs ESRD | 3914.0 | 4.13e-02 | 1.01e-01 | 2.49e-01 |  |
| DN_HistogramMode_10 | Healthy vs ESRD | 2665.0 | 7.22e-02 | 1.65e-01 | 9.09e-02 |  |
| mean_rmssd_ms | Healthy vs CAD_Diabetes | 2768.0 | 8.65e-02 | 1.90e-01 | 8.03e-01 |  |
| SB_BinaryStats_mean_longstretch1 | CAD vs CAD_Diabetes | 2607.0 | 1.34e-01 | 2.73e-01 | 1.77e-01 |  |
| PD_PeriodicityWang_th0_01 | CAD vs ESRD | 3846.0 | 1.69e-01 | 3.08e-01 | 1.13e-01 |  |
| DN_HistogramMode_5 | CAD_Diabetes vs ESRD | 481.0 | 1.79e-01 | 3.17e-01 | 1.01e-01 |  |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Healthy vs CAD | 18540.0 | 2.16e-01 | 3.62e-01 | 9.86e-01 |  |
| DN_OutlierInclude_p_001_mdrmd | CAD vs CAD_Diabetes | 3577.0 | 2.32e-01 | 3.81e-01 | 1.44e-01 |  |

Most significant pairwise comparison per metric (Wilcoxon)

<details>

<summary>

Full pairwise results (click to expand)
</summary>

| Metric | Pair | t stat | t p | t p (BH) | W stat | W p | W p (BH) |
|:---|:---|---:|---:|---:|---:|---:|---:|
| max | Healthy vs CAD | 16.05 | 0.00e+00 | 0.00e+00 | 31073.0 | 0.00e+00 | 0.00e+00 |
| DN_Spread_Std | Healthy vs CAD | 15.16 | 0.00e+00 | 0.00e+00 | 30456.0 | 0.00e+00 | 0.00e+00 |
| sd | Healthy vs CAD | 15.16 | 0.00e+00 | 0.00e+00 | 30456.0 | 0.00e+00 | 0.00e+00 |
| iqr | Healthy vs CAD | 13.95 | 0.00e+00 | 0.00e+00 | 29736.0 | 0.00e+00 | 0.00e+00 |
| mean_sd_hr | Healthy vs CAD | 9.33 | 0.00e+00 | 0.00e+00 | 28639.0 | 0.00e+00 | 0.00e+00 |
| permen | Healthy vs CAD | -10.18 | 0.00e+00 | 0.00e+00 | 6092.0 | 0.00e+00 | 0.00e+00 |
| cv | Healthy vs CAD | 11.55 | 0.00e+00 | 0.00e+00 | 28301.0 | 0.00e+00 | 0.00e+00 |
| DN_Mean | Healthy vs CAD | 10.71 | 0.00e+00 | 0.00e+00 | 27353.0 | 0.00e+00 | 0.00e+00 |
| mean | Healthy vs CAD | 10.71 | 0.00e+00 | 0.00e+00 | 27353.0 | 0.00e+00 | 0.00e+00 |
| median | Healthy vs CAD | 10.61 | 0.00e+00 | 0.00e+00 | 27295.5 | 0.00e+00 | 0.00e+00 |
| mean_median_hr | Healthy vs CAD | 10.39 | 0.00e+00 | 0.00e+00 | 27080.0 | 0.00e+00 | 0.00e+00 |
| iqr | Healthy vs ESRD | 11.56 | 0.00e+00 | 0.00e+00 | 6041.0 | 0.00e+00 | 0.00e+00 |
| permen | Healthy vs ESRD | -10.32 | 0.00e+00 | 0.00e+00 | 629.0 | 0.00e+00 | 0.00e+00 |
| cv | Healthy vs ESRD | 10.38 | 0.00e+00 | 0.00e+00 | 5877.0 | 0.00e+00 | 0.00e+00 |
| DN_Spread_Std | Healthy vs ESRD | 9.22 | 0.00e+00 | 0.00e+00 | 5790.0 | 0.00e+00 | 0.00e+00 |
| sd | Healthy vs ESRD | 9.22 | 0.00e+00 | 0.00e+00 | 5790.0 | 0.00e+00 | 0.00e+00 |
| DN_Spread_Std | Healthy vs CAD_Diabetes | 10.35 | 0.00e+00 | 0.00e+00 | 4344.0 | 0.00e+00 | 0.00e+00 |
| sd | Healthy vs CAD_Diabetes | 10.35 | 0.00e+00 | 0.00e+00 | 4344.0 | 0.00e+00 | 0.00e+00 |
| mean_sd_hr | Healthy vs CAD_Diabetes | 12.07 | 0.00e+00 | 0.00e+00 | 4316.0 | 0.00e+00 | 0.00e+00 |
| mean_sd_hr | Healthy vs ESRD | 6.84 | 0.00e+00 | 1.00e-07 | 5627.0 | 0.00e+00 | 0.00e+00 |
| iqr | Healthy vs CAD_Diabetes | 10.00 | 0.00e+00 | 0.00e+00 | 4197.0 | 0.00e+00 | 0.00e+00 |
| max | Healthy vs CAD_Diabetes | 9.13 | 0.00e+00 | 0.00e+00 | 4196.0 | 0.00e+00 | 0.00e+00 |
| max | Healthy vs ESRD | 8.51 | 0.00e+00 | 0.00e+00 | 5558.5 | 0.00e+00 | 0.00e+00 |
| permen | Healthy vs CAD_Diabetes | -8.91 | 0.00e+00 | 0.00e+00 | 475.0 | 0.00e+00 | 0.00e+00 |
| cv | Healthy vs CAD_Diabetes | 8.85 | 0.00e+00 | 0.00e+00 | 4134.0 | 0.00e+00 | 0.00e+00 |
| min | CAD vs ESRD | -5.74 | 6.00e-07 | 4.80e-06 | 1795.5 | 0.00e+00 | 0.00e+00 |
| median | CAD vs ESRD | -5.28 | 2.40e-06 | 1.88e-05 | 2158.0 | 2.00e-07 | 1.50e-06 |
| sampen | Healthy vs CAD | -5.50 | 1.00e-07 | 6.00e-07 | 11860.0 | 2.00e-07 | 1.80e-06 |
| mean_median_hr | CAD vs ESRD | -5.28 | 2.40e-06 | 1.88e-05 | 2183.0 | 2.00e-07 | 1.90e-06 |
| DN_Mean | CAD vs ESRD | -5.17 | 3.50e-06 | 2.60e-05 | 2214.0 | 3.00e-07 | 2.50e-06 |
| mean | CAD vs ESRD | -5.17 | 3.50e-06 | 2.60e-05 | 2214.0 | 3.00e-07 | 2.50e-06 |
| mean_sdnn_ms | Healthy vs ESRD | 1.97 | 5.50e-02 | 1.55e-01 | 4850.0 | 1.50e-06 | 1.07e-05 |
| cv | CAD vs ESRD | 4.04 | 1.74e-04 | 9.87e-04 | 6494.0 | 3.10e-06 | 2.11e-05 |
| permen | CAD vs ESRD | -3.45 | 1.06e-03 | 4.91e-03 | 2414.0 | 3.50e-06 | 2.32e-05 |
| iqr | CAD vs ESRD | 3.16 | 2.57e-03 | 1.13e-02 | 6346.0 | 1.50e-05 | 9.66e-05 |
| SB_MotifThree_quantile_hh | Healthy vs CAD | -4.17 | 3.83e-05 | 2.73e-04 | 12748.0 | 1.52e-05 | 9.66e-05 |
| FC_LocalSimple_mean1_tauresrat | Healthy vs ESRD | -3.49 | 1.10e-03 | 5.03e-03 | 1875.5 | 2.82e-05 | 1.74e-04 |
| min | Healthy vs CAD | 3.85 | 1.45e-04 | 8.47e-04 | 21513.0 | 4.26e-05 | 2.56e-04 |
| median | Healthy vs CAD_Diabetes | 4.42 | 8.13e-05 | 5.15e-04 | 3380.0 | 6.74e-05 | 3.94e-04 |
| DN_Mean | Healthy vs CAD_Diabetes | 4.44 | 7.87e-05 | 5.13e-04 | 3376.0 | 7.17e-05 | 3.99e-04 |
| mean | Healthy vs CAD_Diabetes | 4.44 | 7.87e-05 | 5.13e-04 | 3376.0 | 7.17e-05 | 3.99e-04 |
| CO_f1ecac | Healthy vs CAD | 3.79 | 1.78e-04 | 9.87e-04 | 21378.0 | 7.40e-05 | 4.02e-04 |
| min | Healthy vs ESRD | -3.61 | 6.61e-04 | 3.35e-03 | 1953.5 | 7.79e-05 | 4.13e-04 |
| mean_median_hr | Healthy vs CAD_Diabetes | 4.38 | 9.13e-05 | 5.63e-04 | 3356.0 | 9.77e-05 | 5.06e-04 |
| SB_TransitionMatrix_3ac_sumdiagcov | Healthy vs ESRD | 4.05 | 1.29e-04 | 7.72e-04 | 4533.5 | 1.07e-04 | 5.43e-04 |
| mean_sdnn_ms | Healthy vs CAD | 0.35 | 7.30e-01 | 8.49e-01 | 21239.0 | 1.28e-04 | 6.37e-04 |
| CO_HistogramAMI_even_2_5 | Healthy vs CAD | 3.57 | 4.01e-04 | 2.08e-03 | 21211.0 | 1.43e-04 | 6.95e-04 |
| SP_Summaries_welch_rect_centroid | Healthy vs CAD | -3.73 | 2.19e-04 | 1.19e-03 | 13353.5 | 1.67e-04 | 7.94e-04 |
| mean_sdnn_ms | Healthy vs CAD_Diabetes | 2.53 | 1.60e-02 | 5.52e-02 | 3291.0 | 2.57e-04 | 1.20e-03 |
| CO_f1ecac | Healthy vs ESRD | 3.08 | 3.14e-03 | 1.35e-02 | 4464.0 | 2.69e-04 | 1.23e-03 |
| FC_LocalSimple_mean1_tauresrat | Healthy vs CAD | -3.36 | 8.58e-04 | 4.08e-03 | 13491.0 | 3.03e-04 | 1.36e-03 |
| MD_hrv_classic_pnn40 | Healthy vs CAD | -3.72 | 2.37e-04 | 1.26e-03 | 13514.0 | 3.31e-04 | 1.43e-03 |
| SP_Summaries_welch_rect_centroid | Healthy vs ESRD | -3.21 | 2.39e-03 | 1.07e-02 | 2081.5 | 3.32e-04 | 1.43e-03 |
| mean_sdnn_ms | CAD vs ESRD | 1.65 | 1.04e-01 | 2.44e-01 | 6004.0 | 3.87e-04 | 1.64e-03 |
| SB_TransitionMatrix_3ac_sumdiagcov | Healthy vs CAD | 3.42 | 7.01e-04 | 3.48e-03 | 20857.5 | 4.96e-04 | 2.06e-03 |
| FC_LocalSimple_mean3_stderr | Healthy vs CAD | -3.36 | 8.50e-04 | 4.08e-03 | 13731.0 | 7.22e-04 | 2.94e-03 |
| DN_Spread_Std | CAD vs ESRD | 1.78 | 8.08e-02 | 2.12e-01 | 5879.0 | 1.10e-03 | 4.33e-03 |
| sd | CAD vs ESRD | 1.78 | 8.08e-02 | 2.12e-01 | 5879.0 | 1.10e-03 | 4.33e-03 |
| mean_sd_hr | CAD vs CAD_Diabetes | 4.23 | 7.65e-05 | 5.13e-04 | 4306.0 | 1.28e-03 | 4.91e-03 |
| apen | Healthy vs CAD | -2.95 | 3.38e-03 | 1.43e-02 | 13901.0 | 1.29e-03 | 4.91e-03 |
| DN_OutlierInclude_n_001_mdrmd | Healthy vs CAD | 2.78 | 5.79e-03 | 2.17e-02 | 20522.0 | 1.68e-03 | 6.30e-03 |
| mean_sd_hr | CAD vs ESRD | 1.66 | 1.02e-01 | 2.44e-01 | 5758.0 | 2.82e-03 | 1.04e-02 |
| min | CAD_Diabetes vs ESRD | -2.96 | 4.32e-03 | 1.73e-02 | 357.5 | 4.81e-03 | 1.74e-02 |
| mean_median_hr | CAD_Diabetes vs ESRD | -3.05 | 3.45e-03 | 1.43e-02 | 362.0 | 5.16e-03 | 1.84e-02 |
| DN_Mean | CAD_Diabetes vs ESRD | -2.96 | 4.48e-03 | 1.73e-02 | 365.0 | 5.79e-03 | 1.97e-02 |
| mean | CAD_Diabetes vs ESRD | -2.96 | 4.48e-03 | 1.73e-02 | 365.0 | 5.79e-03 | 1.97e-02 |
| median | CAD_Diabetes vs ESRD | -3.00 | 4.07e-03 | 1.66e-02 | 365.0 | 5.79e-03 | 1.97e-02 |
| SB_BinaryStats_diff_longstretch0 | Healthy vs ESRD | -2.72 | 8.92e-03 | 3.28e-02 | 2377.0 | 5.99e-03 | 1.98e-02 |
| sampen | Healthy vs ESRD | -2.28 | 2.70e-02 | 8.56e-02 | 2351.0 | 6.00e-03 | 1.98e-02 |
| FC_LocalSimple_mean1_tauresrat | CAD vs ESRD | -2.38 | 2.17e-02 | 6.95e-02 | 3296.5 | 8.58e-03 | 2.79e-02 |
| sampen | Healthy vs CAD_Diabetes | -2.62 | 1.25e-02 | 4.54e-02 | 1607.0 | 9.59e-03 | 3.08e-02 |
| SP_Summaries_welch_rect_area_5_1 | Healthy vs CAD | 2.78 | 5.66e-03 | 2.15e-02 | 19922.0 | 1.03e-02 | 3.27e-02 |
| FC_LocalSimple_mean1_tauresrat | CAD_Diabetes vs ESRD | -2.21 | 3.06e-02 | 9.56e-02 | 385.0 | 1.27e-02 | 3.96e-02 |
| SB_BinaryStats_diff_longstretch0 | CAD vs ESRD | -2.39 | 2.07e-02 | 6.74e-02 | 3390.0 | 1.29e-02 | 3.98e-02 |
| mean_sdnn_ms | CAD vs CAD_Diabetes | 2.09 | 4.11e-02 | 1.23e-01 | 4040.0 | 1.31e-02 | 3.98e-02 |
| FC_LocalSimple_mean3_stderr | Healthy vs ESRD | -1.89 | 6.39e-02 | 1.78e-01 | 2450.0 | 1.44e-02 | 4.31e-02 |
| CO_HistogramAMI_even_2_5 | Healthy vs ESRD | 1.88 | 6.54e-02 | 1.80e-01 | 4064.0 | 1.50e-02 | 4.43e-02 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | CAD vs CAD_Diabetes | -2.47 | 1.88e-02 | 6.30e-02 | 2310.5 | 1.59e-02 | 4.64e-02 |
| SB_TransitionMatrix_3ac_sumdiagcov | CAD_Diabetes vs ESRD | 2.55 | 1.40e-02 | 4.99e-02 | 791.5 | 1.89e-02 | 5.45e-02 |
| DN_OutlierInclude_n_001_mdrmd | CAD vs CAD_Diabetes | -1.71 | 9.73e-02 | 2.39e-01 | 2315.0 | 2.09e-02 | 5.97e-02 |
| SB_TransitionMatrix_3ac_sumdiagcov | CAD vs ESRD | 1.97 | 5.38e-02 | 1.55e-01 | 5442.5 | 2.27e-02 | 6.39e-02 |
| iqr | CAD_Diabetes vs ESRD | 1.30 | 1.96e-01 | 3.84e-01 | 784.0 | 2.36e-02 | 6.55e-02 |
| DN_OutlierInclude_n_001_mdrmd | Healthy vs ESRD | 2.54 | 1.46e-02 | 5.13e-02 | 4003.0 | 2.45e-02 | 6.74e-02 |
| CO_trev_1_num | CAD vs ESRD | -2.42 | 1.89e-02 | 6.30e-02 | 3471.0 | 2.58e-02 | 7.00e-02 |
| permen | CAD vs CAD_Diabetes | -2.04 | 4.76e-02 | 1.41e-01 | 2361.0 | 2.92e-02 | 7.79e-02 |
| cv | CAD vs CAD_Diabetes | 2.16 | 3.69e-02 | 1.14e-01 | 3931.0 | 2.94e-02 | 7.79e-02 |
| CO_FirstMin_ac | Healthy vs ESRD | -1.75 | 8.74e-02 | 2.24e-01 | 2542.5 | 2.98e-02 | 7.81e-02 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Healthy vs ESRD | -1.76 | 8.40e-02 | 2.18e-01 | 2551.5 | 3.18e-02 | 8.23e-02 |
| permen | CAD_Diabetes vs ESRD | -1.00 | 3.23e-01 | 5.15e-01 | 417.0 | 3.42e-02 | 8.77e-02 |
| CO_trev_1_num | Healthy vs ESRD | -2.11 | 3.93e-02 | 1.19e-01 | 2563.0 | 3.52e-02 | 8.91e-02 |
| cv | CAD_Diabetes vs ESRD | 1.54 | 1.29e-01 | 2.75e-01 | 770.0 | 3.63e-02 | 9.11e-02 |
| min | CAD vs CAD_Diabetes | -1.59 | 1.20e-01 | 2.59e-01 | 2408.0 | 4.03e-02 | 9.99e-02 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Healthy vs ESRD | 1.17 | 2.49e-01 | 4.50e-01 | 3914.0 | 4.13e-02 | 1.01e-01 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | CAD vs ESRD | -1.81 | 7.55e-02 | 2.05e-01 | 3618.5 | 4.96e-02 | 1.20e-01 |
| DN_OutlierInclude_n_001_mdrmd | CAD_Diabetes vs ESRD | 2.40 | 1.91e-02 | 6.30e-02 | 755.0 | 5.64e-02 | 1.35e-01 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Healthy vs CAD_Diabetes | -1.80 | 7.92e-02 | 2.12e-01 | 1812.5 | 5.79e-02 | 1.38e-01 |
| max | CAD_Diabetes vs ESRD | -1.65 | 1.04e-01 | 2.44e-01 | 440.0 | 6.61e-02 | 1.55e-01 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Healthy vs CAD_Diabetes | 1.30 | 2.02e-01 | 3.90e-01 | 2782.0 | 6.79e-02 | 1.56e-01 |
| CO_f1ecac | CAD_Diabetes vs ESRD | 1.60 | 1.16e-01 | 2.57e-01 | 748.0 | 6.79e-02 | 1.56e-01 |
| DN_HistogramMode_10 | Healthy vs ESRD | -1.71 | 9.09e-02 | 2.27e-01 | 2665.0 | 7.22e-02 | 1.65e-01 |
| DN_Spread_Std | CAD vs CAD_Diabetes | 1.73 | 9.17e-02 | 2.27e-01 | 3789.0 | 7.45e-02 | 1.66e-01 |
| sd | CAD vs CAD_Diabetes | 1.73 | 9.17e-02 | 2.27e-01 | 3789.0 | 7.45e-02 | 1.66e-01 |
| SB_BinaryStats_diff_longstretch0 | CAD_Diabetes vs ESRD | -1.96 | 5.46e-02 | 1.55e-01 | 453.0 | 8.43e-02 | 1.87e-01 |
| mean_rmssd_ms | Healthy vs CAD_Diabetes | 0.25 | 8.03e-01 | 8.93e-01 | 2768.0 | 8.65e-02 | 1.90e-01 |
| MD_hrv_classic_pnn40 | CAD vs CAD_Diabetes | 1.63 | 1.12e-01 | 2.53e-01 | 3747.0 | 9.54e-02 | 2.07e-01 |
| max | CAD vs ESRD | -1.62 | 1.12e-01 | 2.53e-01 | 3736.0 | 1.04e-01 | 2.24e-01 |
| SP_Summaries_welch_rect_centroid | CAD vs ESRD | -1.31 | 1.97e-01 | 3.84e-01 | 3748.0 | 1.09e-01 | 2.32e-01 |
| SB_TransitionMatrix_3ac_sumdiagcov | CAD vs CAD_Diabetes | -1.61 | 1.18e-01 | 2.58e-01 | 2586.5 | 1.18e-01 | 2.47e-01 |
| CO_f1ecac | CAD vs ESRD | 1.04 | 3.01e-01 | 4.90e-01 | 5134.0 | 1.18e-01 | 2.47e-01 |
| SP_Summaries_welch_rect_centroid | CAD_Diabetes vs ESRD | -1.03 | 3.05e-01 | 4.93e-01 | 464.0 | 1.20e-01 | 2.49e-01 |
| SB_MotifThree_quantile_hh | Healthy vs ESRD | -1.13 | 2.65e-01 | 4.66e-01 | 2758.0 | 1.29e-01 | 2.66e-01 |
| SB_BinaryStats_mean_longstretch1 | CAD vs CAD_Diabetes | -1.38 | 1.77e-01 | 3.63e-01 | 2607.0 | 1.34e-01 | 2.73e-01 |
| CO_FirstMin_ac | CAD vs ESRD | -1.14 | 2.59e-01 | 4.62e-01 | 3802.5 | 1.40e-01 | 2.80e-01 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Healthy vs CAD | -0.94 | 3.50e-01 | 5.41e-01 | 15721.5 | 1.41e-01 | 2.80e-01 |
| SP_Summaries_welch_rect_area_5_1 | Healthy vs ESRD | 1.34 | 1.88e-01 | 3.79e-01 | 3740.0 | 1.46e-01 | 2.80e-01 |
| FC_LocalSimple_mean1_tauresrat | CAD vs CAD_Diabetes | 0.44 | 6.61e-01 | 7.97e-01 | 3669.5 | 1.46e-01 | 2.80e-01 |
| CO_HistogramAMI_even_2_5 | Healthy vs CAD_Diabetes | 1.06 | 2.97e-01 | 4.87e-01 | 2697.0 | 1.47e-01 | 2.80e-01 |
| DN_Spread_Std | CAD_Diabetes vs ESRD | 0.25 | 8.03e-01 | 8.93e-01 | 717.0 | 1.47e-01 | 2.80e-01 |
| sd | CAD_Diabetes vs ESRD | 0.25 | 8.03e-01 | 8.93e-01 | 717.0 | 1.47e-01 | 2.80e-01 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | CAD vs ESRD | 0.03 | 9.73e-01 | 9.92e-01 | 5064.0 | 1.48e-01 | 2.80e-01 |
| DN_HistogramMode_10 | Healthy vs CAD | -0.98 | 3.27e-01 | 5.18e-01 | 15769.0 | 1.55e-01 | 2.91e-01 |
| mean_rmssd_ms | CAD vs CAD_Diabetes | 1.18 | 2.43e-01 | 4.43e-01 | 3648.0 | 1.64e-01 | 3.06e-01 |
| SB_MotifThree_quantile_hh | Healthy vs CAD_Diabetes | -0.90 | 3.72e-01 | 5.47e-01 | 1931.0 | 1.65e-01 | 3.06e-01 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | CAD vs ESRD | -1.28 | 2.06e-01 | 3.94e-01 | 3843.5 | 1.67e-01 | 3.06e-01 |
| PD_PeriodicityWang_th0_01 | CAD vs ESRD | -1.61 | 1.13e-01 | 2.53e-01 | 3846.0 | 1.69e-01 | 3.08e-01 |
| iqr | CAD vs CAD_Diabetes | 1.47 | 1.50e-01 | 3.12e-01 | 3638.5 | 1.72e-01 | 3.11e-01 |
| apen | Healthy vs CAD_Diabetes | -1.32 | 1.94e-01 | 3.84e-01 | 1942.0 | 1.78e-01 | 3.17e-01 |
| mean_rmssd_ms | Healthy vs CAD | -1.56 | 1.19e-01 | 2.58e-01 | 18650.0 | 1.79e-01 | 3.17e-01 |
| DN_HistogramMode_5 | CAD_Diabetes vs ESRD | -1.67 | 1.01e-01 | 2.44e-01 | 481.0 | 1.79e-01 | 3.17e-01 |
| apen | Healthy vs ESRD | 0.09 | 9.29e-01 | 9.68e-01 | 2831.0 | 1.95e-01 | 3.41e-01 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | CAD vs CAD_Diabetes | 0.36 | 7.20e-01 | 8.46e-01 | 3597.0 | 1.96e-01 | 3.41e-01 |
| CO_FirstMin_ac | CAD_Diabetes vs ESRD | -0.97 | 3.35e-01 | 5.23e-01 | 487.0 | 2.01e-01 | 3.47e-01 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Healthy vs ESRD | -1.00 | 3.21e-01 | 5.15e-01 | 2855.0 | 2.06e-01 | 3.53e-01 |
| median | Healthy vs ESRD | 1.21 | 2.30e-01 | 4.22e-01 | 3674.0 | 2.10e-01 | 3.58e-01 |
| DN_OutlierInclude_n_001_mdrmd | CAD vs ESRD | 1.62 | 1.13e-01 | 2.53e-01 | 4996.0 | 2.12e-01 | 3.58e-01 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Healthy vs CAD | -0.02 | 9.86e-01 | 9.95e-01 | 18540.0 | 2.16e-01 | 3.62e-01 |
| SB_BinaryStats_mean_longstretch1 | Healthy vs CAD | 0.97 | 3.31e-01 | 5.20e-01 | 18527.5 | 2.20e-01 | 3.67e-01 |
| PD_PeriodicityWang_th0_01 | CAD_Diabetes vs ESRD | -1.27 | 2.10e-01 | 3.98e-01 | 493.0 | 2.28e-01 | 3.77e-01 |
| DN_OutlierInclude_p_001_mdrmd | CAD vs CAD_Diabetes | 1.49 | 1.44e-01 | 3.01e-01 | 3577.0 | 2.32e-01 | 3.81e-01 |
| DN_Mean | Healthy vs ESRD | 1.25 | 2.16e-01 | 4.03e-01 | 3648.0 | 2.40e-01 | 3.87e-01 |
| mean | Healthy vs ESRD | 1.25 | 2.16e-01 | 4.03e-01 | 3648.0 | 2.40e-01 | 3.87e-01 |
| PD_PeriodicityWang_th0_01 | Healthy vs ESRD | -1.05 | 2.96e-01 | 4.87e-01 | 2874.0 | 2.44e-01 | 3.87e-01 |
| CO_trev_1_num | CAD_Diabetes vs ESRD | -0.74 | 4.62e-01 | 6.23e-01 | 496.0 | 2.44e-01 | 3.87e-01 |
| MD_hrv_classic_pnn40 | Healthy vs ESRD | 0.30 | 7.63e-01 | 8.74e-01 | 2874.5 | 2.45e-01 | 3.87e-01 |
| DN_HistogramMode_5 | CAD vs CAD_Diabetes | 1.33 | 1.91e-01 | 3.81e-01 | 3559.0 | 2.52e-01 | 3.97e-01 |
| CO_FirstMin_ac | Healthy vs CAD | -1.59 | 1.13e-01 | 2.53e-01 | 16088.5 | 2.63e-01 | 4.11e-01 |
| FC_LocalSimple_mean3_stderr | Healthy vs CAD_Diabetes | -0.88 | 3.83e-01 | 5.56e-01 | 2008.0 | 2.70e-01 | 4.19e-01 |
| DN_HistogramMode_10 | CAD vs ESRD | -1.16 | 2.52e-01 | 4.52e-01 | 3969.0 | 2.74e-01 | 4.23e-01 |
| SP_Summaries_welch_rect_area_5_1 | Healthy vs CAD_Diabetes | 1.09 | 2.85e-01 | 4.81e-01 | 2598.0 | 2.79e-01 | 4.26e-01 |
| CO_f1ecac | Healthy vs CAD_Diabetes | 0.53 | 5.97e-01 | 7.65e-01 | 2591.0 | 2.90e-01 | 4.41e-01 |
| mean_rmssd_ms | CAD_Diabetes vs ESRD | -0.91 | 3.65e-01 | 5.47e-01 | 506.0 | 2.96e-01 | 4.47e-01 |
| mean_median_hr | Healthy vs ESRD | 1.06 | 2.95e-01 | 4.87e-01 | 3591.0 | 3.16e-01 | 4.74e-01 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | CAD_Diabetes vs ESRD | -0.35 | 7.25e-01 | 8.48e-01 | 510.5 | 3.18e-01 | 4.74e-01 |
| SP_Summaries_welch_rect_centroid | Healthy vs CAD_Diabetes | -1.35 | 1.86e-01 | 3.78e-01 | 2043.5 | 3.28e-01 | 4.85e-01 |
| SB_BinaryStats_mean_longstretch1 | Healthy vs CAD_Diabetes | -0.95 | 3.51e-01 | 5.41e-01 | 2044.5 | 3.34e-01 | 4.91e-01 |
| CO_f1ecac | CAD vs CAD_Diabetes | -1.10 | 2.78e-01 | 4.80e-01 | 2802.0 | 3.39e-01 | 4.96e-01 |
| DN_HistogramMode_5 | Healthy vs ESRD | -0.87 | 3.88e-01 | 5.57e-01 | 2957.0 | 3.61e-01 | 5.24e-01 |
| DN_OutlierInclude_n_001_mdrmd | Healthy vs CAD_Diabetes | -0.48 | 6.33e-01 | 7.89e-01 | 2062.0 | 3.67e-01 | 5.25e-01 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | CAD_Diabetes vs ESRD | 0.85 | 4.00e-01 | 5.61e-01 | 669.5 | 3.67e-01 | 5.25e-01 |
| max | CAD vs CAD_Diabetes | 0.69 | 4.97e-01 | 6.58e-01 | 3470.5 | 3.69e-01 | 5.25e-01 |
| SB_BinaryStats_mean_longstretch1 | CAD_Diabetes vs ESRD | 0.43 | 6.66e-01 | 7.97e-01 | 667.5 | 3.87e-01 | 5.48e-01 |
| SB_MotifThree_quantile_hh | CAD vs CAD_Diabetes | 0.90 | 3.74e-01 | 5.47e-01 | 3445.0 | 4.08e-01 | 5.74e-01 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Healthy vs CAD | 1.96 | 5.11e-02 | 1.49e-01 | 18063.5 | 4.19e-01 | 5.85e-01 |
| DN_HistogramMode_5 | Healthy vs CAD_Diabetes | 1.12 | 2.68e-01 | 4.66e-01 | 2519.0 | 4.29e-01 | 5.97e-01 |
| DN_OutlierInclude_p_001_mdrmd | Healthy vs CAD_Diabetes | 1.09 | 2.83e-01 | 4.81e-01 | 2516.0 | 4.36e-01 | 6.02e-01 |
| mean_rmssd_ms | Healthy vs ESRD | -0.92 | 3.63e-01 | 5.47e-01 | 3510.0 | 4.49e-01 | 6.17e-01 |
| FC_LocalSimple_mean3_stderr | CAD_Diabetes vs ESRD | -0.61 | 5.42e-01 | 7.10e-01 | 531.0 | 4.55e-01 | 6.18e-01 |
| DN_OutlierInclude_p_001_mdrmd | CAD_Diabetes vs ESRD | -0.79 | 4.32e-01 | 5.96e-01 | 531.5 | 4.56e-01 | 6.18e-01 |
| SP_Summaries_welch_rect_centroid | CAD vs CAD_Diabetes | 0.17 | 8.66e-01 | 9.54e-01 | 3410.5 | 4.62e-01 | 6.18e-01 |
| MD_hrv_classic_pnn40 | CAD_Diabetes vs ESRD | 0.45 | 6.52e-01 | 7.90e-01 | 532.5 | 4.63e-01 | 6.18e-01 |
| DN_OutlierInclude_p_001_mdrmd | Healthy vs CAD | -0.66 | 5.08e-01 | 6.69e-01 | 16490.0 | 4.65e-01 | 6.18e-01 |
| MD_hrv_classic_pnn40 | CAD vs ESRD | 1.53 | 1.33e-01 | 2.82e-01 | 4768.0 | 4.67e-01 | 6.18e-01 |
| DN_HistogramMode_10 | CAD_Diabetes vs ESRD | -0.76 | 4.47e-01 | 6.07e-01 | 534.0 | 4.77e-01 | 6.28e-01 |
| DN_HistogramMode_10 | Healthy vs CAD_Diabetes | -0.55 | 5.85e-01 | 7.54e-01 | 2124.0 | 5.02e-01 | 6.58e-01 |
| SB_MotifThree_quantile_hh | CAD vs ESRD | 0.85 | 3.97e-01 | 5.61e-01 | 4734.0 | 5.15e-01 | 6.72e-01 |
| FC_LocalSimple_mean3_stderr | CAD vs ESRD | -0.30 | 7.68e-01 | 8.76e-01 | 4167.0 | 5.21e-01 | 6.73e-01 |
| CO_HistogramAMI_even_2_5 | CAD_Diabetes vs ESRD | 0.48 | 6.31e-01 | 7.89e-01 | 649.0 | 5.22e-01 | 6.73e-01 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Healthy vs CAD_Diabetes | -0.88 | 3.85e-01 | 5.56e-01 | 2134.5 | 5.26e-01 | 6.73e-01 |
| CO_trev_1_num | CAD vs CAD_Diabetes | -0.90 | 3.74e-01 | 5.47e-01 | 2929.0 | 5.47e-01 | 6.93e-01 |
| DN_Mean | CAD vs CAD_Diabetes | -0.46 | 6.49e-01 | 7.90e-01 | 2931.0 | 5.50e-01 | 6.93e-01 |
| mean | CAD vs CAD_Diabetes | -0.46 | 6.49e-01 | 7.90e-01 | 2931.0 | 5.50e-01 | 6.93e-01 |
| SB_BinaryStats_diff_longstretch0 | Healthy vs CAD | -0.78 | 4.34e-01 | 5.96e-01 | 16657.0 | 5.55e-01 | 6.96e-01 |
| median | CAD vs CAD_Diabetes | -0.48 | 6.36e-01 | 7.89e-01 | 2939.5 | 5.66e-01 | 7.05e-01 |
| mean_median_hr | CAD vs CAD_Diabetes | -0.43 | 6.68e-01 | 7.97e-01 | 2941.0 | 5.69e-01 | 7.05e-01 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Healthy vs CAD | 1.22 | 2.23e-01 | 4.14e-01 | 17809.5 | 5.76e-01 | 7.10e-01 |
| CO_HistogramAMI_even_2_5 | CAD vs ESRD | 0.12 | 9.03e-01 | 9.64e-01 | 4688.0 | 5.85e-01 | 7.17e-01 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | CAD vs CAD_Diabetes | -0.91 | 3.71e-01 | 5.47e-01 | 2951.0 | 5.88e-01 | 7.17e-01 |
| DN_HistogramMode_5 | CAD vs ESRD | -0.79 | 4.34e-01 | 5.96e-01 | 4224.0 | 6.09e-01 | 7.39e-01 |
| SB_BinaryStats_mean_longstretch1 | Healthy vs ESRD | -0.40 | 6.93e-01 | 8.23e-01 | 3425.0 | 6.17e-01 | 7.45e-01 |
| SB_BinaryStats_diff_longstretch0 | Healthy vs CAD_Diabetes | -0.46 | 6.49e-01 | 7.90e-01 | 2181.0 | 6.33e-01 | 7.60e-01 |
| PD_PeriodicityWang_th0_01 | Healthy vs CAD_Diabetes | 0.58 | 5.68e-01 | 7.40e-01 | 2426.5 | 6.55e-01 | 7.81e-01 |
| DN_HistogramMode_5 | Healthy vs CAD | -0.21 | 8.31e-01 | 9.20e-01 | 16791.0 | 6.59e-01 | 7.82e-01 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | CAD_Diabetes vs ESRD | 0.72 | 4.75e-01 | 6.33e-01 | 631.0 | 6.70e-01 | 7.91e-01 |
| CO_HistogramAMI_even_2_5 | CAD vs CAD_Diabetes | -0.50 | 6.18e-01 | 7.79e-01 | 2997.0 | 6.79e-01 | 7.98e-01 |
| mean_sdnn_ms | CAD_Diabetes vs ESRD | -0.16 | 8.71e-01 | 9.54e-01 | 629.0 | 6.87e-01 | 8.03e-01 |
| DN_OutlierInclude_p_001_mdrmd | CAD vs ESRD | 0.55 | 5.84e-01 | 7.54e-01 | 4620.5 | 6.96e-01 | 8.08e-01 |
| FC_LocalSimple_mean3_stderr | CAD vs CAD_Diabetes | 0.51 | 6.11e-01 | 7.74e-01 | 3286.0 | 6.99e-01 | 8.08e-01 |
| CO_trev_1_num | Healthy vs CAD_Diabetes | -0.72 | 4.75e-01 | 6.33e-01 | 2202.0 | 7.02e-01 | 8.08e-01 |
| PD_PeriodicityWang_th0_01 | CAD vs CAD_Diabetes | 0.03 | 9.79e-01 | 9.92e-01 | 3283.0 | 7.05e-01 | 8.08e-01 |
| sampen | CAD vs CAD_Diabetes | 0.26 | 7.96e-01 | 8.93e-01 | 3272.0 | 7.28e-01 | 8.29e-01 |
| sampen | CAD_Diabetes vs ESRD | -0.09 | 9.26e-01 | 9.68e-01 | 565.0 | 7.31e-01 | 8.29e-01 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Healthy vs ESRD | -0.13 | 8.97e-01 | 9.64e-01 | 3367.0 | 7.46e-01 | 8.42e-01 |
| CO_FirstMin_ac | CAD vs CAD_Diabetes | 0.01 | 9.95e-01 | 9.95e-01 | 3260.5 | 7.52e-01 | 8.45e-01 |
| apen | CAD vs ESRD | 1.09 | 2.83e-01 | 4.81e-01 | 4571.0 | 7.81e-01 | 8.70e-01 |
| PD_PeriodicityWang_th0_01 | Healthy vs CAD | 1.05 | 2.95e-01 | 4.87e-01 | 17540.0 | 7.82e-01 | 8.70e-01 |
| CO_FirstMin_ac | Healthy vs CAD_Diabetes | -0.78 | 4.39e-01 | 6.00e-01 | 2232.5 | 7.87e-01 | 8.71e-01 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | CAD vs ESRD | -0.12 | 9.07e-01 | 9.64e-01 | 4337.0 | 8.00e-01 | 8.79e-01 |
| MD_hrv_classic_pnn40 | Healthy vs CAD_Diabetes | -0.33 | 7.42e-01 | 8.59e-01 | 2238.5 | 8.05e-01 | 8.79e-01 |
| apen | CAD vs CAD_Diabetes | 0.14 | 8.91e-01 | 9.64e-01 | 3235.0 | 8.07e-01 | 8.79e-01 |
| CO_trev_1_num | Healthy vs CAD | 0.38 | 7.08e-01 | 8.36e-01 | 17503.0 | 8.09e-01 | 8.79e-01 |
| SB_MotifThree_quantile_hh | CAD_Diabetes vs ESRD | -0.10 | 9.24e-01 | 9.68e-01 | 575.0 | 8.22e-01 | 8.88e-01 |
| mean_sd_hr | CAD_Diabetes vs ESRD | -1.12 | 2.66e-01 | 4.66e-01 | 578.0 | 8.50e-01 | 9.14e-01 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | CAD_Diabetes vs ESRD | -0.28 | 7.83e-01 | 8.88e-01 | 579.5 | 8.60e-01 | 9.21e-01 |
| sampen | CAD vs ESRD | 0.10 | 9.21e-01 | 9.68e-01 | 4377.0 | 8.71e-01 | 9.25e-01 |
| SB_BinaryStats_mean_longstretch1 | CAD vs ESRD | -0.85 | 4.01e-01 | 5.61e-01 | 4377.5 | 8.72e-01 | 9.25e-01 |
| SB_BinaryStats_diff_longstretch0 | CAD vs CAD_Diabetes | -0.03 | 9.76e-01 | 9.92e-01 | 3094.5 | 8.82e-01 | 9.31e-01 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | CAD vs CAD_Diabetes | -0.52 | 6.09e-01 | 7.74e-01 | 3198.5 | 8.86e-01 | 9.31e-01 |
| FC_LocalSimple_mean1_tauresrat | Healthy vs CAD_Diabetes | -0.90 | 3.73e-01 | 5.47e-01 | 2279.0 | 9.23e-01 | 9.65e-01 |
| DN_HistogramMode_10 | CAD vs CAD_Diabetes | -0.01 | 9.93e-01 | 9.95e-01 | 3174.0 | 9.40e-01 | 9.73e-01 |
| SP_Summaries_welch_rect_area_5_1 | CAD vs CAD_Diabetes | -0.13 | 8.99e-01 | 9.64e-01 | 3119.0 | 9.40e-01 | 9.73e-01 |
| mean_rmssd_ms | CAD vs ESRD | -0.05 | 9.64e-01 | 9.90e-01 | 4480.0 | 9.44e-01 | 9.73e-01 |
| DN_OutlierInclude_p_001_mdrmd | Healthy vs ESRD | 0.13 | 8.95e-01 | 9.64e-01 | 3237.0 | 9.47e-01 | 9.73e-01 |
| SP_Summaries_welch_rect_area_5_1 | CAD_Diabetes vs ESRD | 0.05 | 9.62e-01 | 9.90e-01 | 590.0 | 9.62e-01 | 9.76e-01 |
| apen | CAD_Diabetes vs ESRD | 0.85 | 3.96e-01 | 5.61e-01 | 599.0 | 9.62e-01 | 9.76e-01 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Healthy vs CAD_Diabetes | -0.93 | 3.61e-01 | 5.47e-01 | 2317.0 | 9.67e-01 | 9.76e-01 |
| min | Healthy vs CAD_Diabetes | 0.32 | 7.54e-01 | 8.68e-01 | 2316.0 | 9.70e-01 | 9.76e-01 |
| SB_TransitionMatrix_3ac_sumdiagcov | Healthy vs CAD_Diabetes | -0.12 | 9.09e-01 | 9.64e-01 | 2315.5 | 9.72e-01 | 9.76e-01 |
| SP_Summaries_welch_rect_area_5_1 | CAD vs ESRD | -0.08 | 9.37e-01 | 9.71e-01 | 4437.0 | 9.80e-01 | 9.80e-01 |

</details>

### 1-min

**Summary — most significant pair per metric:**

| Metric | Most Sig. Pair | W stat | Wilcox p | Wilcox p (BH) | t-test p | Sig |
|:---|:---|---:|---:|---:|---:|:---|
| max | Healthy vs CAD | 31817.5 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| DN_Spread_Std | Healthy vs CAD | 30500.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| sd | Healthy vs CAD | 30500.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| iqr | Healthy vs CAD | 29844.5 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean_sd_hr | Healthy vs CAD | 28613.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| permen | Healthy vs CAD | 6039.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| cv | Healthy vs CAD | 28394.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| DN_Mean | Healthy vs CAD | 27359.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean | Healthy vs CAD | 27359.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| median | Healthy vs CAD | 27202.5 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| mean_median_hr | Healthy vs CAD | 27090.0 | 0.00e+00 | 0.00e+00 | 0.00e+00 | \*\*\* |
| min | CAD vs ESRD | 1809.0 | 0.00e+00 | 0.00e+00 | 7.00e-07 | \*\*\* |
| FC_LocalSimple_mean1_tauresrat | Healthy vs ESRD | 1373.0 | 0.00e+00 | 1.00e-07 | 1.10e-03 | \*\*\* |
| mean_sdnn_ms | Healthy vs ESRD | 4825.0 | 2.20e-06 | 1.55e-05 | 6.13e-02 | \*\*\* |
| SP_Summaries_welch_rect_centroid | Healthy vs CAD | 12580.0 | 6.00e-06 | 3.82e-05 | 2.02e-03 | \*\*\* |
| MD_hrv_classic_pnn40 | Healthy vs CAD | 12798.0 | 1.89e-05 | 1.17e-04 | 1.22e-04 | \*\*\* |
| sampen | Healthy vs CAD | 12805.0 | 1.95e-05 | 1.17e-04 | 3.50e-06 | \*\*\* |
| CO_f1ecac | Healthy vs CAD | 21414.0 | 6.40e-05 | 3.45e-04 | 1.43e-04 | \*\*\* |
| SB_TransitionMatrix_3ac_sumdiagcov | Healthy vs ESRD | 4494.0 | 1.75e-04 | 8.00e-04 | 1.75e-04 | \*\*\* |
| SB_BinaryStats_diff_longstretch0 | Healthy vs ESRD | 2117.0 | 3.58e-04 | 1.57e-03 | 2.00e-03 | \*\* |
| CO_FirstMin_ac | Healthy vs ESRD | 2110.5 | 5.07e-04 | 2.14e-03 | 5.69e-03 | \*\* |
| CO_trev_1_num | Healthy vs CAD | 13674.0 | 5.91e-04 | 2.41e-03 | 3.54e-03 | \*\* |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Healthy vs ESRD | 2178.0 | 6.88e-04 | 2.75e-03 | 3.20e-03 | \*\* |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Healthy vs ESRD | 2190.0 | 1.16e-03 | 4.25e-03 | 1.29e-03 | \*\* |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | CAD vs ESRD | 3096.5 | 1.65e-03 | 5.78e-03 | 2.13e-03 | \*\* |
| DN_OutlierInclude_n_001_mdrmd | Healthy vs CAD | 20480.0 | 1.93e-03 | 6.58e-03 | 5.40e-03 | \*\* |
| apen | Healthy vs CAD | 14094.0 | 2.43e-03 | 8.02e-03 | 4.74e-03 | \*\* |
| SB_MotifThree_quantile_hh | Healthy vs CAD | 14329.0 | 5.01e-03 | 1.54e-02 | 9.19e-03 | \* |
| SP_Summaries_welch_rect_area_5_1 | CAD vs ESRD | 3256.0 | 6.52e-03 | 1.91e-02 | 4.58e-03 | \* |
| FC_LocalSimple_mean3_stderr | Healthy vs CAD | 14782.0 | 1.77e-02 | 4.93e-02 | 3.38e-02 | \* |
| SB_BinaryStats_mean_longstretch1 | CAD vs CAD_Diabetes | 2326.5 | 2.28e-02 | 5.93e-02 | 5.29e-02 |  |
| CO_Embed2_Dist_tau_d_expfit_meandiff | CAD vs ESRD | 3569.0 | 4.49e-02 | 1.03e-01 | 5.86e-02 |  |
| DN_HistogramMode_10 | CAD vs ESRD | 3603.0 | 5.38e-02 | 1.20e-01 | 5.50e-02 |  |
| mean_rmssd_ms | Healthy vs CAD_Diabetes | 2789.0 | 7.31e-02 | 1.49e-01 | 7.15e-01 |  |
| CO_HistogramAMI_even_2_5 | Healthy vs CAD | 18970.0 | 9.89e-02 | 1.88e-01 | 1.63e-01 |  |
| PD_PeriodicityWang_th0_01 | CAD_Diabetes vs ESRD | 486.0 | 1.98e-01 | 3.15e-01 | 2.31e-01 |  |
| DN_HistogramMode_5 | Healthy vs ESRD | 2956.0 | 3.59e-01 | 4.90e-01 | 3.70e-01 |  |
| DN_OutlierInclude_p_001_mdrmd | CAD vs CAD_Diabetes | 3452.0 | 3.97e-01 | 5.29e-01 | 2.65e-01 |  |

Most significant pairwise comparison per metric (Wilcoxon)

<details>

<summary>

Full pairwise results (click to expand)
</summary>

| Metric | Pair | t stat | t p | t p (BH) | W stat | W p | W p (BH) |
|:---|:---|---:|---:|---:|---:|---:|---:|
| max | Healthy vs CAD | 17.98 | 0.00e+00 | 0.00e+00 | 31817.5 | 0.00e+00 | 0.00e+00 |
| DN_Spread_Std | Healthy vs CAD | 15.26 | 0.00e+00 | 0.00e+00 | 30500.0 | 0.00e+00 | 0.00e+00 |
| sd | Healthy vs CAD | 15.26 | 0.00e+00 | 0.00e+00 | 30500.0 | 0.00e+00 | 0.00e+00 |
| iqr | Healthy vs CAD | 14.13 | 0.00e+00 | 0.00e+00 | 29844.5 | 0.00e+00 | 0.00e+00 |
| mean_sd_hr | Healthy vs CAD | 9.31 | 0.00e+00 | 0.00e+00 | 28613.0 | 0.00e+00 | 0.00e+00 |
| permen | Healthy vs CAD | -10.22 | 0.00e+00 | 0.00e+00 | 6039.0 | 0.00e+00 | 0.00e+00 |
| cv | Healthy vs CAD | 11.61 | 0.00e+00 | 0.00e+00 | 28394.0 | 0.00e+00 | 0.00e+00 |
| DN_Mean | Healthy vs CAD | 10.71 | 0.00e+00 | 0.00e+00 | 27359.0 | 0.00e+00 | 0.00e+00 |
| mean | Healthy vs CAD | 10.71 | 0.00e+00 | 0.00e+00 | 27359.0 | 0.00e+00 | 0.00e+00 |
| median | Healthy vs CAD | 10.54 | 0.00e+00 | 0.00e+00 | 27202.5 | 0.00e+00 | 0.00e+00 |
| mean_median_hr | Healthy vs CAD | 10.41 | 0.00e+00 | 0.00e+00 | 27090.0 | 0.00e+00 | 0.00e+00 |
| iqr | Healthy vs ESRD | 11.65 | 0.00e+00 | 0.00e+00 | 6053.0 | 0.00e+00 | 0.00e+00 |
| cv | Healthy vs ESRD | 10.46 | 0.00e+00 | 0.00e+00 | 5897.0 | 0.00e+00 | 0.00e+00 |
| permen | Healthy vs ESRD | -10.39 | 0.00e+00 | 0.00e+00 | 625.0 | 0.00e+00 | 0.00e+00 |
| DN_Spread_Std | Healthy vs ESRD | 9.29 | 0.00e+00 | 0.00e+00 | 5799.0 | 0.00e+00 | 0.00e+00 |
| sd | Healthy vs ESRD | 9.29 | 0.00e+00 | 0.00e+00 | 5799.0 | 0.00e+00 | 0.00e+00 |
| DN_Spread_Std | Healthy vs CAD_Diabetes | 10.39 | 0.00e+00 | 0.00e+00 | 4346.0 | 0.00e+00 | 0.00e+00 |
| sd | Healthy vs CAD_Diabetes | 10.39 | 0.00e+00 | 0.00e+00 | 4346.0 | 0.00e+00 | 0.00e+00 |
| max | Healthy vs ESRD | 9.83 | 0.00e+00 | 0.00e+00 | 5750.5 | 0.00e+00 | 0.00e+00 |
| mean_sd_hr | Healthy vs CAD_Diabetes | 12.03 | 0.00e+00 | 0.00e+00 | 4323.0 | 0.00e+00 | 0.00e+00 |
| max | Healthy vs CAD_Diabetes | 9.95 | 0.00e+00 | 0.00e+00 | 4275.0 | 0.00e+00 | 0.00e+00 |
| iqr | Healthy vs CAD_Diabetes | 10.37 | 0.00e+00 | 0.00e+00 | 4237.5 | 0.00e+00 | 0.00e+00 |
| mean_sd_hr | Healthy vs ESRD | 6.78 | 0.00e+00 | 1.00e-07 | 5628.0 | 0.00e+00 | 0.00e+00 |
| permen | Healthy vs CAD_Diabetes | -8.91 | 0.00e+00 | 0.00e+00 | 463.0 | 0.00e+00 | 0.00e+00 |
| cv | Healthy vs CAD_Diabetes | 8.94 | 0.00e+00 | 0.00e+00 | 4147.0 | 0.00e+00 | 0.00e+00 |
| min | CAD vs ESRD | -5.70 | 7.00e-07 | 5.90e-06 | 1809.0 | 0.00e+00 | 0.00e+00 |
| FC_LocalSimple_mean1_tauresrat | Healthy vs ESRD | -3.52 | 1.10e-03 | 5.58e-03 | 1373.0 | 0.00e+00 | 1.00e-07 |
| median | CAD vs ESRD | -5.28 | 2.40e-06 | 1.95e-05 | 2160.0 | 2.00e-07 | 1.50e-06 |
| mean_median_hr | CAD vs ESRD | -5.28 | 2.40e-06 | 1.95e-05 | 2180.0 | 2.00e-07 | 1.80e-06 |
| DN_Mean | CAD vs ESRD | -5.17 | 3.50e-06 | 2.60e-05 | 2217.0 | 4.00e-07 | 2.60e-06 |
| mean | CAD vs ESRD | -5.17 | 3.50e-06 | 2.60e-05 | 2217.0 | 4.00e-07 | 2.60e-06 |
| mean_sdnn_ms | Healthy vs ESRD | 1.92 | 6.13e-02 | 1.49e-01 | 4825.0 | 2.20e-06 | 1.55e-05 |
| cv | CAD vs ESRD | 4.08 | 1.53e-04 | 8.69e-04 | 6513.0 | 2.50e-06 | 1.71e-05 |
| permen | CAD vs ESRD | -3.48 | 9.54e-04 | 4.94e-03 | 2394.0 | 2.80e-06 | 1.86e-05 |
| FC_LocalSimple_mean1_tauresrat | CAD vs ESRD | -3.02 | 4.39e-03 | 1.67e-02 | 2458.0 | 5.60e-06 | 3.64e-05 |
| SP_Summaries_welch_rect_centroid | Healthy vs CAD | -3.11 | 2.02e-03 | 9.42e-03 | 12580.0 | 6.00e-06 | 3.82e-05 |
| MD_hrv_classic_pnn40 | Healthy vs CAD | -3.89 | 1.22e-04 | 7.30e-04 | 12798.0 | 1.89e-05 | 1.17e-04 |
| sampen | Healthy vs CAD | -4.71 | 3.50e-06 | 2.60e-05 | 12805.0 | 1.95e-05 | 1.17e-04 |
| iqr | CAD vs ESRD | 3.13 | 2.79e-03 | 1.22e-02 | 6309.0 | 2.19e-05 | 1.28e-04 |
| min | Healthy vs CAD | 3.70 | 2.50e-04 | 1.36e-03 | 21414.5 | 6.39e-05 | 3.45e-04 |
| CO_f1ecac | Healthy vs CAD | 3.85 | 1.43e-04 | 8.34e-04 | 21414.0 | 6.40e-05 | 3.45e-04 |
| DN_Mean | Healthy vs CAD_Diabetes | 4.45 | 7.60e-05 | 5.10e-04 | 3381.0 | 6.63e-05 | 3.45e-04 |
| mean | Healthy vs CAD_Diabetes | 4.45 | 7.60e-05 | 5.10e-04 | 3381.0 | 6.63e-05 | 3.45e-04 |
| median | Healthy vs CAD_Diabetes | 4.43 | 7.99e-05 | 5.10e-04 | 3380.0 | 6.74e-05 | 3.45e-04 |
| min | Healthy vs ESRD | -3.66 | 5.61e-04 | 2.98e-03 | 1943.0 | 6.82e-05 | 3.45e-04 |
| mean_median_hr | Healthy vs CAD_Diabetes | 4.40 | 8.66e-05 | 5.34e-04 | 3354.0 | 1.01e-04 | 4.99e-04 |
| CO_f1ecac | Healthy vs ESRD | 3.37 | 1.35e-03 | 6.56e-03 | 4542.0 | 1.05e-04 | 5.07e-04 |
| FC_LocalSimple_mean1_tauresrat | Healthy vs CAD | -4.41 | 1.38e-05 | 9.80e-05 | 13265.5 | 1.29e-04 | 6.13e-04 |
| mean_sdnn_ms | Healthy vs CAD | 0.34 | 7.33e-01 | 7.96e-01 | 21210.0 | 1.44e-04 | 6.69e-04 |
| SB_TransitionMatrix_3ac_sumdiagcov | Healthy vs ESRD | 3.97 | 1.75e-04 | 9.76e-04 | 4494.0 | 1.75e-04 | 8.00e-04 |
| mean_sdnn_ms | Healthy vs CAD_Diabetes | 2.67 | 1.13e-02 | 3.66e-02 | 3298.0 | 2.32e-04 | 1.04e-03 |
| SB_BinaryStats_diff_longstretch0 | Healthy vs ESRD | -3.27 | 2.00e-03 | 9.42e-03 | 2117.0 | 3.58e-04 | 1.57e-03 |
| SP_Summaries_welch_rect_centroid | Healthy vs ESRD | -2.78 | 7.45e-03 | 2.54e-02 | 2099.5 | 3.82e-04 | 1.64e-03 |
| CO_FirstMin_ac | Healthy vs ESRD | -2.88 | 5.69e-03 | 1.96e-02 | 2110.5 | 5.07e-04 | 2.14e-03 |
| SB_BinaryStats_diff_longstretch0 | CAD vs ESRD | -3.07 | 3.57e-03 | 1.45e-02 | 2975.0 | 5.64e-04 | 2.34e-03 |
| CO_trev_1_num | Healthy vs CAD | -2.94 | 3.54e-03 | 1.45e-02 | 13674.0 | 5.91e-04 | 2.41e-03 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Healthy vs ESRD | -3.10 | 3.20e-03 | 1.38e-02 | 2178.0 | 6.88e-04 | 2.75e-03 |
| mean_sdnn_ms | CAD vs ESRD | 1.60 | 1.14e-01 | 2.29e-01 | 5916.0 | 8.15e-04 | 3.20e-03 |
| DN_Spread_Std | CAD vs ESRD | 1.81 | 7.61e-02 | 1.74e-01 | 5897.0 | 9.52e-04 | 3.62e-03 |
| sd | CAD vs ESRD | 1.81 | 7.61e-02 | 1.74e-01 | 5897.0 | 9.52e-04 | 3.62e-03 |
| CO_trev_1_num | Healthy vs ESRD | -0.09 | 9.32e-01 | 9.35e-01 | 2179.0 | 1.08e-03 | 4.04e-03 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Healthy vs ESRD | -3.38 | 1.29e-03 | 6.39e-03 | 2190.0 | 1.16e-03 | 4.25e-03 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | CAD vs ESRD | -2.57 | 1.33e-02 | 4.22e-02 | 3092.0 | 1.22e-03 | 4.41e-03 |
| mean_sd_hr | CAD vs CAD_Diabetes | 4.21 | 8.05e-05 | 5.10e-04 | 4281.0 | 1.63e-03 | 5.78e-03 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | CAD vs ESRD | -3.21 | 2.13e-03 | 9.73e-03 | 3096.5 | 1.65e-03 | 5.78e-03 |
| SB_TransitionMatrix_3ac_sumdiagcov | Healthy vs CAD | 3.02 | 2.74e-03 | 1.22e-02 | 20480.0 | 1.83e-03 | 6.31e-03 |
| DN_OutlierInclude_n_001_mdrmd | Healthy vs CAD | 2.80 | 5.40e-03 | 1.92e-02 | 20480.0 | 1.93e-03 | 6.58e-03 |
| FC_LocalSimple_mean1_tauresrat | CAD_Diabetes vs ESRD | -2.62 | 1.15e-02 | 3.69e-02 | 335.0 | 2.01e-03 | 6.75e-03 |
| apen | Healthy vs CAD | -2.84 | 4.74e-03 | 1.72e-02 | 14094.0 | 2.43e-03 | 8.02e-03 |
| apen | CAD vs ESRD | 2.92 | 5.46e-03 | 1.92e-02 | 5736.0 | 3.31e-03 | 1.08e-02 |
| min | CAD_Diabetes vs ESRD | -2.93 | 4.73e-03 | 1.72e-02 | 350.5 | 3.69e-03 | 1.19e-02 |
| mean_sd_hr | CAD vs ESRD | 1.61 | 1.13e-01 | 2.29e-01 | 5711.0 | 3.98e-03 | 1.26e-02 |
| mean_median_hr | CAD_Diabetes vs ESRD | -3.06 | 3.36e-03 | 1.42e-02 | 361.0 | 4.96e-03 | 1.54e-02 |
| SB_MotifThree_quantile_hh | Healthy vs CAD | -2.62 | 9.19e-03 | 3.04e-02 | 14329.0 | 5.01e-03 | 1.54e-02 |
| DN_Mean | CAD_Diabetes vs ESRD | -2.97 | 4.37e-03 | 1.67e-02 | 365.0 | 5.79e-03 | 1.71e-02 |
| mean | CAD_Diabetes vs ESRD | -2.97 | 4.37e-03 | 1.67e-02 | 365.0 | 5.79e-03 | 1.71e-02 |
| median | CAD_Diabetes vs ESRD | -3.01 | 3.89e-03 | 1.56e-02 | 365.0 | 5.79e-03 | 1.71e-02 |
| SP_Summaries_welch_rect_area_5_1 | CAD vs ESRD | -2.95 | 4.58e-03 | 1.71e-02 | 3256.0 | 6.52e-03 | 1.91e-02 |
| mean_sdnn_ms | CAD vs CAD_Diabetes | 2.21 | 3.13e-02 | 9.25e-02 | 4044.0 | 1.27e-02 | 3.66e-02 |
| SB_MotifThree_quantile_hh | CAD vs ESRD | 2.55 | 1.38e-02 | 4.25e-02 | 5532.0 | 1.35e-02 | 3.83e-02 |
| CO_trev_1_num | Healthy vs CAD_Diabetes | -2.73 | 8.76e-03 | 2.94e-02 | 1640.0 | 1.36e-02 | 3.83e-02 |
| FC_LocalSimple_mean3_stderr | Healthy vs CAD | -2.13 | 3.38e-02 | 9.44e-02 | 14782.0 | 1.77e-02 | 4.93e-02 |
| DN_OutlierInclude_n_001_mdrmd | CAD vs CAD_Diabetes | -1.76 | 8.78e-02 | 1.92e-01 | 2297.0 | 1.83e-02 | 5.03e-02 |
| CO_FirstMin_ac | CAD vs ESRD | -1.15 | 2.55e-01 | 3.85e-01 | 3425.0 | 1.95e-02 | 5.30e-02 |
| SB_TransitionMatrix_3ac_sumdiagcov | CAD vs ESRD | 2.16 | 3.48e-02 | 9.56e-02 | 5449.0 | 2.20e-02 | 5.90e-02 |
| permen | CAD vs CAD_Diabetes | -2.06 | 4.57e-02 | 1.20e-01 | 2326.0 | 2.27e-02 | 5.93e-02 |
| SB_BinaryStats_mean_longstretch1 | CAD vs CAD_Diabetes | -2.01 | 5.29e-02 | 1.34e-01 | 2326.5 | 2.28e-02 | 5.93e-02 |
| cv | CAD vs CAD_Diabetes | 2.23 | 3.19e-02 | 9.26e-02 | 3966.0 | 2.29e-02 | 5.93e-02 |
| min | CAD vs CAD_Diabetes | -1.71 | 9.57e-02 | 2.06e-01 | 2356.5 | 2.83e-02 | 7.24e-02 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | CAD vs ESRD | -2.20 | 3.21e-02 | 9.26e-02 | 3500.5 | 2.93e-02 | 7.42e-02 |
| iqr | CAD_Diabetes vs ESRD | 1.18 | 2.44e-01 | 3.81e-01 | 775.0 | 3.12e-02 | 7.83e-02 |
| MD_hrv_classic_pnn40 | CAD vs ESRD | 2.57 | 1.36e-02 | 4.24e-02 | 5388.0 | 3.21e-02 | 7.96e-02 |
| cv | CAD_Diabetes vs ESRD | 1.51 | 1.36e-01 | 2.58e-01 | 771.0 | 3.53e-02 | 8.65e-02 |
| permen | CAD_Diabetes vs ESRD | -0.97 | 3.35e-01 | 4.77e-01 | 419.0 | 3.63e-02 | 8.82e-02 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Healthy vs CAD | -2.10 | 3.64e-02 | 9.88e-02 | 15100.5 | 3.81e-02 | 9.15e-02 |
| max | CAD_Diabetes vs ESRD | -1.57 | 1.21e-01 | 2.38e-01 | 421.0 | 3.86e-02 | 9.16e-02 |
| CO_FirstMin_ac | Healthy vs CAD | -2.05 | 4.10e-02 | 1.10e-01 | 15156.5 | 4.42e-02 | 1.03e-01 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | CAD_Diabetes vs ESRD | -2.25 | 2.81e-02 | 8.55e-02 | 428.0 | 4.47e-02 | 1.03e-01 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | CAD vs ESRD | -1.94 | 5.86e-02 | 1.45e-01 | 3569.0 | 4.49e-02 | 1.03e-01 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Healthy vs ESRD | -2.03 | 4.80e-02 | 1.24e-01 | 2605.0 | 4.78e-02 | 1.09e-01 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | CAD vs CAD_Diabetes | -1.44 | 1.59e-01 | 2.83e-01 | 2460.5 | 5.19e-02 | 1.17e-01 |
| DN_HistogramMode_10 | CAD vs ESRD | -1.96 | 5.50e-02 | 1.38e-01 | 3603.0 | 5.38e-02 | 1.20e-01 |
| SP_Summaries_welch_rect_area_5_1 | Healthy vs CAD | 1.86 | 6.37e-02 | 1.53e-01 | 19252.0 | 5.47e-02 | 1.21e-01 |
| SB_MotifThree_quantile_hh | CAD vs CAD_Diabetes | 2.00 | 5.26e-02 | 1.34e-01 | 3829.0 | 5.81e-02 | 1.27e-01 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Healthy vs CAD | 2.01 | 4.58e-02 | 1.20e-01 | 19158.5 | 6.05e-02 | 1.31e-01 |
| SB_TransitionMatrix_3ac_sumdiagcov | CAD_Diabetes vs ESRD | 2.26 | 2.85e-02 | 8.55e-02 | 750.5 | 6.32e-02 | 1.35e-01 |
| SP_Summaries_welch_rect_area_5_1 | Healthy vs ESRD | -1.81 | 7.58e-02 | 1.74e-01 | 2647.0 | 6.40e-02 | 1.35e-01 |
| DN_Spread_Std | CAD vs CAD_Diabetes | 1.78 | 8.35e-02 | 1.85e-01 | 3812.0 | 6.46e-02 | 1.35e-01 |
| sd | CAD vs CAD_Diabetes | 1.78 | 8.35e-02 | 1.85e-01 | 3812.0 | 6.46e-02 | 1.35e-01 |
| CO_FirstMin_ac | CAD_Diabetes vs ESRD | -0.43 | 6.73e-01 | 7.65e-01 | 441.0 | 6.79e-02 | 1.41e-01 |
| mean_rmssd_ms | Healthy vs CAD_Diabetes | 0.37 | 7.15e-01 | 7.84e-01 | 2789.0 | 7.31e-02 | 1.49e-01 |
| SB_BinaryStats_mean_longstretch1 | Healthy vs CAD | 1.57 | 1.17e-01 | 2.32e-01 | 19117.5 | 7.32e-02 | 1.49e-01 |
| SP_Summaries_welch_rect_area_5_1 | CAD vs CAD_Diabetes | -1.83 | 7.58e-02 | 1.74e-01 | 2512.0 | 7.81e-02 | 1.58e-01 |
| FC_LocalSimple_mean3_stderr | CAD vs ESRD | 1.92 | 5.98e-02 | 1.47e-01 | 5199.0 | 8.70e-02 | 1.74e-01 |
| CO_f1ecac | CAD_Diabetes vs ESRD | 1.47 | 1.47e-01 | 2.72e-01 | 738.0 | 8.83e-02 | 1.74e-01 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Healthy vs ESRD | -1.79 | 7.85e-02 | 1.77e-01 | 2713.0 | 8.84e-02 | 1.74e-01 |
| CO_f1ecac | CAD vs ESRD | 1.24 | 2.20e-01 | 3.56e-01 | 5188.0 | 9.17e-02 | 1.79e-01 |
| DN_OutlierInclude_n_001_mdrmd | Healthy vs ESRD | 2.20 | 3.30e-02 | 9.41e-02 | 3808.0 | 9.72e-02 | 1.88e-01 |
| CO_HistogramAMI_even_2_5 | Healthy vs CAD | 1.40 | 1.63e-01 | 2.89e-01 | 18970.0 | 9.89e-02 | 1.88e-01 |
| apen | Healthy vs ESRD | 1.87 | 6.86e-02 | 1.63e-01 | 3805.0 | 9.91e-02 | 1.88e-01 |
| sampen | Healthy vs CAD_Diabetes | -1.68 | 1.02e-01 | 2.15e-01 | 1865.0 | 1.03e-01 | 1.93e-01 |
| DN_HistogramMode_10 | CAD vs CAD_Diabetes | -1.62 | 1.15e-01 | 2.29e-01 | 2565.0 | 1.06e-01 | 1.99e-01 |
| max | CAD vs CAD_Diabetes | 0.95 | 3.49e-01 | 4.85e-01 | 3724.5 | 1.09e-01 | 2.01e-01 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | CAD vs CAD_Diabetes | -1.54 | 1.32e-01 | 2.53e-01 | 2577.0 | 1.14e-01 | 2.09e-01 |
| CO_HistogramAMI_even_2_5 | CAD vs CAD_Diabetes | -1.45 | 1.57e-01 | 2.81e-01 | 2592.0 | 1.24e-01 | 2.26e-01 |
| SB_BinaryStats_diff_longstretch0 | CAD_Diabetes vs ESRD | -0.93 | 3.57e-01 | 4.94e-01 | 469.0 | 1.28e-01 | 2.31e-01 |
| sampen | CAD vs ESRD | 1.54 | 1.31e-01 | 2.52e-01 | 5108.0 | 1.33e-01 | 2.38e-01 |
| DN_OutlierInclude_n_001_mdrmd | CAD_Diabetes vs ESRD | 2.17 | 3.40e-02 | 9.44e-02 | 719.0 | 1.40e-01 | 2.49e-01 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Healthy vs CAD_Diabetes | -1.63 | 1.12e-01 | 2.29e-01 | 1912.0 | 1.45e-01 | 2.55e-01 |
| iqr | CAD vs CAD_Diabetes | 1.64 | 1.09e-01 | 2.29e-01 | 3671.0 | 1.45e-01 | 2.55e-01 |
| mean_rmssd_ms | CAD vs CAD_Diabetes | 1.28 | 2.06e-01 | 3.47e-01 | 3656.0 | 1.57e-01 | 2.74e-01 |
| DN_HistogramMode_10 | Healthy vs ESRD | -1.48 | 1.43e-01 | 2.68e-01 | 2796.0 | 1.61e-01 | 2.78e-01 |
| SP_Summaries_welch_rect_centroid | CAD_Diabetes vs ESRD | -0.78 | 4.39e-01 | 5.78e-01 | 479.0 | 1.68e-01 | 2.88e-01 |
| SB_BinaryStats_mean_longstretch1 | Healthy vs CAD_Diabetes | -1.30 | 2.02e-01 | 3.43e-01 | 1938.0 | 1.73e-01 | 2.90e-01 |
| mean_rmssd_ms | Healthy vs CAD | -1.53 | 1.27e-01 | 2.48e-01 | 18663.0 | 1.75e-01 | 2.90e-01 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Healthy vs CAD_Diabetes | -1.69 | 1.01e-01 | 2.14e-01 | 1956.5 | 1.75e-01 | 2.90e-01 |
| DN_Spread_Std | CAD_Diabetes vs ESRD | 0.23 | 8.18e-01 | 8.60e-01 | 709.0 | 1.75e-01 | 2.90e-01 |
| sd | CAD_Diabetes vs ESRD | 0.23 | 8.18e-01 | 8.60e-01 | 709.0 | 1.75e-01 | 2.90e-01 |
| CO_f1ecac | Healthy vs CAD_Diabetes | 1.16 | 2.52e-01 | 3.83e-01 | 2662.0 | 1.86e-01 | 3.04e-01 |
| CO_HistogramAMI_even_2_5 | CAD vs ESRD | -1.46 | 1.51e-01 | 2.75e-01 | 3869.0 | 1.86e-01 | 3.04e-01 |
| SB_BinaryStats_mean_longstretch1 | CAD_Diabetes vs ESRD | 0.66 | 5.09e-01 | 6.38e-01 | 704.5 | 1.92e-01 | 3.10e-01 |
| apen | CAD vs CAD_Diabetes | 1.36 | 1.83e-01 | 3.20e-01 | 3614.0 | 1.94e-01 | 3.12e-01 |
| PD_PeriodicityWang_th0_01 | CAD_Diabetes vs ESRD | -1.21 | 2.31e-01 | 3.68e-01 | 486.0 | 1.98e-01 | 3.15e-01 |
| FC_LocalSimple_mean3_stderr | CAD vs CAD_Diabetes | 1.29 | 2.07e-01 | 3.47e-01 | 3609.0 | 1.99e-01 | 3.15e-01 |
| apen | CAD_Diabetes vs ESRD | 1.44 | 1.53e-01 | 2.77e-01 | 699.0 | 2.17e-01 | 3.40e-01 |
| median | Healthy vs ESRD | 1.20 | 2.35e-01 | 3.73e-01 | 3658.0 | 2.28e-01 | 3.57e-01 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | CAD vs CAD_Diabetes | -1.25 | 2.19e-01 | 3.56e-01 | 2740.0 | 2.34e-01 | 3.61e-01 |
| SP_Summaries_welch_rect_centroid | Healthy vs CAD_Diabetes | -1.17 | 2.51e-01 | 3.83e-01 | 1990.0 | 2.35e-01 | 3.61e-01 |
| SP_Summaries_welch_rect_centroid | CAD vs ESRD | -0.95 | 3.45e-01 | 4.83e-01 | 3931.0 | 2.36e-01 | 3.61e-01 |
| PD_PeriodicityWang_th0_01 | CAD vs CAD_Diabetes | 0.76 | 4.51e-01 | 5.84e-01 | 3571.5 | 2.38e-01 | 3.62e-01 |
| mean_rmssd_ms | CAD_Diabetes vs ESRD | -1.03 | 3.09e-01 | 4.43e-01 | 495.0 | 2.40e-01 | 3.62e-01 |
| DN_Mean | Healthy vs ESRD | 1.25 | 2.16e-01 | 3.54e-01 | 3645.0 | 2.44e-01 | 3.64e-01 |
| mean | Healthy vs ESRD | 1.25 | 2.16e-01 | 3.54e-01 | 3645.0 | 2.44e-01 | 3.64e-01 |
| DN_HistogramMode_10 | Healthy vs CAD_Diabetes | -1.21 | 2.30e-01 | 3.68e-01 | 1995.0 | 2.50e-01 | 3.70e-01 |
| max | CAD vs ESRD | -1.19 | 2.38e-01 | 3.74e-01 | 3946.0 | 2.52e-01 | 3.71e-01 |
| MD_hrv_classic_pnn40 | Healthy vs CAD_Diabetes | -0.70 | 4.90e-01 | 6.24e-01 | 2002.5 | 2.62e-01 | 3.82e-01 |
| CO_trev_1_num | CAD vs ESRD | 0.39 | 7.01e-01 | 7.72e-01 | 3967.0 | 2.72e-01 | 3.96e-01 |
| SB_MotifThree_quantile_hh | Healthy vs ESRD | 1.27 | 2.11e-01 | 3.51e-01 | 3621.0 | 2.75e-01 | 3.96e-01 |
| MD_hrv_classic_pnn40 | CAD vs CAD_Diabetes | 1.10 | 2.80e-01 | 4.17e-01 | 3533.0 | 2.83e-01 | 4.07e-01 |
| SB_BinaryStats_diff_longstretch0 | Healthy vs CAD_Diabetes | -1.48 | 1.50e-01 | 2.75e-01 | 2042.5 | 3.13e-01 | 4.44e-01 |
| SB_BinaryStats_diff_longstretch0 | CAD vs CAD_Diabetes | -1.31 | 2.00e-01 | 3.43e-01 | 2793.5 | 3.14e-01 | 4.44e-01 |
| mean_median_hr | Healthy vs ESRD | 1.06 | 2.91e-01 | 4.27e-01 | 3590.0 | 3.18e-01 | 4.45e-01 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | CAD_Diabetes vs ESRD | -0.68 | 5.01e-01 | 6.32e-01 | 511.5 | 3.18e-01 | 4.45e-01 |
| DN_OutlierInclude_n_001_mdrmd | Healthy vs CAD_Diabetes | -0.53 | 5.97e-01 | 7.17e-01 | 2045.0 | 3.35e-01 | 4.65e-01 |
| PD_PeriodicityWang_th0_01 | Healthy vs CAD_Diabetes | 1.07 | 2.92e-01 | 4.27e-01 | 2563.5 | 3.39e-01 | 4.69e-01 |
| SP_Summaries_welch_rect_centroid | CAD vs CAD_Diabetes | 0.18 | 8.56e-01 | 8.87e-01 | 3483.0 | 3.48e-01 | 4.78e-01 |
| DN_HistogramMode_5 | Healthy vs ESRD | -0.90 | 3.70e-01 | 5.08e-01 | 2956.0 | 3.59e-01 | 4.90e-01 |
| DN_HistogramMode_5 | CAD vs ESRD | -1.03 | 3.05e-01 | 4.41e-01 | 4050.0 | 3.64e-01 | 4.94e-01 |
| SP_Summaries_welch_rect_area_5_1 | Healthy vs CAD_Diabetes | -0.81 | 4.23e-01 | 5.61e-01 | 2062.0 | 3.67e-01 | 4.95e-01 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | Healthy vs CAD_Diabetes | -0.35 | 7.32e-01 | 7.96e-01 | 2082.5 | 3.95e-01 | 5.29e-01 |
| DN_OutlierInclude_p_001_mdrmd | CAD vs CAD_Diabetes | 1.13 | 2.65e-01 | 3.98e-01 | 3452.0 | 3.97e-01 | 5.29e-01 |
| FC_LocalSimple_mean1_tauresrat | CAD vs CAD_Diabetes | -0.46 | 6.47e-01 | 7.56e-01 | 3439.0 | 4.17e-01 | 5.50e-01 |
| MD_hrv_classic_pnn40 | CAD_Diabetes vs ESRD | 1.70 | 9.38e-02 | 2.04e-01 | 663.0 | 4.18e-01 | 5.50e-01 |
| CO_f1ecac | CAD vs CAD_Diabetes | -0.74 | 4.63e-01 | 5.96e-01 | 2860.0 | 4.27e-01 | 5.59e-01 |
| SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1 | CAD_Diabetes vs ESRD | -0.96 | 3.41e-01 | 4.83e-01 | 533.0 | 4.52e-01 | 5.89e-01 |
| SB_TransitionMatrix_3ac_sumdiagcov | CAD vs CAD_Diabetes | -1.18 | 2.49e-01 | 3.83e-01 | 2884.0 | 4.65e-01 | 6.02e-01 |
| SB_TransitionMatrix_3ac_sumdiagcov | Healthy vs CAD_Diabetes | 0.09 | 9.30e-01 | 9.35e-01 | 2496.5 | 4.77e-01 | 6.12e-01 |
| DN_OutlierInclude_n_001_mdrmd | CAD vs ESRD | 1.31 | 1.97e-01 | 3.41e-01 | 4760.0 | 4.78e-01 | 6.12e-01 |
| PD_PeriodicityWang_th0_01 | Healthy vs ESRD | -0.50 | 6.21e-01 | 7.36e-01 | 3028.5 | 4.85e-01 | 6.16e-01 |
| SB_BinaryStats_mean_longstretch1 | Healthy vs ESRD | -0.40 | 6.91e-01 | 7.72e-01 | 3489.0 | 4.88e-01 | 6.16e-01 |
| DN_HistogramMode_5 | CAD vs CAD_Diabetes | -0.58 | 5.65e-01 | 6.92e-01 | 2897.0 | 4.89e-01 | 6.16e-01 |
| DN_OutlierInclude_p_001_mdrmd | Healthy vs CAD_Diabetes | 0.90 | 3.73e-01 | 5.10e-01 | 2490.0 | 4.95e-01 | 6.20e-01 |
| CO_HistogramAMI_even_2_5 | Healthy vs CAD_Diabetes | -0.77 | 4.48e-01 | 5.84e-01 | 2123.0 | 4.99e-01 | 6.22e-01 |
| FC_LocalSimple_mean1_tauresrat | Healthy vs CAD_Diabetes | -1.65 | 1.10e-01 | 2.29e-01 | 2126.0 | 5.07e-01 | 6.28e-01 |
| PD_PeriodicityWang_th0_01 | CAD vs ESRD | -0.84 | 4.03e-01 | 5.43e-01 | 4172.5 | 5.30e-01 | 6.53e-01 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | CAD vs CAD_Diabetes | 0.77 | 4.43e-01 | 5.81e-01 | 3369.5 | 5.34e-01 | 6.55e-01 |
| SP_Summaries_welch_rect_area_5_1 | CAD_Diabetes vs ESRD | -0.66 | 5.13e-01 | 6.39e-01 | 542.0 | 5.38e-01 | 6.56e-01 |
| mean_rmssd_ms | Healthy vs ESRD | -0.96 | 3.43e-01 | 4.83e-01 | 3462.0 | 5.41e-01 | 6.56e-01 |
| sampen | CAD_Diabetes vs ESRD | 0.81 | 4.20e-01 | 5.60e-01 | 645.0 | 5.53e-01 | 6.56e-01 |
| DN_Mean | CAD vs CAD_Diabetes | -0.45 | 6.56e-01 | 7.56e-01 | 2933.0 | 5.54e-01 | 6.56e-01 |
| mean | CAD vs CAD_Diabetes | -0.45 | 6.56e-01 | 7.56e-01 | 2933.0 | 5.54e-01 | 6.56e-01 |
| CO_FirstMin_ac | Healthy vs CAD_Diabetes | -1.05 | 3.03e-01 | 4.41e-01 | 2146.0 | 5.55e-01 | 6.56e-01 |
| median | CAD vs CAD_Diabetes | -0.46 | 6.51e-01 | 7.56e-01 | 2933.5 | 5.55e-01 | 6.56e-01 |
| IN_AutoMutualInfoStats_40_gaussian_fmmi | Healthy vs CAD_Diabetes | -0.39 | 6.97e-01 | 7.72e-01 | 2150.5 | 5.65e-01 | 6.60e-01 |
| sampen | Healthy vs ESRD | -0.41 | 6.83e-01 | 7.70e-01 | 3070.0 | 5.67e-01 | 6.60e-01 |
| mean_median_hr | CAD vs CAD_Diabetes | -0.42 | 6.75e-01 | 7.65e-01 | 2940.0 | 5.67e-01 | 6.60e-01 |
| sampen | CAD vs CAD_Diabetes | 0.63 | 5.35e-01 | 6.62e-01 | 3349.0 | 5.75e-01 | 6.65e-01 |
| FC_LocalSimple_mean3_stderr | Healthy vs ESRD | 0.85 | 3.98e-01 | 5.40e-01 | 3444.0 | 5.78e-01 | 6.65e-01 |
| DN_OutlierInclude_p_001_mdrmd | CAD_Diabetes vs ESRD | -0.56 | 5.77e-01 | 7.04e-01 | 550.0 | 6.02e-01 | 6.90e-01 |
| CO_trev_1_num | CAD_Diabetes vs ESRD | 0.53 | 5.97e-01 | 7.17e-01 | 552.0 | 6.19e-01 | 7.05e-01 |
| DN_OutlierInclude_p_001_mdrmd | Healthy vs CAD | -0.38 | 7.01e-01 | 7.72e-01 | 16764.5 | 6.40e-01 | 7.26e-01 |
| CO_FirstMin_ac | CAD vs CAD_Diabetes | -0.21 | 8.33e-01 | 8.67e-01 | 3312.5 | 6.46e-01 | 7.29e-01 |
| CO_trev_1_num | CAD vs CAD_Diabetes | -0.68 | 5.02e-01 | 6.32e-01 | 2982.0 | 6.49e-01 | 7.29e-01 |
| SB_MotifThree_quantile_hh | Healthy vs CAD_Diabetes | 0.70 | 4.87e-01 | 6.23e-01 | 2426.0 | 6.56e-01 | 7.33e-01 |
| DN_HistogramMode_5 | Healthy vs CAD_Diabetes | -0.50 | 6.23e-01 | 7.36e-01 | 2188.0 | 6.64e-01 | 7.39e-01 |
| CO_HistogramAMI_even_2_5 | Healthy vs ESRD | -0.83 | 4.13e-01 | 5.54e-01 | 3124.0 | 6.83e-01 | 7.56e-01 |
| SB_MotifThree_quantile_hh | CAD_Diabetes vs ESRD | 0.44 | 6.64e-01 | 7.61e-01 | 626.0 | 7.13e-01 | 7.86e-01 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | CAD_Diabetes vs ESRD | -0.25 | 8.01e-01 | 8.53e-01 | 565.0 | 7.31e-01 | 8.02e-01 |
| SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1 | Healthy vs CAD | -1.30 | 1.96e-01 | 3.41e-01 | 16958.0 | 7.66e-01 | 8.36e-01 |
| FC_LocalSimple_mean3_stderr | CAD_Diabetes vs ESRD | 0.41 | 6.86e-01 | 7.70e-01 | 616.0 | 8.04e-01 | 8.72e-01 |
| mean_sdnn_ms | CAD_Diabetes vs ESRD | -0.26 | 7.93e-01 | 8.49e-01 | 615.0 | 8.13e-01 | 8.78e-01 |
| SB_BinaryStats_mean_longstretch1 | CAD vs ESRD | -1.08 | 2.86e-01 | 4.24e-01 | 4347.5 | 8.19e-01 | 8.79e-01 |
| DN_OutlierInclude_p_001_mdrmd | CAD vs ESRD | 0.49 | 6.26e-01 | 7.36e-01 | 4548.0 | 8.21e-01 | 8.79e-01 |
| mean_sd_hr | CAD_Diabetes vs ESRD | -1.16 | 2.52e-01 | 3.83e-01 | 579.0 | 8.59e-01 | 9.15e-01 |
| MD_hrv_classic_pnn40 | Healthy vs ESRD | 1.51 | 1.39e-01 | 2.62e-01 | 3316.0 | 8.65e-01 | 9.17e-01 |
| CO_HistogramAMI_even_2_5 | CAD_Diabetes vs ESRD | -0.08 | 9.33e-01 | 9.35e-01 | 609.0 | 8.68e-01 | 9.17e-01 |
| DN_HistogramMode_10 | CAD_Diabetes vs ESRD | -0.12 | 9.06e-01 | 9.30e-01 | 582.0 | 8.87e-01 | 9.32e-01 |
| DN_HistogramMode_5 | Healthy vs CAD | 0.09 | 9.28e-01 | 9.35e-01 | 17360.0 | 9.17e-01 | 9.58e-01 |
| mean_rmssd_ms | CAD vs ESRD | -0.10 | 9.23e-01 | 9.35e-01 | 4404.0 | 9.20e-01 | 9.58e-01 |
| DN_HistogramMode_10 | Healthy vs CAD | 0.49 | 6.26e-01 | 7.36e-01 | 17347.0 | 9.27e-01 | 9.61e-01 |
| PD_PeriodicityWang_th0_01 | Healthy vs CAD | 0.61 | 5.39e-01 | 6.65e-01 | 17161.5 | 9.31e-01 | 9.61e-01 |
| apen | Healthy vs CAD_Diabetes | 0.08 | 9.35e-01 | 9.35e-01 | 2287.0 | 9.47e-01 | 9.72e-01 |
| CO_Embed2_Dist_tau_d_expfit_meandiff | Healthy vs CAD | -0.22 | 8.27e-01 | 8.65e-01 | 17196.0 | 9.58e-01 | 9.79e-01 |
| FC_LocalSimple_mean3_stderr | Healthy vs CAD_Diabetes | 0.28 | 7.83e-01 | 8.46e-01 | 2318.0 | 9.64e-01 | 9.82e-01 |
| min | Healthy vs CAD_Diabetes | 0.17 | 8.66e-01 | 8.93e-01 | 2298.0 | 9.79e-01 | 9.89e-01 |
| DN_HistogramMode_5 | CAD_Diabetes vs ESRD | -0.26 | 7.92e-01 | 8.49e-01 | 597.0 | 9.81e-01 | 9.89e-01 |
| DN_OutlierInclude_p_001_mdrmd | Healthy vs ESRD | 0.25 | 8.07e-01 | 8.55e-01 | 3252.5 | 9.84e-01 | 9.89e-01 |
| SB_BinaryStats_diff_longstretch0 | Healthy vs CAD | -0.54 | 5.90e-01 | 7.15e-01 | 17243.0 | 9.94e-01 | 9.94e-01 |

</details>

</div>

## 6 PCA Analysis

### 6.1 All Metrics (38)

<div class="panel-tabset">

#### 5-min

![](thew_analysis_1_files/figure-commonmark/pca-all-5min-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-all-5min-13-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-all-5min-34-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-all-5min-load-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-all-5min-var-1.png)

#### 1-min

![](thew_analysis_1_files/figure-commonmark/pca-all-1min-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-all-1min-13-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-all-1min-34-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-all-1min-load-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-all-1min-var-1.png)

</div>

### 6.2 avg_hr Metrics Only (34)

<div class="panel-tabset">

#### 5-min

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-3d-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-dist-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-pc1-jitter-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-pc2-jitter-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-pc3-jitter-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-dist-line-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-pc1-line-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-pc2-line-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-pc3-line-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-13-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-34-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-42-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-45-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-46-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-47-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-load-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-5min-var-1.png)

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

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(215,227,250); color:black; text-align:right;">

-0.26
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(213,218,226); color:black; text-align:right;">

+0.26
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
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

iqr
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

DN_Spread_Std
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

sd
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

sampen
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

<td style="padding:2px 8px; background-color: rgb(211,225,231); color:black; text-align:right;">

+0.21
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(211,225,231); color:black; text-align:right;">

+0.21
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
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

12
</td>

<td style="padding:2px 8px;">

cv
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

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(222,233,251); color:black; text-align:right;">

-0.21
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

permen
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

apen
</td>

<td style="padding:2px 8px; background-color: rgb(224,234,251); color:black; text-align:right;">

-0.20
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

max
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

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(208,231,236); color:black; text-align:right;">

+0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
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

19
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

20
</td>

<td style="padding:2px 8px;">

median
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

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(207,235,239); color:black; text-align:right;">

+0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
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

23
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(206,238,242); color:black; text-align:right;">

+0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
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

25
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
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

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
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

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
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

min
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

DN_OutlierInclude_n_001_mdrmd
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

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
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

DN_HistogramMode_10
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

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
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

<td style="padding:2px 8px; background-color: rgb(199,216,249); color:black; text-align:right;">

-0.36
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(199,216,249); color:black; text-align:right;">

-0.36
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(201,218,249); color:black; text-align:right;">

-0.35
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(201,218,249); color:black; text-align:right;">

-0.35
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

min
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

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(222,233,251); color:black; text-align:right;">

-0.21
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

sd
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

CO_Embed2_Dist_tau_d_expfit_meandiff
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

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(229,237,252); color:black; text-align:right;">

-0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(208,232,237); color:black; text-align:right;">

+0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(230,238,252); color:black; text-align:right;">

-0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(207,234,238); color:black; text-align:right;">

+0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(207,235,239); color:black; text-align:right;">

+0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(207,235,239); color:black; text-align:right;">

+0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
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

CO_f1ecac
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

apen
</td>

<td style="padding:2px 8px; background-color: rgb(233,240,253); color:black; text-align:right;">

-0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(235,241,253); color:black; text-align:right;">

-0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(235,241,253); color:black; text-align:right;">

-0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
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

21
</td>

<td style="padding:2px 8px;">

sampen
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

cv
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

permen
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

PD_PeriodicityWang_th0_01
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

FC_LocalSimple_mean1_tauresrat
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

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
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

DN_HistogramMode_10
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

DN_OutlierInclude_p_001_mdrmd
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

SB_BinaryStats_diff_longstretch0
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

DN_OutlierInclude_n_001_mdrmd
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

DN_HistogramMode_5
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

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
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

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
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

min
</td>

<td style="padding:2px 8px; background-color: rgb(220,201,212); color:black; text-align:right;">

+0.38
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

cv
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

permen
</td>

<td style="padding:2px 8px; background-color: rgb(218,206,217); color:black; text-align:right;">

+0.34
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(213,218,226); color:black; text-align:right;">

+0.26
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

mean
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

DN_Mean
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

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(219,230,251); color:black; text-align:right;">

-0.23
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

sd
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

DN_HistogramMode_10
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

iqr
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

IN_AutoMutualInfoStats_40_gaussian_fmmi
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

DN_HistogramMode_5
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

CO_Embed2_Dist_tau_d_expfit_meandiff
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

PD_PeriodicityWang_th0_01
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

CO_FirstMin_ac
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

SP_Summaries_welch_rect_area_5_1
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

FC_LocalSimple_mean3_stderr
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

CO_HistogramAMI_even_2_5
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

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(206,238,242); color:black; text-align:right;">

+0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
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

21
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

22
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
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

max
</td>

<td style="padding:2px 8px; background-color: rgb(241,245,253); color:black; text-align:right;">

-0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
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

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(244,248,254); color:black; text-align:right;">

-0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
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

apen
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

DN_OutlierInclude_n_001_mdrmd
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

SB_TransitionMatrix_3ac_sumdiagcov
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

CO_f1ecac
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

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
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

DN_OutlierInclude_p_001_mdrmd
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

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

-0.00
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

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(197,215,248); color:black; text-align:right;">

-0.37
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
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

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(217,209,219); color:black; text-align:right;">

+0.32
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

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(211,225,250); color:black; text-align:right;">

-0.28
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(215,215,224); color:black; text-align:right;">

+0.28
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(214,216,225); color:black; text-align:right;">

+0.27
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
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

SP_Summaries_welch_rect_centroid
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

apen
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

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(227,236,252); color:black; text-align:right;">

-0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
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

SB_BinaryStats_diff_longstretch0
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

SB_BinaryStats_mean_longstretch1
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

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(233,240,253); color:black; text-align:right;">

-0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(233,240,253); color:black; text-align:right;">

-0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
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

18
</td>

<td style="padding:2px 8px;">

permen
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

CO_Embed2_Dist_tau_d_expfit_meandiff
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

max
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

SB_MotifThree_quantile_hh
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

CO_HistogramAMI_even_2_5
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

cv
</td>

<td style="padding:2px 8px; background-color: rgb(202,246,248); color:black; text-align:right;">

+0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
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

median
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

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
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

28
</td>

<td style="padding:2px 8px;">

sd
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

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
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

FC_LocalSimple_mean3_stderr
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

DN_HistogramMode_5
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

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(226,185,200); color:black; text-align:right;">

+0.49
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(215,227,250); color:black; text-align:right;">

-0.26
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
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

DN_OutlierInclude_p_001_mdrmd
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

sampen
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

apen
</td>

<td style="padding:2px 8px; background-color: rgb(211,225,231); color:black; text-align:right;">

+0.21
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(232,239,252); color:black; text-align:right;">

-0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
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

10
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(207,235,239); color:black; text-align:right;">

+0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(235,241,253); color:black; text-align:right;">

-0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(206,238,242); color:black; text-align:right;">

+0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
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

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
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

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
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

21
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
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

DN_Mean
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

mean
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

SB_TransitionMatrix_3ac_sumdiagcov
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

SB_MotifThree_quantile_hh
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

CO_trev_1_num
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

CO_HistogramAMI_even_2_5
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

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
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

31
</td>

<td style="padding:2px 8px;">

max
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

DN_OutlierInclude_n_001_mdrmd
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

CO_f1ecac
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

SP_Summaries_welch_rect_centroid
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

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(171,197,245); color:black; text-align:right;">

-0.54
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(227,184,199); color:black; text-align:right;">

+0.50
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

SP_Summaries_welch_rect_centroid
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

IN_AutoMutualInfoStats_40_gaussian_fmmi
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

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(222,233,251); color:black; text-align:right;">

-0.21
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(227,236,252); color:black; text-align:right;">

-0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
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

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(208,232,237); color:black; text-align:right;">

+0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(232,239,252); color:black; text-align:right;">

-0.15
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
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

SP_Summaries_welch_rect_area_5_1
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

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(238,243,253); color:black; text-align:right;">

-0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
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

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
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

18
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(244,248,254); color:black; text-align:right;">

-0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(246,249,254); color:black; text-align:right;">

-0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
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

SB_MotifThree_quantile_hh
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

cv
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
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

CO_Embed2_Dist_tau_d_expfit_meandiff
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

sd
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

DN_Spread_Std
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

sampen
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

mean
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

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(200,252,253); color:black; text-align:right;">

+0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
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

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
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

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(220,201,212); color:black; text-align:right;">

+0.38
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
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

apen
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

DN_HistogramMode_10
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

DN_HistogramMode_5
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

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(215,227,250); color:black; text-align:right;">

-0.26
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
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

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(221,231,251); color:black; text-align:right;">

-0.22
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
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

CO_FirstMin_ac
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

CO_Embed2_Dist_tau_d_expfit_meandiff
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

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(233,240,253); color:black; text-align:right;">

-0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
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

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(239,244,253); color:black; text-align:right;">

-0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
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

17
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(201,249,251); color:black; text-align:right;">

+0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
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

24
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(200,252,253); color:black; text-align:right;">

+0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

mean
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

DN_Mean
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

max
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

min
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
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

DN_OutlierInclude_p_001_mdrmd
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

SB_TransitionMatrix_3ac_sumdiagcov
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

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(160,190,244); color:white; text-align:right;">

-0.61
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(228,181,197); color:black; text-align:right;">

+0.52
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(207,222,249); color:black; text-align:right;">

-0.31
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
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

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(224,234,251); color:black; text-align:right;">

-0.20
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(229,237,252); color:black; text-align:right;">

-0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(230,238,252); color:black; text-align:right;">

-0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
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

9
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(233,240,253); color:black; text-align:right;">

-0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
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

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
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

14
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
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

17
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(249,251,254); color:black; text-align:right;">

-0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
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

19
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(201,249,251); color:black; text-align:right;">

+0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(249,251,254); color:black; text-align:right;">

-0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
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

25
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(252,253,255); color:black; text-align:right;">

-0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
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

max
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

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
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

31
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
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

median
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

mean
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

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

</table>

</details>

#### 1-min

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-3d-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-dist-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-pc1-jitter-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-pc2-jitter-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-pc3-jitter-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-dist-line-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-pc1-line-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-pc2-line-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-pc3-line-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-13-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-34-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-42-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-45-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-46-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-47-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-load-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-avghr-1min-var-1.png)

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

FC_LocalSimple_mean3_stderr
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

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(216,228,251); color:black; text-align:right;">

-0.25
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(216,228,251); color:black; text-align:right;">

-0.25
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(213,219,227); color:black; text-align:right;">

+0.25
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

apen
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

sampen
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

<td style="padding:2px 8px; background-color: rgb(212,221,228); color:black; text-align:right;">

+0.24
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

iqr
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

DN_Spread_Std
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

sd
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

CO_Embed2_Dist_tau_d_expfit_meandiff
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

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(224,234,251); color:black; text-align:right;">

-0.20
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(210,228,234); color:black; text-align:right;">

+0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(210,228,234); color:black; text-align:right;">

+0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(225,235,252); color:black; text-align:right;">

-0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
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

max
</td>

<td style="padding:2px 8px; background-color: rgb(227,236,252); color:black; text-align:right;">

-0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(229,237,252); color:black; text-align:right;">

-0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(229,237,252); color:black; text-align:right;">

-0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

median
</td>

<td style="padding:2px 8px; background-color: rgb(230,238,252); color:black; text-align:right;">

-0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(235,241,253); color:black; text-align:right;">

-0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
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

23
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(236,242,253); color:black; text-align:right;">

-0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
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

25
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
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

min
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

DN_OutlierInclude_p_001_mdrmd
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

SB_BinaryStats_diff_longstretch0
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

DN_OutlierInclude_n_001_mdrmd
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

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
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

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
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

DN_HistogramMode_10
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

DN_HistogramMode_5
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

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
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

max
</td>

<td style="padding:2px 8px; background-color: rgb(217,209,219); color:black; text-align:right;">

+0.32
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(216,211,220); color:black; text-align:right;">

+0.31
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
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

cv
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

permen
</td>

<td style="padding:2px 8px; background-color: rgb(211,225,250); color:black; text-align:right;">

-0.28
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(215,215,224); color:black; text-align:right;">

+0.28
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
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

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(224,234,251); color:black; text-align:right;">

-0.20
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
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

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(210,228,234); color:black; text-align:right;">

+0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
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

CO_FirstMin_ac
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

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(209,229,235); color:black; text-align:right;">

+0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(209,229,235); color:black; text-align:right;">

+0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
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

16
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

17
</td>

<td style="padding:2px 8px;">

mean
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

DN_Mean
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

PD_PeriodicityWang_th0_01
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

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(206,238,242); color:black; text-align:right;">

+0.12
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

SB_BinaryStats_mean_longstretch1
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

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
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

sampen
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

min
</td>

<td style="padding:2px 8px; background-color: rgb(244,248,254); color:black; text-align:right;">

-0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
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

27
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
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

DN_HistogramMode_10
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

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(246,249,254); color:black; text-align:right;">

-0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
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

31
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
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

CO_f1ecac
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

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
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

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
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

min
</td>

<td style="padding:2px 8px; background-color: rgb(225,189,203); color:black; text-align:right;">

+0.46
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

median
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

mean
</td>

<td style="padding:2px 8px; background-color: rgb(222,196,209); color:black; text-align:right;">

+0.41
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(222,196,209); color:black; text-align:right;">

+0.41
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

cv
</td>

<td style="padding:2px 8px; background-color: rgb(221,231,251); color:black; text-align:right;">

-0.22
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(211,225,231); color:black; text-align:right;">

+0.21
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
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

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(208,232,237); color:black; text-align:right;">

+0.16
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(207,235,239); color:black; text-align:right;">

+0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(207,235,239); color:black; text-align:right;">

+0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
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

12
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

CO_f1ecac
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

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

apen
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

<td style="padding:2px 8px; background-color: rgb(244,248,254); color:black; text-align:right;">

-0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

sd
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

DN_Spread_Std
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

PD_PeriodicityWang_th0_01
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

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
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

27
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
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

CO_trev_1_num
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

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
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

IN_AutoMutualInfoStats_40_gaussian_fmmi
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

+0.00
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

34
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
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

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(220,201,212); color:black; text-align:right;">

+0.38
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(199,216,249); color:black; text-align:right;">

-0.36
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
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

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(213,219,227); color:black; text-align:right;">

+0.25
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
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

DN_OutlierInclude_p_001_mdrmd
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

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(219,230,251); color:black; text-align:right;">

-0.23
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(211,224,230); color:black; text-align:right;">

+0.22
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
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

<td style="padding:2px 8px; background-color: rgb(225,235,252); color:black; text-align:right;">

-0.19
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
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

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(209,229,235); color:black; text-align:right;">

+0.18
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
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

14
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
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

sampen
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

max
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

permen
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

apen
</td>

<td style="padding:2px 8px; background-color: rgb(236,242,253); color:black; text-align:right;">

-0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

cv
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

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
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

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(241,245,253); color:black; text-align:right;">

-0.09
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
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

25
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

26
</td>

<td style="padding:2px 8px;">

median
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

FC_LocalSimple_mean3_stderr
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

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

min
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

CO_Embed2_Dist_tau_d_expfit_meandiff
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

SP_Summaries_welch_rect_area_5_1
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

iqr
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

DN_Mean
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

mean
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

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(227,184,199); color:black; text-align:right;">

+0.50
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(183,206,247); color:black; text-align:right;">

-0.46
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(204,220,249); color:black; text-align:right;">

-0.33
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
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

DN_OutlierInclude_n_001_mdrmd
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

DN_HistogramMode_10
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

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(221,231,251); color:black; text-align:right;">

-0.22
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
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

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(233,240,253); color:black; text-align:right;">

-0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

min
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

SP_Summaries_welch_rect_centroid
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

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
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

16
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
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

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
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

19
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

sampen
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

permen
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

cv
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

max
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

DN_Mean
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

mean
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

SB_MotifThree_quantile_hh
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

DN_Spread_Std
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

sd
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

apen
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

SB_BinaryStats_diff_longstretch0
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

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(200,252,253); color:black; text-align:right;">

+0.02
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

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(177,201,246); color:black; text-align:right;">

-0.50
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(177,201,246); color:black; text-align:right;">

-0.50
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(193,212,248); color:black; text-align:right;">

-0.40
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(213,218,226); color:black; text-align:right;">

+0.26
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(211,225,231); color:black; text-align:right;">

+0.21
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(224,234,251); color:black; text-align:right;">

-0.20
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(229,237,252); color:black; text-align:right;">

-0.17
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(235,241,253); color:black; text-align:right;">

-0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
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

10
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(206,238,242); color:black; text-align:right;">

+0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

CO_f1ecac
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(238,243,253); color:black; text-align:right;">

-0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

permen
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
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

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

mean
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

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
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

19
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

20
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

21
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

22
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
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

sampen
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

MD_hrv_classic_pnn40
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

CO_Embed2_Dist_tau_d_expfit_meandiff
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

median
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(202,248,249); color:black; text-align:right;">

+0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
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

29
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
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

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(249,251,254); color:black; text-align:right;">

-0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

31
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
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

iqr
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

FC_LocalSimple_mean3_stderr
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

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

+0.00
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

<td style="padding:2px 8px; background-color: rgb(180,204,246); color:black; text-align:right;">

-0.48
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(220,201,212); color:black; text-align:right;">

+0.38
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
</td>

<td style="padding:2px 8px;">

IN_AutoMutualInfoStats_40_gaussian_fmmi
</td>

<td style="padding:2px 8px; background-color: rgb(218,206,217); color:black; text-align:right;">

+0.34
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

4
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(205,221,249); color:black; text-align:right;">

-0.32
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
</td>

<td style="padding:2px 8px;">

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(205,221,249); color:black; text-align:right;">

-0.32
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

6
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(216,212,221); color:black; text-align:right;">

+0.30
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(213,226,250); color:black; text-align:right;">

-0.27
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

8
</td>

<td style="padding:2px 8px;">

sampen
</td>

<td style="padding:2px 8px; background-color: rgb(207,235,239); color:black; text-align:right;">

+0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

SB_MotifThree_quantile_hh
</td>

<td style="padding:2px 8px; background-color: rgb(207,235,239); color:black; text-align:right;">

+0.14
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_p_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(206,236,240); color:black; text-align:right;">

+0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_dfa_50_1_2_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(206,236,240); color:black; text-align:right;">

+0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(206,238,242); color:black; text-align:right;">

+0.12
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(205,241,244); color:black; text-align:right;">

+0.10
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

CO_f1ecac
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

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

16
</td>

<td style="padding:2px 8px;">

apen
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

17
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_10
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

18
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(202,246,248); color:black; text-align:right;">

+0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

19
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(246,249,254); color:black; text-align:right;">

-0.06
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(247,250,254); color:black; text-align:right;">

-0.05
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(201,249,251); color:black; text-align:right;">

+0.04
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
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

23
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

25
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

26
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

27
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

28
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
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

31
</td>

<td style="padding:2px 8px;">

mean
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

DN_Mean
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

permen
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

median
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

-0.00
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

CO_trev_1_num
</td>

<td style="padding:2px 8px; background-color: rgb(159,189,244); color:white; text-align:right;">

-0.62
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

2
</td>

<td style="padding:2px 8px;">

SC_FluctAnal_2_rsrangefit_50_1_logi_prop_r1
</td>

<td style="padding:2px 8px; background-color: rgb(190,210,248); color:black; text-align:right;">

-0.42
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

3
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

4
</td>

<td style="padding:2px 8px;">

DN_OutlierInclude_n_001_mdrmd
</td>

<td style="padding:2px 8px; background-color: rgb(219,204,215); color:black; text-align:right;">

+0.36
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

5
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

6
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_mean_longstretch1
</td>

<td style="padding:2px 8px; background-color: rgb(235,241,253); color:black; text-align:right;">

-0.13
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

7
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

8
</td>

<td style="padding:2px 8px;">

SB_TransitionMatrix_3ac_sumdiagcov
</td>

<td style="padding:2px 8px; background-color: rgb(238,243,253); color:black; text-align:right;">

-0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

9
</td>

<td style="padding:2px 8px;">

CO_FirstMin_ac
</td>

<td style="padding:2px 8px; background-color: rgb(205,239,243); color:black; text-align:right;">

+0.11
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

10
</td>

<td style="padding:2px 8px;">

DN_HistogramMode_5
</td>

<td style="padding:2px 8px; background-color: rgb(243,246,254); color:black; text-align:right;">

-0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

11
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean1_tauresrat
</td>

<td style="padding:2px 8px; background-color: rgb(203,244,246); color:black; text-align:right;">

+0.08
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

12
</td>

<td style="padding:2px 8px;">

min
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

13
</td>

<td style="padding:2px 8px;">

PD_PeriodicityWang_th0_01
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

14
</td>

<td style="padding:2px 8px;">

CO_Embed2_Dist_tau_d_expfit_meandiff
</td>

<td style="padding:2px 8px; background-color: rgb(203,245,247); color:black; text-align:right;">

+0.07
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

15
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

16
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

17
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

18
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

19
</td>

<td style="padding:2px 8px;">

FC_LocalSimple_mean3_stderr
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

20
</td>

<td style="padding:2px 8px;">

sd
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

21
</td>

<td style="padding:2px 8px;">

DN_Spread_Std
</td>

<td style="padding:2px 8px; background-color: rgb(250,252,254); color:black; text-align:right;">

-0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

22
</td>

<td style="padding:2px 8px;">

SB_BinaryStats_diff_longstretch0
</td>

<td style="padding:2px 8px; background-color: rgb(201,251,252); color:black; text-align:right;">

+0.03
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

23
</td>

<td style="padding:2px 8px;">

MD_hrv_classic_pnn40
</td>

<td style="padding:2px 8px; background-color: rgb(200,252,253); color:black; text-align:right;">

+0.02
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

24
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

25
</td>

<td style="padding:2px 8px;">

CO_HistogramAMI_even_2_5
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

26
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

27
</td>

<td style="padding:2px 8px;">

SP_Summaries_welch_rect_centroid
</td>

<td style="padding:2px 8px; background-color: rgb(253,254,255); color:black; text-align:right;">

-0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

28
</td>

<td style="padding:2px 8px;">

DN_Mean
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

29
</td>

<td style="padding:2px 8px;">

mean
</td>

<td style="padding:2px 8px; background-color: rgb(199,254,254); color:black; text-align:right;">

+0.01
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

30
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

31
</td>

<td style="padding:2px 8px;">

iqr
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

-0.00
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

32
</td>

<td style="padding:2px 8px;">

max
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

+0.00
</td>

</tr>

<tr>

<td style="padding:2px 8px;">

33
</td>

<td style="padding:2px 8px;">

apen
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

SP_Summaries_welch_rect_area_5_1
</td>

<td style="padding:2px 8px; background-color: rgb(199,255,255); color:black; text-align:right;">

-0.00
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

![](thew_analysis_1_files/figure-commonmark/hrv-pca-corr-5min-1.png)

![](thew_analysis_1_files/figure-commonmark/hrv-pca-scatter-5min-1.png)

![](thew_analysis_1_files/figure-commonmark/hrv-pca-ba-5min-1.png)

| HRV Metric    | PC  |    ICC | 95% CI Lower | 95% CI Upper |
|:--------------|:----|-------:|-------------:|-------------:|
| mean_rmssd_ms | PC1 | -0.143 |       -0.233 |       -0.051 |
| mean_rmssd_ms | PC2 |  0.077 |       -0.017 |        0.168 |
| mean_rmssd_ms | PC3 | -0.227 |       -0.314 |       -0.137 |
| mean_rmssd_ms | PC4 |  0.014 |       -0.079 |        0.107 |
| mean_rmssd_ms | PC5 |  0.090 |       -0.003 |        0.181 |
| mean_rmssd_ms | PC6 | -0.066 |       -0.158 |        0.028 |
| mean_rmssd_ms | PC7 | -0.038 |       -0.130 |        0.056 |
| mean_rmssd_ms | PC8 | -0.096 |       -0.188 |       -0.004 |
| mean_sdnn_ms  | PC1 | -0.109 |       -0.200 |       -0.017 |
| mean_sdnn_ms  | PC2 |  0.026 |       -0.067 |        0.118 |
| mean_sdnn_ms  | PC3 | -0.388 |       -0.465 |       -0.306 |
| mean_sdnn_ms  | PC4 | -0.016 |       -0.109 |        0.077 |
| mean_sdnn_ms  | PC5 |  0.157 |        0.065 |        0.246 |
| mean_sdnn_ms  | PC6 | -0.062 |       -0.154 |        0.031 |
| mean_sdnn_ms  | PC7 | -0.083 |       -0.175 |        0.010 |
| mean_sdnn_ms  | PC8 | -0.076 |       -0.168 |        0.017 |

ICC (two-way, agreement) between z-scored HRV metrics and PC scores
(5-min)

#### 1-min

![](thew_analysis_1_files/figure-commonmark/hrv-pca-corr-1min-1.png)

![](thew_analysis_1_files/figure-commonmark/hrv-pca-scatter-1min-1.png)

![](thew_analysis_1_files/figure-commonmark/hrv-pca-ba-1min-1.png)

| HRV Metric    | PC  |    ICC | 95% CI Lower | 95% CI Upper |
|:--------------|:----|-------:|-------------:|-------------:|
| mean_rmssd_ms | PC1 |  0.211 |        0.121 |        0.298 |
| mean_rmssd_ms | PC2 |  0.143 |        0.051 |        0.233 |
| mean_rmssd_ms | PC3 | -0.196 |       -0.284 |       -0.105 |
| mean_rmssd_ms | PC4 |  0.053 |       -0.041 |        0.145 |
| mean_rmssd_ms | PC5 | -0.010 |       -0.103 |        0.083 |
| mean_rmssd_ms | PC6 | -0.125 |       -0.216 |       -0.032 |
| mean_rmssd_ms | PC7 |  0.141 |        0.049 |        0.231 |
| mean_rmssd_ms | PC8 | -0.047 |       -0.139 |        0.046 |
| mean_sdnn_ms  | PC1 |  0.210 |        0.119 |        0.297 |
| mean_sdnn_ms  | PC2 |  0.319 |        0.233 |        0.400 |
| mean_sdnn_ms  | PC3 | -0.281 |       -0.364 |       -0.193 |
| mean_sdnn_ms  | PC4 |  0.045 |       -0.048 |        0.137 |
| mean_sdnn_ms  | PC5 |  0.015 |       -0.078 |        0.108 |
| mean_sdnn_ms  | PC6 | -0.148 |       -0.238 |       -0.055 |
| mean_sdnn_ms  | PC7 |  0.156 |        0.064 |        0.245 |
| mean_sdnn_ms  | PC8 | -0.038 |       -0.130 |        0.056 |

ICC (two-way, agreement) between z-scored HRV metrics and PC scores
(1-min)

</div>

### 6.2.2 SDNN vs −PC3: Sign-Flipped Agreement

SDNN and PC3 appear anticorrelated. Flipping the sign of PC3 and
comparing z-scored SDNN vs z(−PC3) via scatter (identity line) and
Bland-Altman.

<div class="panel-tabset">

#### 5-min

![](thew_analysis_1_files/figure-commonmark/sdnn-pc3-scatter-5min-1.png)

    r = 0.387, p = 2.21e-17

![](thew_analysis_1_files/figure-commonmark/sdnn-pc3-ba-5min-1.png)

    Mean diff = 0.000, 95% LoA = [-2.170, 2.170]

    ICC = 0.388 [0.306, 0.464]

#### 1-min

![](thew_analysis_1_files/figure-commonmark/sdnn-pc3-scatter-1min-1.png)

    r = 0.280, p = 1.83e-09

![](thew_analysis_1_files/figure-commonmark/sdnn-pc3-ba-1min-1.png)

    Mean diff = 0.000, 95% LoA = [-2.352, 2.352]

    ICC = 0.280 [0.192, 0.364]

</div>

### 6.3 Top Significant avg_hr Metrics

    Using 21 significant avg_hr metrics for PCA:

    - CO_HistogramAMI_even_2_5
    - CO_f1ecac
    - DN_Mean
    - DN_OutlierInclude_n_001_mdrmd
    - DN_Spread_Std
    - FC_LocalSimple_mean1_tauresrat
    - FC_LocalSimple_mean3_stderr
    - MD_hrv_classic_pnn40
    - SB_MotifThree_quantile_hh
    - SB_TransitionMatrix_3ac_sumdiagcov
    - SP_Summaries_welch_rect_centroid
    - apen
    - cv
    - iqr
    - max
    - mean
    - median
    - min
    - permen
    - sampen
    - sd

<div class="panel-tabset">

#### 5-min

![](thew_analysis_1_files/figure-commonmark/pca-top-5min-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-top-5min-13-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-top-5min-34-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-top-5min-load-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-top-5min-var-1.png)

#### 1-min

![](thew_analysis_1_files/figure-commonmark/pca-top-1min-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-top-1min-13-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-top-1min-34-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-top-1min-load-1.png)

![](thew_analysis_1_files/figure-commonmark/pca-top-1min-var-1.png)

</div>

## 7 Summary

### Key Findings

**Omnibus tests**: 24 of 38 metrics show significant group differences
(KW p_adj \< 0.05, 5-min resolution).

**Top 5 most discriminating metrics** (Kruskal-Wallis, 5-min,
BH-adjusted):

1.  **DN_Spread_Std** — p_adj = 2.82e-40 \*\*\*
2.  **max** — p_adj = 2.82e-40 \*\*\*
3.  **sd** — p_adj = 2.82e-40 \*\*\*
4.  **iqr** — p_adj = 8.95e-39 \*\*\*
5.  **permen** — p_adj = 3.04e-33 \*\*\*

**Most significant pairwise comparison**: Healthy vs CAD on metric max
(Wilcoxon p = 3.24e-40).

**Note**: CAD_Diabetes (n=29) and ESRD (n=41) groups have relatively
small sample sizes; non-parametric tests (Kruskal-Wallis, Wilcoxon) are
more reliable than parametric alternatives for these groups.

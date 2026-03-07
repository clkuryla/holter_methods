# THEW Python DHI Features: Diagnostic Analysis

2026-03-06

- [1 Setup & Data Loading](#1-setup--data-loading)
- [2 NaN Audit](#2-nan-audit)
- [3 Correlation Heatmaps](#3-correlation-heatmaps)
  - [All Features](#all-features)
  - [Highly correlated pairs (\|r\| \>
    0.95)](#highly-correlated-pairs-r--095)
  - [Cosinor](#cosinor)
  - [Nonparametric Circadian](#nonparametric-circadian)
  - [Spectral](#spectral)
  - [Complexity](#complexity)
  - [Temporal](#temporal)
  - [Dynamical](#dynamical)
  - [Descriptive](#descriptive)
  - [MiniROCKET](#minirocket)
  - [FPCA](#fpca)
  - [Residual Spectral](#residual-spectral)
  - [Residual Complexity](#residual-complexity)
  - [Residual Temporal](#residual-temporal)
  - [Residual Dynamical](#residual-dynamical)
- [4 PCA Analysis](#4-pca-analysis)
  - [4a. All Features (incl
    MiniROCKET)](#4a-all-features-incl-minirocket)
  - [4b. All Features (no MiniROCKET)](#4b-all-features-no-minirocket)
  - [4c. Raw Interpretable Only](#4c-raw-interpretable-only)
  - [4d. Residuals Only](#4d-residuals-only)
  - [4e. Interpretable (no Circadian, no
    MiniROCKET)](#4e-interpretable-no-circadian-no-minirocket)
  - [4f. Circadian Only](#4f-circadian-only)
  - [4g. MiniROCKET Only](#4g-minirocket-only)
  - [4h. Raw Non-Circadian,
    Non-MiniROCKET](#4h-raw-non-circadian-non-minirocket)
- [5 Violin Plots](#5-violin-plots)
  - [Key Features Overview](#key-features-overview)
  - [Cosinor Features](#cosinor-features)
  - [Nonparametric Circadian
    Features](#nonparametric-circadian-features)
  - [Spectral / Rhythm Features](#spectral--rhythm-features)
  - [Complexity Features](#complexity-features)
  - [Temporal / Autocorrelation
    Features](#temporal--autocorrelation-features)
  - [Dynamical / RQA Features](#dynamical--rqa-features)
  - [Descriptive Features](#descriptive-features)
  - [MiniROCKET PCs](#minirocket-pcs)
  - [FPCA Scores](#fpca-scores)
  - [Residual Spectral Features](#residual-spectral-features)
  - [Residual Complexity Features](#residual-complexity-features)
  - [Residual Temporal Features](#residual-temporal-features)
  - [Residual Dynamical Features](#residual-dynamical-features)
- [6 Group Comparisons
  (Kruskal-Wallis)](#6-group-comparisons-kruskal-wallis)
  - [Median by group for significant
    features](#median-by-group-for-significant-features)

## 1 Setup & Data Loading

**Dataset summary:**

| condition4   | condition |   n |
|:-------------|:----------|----:|
| Healthy      | Healthy   | 128 |
| CAD          | CAD       | 195 |
| CAD_Diabetes | CAD+DM    |  26 |
| ESRD         | ESRD      |  41 |

Participant counts by condition

Total: 390 participants, 104 features.

## 2 NaN Audit

    No missing values in any feature column.

## 3 Correlation Heatmaps

### All Features

![](thew_analysis_2_files/figure-commonmark/corr-all-1.png)

### Highly correlated pairs (\|r\| \> 0.95)

| feature_1           | feature_2                      |       r |
|:--------------------|:-------------------------------|--------:|
| perm_entropy        | pe_tau1                        |  1.0000 |
| power_circ          | resid_power_circ               |  1.0000 |
| power_meso          | resid_power_meso               |  1.0000 |
| power_hf            | resid_power_hf                 |  1.0000 |
| resid_perm_entropy  | resid_pe_tau1                  |  1.0000 |
| mesor               | fpca_score_1                   |  0.9991 |
| iv                  | acf_lag1                       | -0.9984 |
| higuchi_fd          | resid_higuchi_fd               |  0.9820 |
| resid_trans_entropy | resid_trans_diagonal_dominance | -0.9517 |
| trans_entropy       | trans_diagonal_dominance       | -0.9509 |

Feature pairs with \|r\| \> 0.95

### Cosinor

![](thew_analysis_2_files/figure-commonmark/corr-cosinor-1.png)

### Nonparametric Circadian

![](thew_analysis_2_files/figure-commonmark/corr-nonparametric-1.png)

### Spectral

![](thew_analysis_2_files/figure-commonmark/corr-spectral-1.png)

### Complexity

![](thew_analysis_2_files/figure-commonmark/corr-complexity-1.png)

### Temporal

![](thew_analysis_2_files/figure-commonmark/corr-temporal-1.png)

### Dynamical

![](thew_analysis_2_files/figure-commonmark/corr-dynamical-1.png)

### Descriptive

![](thew_analysis_2_files/figure-commonmark/corr-descriptive-1.png)

### MiniROCKET

![](thew_analysis_2_files/figure-commonmark/corr-minirocket-1.png)

### FPCA

![](thew_analysis_2_files/figure-commonmark/corr-fpca-1.png)

### Residual Spectral

![](thew_analysis_2_files/figure-commonmark/corr-resid-spectral-1.png)

### Residual Complexity

![](thew_analysis_2_files/figure-commonmark/corr-resid-complexity-1.png)

### Residual Temporal

![](thew_analysis_2_files/figure-commonmark/corr-resid-temporal-1.png)

### Residual Dynamical

![](thew_analysis_2_files/figure-commonmark/corr-resid-dynamical-1.png)

## 4 PCA Analysis

### 4a. All Features (incl MiniROCKET)

![](thew_analysis_2_files/figure-commonmark/pca-4a-1.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-2.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-3.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-4.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-5.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-6.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-7.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-8.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-9.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-10.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-11.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-12.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-13.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-14.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-15.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-16.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-17.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-18.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-19.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-20.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-21.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-22.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-23.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-24.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-25.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-26.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-27.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-28.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-29.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-30.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-31.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-32.png)
![](thew_analysis_2_files/figure-commonmark/pca-4a-33.png)

**PC1** (23.7% variance)

| feature                        | loading | rank |
|:-------------------------------|--------:|-----:|
| rqa_determinism                |  0.1692 |    1 |
| iv                             | -0.1687 |    2 |
| acf_lag1                       |  0.1686 |    3 |
| sample_entropy                 | -0.1648 |    4 |
| trans_entropy                  | -0.1648 |    5 |
| rqa_laminarity                 |  0.1593 |    6 |
| dfa_alpha                      |  0.1591 |    7 |
| trans_diagonal_dominance       |  0.1591 |    8 |
| resid_trans_diagonal_dominance |  0.1548 |    9 |
| resid_trans_entropy            | -0.1519 |   10 |

**PC2** (12.3% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| power_hf              | -0.2256 |    1 |
| resid_power_hf        | -0.2256 |    2 |
| minirocket_pc1        |  0.2136 |    3 |
| sd                    | -0.1980 |    4 |
| cv                    | -0.1932 |    5 |
| dip_sharpness_descent |  0.1914 |    6 |
| dip_sharpness_ascent  | -0.1909 |    7 |
| resid_sd              | -0.1860 |    8 |
| amplitude_24h         | -0.1789 |    9 |
| peak_trough_diff      | -0.1706 |   10 |

**PC3** (8.7% variance)

| feature          | loading | rank |
|:-----------------|--------:|-----:|
| r_squared_1h     | -0.2653 |    1 |
| r_squared_2h     | -0.2438 |    2 |
| acf_lag12        | -0.2260 |    3 |
| acf_lag144       |  0.2198 |    4 |
| acf_first_zero   | -0.2141 |    5 |
| spectral_entropy |  0.2109 |    6 |
| acf_decay_rate   |  0.1927 |    7 |
| lzc_median       |  0.1751 |    8 |
| power_circ       |  0.1712 |    9 |
| resid_power_circ |  0.1712 |   10 |

**PC4** (6.4% variance)

| feature                     | loading | rank |
|:----------------------------|--------:|-----:|
| pe_slope                    |  0.2560 |    1 |
| resid_pe_slope              |  0.2434 |    2 |
| resid_acf_decay_rate        |  0.2278 |    3 |
| resid_circadian_power_ratio | -0.2186 |    4 |
| resid_acf_lag12             | -0.2118 |    5 |
| resid_acf_first_zero        | -0.2116 |    6 |
| perm_entropy                | -0.1988 |    7 |
| pe_tau1                     | -0.1988 |    8 |
| resid_perm_entropy          | -0.1938 |    9 |
| resid_pe_tau1               | -0.1938 |   10 |

**PC5** (4.5% variance)

| feature                 | loading | rank |
|:------------------------|--------:|-----:|
| trough_hr               |  0.3586 |    1 |
| mesor                   |  0.3519 |    2 |
| fpca_score_1            |  0.3488 |    3 |
| minirocket_pc9          | -0.3323 |    4 |
| peak_hr                 |  0.2069 |    5 |
| resid_pe_slope          |  0.1829 |    6 |
| resid_rqa_trapping_time | -0.1771 |    7 |
| resid_sample_entropy    |  0.1707 |    8 |
| resid_rqa_laminarity    | -0.1482 |    9 |
| minirocket_pc7          |  0.1444 |   10 |

**PC6** (3.0% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| r_squared_improvement |  0.3453 |    1 |
| minirocket_pc2        |  0.3151 |    2 |
| fpca_score_2          |  0.2701 |    3 |
| time_of_trough        | -0.2673 |    4 |
| acrophase_24h         |  0.2394 |    5 |
| time_of_peak          |  0.2214 |    6 |
| amplitude_12h         |  0.2117 |    7 |
| a2_a1_ratio           |  0.2089 |    8 |
| acf_lag144            |  0.2033 |    9 |
| minirocket_pc5        |  0.1871 |   10 |

### 4b. All Features (no MiniROCKET)

![](thew_analysis_2_files/figure-commonmark/pca-4b-1.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-2.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-3.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-4.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-5.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-6.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-7.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-8.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-9.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-10.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-11.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-12.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-13.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-14.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-15.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-16.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-17.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-18.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-19.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-20.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-21.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-22.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-23.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-24.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-25.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-26.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-27.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-28.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-29.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-30.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-31.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-32.png)
![](thew_analysis_2_files/figure-commonmark/pca-4b-33.png)

**PC1** (25.4% variance)

| feature                        | loading | rank |
|:-------------------------------|--------:|-----:|
| rqa_determinism                |  0.1713 |    1 |
| iv                             | -0.1710 |    2 |
| acf_lag1                       |  0.1709 |    3 |
| sample_entropy                 | -0.1670 |    4 |
| trans_entropy                  | -0.1665 |    5 |
| rqa_laminarity                 |  0.1620 |    6 |
| dfa_alpha                      |  0.1616 |    7 |
| trans_diagonal_dominance       |  0.1614 |    8 |
| resid_trans_diagonal_dominance |  0.1595 |    9 |
| resid_trans_entropy            | -0.1566 |   10 |

**PC2** (12.9% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| power_hf              | -0.2254 |    1 |
| resid_power_hf        | -0.2254 |    2 |
| sd                    | -0.2034 |    3 |
| cv                    | -0.1976 |    4 |
| dip_sharpness_descent |  0.1922 |    5 |
| dip_sharpness_ascent  | -0.1921 |    6 |
| amplitude_24h         | -0.1892 |    7 |
| resid_sd              | -0.1853 |    8 |
| peak_trough_diff      | -0.1752 |    9 |
| power_ulf             | -0.1742 |   10 |

**PC3** (9.1% variance)

| feature          | loading | rank |
|:-----------------|--------:|-----:|
| r_squared_1h     | -0.2720 |    1 |
| r_squared_2h     | -0.2488 |    2 |
| acf_lag12        | -0.2286 |    3 |
| acf_lag144       |  0.2273 |    4 |
| acf_first_zero   | -0.2199 |    5 |
| spectral_entropy |  0.2167 |    6 |
| acf_decay_rate   |  0.1964 |    7 |
| power_circ       |  0.1848 |    8 |
| resid_power_circ |  0.1848 |    9 |
| lzc_median       |  0.1826 |   10 |

**PC4** (6.8% variance)

| feature                     | loading | rank |
|:----------------------------|--------:|-----:|
| pe_slope                    |  0.2651 |    1 |
| resid_pe_slope              |  0.2510 |    2 |
| resid_acf_decay_rate        |  0.2317 |    3 |
| resid_circadian_power_ratio | -0.2246 |    4 |
| resid_acf_lag12             | -0.2236 |    5 |
| resid_acf_first_zero        | -0.2208 |    6 |
| perm_entropy                | -0.1998 |    7 |
| pe_tau1                     | -0.1998 |    8 |
| resid_perm_entropy          | -0.1948 |    9 |
| resid_pe_tau1               | -0.1948 |   10 |

**PC5** (4.3% variance)

| feature                 | loading | rank |
|:------------------------|--------:|-----:|
| mesor                   |  0.3336 |    1 |
| fpca_score_1            |  0.3307 |    2 |
| trough_hr               |  0.3273 |    3 |
| resid_rqa_trapping_time | -0.2187 |    4 |
| peak_hr                 |  0.2095 |    5 |
| resid_pe_slope          |  0.2084 |    6 |
| resid_sample_entropy    |  0.2045 |    7 |
| resid_rqa_laminarity    | -0.1830 |    8 |
| perm_entropy            | -0.1735 |    9 |
| pe_tau1                 | -0.1735 |   10 |

**PC6** (3.0% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| r_squared_improvement | -0.3467 |    1 |
| acf_lag144            | -0.2951 |    2 |
| resid_acf_lag12       |  0.2501 |    3 |
| resid_acf_first_zero  |  0.2447 |    4 |
| a2_a1_ratio           | -0.2278 |    5 |
| resid_acf_lag144      | -0.2220 |    6 |
| perm_entropy          | -0.1877 |    7 |
| pe_tau1               | -0.1877 |    8 |
| resid_power_ulf       |  0.1862 |    9 |
| amplitude_12h         | -0.1830 |   10 |

### 4c. Raw Interpretable Only

![](thew_analysis_2_files/figure-commonmark/pca-4c-1.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-2.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-3.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-4.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-5.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-6.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-7.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-8.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-9.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-10.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-11.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-12.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-13.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-14.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-15.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-16.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-17.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-18.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-19.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-20.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-21.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-22.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-23.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-24.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-25.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-26.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-27.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-28.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-29.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-30.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-31.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-32.png)
![](thew_analysis_2_files/figure-commonmark/pca-4c-33.png)

**PC1** (29.1% variance)

| feature                  | loading | rank |
|:-------------------------|--------:|-----:|
| rqa_determinism          |  0.2096 |    1 |
| trans_entropy            | -0.2092 |    2 |
| amplitude_24h            |  0.2052 |    3 |
| spectral_entropy         | -0.2045 |    4 |
| acf_lag1                 |  0.2005 |    5 |
| iv                       | -0.2003 |    6 |
| sample_entropy           | -0.1963 |    7 |
| trans_diagonal_dominance |  0.1953 |    8 |
| power_ulf                |  0.1895 |    9 |
| rqa_laminarity           |  0.1877 |   10 |

**PC2** (12.4% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| power_hf              | -0.2968 |    1 |
| dip_sharpness_ascent  | -0.2762 |    2 |
| dip_sharpness_descent |  0.2749 |    3 |
| power_meso            | -0.2449 |    4 |
| sd                    | -0.2275 |    5 |
| peak_trough_diff      | -0.2246 |    6 |
| power_circ            | -0.2234 |    7 |
| peak_hr               | -0.2107 |    8 |
| cv                    | -0.2097 |    9 |
| amplitude_12h         | -0.2027 |   10 |

**PC3** (8.8% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| higuchi_fd            | -0.2901 |    1 |
| acf_lag144            |  0.2561 |    2 |
| r_squared_1h          | -0.2518 |    3 |
| acf_first_zero        | -0.2485 |    4 |
| dfa_alpha             |  0.2376 |    5 |
| circadian_power_ratio |  0.2335 |    6 |
| acf_decay_rate        |  0.2118 |    7 |
| perm_entropy          | -0.2072 |    8 |
| pe_tau1               | -0.2072 |    9 |
| a2_a1_ratio           |  0.2054 |   10 |

**PC4** (5.5% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| pe_slope              |  0.3649 |    1 |
| perm_entropy          | -0.2961 |    2 |
| pe_tau1               | -0.2961 |    3 |
| mse_slope             |  0.2637 |    4 |
| lzc_running_mean      | -0.2507 |    5 |
| r_squared_improvement | -0.2302 |    6 |
| pe_tau12              |  0.2207 |    7 |
| rqa_entropy           |  0.1722 |    8 |
| trough_hr             | -0.1681 |    9 |
| acf_lag12             | -0.1665 |   10 |

**PC5** (5.1% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| trough_hr             |  0.4677 |    1 |
| mesor                 |  0.4217 |    2 |
| fpca_score_1          |  0.4177 |    3 |
| pe_slope              |  0.2304 |    4 |
| peak_hr               |  0.2118 |    5 |
| perm_entropy          | -0.1626 |    6 |
| pe_tau1               | -0.1626 |    7 |
| circadian_power_ratio | -0.1597 |    8 |
| pe_tau12              |  0.1551 |    9 |
| cv                    | -0.1520 |   10 |

**PC6** (3.9% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| r_squared_improvement |  0.3363 |    1 |
| acrophase_24h         |  0.2994 |    2 |
| fpca_score_2          |  0.2926 |    3 |
| time_of_trough        | -0.2659 |    4 |
| circadian_power_ratio | -0.2657 |    5 |
| pe_tau12              |  0.2652 |    6 |
| time_of_peak          |  0.2635 |    7 |
| pe_slope              |  0.2581 |    8 |
| a2_a1_ratio           |  0.2189 |    9 |
| pe_tau6               |  0.2119 |   10 |

### 4d. Residuals Only

![](thew_analysis_2_files/figure-commonmark/pca-4d-1.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-2.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-3.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-4.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-5.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-6.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-7.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-8.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-9.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-10.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-11.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-12.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-13.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-14.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-15.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-16.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-17.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-18.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-19.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-20.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-21.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-22.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-23.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-24.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-25.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-26.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-27.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-28.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-29.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-30.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-31.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-32.png)
![](thew_analysis_2_files/figure-commonmark/pca-4d-33.png)

**PC1** (34.7% variance)

| feature                        | loading | rank |
|:-------------------------------|--------:|-----:|
| resid_trans_entropy            | -0.2662 |    1 |
| resid_trans_diagonal_dominance |  0.2588 |    2 |
| resid_acf_lag1                 |  0.2433 |    3 |
| resid_spectral_entropy         | -0.2422 |    4 |
| resid_rqa_determinism          |  0.2413 |    5 |
| resid_higuchi_fd               | -0.2404 |    6 |
| resid_dfa_alpha                |  0.2371 |    7 |
| resid_trans_entropy_q1         | -0.2358 |    8 |
| resid_lzc_median               | -0.2352 |    9 |
| resid_trans_entropy_q4         | -0.2351 |   10 |

**PC2** (11.4% variance)

| feature              | loading | rank |
|:---------------------|--------:|-----:|
| resid_pe_slope       |  0.3483 |    1 |
| resid_perm_entropy   | -0.3215 |    2 |
| resid_pe_tau1        | -0.3215 |    3 |
| resid_sd             | -0.2841 |    4 |
| resid_power_circ     | -0.2773 |    5 |
| resid_power_hf       | -0.2591 |    6 |
| resid_power_ulf      | -0.2358 |    7 |
| resid_acf_lag12      | -0.1979 |    8 |
| resid_acf_decay_rate |  0.1964 |    9 |
| resid_pe_tau3        | -0.1936 |   10 |

**PC3** (10.4% variance)

| feature                     | loading | rank |
|:----------------------------|--------:|-----:|
| resid_power_meso            |  0.3687 |    1 |
| resid_power_hf              |  0.3677 |    2 |
| resid_sd                    |  0.3371 |    3 |
| resid_acf_first_zero        | -0.2669 |    4 |
| resid_acf_decay_rate        |  0.2576 |    5 |
| resid_rqa_trapping_time     |  0.2471 |    6 |
| resid_acf_lag12             | -0.2452 |    7 |
| resid_sample_entropy        | -0.2427 |    8 |
| resid_circadian_power_ratio | -0.2290 |    9 |
| resid_rqa_laminarity        |  0.1768 |   10 |

**PC4** (5.2% variance)

| feature            | loading | rank |
|:-------------------|--------:|-----:|
| resid_pe_slope     | -0.4152 |    1 |
| resid_pe_tau1      |  0.3352 |    2 |
| resid_perm_entropy |  0.3352 |    3 |
| resid_power_ulf    | -0.2497 |    4 |
| resid_pe_tau12     | -0.2320 |    5 |
| resid_pe_tau6      | -0.2145 |    6 |
| resid_sd           | -0.2112 |    7 |
| resid_power_circ   | -0.2112 |    8 |
| resid_power_hf     | -0.2034 |    9 |
| resid_acf_lag144   |  0.1954 |   10 |

**PC5** (4.8% variance)

| feature                 | loading | rank |
|:------------------------|--------:|-----:|
| resid_acf_lag12         |  0.3626 |    1 |
| resid_acf_first_zero    |  0.3285 |    2 |
| resid_acf_lag144        | -0.2784 |    3 |
| resid_higuchi_fd        |  0.2677 |    4 |
| resid_rqa_trapping_time |  0.2605 |    5 |
| resid_hfd_instability   | -0.2572 |    6 |
| resid_dfa_alpha         | -0.2219 |    7 |
| resid_rqa_laminarity    |  0.2175 |    8 |
| resid_pe_tau6           |  0.2103 |    9 |
| resid_mse_slope         |  0.2049 |   10 |

**PC6** (3.4% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| resid_dfa_r_squared   |  0.5007 |    1 |
| resid_hfd_instability | -0.3942 |    2 |
| resid_acf_lag144      |  0.3365 |    3 |
| resid_mse_slope       |  0.2949 |    4 |
| resid_pe_tau12        |  0.2744 |    5 |
| resid_power_ulf       | -0.2677 |    6 |
| resid_acf_decay_rate  | -0.2580 |    7 |
| resid_acf_lag12       | -0.1857 |    8 |
| resid_perm_entropy    |  0.1450 |    9 |
| resid_pe_tau1         |  0.1450 |   10 |

### 4e. Interpretable (no Circadian, no MiniROCKET)

![](thew_analysis_2_files/figure-commonmark/pca-4e-1.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-2.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-3.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-4.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-5.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-6.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-7.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-8.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-9.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-10.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-11.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-12.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-13.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-14.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-15.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-16.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-17.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-18.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-19.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-20.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-21.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-22.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-23.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-24.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-25.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-26.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-27.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-28.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-29.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-30.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-31.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-32.png)
![](thew_analysis_2_files/figure-commonmark/pca-4e-33.png)

**PC1** (29.0% variance)

| feature                        | loading | rank |
|:-------------------------------|--------:|-----:|
| resid_trans_entropy            | -0.1875 |    1 |
| resid_trans_diagonal_dominance |  0.1870 |    2 |
| acf_lag1                       |  0.1784 |    3 |
| dfa_alpha                      |  0.1777 |    4 |
| rqa_determinism                |  0.1769 |    5 |
| resid_higuchi_fd               | -0.1760 |    6 |
| higuchi_fd                     | -0.1757 |    7 |
| resid_rqa_determinism          |  0.1751 |    8 |
| resid_acf_lag1                 |  0.1738 |    9 |
| trans_entropy                  | -0.1731 |   10 |

**PC2** (12.3% variance)

| feature            | loading | rank |
|:-------------------|--------:|-----:|
| sd                 | -0.2545 |    1 |
| cv                 | -0.2529 |    2 |
| resid_power_hf     | -0.2512 |    3 |
| power_hf           | -0.2512 |    4 |
| power_ulf          | -0.2250 |    5 |
| resid_sd           | -0.2244 |    6 |
| resid_perm_entropy | -0.2006 |    7 |
| resid_pe_tau1      | -0.2006 |    8 |
| pe_tau1            | -0.1966 |    9 |
| perm_entropy       | -0.1966 |   10 |

**PC3** (8.7% variance)

| feature          | loading | rank |
|:-----------------|--------:|-----:|
| acf_lag12        | -0.2684 |    1 |
| spectral_entropy |  0.2516 |    2 |
| acf_first_zero   | -0.2256 |    3 |
| acf_decay_rate   |  0.2251 |    4 |
| resid_sd         |  0.2231 |    5 |
| acf_lag144       |  0.2225 |    6 |
| resid_power_meso |  0.2194 |    7 |
| power_meso       |  0.2194 |    8 |
| lzc_median       |  0.2134 |    9 |
| resid_power_circ |  0.2108 |   10 |

**PC4** (8.5% variance)

| feature                     | loading | rank |
|:----------------------------|--------:|-----:|
| circadian_power_ratio       |  0.2553 |    1 |
| resid_circadian_power_ratio |  0.2472 |    2 |
| resid_pe_slope              | -0.2447 |    3 |
| pe_slope                    | -0.2427 |    4 |
| resid_acf_decay_rate        | -0.2394 |    5 |
| resid_acf_lag12             |  0.2293 |    6 |
| resid_acf_first_zero        |  0.2231 |    7 |
| pe_tau1                     |  0.1652 |    8 |
| perm_entropy                |  0.1652 |    9 |
| resid_spectral_entropy      | -0.1646 |   10 |

**PC5** (4.2% variance)

| feature                 | loading | rank |
|:------------------------|--------:|-----:|
| resid_pe_slope          |  0.2538 |    1 |
| pe_tau1                 | -0.2522 |    2 |
| perm_entropy            | -0.2522 |    3 |
| resid_rqa_trapping_time | -0.2413 |    4 |
| resid_perm_entropy      | -0.2363 |    5 |
| resid_pe_tau1           | -0.2363 |    6 |
| resid_sample_entropy    |  0.2099 |    7 |
| pe_slope                |  0.2072 |    8 |
| resid_rqa_laminarity    | -0.2033 |    9 |
| resid_rqa_determinism   | -0.1844 |   10 |

**PC6** (3.5% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| resid_acf_lag12       |  0.3612 |    1 |
| resid_acf_first_zero  |  0.3444 |    2 |
| resid_hfd_instability | -0.2445 |    3 |
| hfd_instability       | -0.2311 |    4 |
| higuchi_fd            |  0.2118 |    5 |
| resid_higuchi_fd      |  0.2038 |    6 |
| pe_tau3               |  0.2007 |    7 |
| resid_pe_tau3         |  0.1842 |    8 |
| resid_acf_lag144      | -0.1827 |    9 |
| pe_tau6               |  0.1515 |   10 |

### 4f. Circadian Only

![](thew_analysis_2_files/figure-commonmark/pca-4f-1.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-2.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-3.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-4.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-5.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-6.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-7.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-8.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-9.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-10.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-11.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-12.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-13.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-14.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-15.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-16.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-17.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-18.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-19.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-20.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-21.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-22.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-23.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-24.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-25.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-26.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-27.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-28.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-29.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-30.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-31.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-32.png)
![](thew_analysis_2_files/figure-commonmark/pca-4f-33.png)

**PC1** (29.1% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| peak_hr               |  0.3687 |    1 |
| peak_trough_diff      |  0.3594 |    2 |
| amplitude_24h         |  0.3538 |    3 |
| fpca_score_1          |  0.2908 |    4 |
| dip_sharpness_descent | -0.2845 |    5 |
| mesor                 |  0.2834 |    6 |
| dip_sharpness_ascent  |  0.2818 |    7 |
| amplitude_12h         |  0.2792 |    8 |
| r_squared_2h          |  0.2392 |    9 |
| iv                    | -0.2285 |   10 |

**PC2** (15.7% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| r_squared_1h          |  0.3817 |    1 |
| a2_a1_ratio           | -0.3634 |    2 |
| trough_hr             | -0.3191 |    3 |
| r_squared_improvement | -0.2810 |    4 |
| fpca_score_3          | -0.2721 |    5 |
| mesor                 | -0.2538 |    6 |
| r_squared_2h          |  0.2524 |    7 |
| fpca_score_1          | -0.2405 |    8 |
| acrophase_24h         | -0.2027 |    9 |
| amplitude_24h         |  0.2000 |   10 |

**PC3** (11.0% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| trough_hr             |  0.4742 |    1 |
| mesor                 |  0.3365 |    2 |
| fpca_score_1          |  0.3301 |    3 |
| amplitude_12h         | -0.2900 |    4 |
| dip_sharpness_ascent  | -0.2830 |    5 |
| dip_sharpness_descent |  0.2630 |    6 |
| r_squared_improvement | -0.2248 |    7 |
| peak_trough_diff      | -0.2147 |    8 |
| r_squared_1h          |  0.2098 |    9 |
| acrophase_12h         | -0.1949 |   10 |

**PC4** (8.8% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| fpca_score_2          |  0.4084 |    1 |
| r_squared_2h          |  0.3810 |    2 |
| acrophase_24h         |  0.3740 |    3 |
| time_of_trough        | -0.3585 |    4 |
| iv                    | -0.3364 |    5 |
| dip_sharpness_descent |  0.2582 |    6 |
| r_squared_1h          |  0.2441 |    7 |
| r_squared_improvement |  0.2342 |    8 |
| dip_sharpness_ascent  | -0.2101 |    9 |
| time_of_peak          |  0.1968 |   10 |

**PC5** (7.7% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| r_squared_improvement | -0.4991 |    1 |
| fpca_score_2          |  0.3615 |    2 |
| acrophase_24h         |  0.3166 |    3 |
| a2_a1_ratio           | -0.3097 |    4 |
| time_of_trough        | -0.2937 |    5 |
| dip_sharpness_ascent  |  0.2516 |    6 |
| amplitude_12h         | -0.2499 |    7 |
| iv                    |  0.2264 |    8 |
| dip_sharpness_descent | -0.2192 |    9 |
| r_squared_2h          | -0.2068 |   10 |

**PC6** (5.6% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| acrophase_12h         | -0.7372 |    1 |
| time_of_peak          | -0.3529 |    2 |
| acrophase_24h         |  0.3485 |    3 |
| fpca_score_3          |  0.2913 |    4 |
| trough_hr             | -0.1524 |    5 |
| dip_duration          |  0.1468 |    6 |
| dip_sharpness_descent | -0.1301 |    7 |
| fpca_score_1          | -0.1183 |    8 |
| mesor                 | -0.1104 |    9 |
| a2_a1_ratio           |  0.1042 |   10 |

### 4g. MiniROCKET Only

![](thew_analysis_2_files/figure-commonmark/pca-4g-1.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-2.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-3.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-4.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-5.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-6.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-7.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-8.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-9.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-10.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-11.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-12.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-13.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-14.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-15.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-16.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-17.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-18.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-19.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-20.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-21.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-22.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-23.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-24.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-25.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-26.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-27.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-28.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-29.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-30.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-31.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-32.png)
![](thew_analysis_2_files/figure-commonmark/pca-4g-33.png)

**PC1** (10.0% variance)

| feature         | loading | rank |
|:----------------|--------:|-----:|
| minirocket_pc8  |  0.5180 |    1 |
| minirocket_pc7  |  0.5178 |    2 |
| minirocket_pc3  |  0.5063 |    3 |
| minirocket_pc9  | -0.3188 |    4 |
| minirocket_pc4  |  0.1993 |    5 |
| minirocket_pc6  |  0.1762 |    6 |
| minirocket_pc5  | -0.1542 |    7 |
| minirocket_pc10 |  0.1010 |    8 |
| minirocket_pc2  |  0.0306 |    9 |
| minirocket_pc1  |  0.0001 |   10 |

**PC2** (10.0% variance)

| feature         | loading | rank |
|:----------------|--------:|-----:|
| minirocket_pc5  | -0.6767 |    1 |
| minirocket_pc7  |  0.3924 |    2 |
| minirocket_pc6  | -0.3187 |    3 |
| minirocket_pc3  | -0.2942 |    4 |
| minirocket_pc4  | -0.2504 |    5 |
| minirocket_pc9  | -0.2145 |    6 |
| minirocket_pc10 | -0.2003 |    7 |
| minirocket_pc8  | -0.1966 |    8 |
| minirocket_pc1  | -0.1046 |    9 |
| minirocket_pc2  |  0.0393 |   10 |

**PC3** (10.0% variance)

| feature         | loading | rank |
|:----------------|--------:|-----:|
| minirocket_pc10 |  0.6827 |    1 |
| minirocket_pc9  |  0.5011 |    2 |
| minirocket_pc8  |  0.2654 |    3 |
| minirocket_pc3  | -0.2546 |    4 |
| minirocket_pc5  | -0.2154 |    5 |
| minirocket_pc4  | -0.2126 |    6 |
| minirocket_pc2  |  0.1581 |    7 |
| minirocket_pc7  |  0.1275 |    8 |
| minirocket_pc6  |  0.1165 |    9 |
| minirocket_pc1  | -0.0326 |   10 |

**PC4** (10.0% variance)

| feature         | loading | rank |
|:----------------|--------:|-----:|
| minirocket_pc4  |  0.6043 |    1 |
| minirocket_pc1  | -0.4609 |    2 |
| minirocket_pc6  | -0.3808 |    3 |
| minirocket_pc9  |  0.3588 |    4 |
| minirocket_pc2  | -0.2805 |    5 |
| minirocket_pc3  |  0.1472 |    6 |
| minirocket_pc8  | -0.1451 |    7 |
| minirocket_pc5  | -0.1030 |    8 |
| minirocket_pc10 |  0.0955 |    9 |
| minirocket_pc7  |  0.0865 |   10 |

**PC5** (10.0% variance)

| feature         | loading | rank |
|:----------------|--------:|-----:|
| minirocket_pc2  |  0.5191 |    1 |
| minirocket_pc6  | -0.4891 |    2 |
| minirocket_pc7  | -0.3855 |    3 |
| minirocket_pc10 |  0.3012 |    4 |
| minirocket_pc1  |  0.2781 |    5 |
| minirocket_pc3  |  0.2522 |    6 |
| minirocket_pc9  | -0.2071 |    7 |
| minirocket_pc5  | -0.1928 |    8 |
| minirocket_pc4  |  0.1726 |    9 |
| minirocket_pc8  | -0.0354 |   10 |

**PC6** (10.0% variance)

| feature         | loading | rank |
|:----------------|--------:|-----:|
| minirocket_pc2  | -0.6313 |    1 |
| minirocket_pc1  |  0.6086 |    2 |
| minirocket_pc5  | -0.3178 |    3 |
| minirocket_pc10 |  0.2169 |    4 |
| minirocket_pc8  | -0.2069 |    5 |
| minirocket_pc3  |  0.1353 |    6 |
| minirocket_pc6  |  0.1027 |    7 |
| minirocket_pc7  | -0.0801 |    8 |
| minirocket_pc4  |  0.0697 |    9 |
| minirocket_pc9  |  0.0111 |   10 |

### 4h. Raw Non-Circadian, Non-MiniROCKET

![](thew_analysis_2_files/figure-commonmark/pca-4h-1.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-2.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-3.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-4.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-5.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-6.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-7.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-8.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-9.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-10.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-11.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-12.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-13.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-14.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-15.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-16.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-17.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-18.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-19.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-20.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-21.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-22.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-23.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-24.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-25.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-26.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-27.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-28.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-29.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-30.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-31.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-32.png)
![](thew_analysis_2_files/figure-commonmark/pca-4h-33.png)

**PC1** (33.8% variance)

| feature                  | loading | rank |
|:-------------------------|--------:|-----:|
| trans_entropy            | -0.2621 |    1 |
| rqa_determinism          |  0.2597 |    2 |
| trans_diagonal_dominance |  0.2494 |    3 |
| acf_lag1                 |  0.2463 |    4 |
| spectral_entropy         | -0.2408 |    5 |
| rqa_laminarity           |  0.2393 |    6 |
| sample_entropy           | -0.2375 |    7 |
| lzc_median               | -0.2294 |    8 |
| trans_entropy_q4         | -0.2226 |    9 |
| trans_entropy_q1         | -0.2183 |   10 |

**PC2** (12.2% variance)

| feature      | loading | rank |
|:-------------|--------:|-----:|
| power_hf     | -0.3673 |    1 |
| cv           | -0.3163 |    2 |
| sd           | -0.3118 |    3 |
| pe_tau1      | -0.2885 |    4 |
| perm_entropy | -0.2885 |    5 |
| power_ulf    | -0.2597 |    6 |
| power_meso   | -0.2419 |    7 |
| higuchi_fd   | -0.2355 |    8 |
| pe_tau3      | -0.2168 |    9 |
| power_circ   | -0.2082 |   10 |

**PC3** (9.6% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| power_circ            |  0.3340 |    1 |
| power_meso            |  0.3136 |    2 |
| acf_decay_rate        |  0.3075 |    3 |
| acf_first_zero        | -0.3034 |    4 |
| acf_lag144            |  0.2874 |    5 |
| acf_lag12             | -0.2580 |    6 |
| circadian_power_ratio |  0.2513 |    7 |
| higuchi_fd            | -0.2147 |    8 |
| pe_tau1               | -0.1857 |    9 |
| perm_entropy          | -0.1857 |   10 |

**PC4** (7.7% variance)

| feature               | loading | rank |
|:----------------------|--------:|-----:|
| pe_slope              | -0.4650 |    1 |
| pe_tau12              | -0.3632 |    2 |
| circadian_power_ratio |  0.3180 |    3 |
| pe_tau6               | -0.2605 |    4 |
| pe_tau1               |  0.2525 |    5 |
| perm_entropy          |  0.2525 |    6 |
| dfa_alpha             |  0.2418 |    7 |
| mse_slope             | -0.2233 |    8 |
| lzc_running_mean      |  0.1897 |    9 |
| power_hf              | -0.1716 |   10 |

**PC5** (4.0% variance)

| feature           | loading | rank |
|:------------------|--------:|-----:|
| pe_tau1           | -0.3330 |    1 |
| perm_entropy      | -0.3330 |    2 |
| rqa_trapping_time | -0.3206 |    3 |
| rqa_entropy       | -0.2967 |    4 |
| rqa_laminarity    | -0.2575 |    5 |
| lzc_running_mean  |  0.2444 |    6 |
| hfd_instability   |  0.2352 |    7 |
| mse_slope         | -0.2342 |    8 |
| sample_entropy    |  0.2241 |    9 |
| power_ulf         |  0.2052 |   10 |

**PC6** (3.4% variance)

| feature             | loading | rank |
|:--------------------|--------:|-----:|
| dfa_r_squared       |  0.6961 |    1 |
| pe_tau12            |  0.3192 |    2 |
| rqa_recurrence_rate |  0.2304 |    3 |
| lzc_running_mean    |  0.2185 |    4 |
| acf_decay_rate      | -0.2005 |    5 |
| pe_tau1             |  0.1871 |    6 |
| perm_entropy        |  0.1871 |    7 |
| higuchi_fd          | -0.1774 |    8 |
| rqa_entropy         |  0.1528 |    9 |
| pe_slope            |  0.1505 |   10 |

## 5 Violin Plots

### Key Features Overview

![](thew_analysis_2_files/figure-commonmark/violin-key-1.png)

### Cosinor Features

![](thew_analysis_2_files/figure-commonmark/violin-cosinor-1.png)

### Nonparametric Circadian Features

![](thew_analysis_2_files/figure-commonmark/violin-nonparametric-1.png)

### Spectral / Rhythm Features

![](thew_analysis_2_files/figure-commonmark/violin-spectral-1.png)

### Complexity Features

![](thew_analysis_2_files/figure-commonmark/violin-complexity-1.png)

### Temporal / Autocorrelation Features

![](thew_analysis_2_files/figure-commonmark/violin-temporal-1.png)

### Dynamical / RQA Features

![](thew_analysis_2_files/figure-commonmark/violin-dynamical-1.png)

### Descriptive Features

![](thew_analysis_2_files/figure-commonmark/violin-descriptive-1.png)

### MiniROCKET PCs

![](thew_analysis_2_files/figure-commonmark/violin-minirocket-1.png)

### FPCA Scores

![](thew_analysis_2_files/figure-commonmark/violin-fpca-1.png)

### Residual Spectral Features

![](thew_analysis_2_files/figure-commonmark/violin-resid-spectral-1.png)

### Residual Complexity Features

![](thew_analysis_2_files/figure-commonmark/violin-resid-complexity-1.png)

### Residual Temporal Features

![](thew_analysis_2_files/figure-commonmark/violin-resid-temporal-1.png)

### Residual Dynamical Features

![](thew_analysis_2_files/figure-commonmark/violin-resid-dynamical-1.png)

## 6 Group Comparisons (Kruskal-Wallis)

| feature                        | statistic | p_value |  df |  p_adj |
|:-------------------------------|----------:|--------:|----:|-------:|
| minirocket_pc1                 |    180.13 |    0.00 |   3 | 0.0000 |
| power_hf                       |    175.04 |    0.00 |   3 | 0.0000 |
| resid_power_hf                 |    175.04 |    0.00 |   3 | 0.0000 |
| sd                             |    166.53 |    0.00 |   3 | 0.0000 |
| dip_sharpness_ascent           |    160.63 |    0.00 |   3 | 0.0000 |
| resid_sd                       |    155.55 |    0.00 |   3 | 0.0000 |
| dip_sharpness_descent          |    152.66 |    0.00 |   3 | 0.0000 |
| power_ulf                      |    147.49 |    0.00 |   3 | 0.0000 |
| cv                             |    140.42 |    0.00 |   3 | 0.0000 |
| peak_trough_diff               |    140.18 |    0.00 |   3 | 0.0000 |
| amplitude_24h                  |    133.82 |    0.00 |   3 | 0.0000 |
| peak_hr                        |    127.82 |    0.00 |   3 | 0.0000 |
| power_meso                     |    126.85 |    0.00 |   3 | 0.0000 |
| resid_power_meso               |    126.85 |    0.00 |   3 | 0.0000 |
| fpca_score_1                   |     93.45 |    0.00 |   3 | 0.0000 |
| mesor                          |     91.68 |    0.00 |   3 | 0.0000 |
| power_circ                     |     89.75 |    0.00 |   3 | 0.0000 |
| resid_power_circ               |     89.75 |    0.00 |   3 | 0.0000 |
| fpca_score_3                   |     80.36 |    0.00 |   3 | 0.0000 |
| amplitude_12h                  |     69.92 |    0.00 |   3 | 0.0000 |
| trough_hr                      |     42.89 |    0.00 |   3 | 0.0000 |
| minirocket_pc4                 |     35.63 |    0.00 |   3 | 0.0000 |
| resid_power_ulf                |     35.04 |    0.00 |   3 | 0.0000 |
| minirocket_pc9                 |     32.23 |    0.00 |   3 | 0.0000 |
| rqa_trapping_time              |     28.19 |    0.00 |   3 | 0.0000 |
| r_squared_2h                   |     26.74 |    0.00 |   3 | 0.0000 |
| trans_entropy_q1               |     26.23 |    0.00 |   3 | 0.0000 |
| r_squared_1h                   |     25.70 |    0.00 |   3 | 0.0000 |
| sample_entropy                 |     24.58 |    0.00 |   3 | 0.0001 |
| resid_trans_entropy_q4         |     22.36 |    0.00 |   3 | 0.0002 |
| acf_first_zero                 |     21.56 |    0.00 |   3 | 0.0003 |
| resid_perm_entropy             |     20.91 |    0.00 |   3 | 0.0003 |
| resid_pe_tau1                  |     20.91 |    0.00 |   3 | 0.0003 |
| rqa_determinism                |     20.84 |    0.00 |   3 | 0.0003 |
| acf_lag12                      |     19.94 |    0.00 |   3 | 0.0005 |
| minirocket_pc3                 |     19.10 |    0.00 |   3 | 0.0007 |
| acf_decay_rate                 |     18.90 |    0.00 |   3 | 0.0008 |
| perm_entropy                   |     17.62 |    0.00 |   3 | 0.0014 |
| pe_tau1                        |     17.62 |    0.00 |   3 | 0.0014 |
| spectral_entropy               |     17.07 |    0.00 |   3 | 0.0018 |
| minirocket_pc5                 |     16.22 |    0.00 |   3 | 0.0026 |
| acf_lag144                     |     15.55 |    0.00 |   3 | 0.0034 |
| pe_tau3                        |     15.19 |    0.00 |   3 | 0.0040 |
| acrophase_12h                  |     14.90 |    0.00 |   3 | 0.0045 |
| resid_trans_entropy            |     14.61 |    0.00 |   3 | 0.0050 |
| trans_asymmetry                |     14.21 |    0.00 |   3 | 0.0059 |
| acrophase_24h                  |     12.39 |    0.01 |   3 | 0.0135 |
| resid_pe_tau3                  |     12.34 |    0.01 |   3 | 0.0136 |
| circadian_power_ratio          |     11.66 |    0.01 |   3 | 0.0182 |
| resid_acf_lag1                 |     11.52 |    0.01 |   3 | 0.0190 |
| minirocket_pc6                 |     11.45 |    0.01 |   3 | 0.0193 |
| fpca_score_2                   |     11.13 |    0.01 |   3 | 0.0219 |
| resid_lzc_running_mean         |     10.31 |    0.02 |   3 | 0.0309 |
| resid_rqa_determinism          |     10.29 |    0.02 |   3 | 0.0309 |
| trans_entropy                  |      9.68 |    0.02 |   3 | 0.0402 |
| resid_trans_diagonal_dominance |      9.49 |    0.02 |   3 | 0.0432 |
| resid_pe_slope                 |      9.26 |    0.03 |   3 | 0.0470 |

Features with significant Kruskal-Wallis test (BH-adjusted p \< 0.05)

**Total significant (BH p \< 0.05):** NA / 104 features.

### Median by group for significant features

| feature                        |  Healthy |       CAD | CAD_Diabetes |     ESRD |
|:-------------------------------|---------:|----------:|-------------:|---------:|
| minirocket_pc1                 |  -4.3942 |    1.4681 |       2.4883 |   3.4953 |
| power_hf                       |  34.1585 |   13.5206 |       9.9089 |  10.2114 |
| resid_power_hf                 |  34.1585 |   13.5206 |       9.9089 |  10.2114 |
| sd                             |  13.2231 |    7.8226 |       6.9116 |   6.1056 |
| dip_sharpness_ascent           |  47.4100 |   27.8600 |      25.2879 |  22.1300 |
| resid_sd                       |   9.1414 |    5.7530 |       5.3429 |   5.0601 |
| dip_sharpness_descent          | -40.5000 |  -25.1900 |     -20.1950 | -21.3900 |
| power_ulf                      |  58.9329 |   18.0401 |      15.3983 |   8.6116 |
| cv                             |   0.1784 |    0.1196 |       0.1056 |   0.0815 |
| peak_trough_diff               |  40.6921 |   25.6325 |      24.0275 |  21.6492 |
| amplitude_24h                  |  11.8337 |    6.2060 |       5.8095 |   3.5962 |
| peak_hr                        | 100.6496 |   81.6808 |      82.2650 |  86.7933 |
| power_meso                     |  20.3789 |    9.2816 |       6.9572 |   7.4935 |
| resid_power_meso               |  20.3789 |    9.2816 |       6.9572 |   7.4935 |
| fpca_score_1                   | 253.0332 | -194.9112 |    -197.5820 | 115.2611 |
| mesor                          |  77.6593 |   66.0967 |      66.2799 |  74.7039 |
| power_circ                     |  16.4419 |    7.2989 |       6.3577 |   4.8001 |
| resid_power_circ               |  16.4419 |    7.2989 |       6.3577 |   4.8001 |
| fpca_score_3                   | -70.3969 |   -2.8417 |      49.6584 | 149.7798 |
| amplitude_12h                  |   5.7192 |    3.2906 |       2.7913 |   2.1576 |
| trough_hr                      |  59.7558 |   55.0225 |      57.5033 |  64.5567 |
| minirocket_pc4                 |  -0.2073 |    0.5653 |       0.3214 |  -0.8475 |
| resid_power_ulf                |   2.4606 |    1.2736 |       0.9207 |   1.1150 |
| minirocket_pc9                 |  -0.0644 |    0.1201 |       0.0649 |  -0.5255 |
| rqa_trapping_time              |   3.9922 |    3.6399 |       3.7554 |   3.5450 |
| r_squared_2h                   |   0.5108 |    0.4420 |       0.4162 |   0.3565 |
| trans_entropy_q1               |   0.4393 |    0.5255 |       0.5281 |   0.5480 |
| r_squared_1h                   |   0.4004 |    0.3215 |       0.3393 |   0.2157 |
| sample_entropy                 |   0.8941 |    1.0224 |       1.0415 |   1.0506 |
| resid_trans_entropy_q4         |   0.8017 |    0.7752 |       0.7683 |   0.7157 |
| acf_first_zero                 |   4.7917 |    4.1667 |       4.7917 |   3.3333 |
| resid_perm_entropy             |   0.9912 |    0.9902 |       0.9874 |   0.9848 |
| resid_pe_tau1                  |   0.9912 |    0.9902 |       0.9874 |   0.9848 |
| rqa_determinism                |   0.7566 |    0.7281 |       0.7357 |   0.7169 |
| acf_lag12                      |   0.4803 |    0.4245 |       0.4334 |   0.3575 |
| minirocket_pc3                 |  -0.3490 |   -0.2703 |      -0.1792 |   0.8487 |
| acf_decay_rate                 |   0.0383 |    0.0480 |       0.0482 |   0.0593 |
| perm_entropy                   |   0.9920 |    0.9906 |       0.9885 |   0.9857 |
| pe_tau1                        |   0.9920 |    0.9906 |       0.9885 |   0.9857 |
| spectral_entropy               |   0.5605 |    0.6073 |       0.6052 |   0.6240 |
| minirocket_pc5                 |  -0.1690 |    0.2386 |      -0.1061 |  -0.3615 |
| acf_lag144                     |  -0.1596 |   -0.1187 |      -0.1488 |  -0.0606 |
| pe_tau3                        |   0.9904 |    0.9908 |       0.9892 |   0.9854 |
| acrophase_12h                  |   8.4950 |    8.5096 |       7.0436 |   5.3942 |
| resid_trans_entropy            |   1.6559 |    1.6266 |       1.6235 |   1.5308 |
| trans_asymmetry                |   0.0084 |    0.0106 |       0.0141 |   0.0115 |
| acrophase_24h                  |   3.9613 |    4.1516 |       4.9608 |   8.9076 |
| resid_pe_tau3                  |   0.9907 |    0.9899 |       0.9903 |   0.9846 |
| circadian_power_ratio          |   0.1311 |    0.1422 |       0.1830 |   0.1493 |
| resid_acf_lag1                 |   0.5749 |    0.5933 |       0.5918 |   0.6754 |
| minirocket_pc6                 |   0.1038 |   -0.1431 |      -0.0651 |  -0.0353 |
| fpca_score_2                   | -46.2116 |    0.5128 |     -42.5691 |  34.2471 |
| resid_lzc_running_mean         |  37.0000 |   37.0000 |      37.0000 |  36.0000 |
| resid_rqa_determinism          |   0.6654 |    0.6560 |       0.6691 |   0.6916 |
| trans_entropy                  |   1.2960 |    1.3904 |       1.3588 |   1.4010 |
| resid_trans_diagonal_dominance |   0.5299 |    0.5300 |       0.5432 |   0.5719 |
| resid_pe_slope                 |  -0.0001 |    0.0000 |       0.0006 |   0.0021 |

Median values by condition for significant features

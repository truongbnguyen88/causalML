# LaLonde Job Training Dataset

## Overview

The LaLonde dataset is one of the most widely used datasets in causal inference, originating from a real randomized experiment evaluating a job training program.

## Source

- **Primary Paper**: Lalonde, R. (1986). ["Evaluating the Econometric Evaluations of Training Programs with Experimental Data"](https://www.jstor.org/stable/1806062). *American Economic Review*, 76(4), 604-620.
- **Secondary Analysis**: Dehejia, R. and Wahba, S. (1999). ["Causal Effects in Non-Experimental Studies: Reevaluating the Evaluation of Training Programs"](https://www.tandfonline.com/doi/abs/10.1080/01621459.1999.10473858). *Journal of the American Statistical Association*, 94(448), 1053-1062.
- **Data Repository**: [NBER - Rajeev Dehejia](https://users.nber.org/~rdehejia/data/.nswdata2.html)

## Description

### The Program

The **National Supported Work (NSW) Demonstration** was a federally funded program in the mid-1970s designed to provide work experience to individuals who faced economic and social problems prior to enrollment. The program offered subsidized employment for 9-18 months.

### The Experiment

- **Treatment**: Participation in the NSW job training program
- **Outcome**: Real earnings in 1978 (RE78)
- **Sample**: Male participants from the NSW demonstration

### Causal Question

**What is the causal effect of job training on subsequent earnings?**

## Dataset Variants

This directory contains several versions of the data:

### 1. Experimental Data (`nsw_experimental.csv`)
- **Treated units**: 185 participants randomly assigned to the NSW program
- **Control units**: 260 participants randomly assigned to the control group
- **Total**: 445 observations
- **Setting**: Randomized experiment (gold standard)
- **Use for**: Estimating the true causal effect

### 2. Observational Data (`nsw_psid_observational.csv`)
- **Treated units**: 185 NSW participants (same as above)
- **Control units**: 2,490 individuals from PSID (Panel Study of Income Dynamics)
- **Total**: 2,675 observations
- **Setting**: Observational study (treated vs. non-experimental comparison group)
- **Use for**: Demonstrating the need for causal inference methods (backdoor adjustment, propensity scores, etc.)

The observational setting creates **confounding** because PSID controls differ systematically from NSW participants (education, prior earnings, demographics, etc.)

## Variables

| Variable | Description | Type |
|----------|-------------|------|
| `treat` | Treatment indicator (1=participated in NSW, 0=control) | Binary |
| `age` | Age in years | Continuous |
| `education` | Years of schooling | Continuous |
| `black` | 1 if Black, 0 otherwise | Binary |
| `hispanic` | 1 if Hispanic, 0 otherwise | Binary |
| `married` | 1 if married, 0 otherwise | Binary |
| `nodegree` | 1 if no high school degree, 0 otherwise | Binary |
| `re74` | Real earnings in 1974 (pre-treatment) | Continuous |
| `re75` | Real earnings in 1975 (pre-treatment) | Continuous |
| `re78` | Real earnings in 1978 (outcome) | Continuous |

**Notes:**
- Earnings are in 1978 dollars
- RE74 and RE75 are pre-treatment covariates (measured before program participation)
- RE78 is the outcome measured after program completion

## Causal Graph (Observational Setting)

```
Demographics (Age, Education, Race)
         ↓                    ↓
    NSW Participation  →  Earnings (1978)
         ↑                    ↑
    Prior Earnings (RE74, RE75)
```

**Confounders**: Age, education, race, marital status, prior earnings
- These variables affect both the likelihood of participating in NSW AND future earnings
- In the observational setting, we must control for these to estimate the causal effect

## Known Results

### Experimental Estimate (Benchmark)
Using the randomized experimental data:
- **ATE ≈ $1,794** (Lalonde 1986)
- This is the "true" causal effect from randomization

### Naive Observational Estimate
Comparing NSW participants to PSID controls without adjustment:
- **Biased estimate**: Negative or very small effect (wrong!)
- **Reason**: PSID controls have higher education and prior earnings than NSW participants

### Adjusted Observational Estimate
Using propensity score matching or regression adjustment with confounders:
- **Can recover** estimates close to the experimental benchmark
- **Demonstrates**: Proper causal inference methods work when assumptions hold

## Usage Examples

### Loading the Data

```python
import pandas as pd

# Load experimental data (randomized)
df_exp = pd.read_csv('datasets/lalonde/nsw_experimental.csv')

# Load observational data (with confounding)
df_obs = pd.read_csv('datasets/lalonde/nsw_psid_observational.csv')

print(f"Experimental data: {len(df_exp)} observations")
print(f"Observational data: {len(df_obs)} observations")
```

### Basic Analysis

```python
# Experimental estimate (true causal effect)
treated_exp = df_exp[df_exp['treat'] == 1]['re78'].mean()
control_exp = df_exp[df_exp['treat'] == 0]['re78'].mean()
ate_exp = treated_exp - control_exp
print(f"Experimental ATE: ${ate_exp:,.2f}")

# Naive observational estimate (biased!)
treated_obs = df_obs[df_obs['treat'] == 1]['re78'].mean()
control_obs = df_obs[df_obs['treat'] == 0]['re78'].mean()
ate_naive = treated_obs - control_obs
print(f"Naive observational estimate: ${ate_naive:,.2f}")
```

## Pedagogical Value

This dataset is ideal for teaching causal inference because:

1. **Known ground truth**: The experimental data provides the true causal effect
2. **Realistic confounding**: The observational version shows real-world selection bias
3. **Moderate size**: Not too large (easy to explore), not too small (stable estimates)
4. **Classic example**: Widely used in textbooks and papers
5. **Economic interpretation**: Clear policy relevance (job training effectiveness)

## Use in Modules

- **Module 2 (Identification)**: Demonstrate backdoor criterion and adjustment sets
- **Module 3 (Estimation Basics)**: Regression adjustment, stratification
- **Module 4 (Propensity Scores)**: Propensity score matching, IPW, doubly robust
- **Module 7 (Advanced)**: Sensitivity analysis

## Files in This Directory

- `README.md`: This file
- `download_data.py`: Script to download data from NBER
- `nsw_experimental.csv`: Experimental data (445 obs)
- `nsw_psid_observational.csv`: Observational data (2,675 obs)
- `nsw_treated.csv`: NSW treated units only (185 obs)
- `nsw_control.csv`: NSW control units only (260 obs)
- `psid_controls.csv`: PSID control units (2,490 obs)

## Download Instructions

To download the data:

```bash
cd datasets/lalonde
python download_data.py
```

Or manually download from: [NBER Data Repository](https://users.nber.org/~rdehejia/data/.nswdata2.html)

## References

1. Lalonde, R. J. (1986). Evaluating the econometric evaluations of training programs with experimental data. *American Economic Review*, 76(4), 604-620.

2. Dehejia, R. H., & Wahba, S. (1999). Causal effects in nonexperimental studies: Reevaluating the evaluation of training programs. *Journal of the American Statistical Association*, 94(448), 1053-1062.

3. Dehejia, R. H., & Wahba, S. (2002). Propensity score-matching methods for nonexperimental causal studies. *Review of Economics and Statistics*, 84(1), 151-161.

## Citation

If you use this dataset in publications, please cite:

```
Lalonde, R. J. (1986). Evaluating the econometric evaluations of 
training programs with experimental data. American Economic Review, 
76(4), 604-620.
```

## License

This data is publicly available for research and educational purposes. Please cite the original sources when using the data.

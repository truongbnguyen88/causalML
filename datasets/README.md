# Datasets for Causal Inference Learning

This directory contains curated datasets for practicing causal inference methods throughout the course.

## Dataset Overview

### 1. LaLonde Dataset (`lalonde/`)
**Source**: LaLonde (1986), Dehejia & Wahba (1999)  
**Description**: Job training program evaluation (National Supported Work Demonstration)  
**Size**: ~600 observations  
**Treatment**: Job training program participation  
**Outcome**: Real earnings in 1978  
**Use Cases**: 
- Propensity score matching
- Basic causal effect estimation
- Benchmark for observational study methods

**Files**:
- `lalonde.csv` - Main dataset
- `lalonde_description.md` - Variable descriptions and background

### 2. IHDP Dataset (`ihdp/`)
**Source**: Infant Health and Development Program (Hill, 2011)  
**Description**: Randomized experiment on early childhood intervention  
**Size**: ~600 observations  
**Treatment**: Home visits by specialists  
**Outcome**: Child IQ score at age 3  
**Use Cases**:
- Heterogeneous treatment effects
- CATE estimation benchmarking
- Method comparison (known ground truth)

**Files**:
- `ihdp.csv` - Main dataset
- `ihdp_description.md` - Variable descriptions

### 3. Twins Dataset (`twins/`)
**Source**: Twin births mortality study  
**Description**: Mortality outcomes for twin births  
**Size**: ~10,000+ observations  
**Treatment**: Being born lighter/heavier  
**Outcome**: Mortality within first year  
**Use Cases**:
- Natural experiments
- Larger-scale causal estimation
- Sensitivity analysis

**Files**:
- `twins.csv` - Main dataset
- `twins_description.md` - Variable descriptions

### 4. Criteo Uplift Dataset (`criteo/`)
**Source**: Criteo AI Lab (2018)  
**Description**: Online advertising campaign randomized trial  
**Size**: ~13M observations (sampled versions available)  
**Treatment**: Showing ad vs no ad  
**Outcome**: Conversion/visit  
**Use Cases**:
- Uplift modeling
- Large-scale heterogeneous effects
- Marketing applications

**Files**:
- `criteo_sample_10k.csv` - Small sample (10k rows)
- `criteo_sample_100k.csv` - Medium sample (100k rows)
- `criteo_description.md` - Variable descriptions
- `download_full.py` - Script to download full dataset

### 5. Synthetic Datasets (`synthetic/`)
**Description**: Simulated data with known ground truth treatment effects  
**Use Cases**:
- Method validation
- Understanding bias and variance
- Educational examples

**Files**:
- `linear_synthetic.csv` - Simple linear DGP
- `nonlinear_synthetic.csv` - Non-linear relationships
- `heterogeneous_synthetic.csv` - Heterogeneous effects
- `confounded_synthetic.csv` - Strong confounding
- `generate_synthetic.py` - Data generation scripts
- `synthetic_description.md` - DGP specifications

## Usage Guidelines

### Loading Data in Python

```python
import pandas as pd

# LaLonde dataset
lalonde = pd.read_csv('datasets/lalonde/lalonde.csv')

# IHDP dataset
ihdp = pd.read_csv('datasets/ihdp/ihdp.csv')

# Synthetic data
synthetic = pd.read_csv('datasets/synthetic/linear_synthetic.csv')
```

### Dataset Selection by Module

- **Modules 1-3**: Start with synthetic data, then LaLonde
- **Module 4**: LaLonde (propensity scores), IHDP
- **Module 5**: All datasets for method comparison
- **Module 6**: IHDP, Criteo (heterogeneous effects)
- **Module 7**: Twins (sensitivity), synthetic (discovery)
- **Module 8**: Criteo (marketing), LaLonde (policy), all for projects

## Data Preparation Notes

### Missing Data
Some datasets have missing values. Handle appropriately:
- Imputation (mean, median, model-based)
- Complete case analysis (if missingness is ignorable)
- Document your approach

### Train/Test Splits
For predictive models (e.g., meta-learners):
- Use cross-validation for hyperparameter tuning
- Hold out test set for final evaluation
- For causal effect estimation, use entire sample when appropriate

### Covariate Scaling
Some methods benefit from scaled features:
- Standardize continuous variables (mean=0, sd=1) for matching
- Keep binary variables as 0/1
- Document transformations

## Citations

**LaLonde**:
- LaLonde, R. J. (1986). Evaluating the econometric evaluations of training programs with experimental data. American Economic Review, 76(4), 604-620.
- Dehejia, R. H., & Wahba, S. (1999). Causal effects in nonexperimental studies: Reevaluating the evaluation of training programs. Journal of the American Statistical Association, 94(448), 1053-1062.

**IHDP**:
- Hill, J. L. (2011). Bayesian nonparametric modeling for causal inference. Journal of Computational and Graphical Statistics, 20(1), 217-240.

**Criteo**:
- Diemert, E., Betlei, A., Renaudin, C., & Amini, M. R. (2018). A large scale benchmark for uplift modeling. ACM SIGKDD Conference on Knowledge Discovery and Data Mining.

## Adding New Datasets

When adding datasets:
1. Create subdirectory with dataset name
2. Include CSV file(s)
3. Add description markdown file with:
   - Source and citation
   - Variable descriptions
   - Treatment and outcome definitions
   - Suggested use cases
4. Update this README with dataset information

## License & Usage

Datasets are provided for educational purposes. Please cite original sources when using in publications or presentations.

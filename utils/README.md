# Utilities for Causal Inference

This directory contains reusable code for common causal inference tasks used throughout the course.

## Module Overview

### `data_generation.py`
Generate synthetic datasets with known causal structures.

**Functions**:
- `generate_simple_dag()` - Basic confounded treatment-outcome
- `generate_heterogeneous_data()` - Variable treatment effects
- `generate_iv_data()` - Instrumental variable structure
- `generate_mediation_data()` - Mediation analysis
- `generate_rdd_data()` - Regression discontinuity
- `generate_did_data()` - Difference-in-differences panel data

**Example**:
```python
from utils.data_generation import generate_heterogeneous_data

df, true_cate = generate_heterogeneous_data(
    n=1000, 
    treatment_effect_fn=lambda x: 2 + 3*x[:, 0]  # Effect varies with X1
)
```

### `evaluation.py`
Metrics and evaluation functions for causal inference methods.

**Functions**:
- `calc_ate()` - Compute Average Treatment Effect
- `calc_att()` - Average Treatment effect on the Treated
- `calc_pehe()` - Precision in Estimation of Heterogeneous Effect
- `calc_bias()` - Bias of estimator
- `calc_rmse()` - Root Mean Squared Error
- `calc_coverage()` - Confidence interval coverage
- `qini_curve()` - Qini curve for uplift models
- `uplift_curve()` - Uplift curve and AUUC

**Example**:
```python
from utils.evaluation import calc_pehe, calc_ate

# Compare estimated vs true CATE
pehe = calc_pehe(estimated_cate, true_cate)

# Estimate ATE
ate = calc_ate(y, treatment, method='ipw', ps=propensity_scores)
```

### `visualization.py`
Plotting functions for causal inference analysis.

**Functions**:
- `plot_dag()` - Visualize causal graphs
- `plot_treatment_distribution()` - Covariate balance plots
- `plot_love_plot()` - Standardized mean differences
- `plot_propensity_overlap()` - Propensity score distributions
- `plot_cate_distribution()` - CATE estimates
- `plot_uplift_curve()` - Uplift and Qini curves
- `plot_policy_value()` - Policy learning evaluation
- `plot_sensitivity()` - Sensitivity analysis results

**Example**:
```python
from utils.visualization import plot_love_plot, plot_cate_distribution

# Check covariate balance
plot_love_plot(df, treatment_col='T', covariates=['X1', 'X2', 'X3'])

# Visualize heterogeneous effects
plot_cate_distribution(cate_estimates, feature=df['age'])
```

### `estimators.py`
Common causal effect estimators implemented from scratch (for learning).

**Classes**:
- `SLearner` - Single model meta-learner
- `TLearner` - Two model meta-learner
- `XLearner` - X-learner meta-learner
- `IPWEstimator` - Inverse Probability Weighting
- `DREstimator` - Doubly Robust estimator
- `RegressionAdjustment` - Outcome regression
- `MatchingEstimator` - Propensity score matching

**Example**:
```python
from utils.estimators import TLearner
from sklearn.ensemble import RandomForestRegressor

# T-learner with random forests
tlearner = TLearner(model=RandomForestRegressor(n_estimators=100))
tlearner.fit(X, y, treatment)
cate = tlearner.predict(X_test)
```

### `balance_checks.py`
Functions for assessing covariate balance in observational studies.

**Functions**:
- `calc_smd()` - Standardized mean difference
- `calc_variance_ratio()` - Variance ratio
- `calc_ks_statistic()` - Kolmogorov-Smirnov statistic
- `check_overlap()` - Propensity score overlap
- `balance_table()` - Generate balance table
- `assess_balance()` - Comprehensive balance assessment

**Example**:
```python
from utils.balance_checks import balance_table, assess_balance

# Before matching
balance_before = balance_table(df, treatment_col='T', covariates=X_cols)

# After matching
balance_after = balance_table(df_matched, treatment_col='T', covariates=X_cols)

# Overall assessment
assessment = assess_balance(balance_after, threshold=0.1)
print(f"Balance achieved: {assessment['balanced']}")
```

## Installation Requirements

The utility functions depend on:

```python
# Core dependencies
numpy>=1.21.0
pandas>=1.3.0
scipy>=1.7.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0

# Graph visualization
networkx>=2.6.0
graphviz>=0.17

# Optional (for specific functions)
statsmodels>=0.13.0
causalml>=0.12.0
econml>=0.13.0
```

## Usage Pattern

Import utilities at the top of your notebooks:

```python
# Standard imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Causal ML utilities
from utils.data_generation import generate_heterogeneous_data
from utils.evaluation import calc_pehe, calc_ate
from utils.visualization import plot_cate_distribution
from utils.estimators import TLearner
from utils.balance_checks import balance_table
```

## Development Guidelines

When adding new utilities:

1. **Document thoroughly** - Include docstrings with parameters, returns, and examples
2. **Add type hints** - Use Python type annotations
3. **Write tests** - Add unit tests in `tests/` directory
4. **Keep focused** - Each function should do one thing well
5. **Avoid dependencies on course-specific data** - Keep utilities general

## Examples Directory

See `examples/` subdirectory for detailed usage examples:
- `example_data_generation.ipynb` - Generating synthetic data
- `example_evaluation.ipynb` - Evaluating causal estimators
- `example_visualization.ipynb` - Visualizing results
- `example_estimators.ipynb` - Using custom estimators

## Contributing

To contribute a new utility:
1. Add function to appropriate module
2. Include comprehensive docstring
3. Add example to examples directory
4. Update this README

## Citation

If you use these utilities in research, please cite:
```
CausalML Learning Repository (2026)
https://github.com/yourusername/causalML
```

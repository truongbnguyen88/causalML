# Module 5: Causal Machine Learning Algorithms

## Overview
Apply modern machine learning methods to causal effect estimation, including meta-learners, causal forests, and double/debiased machine learning.

## Learning Objectives
- Implement meta-learners (S-learner, T-learner, X-learner)
- Use Causal Forests and Generalized Random Forests
- Apply Bayesian Additive Regression Trees (BART) for causal inference
- Understand Targeted Maximum Likelihood Estimation (TMLE)
- Implement Double/Debiased Machine Learning (DML)
- Compare different causal ML methods

## Contents

### Methods & Implementation
- `01_meta_learners.ipynb` - S/T/X-learner implementations
- `02_causal_forests.ipynb` - Using GRF and EconML
- `03_bart_causal.ipynb` - BART for causal inference
- `04_tmle.ipynb` - TMLE implementation
- `05_double_ml.ipynb` - DML framework with cross-fitting
- `06_comparison.ipynb` - Comparing methods on benchmark datasets

### Exercises
- `exercises/` - Practice problems with solutions

## Key Concepts

**Meta-Learners**:
- S-learner: Single model with treatment as feature
- T-learner: Separate models for treated/control
- X-learner: Combines models with propensity scores

**Causal Forests**:
- Extension of random forests for heterogeneous effects
- Honest splitting for valid inference
- Provides confidence intervals

**BART (Bayesian Additive Regression Trees)**:
- Bayesian ensemble of trees
- Automatic regularization
- Uncertainty quantification

**TMLE (Targeted Maximum Likelihood Estimation)**:
- Doubly robust with ML models
- Targets specific estimand
- Valid asymptotic inference

**Double/Debiased ML**:
- Uses cross-fitting to avoid overfitting bias
- Combines ML flexibility with valid inference
- Neyman orthogonality for robustness

## Estimated Time
**4 weeks** (16-20 hours total)

## Prerequisites
- Module 1-4 completed
- Familiarity with scikit-learn
- Understanding of random forests and gradient boosting

## Next Module
[Module 6: Heterogeneous Treatment Effects](../06_heterogeneous_effects/)

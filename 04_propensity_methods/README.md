# Module 4: Propensity Score Methods

## Overview
Master propensity score techniques for handling confounding in observational studies through matching, weighting, and doubly robust estimation.

## Learning Objectives
- Understand propensity score theory and estimation
- Implement propensity score matching algorithms
- Use Inverse Probability Weighting (IPW)
- Apply doubly robust estimation methods
- Assess covariate balance

## Contents

### Theory & Methods
- `01_propensity_scores.md` - Theory, assumptions, and intuition
- `02_ps_matching.ipynb` - Matching algorithms (nearest neighbor, caliper, optimal)
- `03_ipw.ipynb` - Inverse Probability Weighting implementation
- `04_doubly_robust.ipynb` - Doubly robust estimators
- `05_balance_diagnostics.ipynb` - Assessing and visualizing balance

### Exercises
- `exercises/` - Practice problems with solutions

## Key Concepts

**Propensity Score**: e(X) = P(T=1|X) - probability of treatment given covariates

**Matching**:
- Pair treated units with similar control units
- Common methods: nearest neighbor, caliper, kernel

**Inverse Probability Weighting**:
- Weight by inverse of propensity score
- Creates pseudo-population where treatment is random

**Doubly Robust Estimation**:
- Combines outcome regression and propensity scores
- Consistent if either model is correct

**Balance Diagnostics**:
- Standardized mean differences
- Variance ratios
- Visual inspection (love plots, QQ plots)

## Estimated Time
**2 weeks** (10-12 hours total)

## Prerequisites
- Module 1: Foundations of Causal Inference
- Module 2: Causal Identification
- Module 3: Basic Estimation Methods

## Next Module
[Module 5: Causal Machine Learning Algorithms](../05_causal_ml_algorithms/)

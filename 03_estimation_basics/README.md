# Module 3: Basic Estimation Methods

## Overview
Implement fundamental techniques for estimating causal effects from data, including regression-based and design-based approaches.

## Learning Objectives
- Estimate Average Treatment Effects (ATE)
- Compute Conditional Average Treatment Effects (CATE)
- Use regression adjustment for causal estimation
- Apply stratification and subclassification
- Implement Difference-in-Differences (DiD)
- Use Regression Discontinuity Design (RDD)

## Contents

### Methods & Implementation
- `01_ate_estimation.ipynb` - Computing ATE using regression
- `02_stratification.ipynb` - Stratification methods
- `03_diff_in_diff.ipynb` - Difference-in-Differences implementation
- `04_regression_discontinuity.ipynb` - RDD examples and applications

### Exercises
- `exercises/` - Practice problems with solutions

## Key Concepts

**Average Treatment Effect (ATE)**: E[Y(1) - Y(0)]

**Regression Adjustment**:
- Control for confounders via regression
- Assumes linear relationships and correct model specification

**Stratification**:
- Divide data into homogeneous strata
- Estimate effects within strata, then aggregate

**Difference-in-Differences**:
- Requires treatment and control groups, pre/post periods
- Assumes parallel trends

**Regression Discontinuity**:
- Treatment determined by threshold
- Compares units just above/below cutoff

## Estimated Time
**2 weeks** (10-12 hours total)

## Prerequisites
- Module 1: Foundations of Causal Inference
- Module 2: Causal Identification

## Next Module
[Module 4: Propensity Score Methods](../04_propensity_methods/)

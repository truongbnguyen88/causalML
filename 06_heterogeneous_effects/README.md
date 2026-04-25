# Module 6: Heterogeneous Treatment Effects

## Overview
Discover and estimate how treatment effects vary across individuals and subgroups, and learn to optimize treatment assignment.

## Learning Objectives
- Estimate Conditional Average Treatment Effects (CATE)
- Build uplift models for customer targeting
- Analyze treatment effect heterogeneity
- Compute Group Average Treatment Effects (GATE)
- Learn optimal treatment assignment policies

## Contents

### Methods & Applications
- `01_cate_estimation.ipynb` - CATE estimation methods
- `02_uplift_modeling.ipynb` - Uplift modeling for marketing
- `03_heterogeneity_analysis.ipynb` - Analyzing and visualizing variation
- `04_policy_learning.ipynb` - Learning optimal treatment rules

### Exercises
- `exercises/` - Practice problems with solutions

## Key Concepts

**CATE (Conditional Average Treatment Effect)**:
- τ(x) = E[Y(1) - Y(0) | X = x]
- Treatment effect as function of covariates
- Requires strong assumptions or experimental data

**Uplift Modeling**:
- Identify individuals most responsive to treatment
- Four customer segments: persuadables, sure things, lost causes, sleeping dogs
- Optimize targeting decisions

**Heterogeneity Analysis**:
- Best Linear Projection (BLP) for overall heterogeneity
- GATE (Group Average Treatment Effects) for discrete groups
- Variable importance for effect modifiers

**Policy Learning**:
- Learn decision rules that maximize welfare
- Counterfactual policy evaluation
- Regret minimization

## Estimated Time
**2 weeks** (10-12 hours total)

## Prerequisites
- Module 5: Causal Machine Learning Algorithms
- Understanding of CATE estimation

## Next Module
[Module 7: Advanced Topics](../07_advanced_topics/)

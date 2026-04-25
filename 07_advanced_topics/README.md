# Module 7: Advanced Topics

## Overview
Explore cutting-edge methods and handle complex scenarios including mediation, time-varying treatments, synthetic controls, and causal discovery.

## Learning Objectives
- Decompose effects into direct and indirect (mediation analysis)
- Handle time-varying treatments with Marginal Structural Models
- Apply synthetic control methods for comparative case studies
- Conduct sensitivity analysis for unmeasured confounding
- Understand partial identification and bounds
- Explore causal discovery algorithms
- Generate counterfactual predictions

## Contents

### Advanced Methods
- `01_mediation_analysis.ipynb` - Direct and indirect effects
- `02_time_varying_treatments.ipynb` - MSM and g-formula
- `03_synthetic_control.ipynb` - Synthetic control implementation
- `04_sensitivity_analysis.ipynb` - Robustness checks and bounds
- `05_causal_discovery.ipynb` - Learning DAGs from data
- `06_counterfactuals.ipynb` - Counterfactual inference

### Exercises
- `exercises/` - Practice problems with solutions

## Key Concepts

**Mediation Analysis**:
- Direct effect: T → Y
- Indirect effect: T → M → Y
- Natural vs controlled mediation

**Time-Varying Treatments**:
- Treatment varies over time
- Time-varying confounding
- Marginal Structural Models with IPTW

**Synthetic Control**:
- Create synthetic control from donor pool
- Compare treated unit to synthetic
- Requires pre-treatment fit and parallel trends

**Sensitivity Analysis**:
- E-values for unmeasured confounding
- Rosenbaum bounds
- Partial identification when assumptions fail

**Causal Discovery**:
- PC algorithm, GES, LiNGAM
- Learning DAG structure from data
- Strong assumptions required

**Counterfactuals**:
- What would have happened under different treatment
- Individual-level predictions
- Requires structural assumptions

## Estimated Time
**2 weeks** (10-12 hours total)

## Prerequisites
- Modules 1-6 completed
- Solid understanding of causal identification

## Next Module
[Module 8: Real-World Applications](../08_applications/)

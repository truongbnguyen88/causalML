# Module 2: Causal Identification

## Overview
Learn when and how causal effects can be identified from observational data using graphical and statistical criteria.

## Learning Objectives
- Understand the ignorability/unconfoundedness assumption
- Apply the backdoor criterion to identify valid adjustment sets
- Use the frontdoor criterion for identification
- Grasp the basics of do-calculus
- Understand instrumental variables and their requirements

## Contents

### Theory & Concepts
- `01_identification_strategies.md` - Overview of identification approaches
- `additional_notes.md` - Detailed examples for ignorability and using multiple strategies
- `02_backdoor_adjustment.ipynb` - Backdoor criterion with examples
- `03_frontdoor_criterion.ipynb` - Frontdoor adjustment examples
- `04_instrumental_variables.ipynb` - IV intuition and applications
- `05_identification_with_software.ipynb` - **[Planned]** Using DoWhy and dagitty for automated identification
  - Automatically check identifiability given a DAG
  - Compare manual backdoor criterion vs. automated identification
  - Visualize DAGs and determine valid adjustment sets
  - Examples where do-calculus finds identification when simple methods don't apply

### Exercises
- `exercises/` - Practice problems with solutions

## Key Concepts

**Ignorability**: Treatment assignment is independent of potential outcomes given covariates

**Backdoor Criterion**: 
- Block all backdoor paths from treatment to outcome
- Don't block any directed paths

**Frontdoor Criterion**:
- When backdoor is blocked but confounders are unmeasured
- Uses mediators to identify effects

**Instrumental Variables**:
- Affects treatment but not outcome (except through treatment)
- Not affected by confounders

## Data Requirements

This module uses the **LaLonde Job Training dataset** for practical examples.

**To download the data:**
```bash
cd datasets/lalonde
python download_data.py
```

Or manually from: [NBER Data Repository](https://users.nber.org/~rdehejia/data/.nswdata2.html)

See [`datasets/lalonde/README.md`](../datasets/lalonde/README.md) for full documentation.

## Estimated Time
**2 weeks** (10-12 hours total)

## Prerequisites
- Module 1: Foundations of Causal Inference

## Next Module
[Module 3: Basic Estimation Methods](../03_estimation_basics/)

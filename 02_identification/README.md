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
- `02_backdoor_adjustment.ipynb` - Backdoor criterion with examples
- `03_frontdoor_criterion.ipynb` - Frontdoor adjustment examples
- `04_instrumental_variables.ipynb` - IV intuition and applications

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

## Estimated Time
**2 weeks** (10-12 hours total)

## Prerequisites
- Module 1: Foundations of Causal Inference

## Next Module
[Module 3: Basic Estimation Methods](../03_estimation_basics/)

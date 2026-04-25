# Module 1: Foundations of Causal Inference

## Overview
This module introduces core concepts in causal inference, contrasting causation with correlation and establishing the theoretical frameworks needed for causal reasoning.

## Learning Objectives
- Understand the difference between correlation and causation
- Learn the Rubin Causal Model (Potential Outcomes Framework)
- Interpret and construct Directed Acyclic Graphs (DAGs)
- Identify confounders, mediators, and colliders
- Grasp the fundamental problem of causal inference

## Contents

### Theory & Concepts
- `01_intro_causality.md` - Introduction to causal thinking
- `02_potential_outcomes.ipynb` - The potential outcomes framework with examples
- `03_dags_basics.ipynb` - DAG construction and interpretation
- `04_confounding_examples.ipynb` - Identifying and understanding confounding

### Exercises
- `exercises/` - Practice problems with solutions

## Key Concepts

**Correlation vs Causation**: Understanding why correlation doesn't imply causation

**Potential Outcomes**: 
- Y(1) = outcome if treated
- Y(0) = outcome if not treated
- Causal effect = Y(1) - Y(0)

**DAGs (Directed Acyclic Graphs)**:
- Nodes represent variables
- Arrows represent causal relationships
- No cycles allowed

**Confounding**: When a variable affects both treatment and outcome

## Estimated Time
**2 weeks** (10-12 hours total)

## Prerequisites
- Basic probability and statistics
- Python programming fundamentals
- Familiarity with Jupyter notebooks

## Next Module
[Module 2: Causal Identification](../02_identification/)

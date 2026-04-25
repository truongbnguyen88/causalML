# Causal Inference & Causal Machine Learning - Learning Path

**Target Audience**: Data scientists with no prior causal inference experience  
**Goal**: Progress from foundational concepts to advanced causal ML techniques

---

## Repository Structure

```
causalML/
├── 01_foundations/              # Week 1-2: Core concepts
├── 02_identification/           # Week 3-4: Causal identification
├── 03_estimation_basics/        # Week 5-6: Basic estimation methods
├── 04_propensity_methods/       # Week 7-8: Propensity-based approaches
├── 05_causal_ml_algorithms/     # Week 9-12: Machine learning methods
├── 06_heterogeneous_effects/    # Week 13-14: Treatment effect heterogeneity
├── 07_advanced_topics/          # Week 15-16: Advanced methods
├── 08_applications/             # Week 17-18: Real-world case studies
├── datasets/                    # Shared datasets for exercises
├── utils/                       # Reusable functions and helpers
└── references/                  # Papers, books, and additional resources
```

---

## Course Outline

### **Module 1: Foundations of Causal Inference** (01_foundations/)

**Learning Objectives**: Understand correlation vs causation, causal graphs, and the potential outcomes framework

**Topics**:
1. Correlation vs Causation
2. The Rubin Causal Model (Potential Outcomes)
3. Introduction to Directed Acyclic Graphs (DAGs)
4. Confounding, Selection Bias, and Colliders
5. The Fundamental Problem of Causal Inference

**Files**:
- `01_intro_causality.md` - Conceptual overview
- `02_potential_outcomes.ipynb` - Interactive examples
- `03_dags_basics.ipynb` - DAG construction and interpretation
- `04_confounding_examples.ipynb` - Identifying confounders
- `exercises/` - Practice problems

**Example Problems**:
- Simpson's Paradox demonstration
- Drawing and interpreting simple DAGs
- Identifying confounders in synthetic datasets

---

### **Module 2: Causal Identification** (02_identification/)

**Learning Objectives**: Learn when and how causal effects can be identified from data

**Topics**:
1. Ignorability/Unconfoundedness Assumption
2. Backdoor Criterion
3. Frontdoor Criterion
4. do-Calculus Basics
5. Instrumental Variables (IV) Introduction

**Files**:
- `01_identification_strategies.md` - Theory overview
- `02_backdoor_adjustment.ipynb` - Backdoor criterion examples
- `03_frontdoor_criterion.ipynb` - Frontdoor examples
- `04_instrumental_variables.ipynb` - IV intuition and examples
- `exercises/` - Practice problems

**Example Problems**:
- Applying backdoor criterion to various DAGs
- Finding valid adjustment sets
- Identifying valid instruments

---

### **Module 3: Basic Estimation Methods** (03_estimation_basics/)

**Learning Objectives**: Implement fundamental causal effect estimation techniques

**Topics**:
1. Average Treatment Effect (ATE)
2. Conditional Average Treatment Effect (CATE)
3. Regression Adjustment
4. Stratification and Subclassification
5. Difference-in-Differences (DiD)
6. Regression Discontinuity Design (RDD)

**Files**:
- `01_ate_estimation.ipynb` - Computing ATE with regression
- `02_stratification.ipynb` - Stratification methods
- `03_diff_in_diff.ipynb` - DiD implementation
- `04_regression_discontinuity.ipynb` - RDD examples
- `exercises/` - Practice problems

**Example Problems**:
- Estimating treatment effects in education data
- DiD for policy evaluation
- RDD for eligibility cutoff analysis

---

### **Module 4: Propensity Score Methods** (04_propensity_methods/)

**Learning Objectives**: Master propensity score techniques for causal inference

**Topics**:
1. Propensity Score Theory
2. Propensity Score Matching
3. Inverse Probability Weighting (IPW)
4. Doubly Robust Estimation
5. Covariate Balance Checking

**Files**:
- `01_propensity_scores.md` - Theory and intuition
- `02_ps_matching.ipynb` - Matching algorithms
- `03_ipw.ipynb` - IPW implementation
- `04_doubly_robust.ipynb` - Doubly robust estimators
- `05_balance_diagnostics.ipynb` - Checking balance
- `exercises/` - Practice problems

**Example Problems**:
- Matching treated/control units in observational data
- IPW for marketing campaign analysis
- Balance diagnostics on real datasets

---

### **Module 5: Causal Machine Learning Algorithms** (05_causal_ml_algorithms/)

**Learning Objectives**: Apply modern ML methods to causal estimation

**Topics**:
1. Meta-Learners (S-learner, T-learner, X-learner)
2. Causal Forests and Generalized Random Forests
3. Bayesian Additive Regression Trees (BART)
4. Targeted Maximum Likelihood Estimation (TMLE)
5. Double/Debiased Machine Learning (DML)
6. Causal Gradient Boosting

**Files**:
- `01_meta_learners.ipynb` - S/T/X-learner implementations
- `02_causal_forests.ipynb` - Using GRF/EconML
- `03_bart_causal.ipynb` - BART for causal inference
- `04_tmle.ipynb` - TMLE implementation
- `05_double_ml.ipynb` - DML framework
- `06_comparison.ipynb` - Method comparison
- `exercises/` - Practice problems

**Example Problems**:
- Comparing meta-learners on synthetic data
- Causal forest for heterogeneous effects
- DML with cross-fitting

---

### **Module 6: Heterogeneous Treatment Effects** (06_heterogeneous_effects/)

**Learning Objectives**: Discover and estimate treatment effect variation across subgroups

**Topics**:
1. Conditional Average Treatment Effects (CATE)
2. Uplift Modeling
3. Causal Trees and Forests
4. Best Linear Projection (BLP)
5. Group Average Treatment Effects (GATE)
6. Policy Learning

**Files**:
- `01_cate_estimation.ipynb` - CATE methods
- `02_uplift_modeling.ipynb` - Uplift for marketing
- `03_heterogeneity_analysis.ipynb` - Analyzing variation
- `04_policy_learning.ipynb` - Optimal treatment rules
- `exercises/` - Practice problems

**Example Problems**:
- Finding who benefits most from treatment
- Uplift modeling for customer targeting
- Learning optimal treatment assignment policies

---

### **Module 7: Advanced Topics** (07_advanced_topics/)

**Learning Objectives**: Explore cutting-edge methods and complex scenarios

**Topics**:
1. Mediation Analysis
2. Time-Varying Treatments and Marginal Structural Models
3. Synthetic Control Methods
4. Sensitivity Analysis
5. Bounds and Partial Identification
6. Causal Discovery
7. Counterfactual Prediction

**Files**:
- `01_mediation_analysis.ipynb` - Direct/indirect effects
- `02_time_varying_treatments.ipynb` - MSM implementation
- `03_synthetic_control.ipynb` - Synthetic control examples
- `04_sensitivity_analysis.ipynb` - Robustness checks
- `05_causal_discovery.ipynb` - Learning DAGs from data
- `06_counterfactuals.ipynb` - Counterfactual inference
- `exercises/` - Practice problems

**Example Problems**:
- Mediation in psychological studies
- Synthetic control for case studies
- Sensitivity analysis for hidden confounding

---

### **Module 8: Real-World Applications** (08_applications/)

**Learning Objectives**: Apply causal methods to realistic, complex problems

**Topics**:
1. Marketing and Customer Analytics
2. Healthcare and Clinical Trials
3. Economics and Policy Evaluation
4. Tech/Product: A/B Testing and Beyond
5. Fairness and Algorithmic Bias

**Files**:
- `01_marketing_case_study.ipynb` - Campaign effectiveness
- `02_healthcare_analysis.ipynb` - Treatment effectiveness
- `03_policy_evaluation.ipynb` - Government program impact
- `04_ab_testing_advanced.ipynb` - Beyond simple A/B tests
- `05_fairness_causality.ipynb` - Fair decision-making
- `final_project/` - Capstone project templates

**Example Problems**:
- Email campaign ROI with causal ML
- Drug effectiveness in observational data
- Job training program evaluation
- Feature launch impact analysis

---

## Supporting Directories

### **datasets/**

Curated datasets for exercises:
- `lalonde/` - Job training program (classic causal dataset)
- `ihdp/` - Infant health and development
- `twins/` - Twin births mortality
- `criteo/` - Uplift modeling dataset
- `synthetic/` - Generated data with known ground truth
- `README.md` - Dataset descriptions and sources

### **utils/**

Reusable code:
- `data_generation.py` - Synthetic data generators
- `evaluation.py` - Metrics for causal methods
- `visualization.py` - Plotting functions
- `estimators.py` - Common estimator implementations
- `balance_checks.py` - Covariate balance utilities

### **references/**

Learning resources:
- `books.md` - Recommended textbooks
- `papers.md` - Seminal and recent papers by topic
- `software.md` - Python libraries (EconML, DoWhy, CausalML, etc.)
- `online_courses.md` - MOOCs and tutorials
- `glossary.md` - Causal inference terminology

---

## Recommended Learning Path

### **Phase 1: Foundations** (Weeks 1-6)
- Modules 1-3
- Focus on understanding concepts before algorithms
- Work through all exercises
- Use simple datasets (synthetic, Lalonde)

### **Phase 2: Methods** (Weeks 7-12)
- Modules 4-5
- Implement methods from scratch before using libraries
- Compare different approaches on same datasets
- Start using real libraries (EconML, DoWhy)

### **Phase 3: Advanced & Applied** (Weeks 13-18)
- Modules 6-8
- Focus on practical application
- Complete multiple case studies
- Work on final capstone project

---

## Prerequisites

**Required**:
- Python programming (intermediate level)
- Statistics (regression, hypothesis testing)
- Machine learning basics (scikit-learn familiarity)
- Probability theory fundamentals

**Recommended**:
- Pandas, NumPy proficiency
- Data visualization (matplotlib, seaborn)
- Some experience with scikit-learn models

---

## Tools and Libraries

**Core Libraries**:
- `econml` - Causal ML methods from Microsoft
- `dowhy` - Causal inference framework from Microsoft
- `causalml` - Causal ML from Uber
- `scikit-learn` - Standard ML
- `statsmodels` - Statistical models
- `pandas`, `numpy` - Data manipulation

**Visualization**:
- `matplotlib`, `seaborn` - Plotting
- `networkx` - DAG visualization
- `graphviz` - Causal graphs

**Optional**:
- `pymc` - Bayesian methods
- `pgmpy` - Probabilistic graphical models
- `causal-learn` - Causal discovery

---

## Assessment Strategy

Each module includes:
1. **Conceptual Questions** - Test understanding
2. **Coding Exercises** - Implement methods
3. **Applied Problems** - Use methods on datasets
4. **Mini-Projects** - Combine multiple techniques

**Final Assessment**: Capstone project applying causal ML to a real-world problem

---

## Next Steps

1. **Start with Module 1** - Build strong foundations
2. **Work sequentially** - Each module builds on previous ones
3. **Code along** - Don't just read, implement everything
4. **Experiment** - Modify examples and see what happens
5. **Read papers** - Supplement notebooks with original research
6. **Join community** - Engage with causal inference communities online

---

## Additional Resources

**Books** (to be detailed in `references/books.md`):
- "Causal Inference: The Mixtape" by Cunningham
- "The Book of Why" by Pearl and Mackenzie
- "Causal Inference for Statistics, Social, and Biomedical Sciences" by Imbens and Rubin
- "Elements of Causal Inference" by Peters, Janzing, and Schölkopf

**Online Resources**:
- Brady Neal's Causal Inference course (YouTube)
- Microsoft's DoWhy tutorials
- EconML documentation and case studies

---

**Last Updated**: 2026-04-25  
**Maintainer**: Data Science Learning Path  
**Estimated Completion Time**: 18 weeks (10-15 hours/week)

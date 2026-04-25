# Repository Structure Overview

Complete directory structure for the Causal ML learning repository.

## Directory Tree

```
causalML/
│
├── README.md                           # Main repository overview
├── CURRICULUM.md                       # Detailed course outline
├── STRUCTURE.md                        # This file - structure overview
│
├── 01_foundations/                     # Module 1: Foundations
│   ├── README.md                       # Module overview
│   ├── 01_intro_causality.md          # Theory: Introduction
│   ├── 02_potential_outcomes.ipynb    # Code: Potential outcomes
│   ├── 03_dags_basics.ipynb           # Code: DAGs
│   ├── 04_confounding_examples.ipynb  # Code: Confounding
│   └── exercises/                      # Practice problems
│
├── 02_identification/                  # Module 2: Causal Identification
│   ├── README.md                       # Module overview
│   ├── 01_identification_strategies.md # Theory
│   ├── 02_backdoor_adjustment.ipynb   # Code: Backdoor criterion
│   ├── 03_frontdoor_criterion.ipynb   # Code: Frontdoor criterion
│   ├── 04_instrumental_variables.ipynb # Code: IV
│   └── exercises/                      # Practice problems
│
├── 03_estimation_basics/               # Module 3: Basic Estimation
│   ├── README.md                       # Module overview
│   ├── 01_ate_estimation.ipynb        # Code: ATE
│   ├── 02_stratification.ipynb        # Code: Stratification
│   ├── 03_diff_in_diff.ipynb          # Code: DiD
│   ├── 04_regression_discontinuity.ipynb # Code: RDD
│   └── exercises/                      # Practice problems
│
├── 04_propensity_methods/              # Module 4: Propensity Scores
│   ├── README.md                       # Module overview
│   ├── 01_propensity_scores.md        # Theory
│   ├── 02_ps_matching.ipynb           # Code: Matching
│   ├── 03_ipw.ipynb                   # Code: IPW
│   ├── 04_doubly_robust.ipynb         # Code: Doubly robust
│   ├── 05_balance_diagnostics.ipynb   # Code: Balance checking
│   └── exercises/                      # Practice problems
│
├── 05_causal_ml_algorithms/            # Module 5: Causal ML
│   ├── README.md                       # Module overview
│   ├── 01_meta_learners.ipynb         # Code: S/T/X-learners
│   ├── 02_causal_forests.ipynb        # Code: Causal forests
│   ├── 03_bart_causal.ipynb           # Code: BART
│   ├── 04_tmle.ipynb                  # Code: TMLE
│   ├── 05_double_ml.ipynb             # Code: DML
│   ├── 06_comparison.ipynb            # Code: Method comparison
│   └── exercises/                      # Practice problems
│
├── 06_heterogeneous_effects/           # Module 6: Heterogeneity
│   ├── README.md                       # Module overview
│   ├── 01_cate_estimation.ipynb       # Code: CATE
│   ├── 02_uplift_modeling.ipynb       # Code: Uplift
│   ├── 03_heterogeneity_analysis.ipynb # Code: Analysis
│   ├── 04_policy_learning.ipynb       # Code: Policy learning
│   └── exercises/                      # Practice problems
│
├── 07_advanced_topics/                 # Module 7: Advanced Methods
│   ├── README.md                       # Module overview
│   ├── 01_mediation_analysis.ipynb    # Code: Mediation
│   ├── 02_time_varying_treatments.ipynb # Code: MSM
│   ├── 03_synthetic_control.ipynb     # Code: Synthetic control
│   ├── 04_sensitivity_analysis.ipynb  # Code: Sensitivity
│   ├── 05_causal_discovery.ipynb      # Code: Discovery
│   ├── 06_counterfactuals.ipynb       # Code: Counterfactuals
│   └── exercises/                      # Practice problems
│
├── 08_applications/                    # Module 8: Applications
│   ├── README.md                       # Module overview
│   ├── 01_marketing_case_study.ipynb  # Case: Marketing
│   ├── 02_healthcare_analysis.ipynb   # Case: Healthcare
│   ├── 03_policy_evaluation.ipynb     # Case: Policy
│   ├── 04_ab_testing_advanced.ipynb   # Case: A/B testing
│   ├── 05_fairness_causality.ipynb    # Case: Fairness
│   └── final_project/                  # Capstone project templates
│
├── datasets/                           # Datasets for learning
│   ├── README.md                       # Dataset documentation
│   ├── lalonde/                        # Job training data
│   │   ├── lalonde.csv
│   │   └── lalonde_description.md
│   ├── ihdp/                           # Infant health data
│   │   ├── ihdp.csv
│   │   └── ihdp_description.md
│   ├── twins/                          # Twin births data
│   │   ├── twins.csv
│   │   └── twins_description.md
│   ├── criteo/                         # Uplift modeling data
│   │   ├── criteo_sample_10k.csv
│   │   ├── criteo_sample_100k.csv
│   │   ├── criteo_description.md
│   │   └── download_full.py
│   └── synthetic/                      # Generated datasets
│       ├── linear_synthetic.csv
│       ├── nonlinear_synthetic.csv
│       ├── heterogeneous_synthetic.csv
│       ├── confounded_synthetic.csv
│       ├── generate_synthetic.py
│       └── synthetic_description.md
│
├── utils/                              # Reusable utilities
│   ├── README.md                       # Utils documentation
│   ├── data_generation.py             # Synthetic data generators
│   ├── evaluation.py                  # Causal metrics
│   ├── visualization.py               # Plotting functions
│   ├── estimators.py                  # Custom estimators
│   └── balance_checks.py              # Balance diagnostics
│
└── references/                         # Learning resources
    ├── README.md                       # References overview
    ├── books.md                        # Recommended books
    ├── papers.md                       # Key papers by topic
    ├── software.md                     # Python libraries guide
    ├── online_courses.md               # MOOCs and tutorials
    └── glossary.md                     # Terminology definitions
```

## File Status Legend

- ✅ **Created**: README files for all modules and directories
- 📝 **To Create**: Individual notebook and markdown files within modules
- 🗂️ **Directories**: All directories created successfully

## Current Status

### ✅ Completed
- [x] Full directory structure (all 8 modules + support dirs)
- [x] README.md files for all modules (01-08)
- [x] datasets/README.md with comprehensive dataset descriptions
- [x] utils/README.md with utility function documentation
- [x] references/README.md with learning resource guides
- [x] Main README.md with course overview
- [x] CURRICULUM.md with detailed course outline

### 📝 Next Steps (Content Creation)
1. Create theory markdown files (e.g., `01_intro_causality.md`)
2. Create Jupyter notebooks for each topic
3. Add exercise notebooks with solutions
4. Populate datasets directory with actual data
5. Implement utility functions in utils/
6. Create reference documents (books.md, papers.md, etc.)

## Quick Navigation

### By Learning Phase

**Phase 1 - Foundations** (Weeks 1-6):
- [01_foundations/](01_foundations/)
- [02_identification/](02_identification/)
- [03_estimation_basics/](03_estimation_basics/)

**Phase 2 - Methods** (Weeks 7-12):
- [04_propensity_methods/](04_propensity_methods/)
- [05_causal_ml_algorithms/](05_causal_ml_algorithms/)

**Phase 3 - Advanced & Applied** (Weeks 13-18):
- [06_heterogeneous_effects/](06_heterogeneous_effects/)
- [07_advanced_topics/](07_advanced_topics/)
- [08_applications/](08_applications/)

### Support Resources
- [datasets/](datasets/) - All learning datasets
- [utils/](utils/) - Reusable code
- [references/](references/) - Books, papers, courses

## File Count Summary

```
Directories created: 23
  - 8 module directories
  - 8 exercise subdirectories
  - 5 dataset subdirectories
  - 1 final_project directory
  - 1 utils directory
  - 1 references directory

README files created: 11
  - 8 module READMEs
  - 1 main README
  - 1 datasets README
  - 1 utils README
  - 1 references README

Additional files: 2
  - CURRICULUM.md (detailed course outline)
  - STRUCTURE.md (this file)
```

## Size Estimate

**Completed Repository (estimated)**:
- ~60 Jupyter notebooks
- ~20 markdown theory files
- ~40 exercise notebooks
- ~10 datasets with descriptions
- ~10 utility modules
- ~10 reference documents
- **Total**: ~150 files across 23 directories

---

**Status**: Repository structure complete ✅  
**Next**: Begin content creation starting with Module 1  
**Last Updated**: 2026-04-25

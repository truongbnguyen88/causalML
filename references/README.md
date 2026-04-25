# References and Learning Resources

This directory contains curated references for causal inference and causal machine learning.

## Contents

- `books.md` - Recommended textbooks and comprehensive references
- `papers.md` - Key papers organized by topic
- `software.md` - Python libraries and tools
- `online_courses.md` - MOOCs, video lectures, and tutorials
- `glossary.md` - Causal inference terminology and definitions

## Quick Reference

### Essential Books (Beginner)
1. **"The Book of Why"** by Judea Pearl & Dana Mackenzie - Accessible introduction
2. **"Causal Inference: The Mixtape"** by Scott Cunningham - Applied econometrics approach
3. **"Causal Inference in Statistics: A Primer"** by Pearl, Glymour, Jewell - Short introduction

### Essential Books (Advanced)
1. **"Causal Inference for Statistics, Social, and Biomedical Sciences"** by Imbens & Rubin - Potential outcomes framework
2. **"Causality"** by Judea Pearl - Comprehensive graphical models approach
3. **"Elements of Causal Inference"** by Peters, Janzing, Schölkopf - ML perspective

### Must-Read Papers
- Rubin (1974) - Estimating causal effects of treatments
- Pearl (1995) - Causal diagrams for empirical research
- Angrist & Krueger (2001) - Instrumental variables review
- Athey & Imbens (2016) - Recursive partitioning for heterogeneous effects
- Chernozhukov et al. (2018) - Double/debiased machine learning

### Key Software Libraries
- **EconML** (Microsoft) - Heterogeneous effects and causal ML
- **DoWhy** (Microsoft) - Causal inference workflow
- **CausalML** (Uber) - Uplift modeling and meta-learners
- **scikit-learn** - Base ML algorithms
- **statsmodels** - Statistical models

### Online Courses
- Brady Neal's "Introduction to Causal Inference" (YouTube)
- Stanford CS229 Causal Inference lectures
- Miguel Hernán's "Causal Diagrams" (edX)

## Using These References

### By Module

**Module 1 (Foundations)**:
- Read: Pearl's "Book of Why" (Ch 1-3)
- Watch: Brady Neal lectures 1-3
- Reference: `glossary.md` for terminology

**Module 2 (Identification)**:
- Read: Pearl "Causality" (Ch 3)
- Paper: Pearl (1995) on causal diagrams
- Tool: DoWhy for identification

**Module 3 (Basic Estimation)**:
- Read: Cunningham "Mixtape" (Ch 4-5)
- Paper: Angrist & Pischke on design-based methods
- Tool: statsmodels

**Module 4 (Propensity Scores)**:
- Read: Imbens & Rubin (Ch 12-13)
- Paper: Rosenbaum & Rubin (1983)
- Tool: scikit-learn for propensity estimation

**Module 5 (Causal ML)**:
- Read: Elements of Causal Inference (Ch 4)
- Papers: Künzel et al. (2019) on meta-learners, Wager & Athey (2018) on causal forests
- Tool: EconML, CausalML

**Module 6 (Heterogeneous Effects)**:
- Paper: Athey & Imbens (2016) on causal trees
- Tool: EconML for CATE estimation
- Reference: EconML documentation

**Module 7 (Advanced)**:
- Paper: Robins (1986) on MSMs
- Paper: Abadie et al. on synthetic control
- Tool: Various (causal-learn for discovery)

**Module 8 (Applications)**:
- Read: Domain-specific case studies
- Reference: All previous materials

## Contributing

To add a reference:
1. Add citation to appropriate `.md` file
2. Include brief description and relevance
3. Tag with difficulty level (beginner/intermediate/advanced)
4. Update this README if it's essential

## Citation Management

Consider using citation managers for your research:
- Zotero (free, open-source)
- Mendeley (free)
- EndNote (paid)

Export `.bib` file for LaTeX/papers.

## Community Resources

### Forums & Discussion
- Cross Validated (stats.stackexchange.com) - "causal-inference" tag
- Reddit: r/causality, r/statistics
- Twitter: #CausalInference

### Research Groups
- Stanford Causal Science Center
- Microsoft Research (EconML team)
- MIT IDSS

### Conferences
- Conference on Causal Learning and Reasoning (CLeaR)
- UAI (Uncertainty in AI)
- NeurIPS (causal inference workshops)

## Updates

This reference collection is updated regularly. Check back for:
- New paper releases
- Updated software versions
- New courses and tutorials
- Community contributions

**Last Updated**: 2026-04-25

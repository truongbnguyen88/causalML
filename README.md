# Causal Inference & Causal Machine Learning - Learning Repository

A comprehensive, hands-on course for learning causal inference and causal machine learning from beginner to advanced level.

## 🎯 Purpose

This repository is designed for data scientists with no prior causal inference experience who want to master causal reasoning and modern causal ML techniques. Through structured modules, code examples, and real datasets, you'll progress from understanding "correlation vs causation" to implementing state-of-the-art causal ML algorithms.

## 📚 Course Structure

The course consists of **8 modules** spanning approximately **18 weeks** (10-15 hours/week):

| Module | Topic | Duration | Difficulty |
|--------|-------|----------|------------|
| [01_foundations](01_foundations/) | Foundations of Causal Inference | 2 weeks | Beginner |
| [02_identification](02_identification/) | Causal Identification | 2 weeks | Beginner |
| [03_estimation_basics](03_estimation_basics/) | Basic Estimation Methods | 2 weeks | Intermediate |
| [04_propensity_methods](04_propensity_methods/) | Propensity Score Methods | 2 weeks | Intermediate |
| [05_causal_ml_algorithms](05_causal_ml_algorithms/) | Causal ML Algorithms | 4 weeks | Advanced |
| [06_heterogeneous_effects](06_heterogeneous_effects/) | Heterogeneous Treatment Effects | 2 weeks | Advanced |
| [07_advanced_topics](07_advanced_topics/) | Advanced Topics | 2 weeks | Advanced |
| [08_applications](08_applications/) | Real-World Applications | 2 weeks | Advanced |

## 🗂️ Repository Organization

```
causalML/
├── 01_foundations/              # Potential outcomes, DAGs, confounding
├── 02_identification/           # Backdoor, frontdoor, IV
├── 03_estimation_basics/        # ATE, regression, DiD, RDD
├── 04_propensity_methods/       # Matching, IPW, doubly robust
├── 05_causal_ml_algorithms/     # Meta-learners, forests, DML
├── 06_heterogeneous_effects/    # CATE, uplift, policy learning
├── 07_advanced_topics/          # Mediation, synthetic control, discovery
├── 08_applications/             # Marketing, healthcare, policy cases
├── datasets/                    # LaLonde, IHDP, Criteo, synthetic data
├── utils/                       # Reusable functions and estimators
├── references/                  # Books, papers, software guides
└── CURRICULUM.md                # Detailed course outline
```

Each module contains:
- **Theory** (`.md` files) - Conceptual explanations
- **Code** (`.ipynb` notebooks) - Interactive implementations
- **Exercises** - Practice problems with solutions
- **README** - Module overview and learning objectives

## 🚀 Getting Started

### Prerequisites

**Required Knowledge**:
- Python programming (intermediate)
- Statistics (regression, hypothesis testing)
- Machine learning basics (scikit-learn)
- Probability theory fundamentals

**Technical Requirements**:
- Python 3.8+
- Jupyter Notebook/Lab
- 4GB+ RAM

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/causalML.git
cd causalML
```

2. **Create virtual environment**:
```bash
python -m venv causal_env
source causal_env/bin/activate  # On Windows: causal_env\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Launch Jupyter**:
```bash
jupyter lab
```

5. **Start with Module 1**:
Navigate to `01_foundations/` and open the first notebook.

## 📦 Key Libraries

This course uses modern Python libraries for causal inference:

- **[EconML](https://github.com/microsoft/EconML)** - Causal ML methods (Microsoft)
- **[DoWhy](https://github.com/microsoft/dowhy)** - Causal inference framework (Microsoft)
- **[CausalML](https://github.com/uber/causalml)** - Uplift modeling (Uber)
- **scikit-learn** - Machine learning algorithms
- **statsmodels** - Statistical models
- **pandas**, **numpy** - Data manipulation

See [references/software.md](references/software.md) for detailed installation and usage.

## 📖 Learning Path

### Phase 1: Foundations (Weeks 1-6)
**Goal**: Understand core concepts before algorithms

1. Complete Modules 1-3 sequentially
2. Focus on conceptual understanding
3. Work through all exercises
4. Use simple datasets (synthetic, LaLonde)

**Key Skills**: DAGs, potential outcomes, basic estimation

### Phase 2: Methods (Weeks 7-12)
**Goal**: Master modern causal ML techniques

1. Complete Modules 4-5
2. Implement methods from scratch first
3. Then use professional libraries
4. Compare approaches on benchmarks

**Key Skills**: Propensity scores, meta-learners, causal forests, DML

### Phase 3: Advanced & Applied (Weeks 13-18)
**Goal**: Apply to complex, realistic problems

1. Complete Modules 6-8
2. Work on case studies
3. Develop final capstone project
4. Explore domain applications

**Key Skills**: Heterogeneous effects, advanced methods, real-world deployment

## 🎓 Assessment

Each module includes:
- ✅ **Conceptual questions** - Test understanding
- 💻 **Coding exercises** - Implement methods
- 📊 **Applied problems** - Analyze datasets
- 🔬 **Mini-projects** - Combine techniques

**Final Assessment**: Capstone project applying causal ML to a domain of your choice (marketing, healthcare, economics, etc.)

## 📚 Recommended Reading

**Beginner-Friendly**:
- "The Book of Why" - Pearl & Mackenzie
- "Causal Inference: The Mixtape" - Cunningham

**Technical References**:
- "Causal Inference for Statistics..." - Imbens & Rubin
- "Causality" - Pearl
- "Elements of Causal Inference" - Peters et al.

See [references/books.md](references/books.md) for complete list.

## 🌐 Online Resources

- [Brady Neal's Course](https://www.bradyneal.com/causal-inference-course) - Excellent video lectures
- [EconML Documentation](https://econml.azurewebsites.net/) - Tutorials and examples
- [DoWhy Examples](https://microsoft.github.io/dowhy/) - Causal inference workflows

See [references/online_courses.md](references/online_courses.md) for more.

## 🤝 Contributing

Contributions welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-content`)
3. Add your content (notebooks, exercises, datasets)
4. Commit changes (`git commit -m 'Add new exercise'`)
5. Push to branch (`git push origin feature/new-content`)
6. Open a Pull Request

Please maintain the existing structure and documentation style.

## 📧 Support & Community

- **Issues**: Report bugs or request features via GitHub Issues
- **Discussions**: Ask questions in GitHub Discussions

## 📜 License

This educational repository is licensed under the MIT License - see LICENSE file for details.

## 🙏 Acknowledgments

This course draws from:
- Research from Pearl, Rubin, Imbens, Athey, and many others
- Open-source libraries: EconML, DoWhy, CausalML
- Classic datasets: LaLonde, IHDP, Criteo
- Educational materials from leading universities

## 📊 Progress Tracking

Track your progress through the course:

- [ ] Module 1: Foundations of Causal Inference
- [ ] Module 2: Causal Identification
- [ ] Module 3: Basic Estimation Methods
- [ ] Module 4: Propensity Score Methods
- [ ] Module 5: Causal ML Algorithms
- [ ] Module 6: Heterogeneous Treatment Effects
- [ ] Module 7: Advanced Topics
- [ ] Module 8: Real-World Applications
- [ ] Final Capstone Project

## 🎯 Next Steps

1. **Review** [CURRICULUM.md](CURRICULUM.md) for detailed course outline
2. **Install** required dependencies
3. **Start** with [Module 1](01_foundations/)
4. **Join** the learning community

---

**Happy Learning! 🚀**

*Last Updated: 2026-04-25*
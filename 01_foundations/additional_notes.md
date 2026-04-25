# Additional Notes: Common Pitfalls Explained

Supplementary explanations for [01_intro_causality.md](01_intro_causality.md)

---

## Pitfall 4: "Causation flows from correlation + time order"

### The Core Issue

**Misconception**: Correlation + temporal ordering (X before Y) → Causation

**Reality**: Temporal ordering is **necessary but not sufficient** for causation.

### Why Time Order Isn't Enough

**Problem: Earlier confounders can affect both X and Y**

Example - Education → Income:
```
Family Wealth (Time 1)
    ↓           ↓
Education → Income
(Time 2)   (Time 3)
```

Even though education precedes income, family wealth (occurring before both) creates spurious correlation:
- Wealthy families → More education (affordability)
- Wealthy families → Higher income (networks, inheritance)

**Other time-ordered confounders**:
- Innate ability → Education choice & earnings
- Motivation → Years of schooling & job performance  
- Location → School quality & job opportunities

All these exist **before** the education decision yet confound the relationship.

### What You Actually Need

Beyond correlation + time order:
1. ✓ Temporal ordering (X before Y)
2. ✓ Association (correlation exists)
3. ✗ **No confounding** - The hard part!
4. ✗ **No selection bias**
5. ✗ **Correct causal model**

### Bottom Line

**Time order eliminates reverse causation but doesn't eliminate confounding.**

You still need: randomization, control for all confounders, instrumental variables, natural experiments, or sensitivity analysis.

---

## Pitfall 5: "Causal inference is just for experiments"

### The Core Issue

**Misconception**: Only RCTs can establish causation; observational data is useless.

**Reality**: Many powerful methods exist for causal inference without randomization.

### Why We Can't Always Experiment

**Ethical**: Can't randomly assign smoking, poverty, pollution
**Feasibility**: Too expensive, too long, politically infeasible  
**Already happened**: Historical events, implemented policies
**External validity**: RCTs may not reflect real-world conditions

### Six Observational Methods

**1. Natural Experiments**
- Nature/policy creates quasi-random variation
- Example: Vietnam draft lottery (birthdates randomly assigned)

**2. Instrumental Variables (IV)**
- Find variable affecting treatment but not outcome (except through treatment)
- Example: Compulsory schooling laws → education → earnings

**3. Regression Discontinuity (RDD)**
- Treatment assigned at threshold; compare units just above/below
- Example: GPA cutoff for scholarships (3.0 vs 2.99)

**4. Difference-in-Differences (DiD)**
- Compare treatment vs control group changes over time
- Example: Minimum wage increase in NJ vs PA (Card & Krueger 1994)

**5. Matching/Propensity Scores**
- Match treated/control units on observables
- Example: Job training participants matched to non-participants

**6. Synthetic Control**
- Create synthetic control from weighted untreated units
- Example: German reunification effect (synthetic West Germany)

### When Observational Methods Work

Strong assumptions are justifiable when:
- All confounders measured and controlled
- Natural variation exists (policy changes, geography)
- Domain knowledge supports assumptions (biological mechanisms)
- Parallel trends hold (for DiD)
- Valid instruments exist (for IV)

### Key Examples Without RCTs

**Smoking → Lung cancer**: Cohort studies, dose-response, biological mechanism  
**Cholera → Contaminated water**: John Snow's natural experiment (1854)  
**TV → Child behavior**: Natural experiments (towns getting TV at different times)

### RCTs vs Observational Studies

**RCTs win**: Internal validity, fewer assumptions, no unmeasured confounding  
**Observational win**: External validity, larger samples, longer horizons, ethical, lower cost

**Best approach**: Triangulation - use multiple methods with different assumptions

### Bottom Line

**Experiments are NOT required for causal inference.**

Quote from Joshua Angrist:
> "Randomization is not the only path to credible causal inference."

Observational methods require **stronger assumptions** but are powerful and essential when RCTs are impossible. The key is justifying assumptions and testing robustness.

---

## Further Reading

**On confounding & time**: Pearl et al. (2016) *Causal Inference in Statistics: A Primer*, Ch 3

**On observational methods**: 
- Angrist & Pischke (2009) *Mostly Harmless Econometrics*, Ch 3-6
- Cunningham (2021) *Causal Inference: The Mixtape*

**Classic papers**:
- Rosenbaum & Rubin (1983) on propensity scores
- Card & Krueger (1994) on DiD (minimum wage study)

---

*Return to [01_intro_causality.md](01_intro_causality.md)*

# Additional Notes:

## Strategy #4 - Ignorability/Unconfoundedness (Core Concepts)

**Ignorability/Unconfoundedness** means that once we condition on (control for) a set of measured variables **X**, treatment assignment is "as-if random" — there are no remaining unmeasured confounders affecting both treatment and outcome.

Formally: **Y(0), Y(1) ⊥ T | X**

This means: "Potential outcomes are independent of treatment assignment, given X"

---

## Concrete Example: Online Course Effectiveness

### Setting
You want to estimate the causal effect of taking an online coding bootcamp (treatment T) on salary one year later (outcome Y).

### The Problem
People who choose to take the bootcamp are different from those who don't:
- More motivated individuals self-select into bootcamp
- People with more free time can complete it
- Those already in tech might be more likely to enroll

These differences could confound our estimate — we might wrongly attribute salary gains to the bootcamp when they're actually due to motivation, prior experience, etc.

### Applying Ignorability

**Step 1: Identify measurable confounders (X)**

We measure:
- Age
- Prior education level
- Current employment status
- Years of programming experience
- Motivation score (from initial survey)
- Available study time per week

**Step 2: The Ignorability Assumption**

We assume that **conditional on these X variables**, treatment assignment is random. 

In other words:
- Among people with the same age, education, employment status, experience, motivation, and available time...
- Whether they chose to take the bootcamp or not is essentially random
- There are no other unmeasured factors affecting both their decision to enroll AND their future salary

**Step 3: What This Enables**

If ignorability holds, we can estimate the causal effect by:

```python
# Among people with similar X values, compare outcomes
# For example, using regression adjustment:

# People with X = {age=25, education=bachelor's, employed=yes, 
#                   experience=1yr, motivation=high, time=15hrs/week}

bootcamp_group = data[(data.X == x_profile) & (data.bootcamp == 1)]
no_bootcamp_group = data[(data.X == x_profile) & (data.bootcamp == 0)]

effect = bootcamp_group.salary.mean() - no_bootcamp_group.salary.mean()
```

Since we've controlled for X and assume ignorability, this difference is the **causal effect** of the bootcamp for people with profile x_profile.

### Why This Matters

**The key insight**: We're claiming that after matching on these measured variables, the remaining variation in who took the bootcamp is unrelated to their potential salaries — it's just random chance, personal preference unrelated to earnings potential, etc.

### When Ignorability Might Fail

Ignorability would be **violated** if there were unmeasured confounders, such as:

- **Underlying ability**: Maybe highly talented people both choose bootcamps AND would earn more regardless
- **Social networks**: People with tech industry connections both enroll more AND have better job prospects
- **Geographic location**: Living in a tech hub affects both bootcamp access AND salary opportunities

If these unmeasured factors exist and affect both treatment and outcome, then even after conditioning on X, treatment assignment is NOT random — ignorability fails.

### How To Check (Indirectly)

You can't directly verify ignorability (it's untestable), but you can:

1. **Think hard about domain knowledge**: What factors influence both bootcamp enrollment and salary?
2. **Check balance**: After conditioning on X, are treatment/control groups similar on other observed characteristics?
3. **Sensitivity analysis**: How strong would an unmeasured confounder need to be to change your conclusions?

---

## What the Effect Estimate Tells Us

When we calculate the effect for a specific X profile:

```python
effect = bootcamp_group.salary.mean() - no_bootcamp_group.salary.mean()
```

### What This Comparison Tells Us

We get the **Average Treatment Effect (ATE) for people with this specific X profile**.

**For people who are 25 years old, have a bachelor's degree, are employed, have 1 year of programming experience, high motivation, and 15 hours/week available:**

- The bootcamp **causes** an average salary increase (or decrease) of `effect` dollars

**Why is this causal?**

Because under the ignorability assumption, among people with identical X values:
- The choice to take the bootcamp is "as-if random"
- No other factors are influencing both bootcamp enrollment AND salary
- Therefore, the salary difference is **caused by** the bootcamp, not by confounding

### What This Comparison Does NOT Tell Us

#### 1. Only applies to this specific subgroup

This effect is for people with **exactly** this X profile. It doesn't tell us:
- The effect for 30-year-olds
- The effect for people with only 5 hours/week available
- The effect for people with no prior programming experience

#### 2. Sample size limitations

In practice, finding enough people with **exactly** the same X values can be challenging:

```python
# This might return very few (or zero!) people:
bootcamp_group = data[(data.age == 25) & 
                      (data.education == "bachelor's") &
                      (data.employed == True) &
                      (data.experience == 1) &
                      (data.motivation == "high") &
                      (data.time == 15) &
                      (data.bootcamp == 1)]
```

**Problem**: If you have 6 covariates, finding exact matches becomes sparse (the "curse of dimensionality")

#### 3. Doesn't tell us about heterogeneity

This single effect estimate doesn't reveal:
- Whether effects vary across different X profiles
- Who benefits most from the bootcamp
- Whether there are negative effects for some subgroups

---

## How to Get a More General Effect Estimate

In practice, we use methods that aggregate across **all** X profiles:

### Option 1: Regression Adjustment

```python
from sklearn.linear_model import LinearRegression

# Control for X while estimating bootcamp effect
X_controls = data[['age', 'education', 'employed', 'experience', 'motivation', 'time']]
X_with_treatment = pd.concat([X_controls, data[['bootcamp']]], axis=1)
# Note that data[['bootcamp']] is binary (1 or 0)

model = LinearRegression()
model.fit(X_with_treatment, data['salary'])

# Coefficient on 'bootcamp' is the ATE, averaged over all X profiles
ate = model.coef_[-1]  # Last coefficient (bootcamp)
```

**Interpretation**: The average effect of bootcamp across the entire population, adjusting for X

### Option 2: Propensity Score Matching

```python
from sklearn.linear_model import LogisticRegression

# Estimate propensity scores: P(bootcamp=1|X)
ps_model = LogisticRegression()
ps_model.fit(X_controls, data['bootcamp'])
propensity_scores = ps_model.predict_proba(X_controls)[:, 1]

# Match treated and control units with similar propensity scores
# Then compare their outcomes
# (This relaxes the need for exact matching on X)
```

**Interpretation**: Effect estimated by comparing similar people (similar probability of treatment), not exact matches

### Option 3: Inverse Probability Weighting (IPW)

```python
# Weight observations by inverse propensity scores
weights = np.where(data['bootcamp'] == 1, 
                   1 / propensity_scores,
                   1 / (1 - propensity_scores))

# Weighted mean difference
ate = (data[data.bootcamp == 1]['salary'] * weights[data.bootcamp == 1]).mean() - \
      (data[data.bootcamp == 0]['salary'] * weights[data.bootcamp == 0]).mean()
```

**Interpretation**: Creates a "pseudo-population" where treatment is randomized

---

## Summary Table

| What you can conclude | What you cannot conclude |
|----------------------|--------------------------|
| ✅ Causal effect **for this exact X profile** (under ignorability) | ❌ Causal effect for other X profiles |
| ✅ If positive: bootcamp **causes** higher salary for these people | ❌ Population-average effect (ATE) |
| ✅ Local treatment effect (LATE) for this subgroup | ❌ Whether effects vary across groups (heterogeneity) |
| ✅ Direction of effect (positive/negative/zero) for this group | ❌ External validity to other populations |

---

## Key Takeaways

### 1. The Central Idea

**Ignorability/Unconfoundedness** is the assumption that you've measured all the important confounders. Once you control for those measured variables (X), any remaining differences in who gets treated are essentially random noise — not systematically related to potential outcomes.

In our bootcamp example: we assume that among people with the same age, education, experience, motivation, and available time, whether they enrolled is "as-if random" for purposes of estimating salary effects.

### 2. Strength of the Assumption

This is a **strong assumption** and requires careful thought about what confounders exist in your specific problem domain. When it holds (or approximately holds), it allows us to estimate causal effects from observational data using standard methods like regression, matching, or propensity scores.

### 3. Practical Implementation

Your exact-matching approach gives you a **local causal effect** for a narrow subgroup. To get:

1. **Population-average effects**: Use regression adjustment, propensity scores, or IPW
2. **Heterogeneous effects**: Estimate effects separately for different X profiles or use CATE methods
3. **Practical estimates with sparse data**: Use propensity score methods instead of exact matching

The fundamental principle remains the same: **under ignorability, controlling for X allows causal interpretation** — whether you do it via exact matching, regression, or propensity scores.

---

## Can You Use Multiple Strategies at Once?

### Short Answer

Generally, you should **choose one primary strategy** based on what assumptions are most credible in your context. However, you can use multiple strategies for **robustness checking** or **sensitivity analysis**.

### Why Usually Pick One Primary Strategy?

Each identification strategy makes **different assumptions** about the causal structure.

#### Example Scenario: Effect of Education (X) on Earnings (Y)

Let's say you could potentially use all three:

1. **Backdoor**: Control for family background, ability test scores, location
2. **Frontdoor**: Education → Job Skills (M) → Earnings (mechanism is measurable)
3. **IV**: Distance to college (Z) affects education but not directly earnings

#### The Problem with Using All Three Simultaneously

Each strategy assumes a **different causal graph**:

**Backdoor assumption:**
```
Family Background (C) → Education (X) → Earnings (Y)
                     ↘                 ↗
```
Assumes: controlling for C blocks all confounding

**Frontdoor assumption:**
```
Education (X) → Job Skills (M) → Earnings (Y)
         ↖                      ↗
          Unobserved Ability (U)
```
Assumes: the effect goes entirely through M, and you can measure M completely

**IV assumption:**
```
Distance to College (Z) → Education (X) → Earnings (Y)
                                    ↖
                          Unobserved Ability (U)
```
Assumes: Z affects Y only through X, and Z is independent of U

These are **incompatible frameworks** — you can't literally apply all three formulas to the same data and expect them to give the same answer.

### What You SHOULD Do: Robustness Checks

Instead of using all three simultaneously, use them as **independent checks**.

#### Strategy: Primary Analysis + Robustness Checks

**Primary approach: Backdoor (if you believe confounders are measurable)**

```python
from sklearn.linear_model import LinearRegression

# Control for observed confounders
X_controls = data[['family_income', 'ability_test', 'location']]
X_with_treatment = pd.concat([X_controls, data[['education_years']]], axis=1)

model_backdoor = LinearRegression()
model_backdoor.fit(X_with_treatment, data['earnings'])
ate_backdoor = model_backdoor.coef_[-1]

print(f"Backdoor ATE: ${ate_backdoor:,.0f}")
```

**Robustness check 1: Instrumental Variables**

```python
from linearmodels import IV2SLS

# Use distance to college as instrument
iv_model = IV2SLS(dependent=data['earnings'],
                   exog=data[['family_income', 'ability_test', 'location']],
                   endog=data[['education_years']],
                   instruments=data[['distance_to_college']])
iv_result = iv_model.fit()
ate_iv = iv_result.params['education_years']

print(f"IV ATE: ${ate_iv:,.0f}")
```

**Robustness check 2: Frontdoor (if mechanism is measurable)**

```python
# Step 1: Education → Job Skills
model_xm = LinearRegression()
model_xm.fit(data[['education_years']], data['job_skills'])

# Step 2: Job Skills → Earnings (controlling for Education)
model_my = LinearRegression()
model_my.fit(data[['education_years', 'job_skills']], data['earnings'])

# Frontdoor formula (simplified)
ate_frontdoor = model_xm.coef_[0] * model_my.coef_[1]

print(f"Frontdoor ATE: ${ate_frontdoor:,.0f}")
```

**Interpretation**:
- If all three estimates are **similar** → Strong evidence for causal effect (robust across different assumptions)
- If estimates **differ substantially** → Suggests at least one set of assumptions is violated; need to investigate which

### When Estimates Differ: What Does It Mean?

#### Scenario A: All Three Similar
```
Backdoor ATE:   $8,500
IV ATE:         $8,200
Frontdoor ATE:  $8,700
```
**Interpretation**: Strong causal evidence. The effect is robust across different identification assumptions.

#### Scenario B: IV Much Larger
```
Backdoor ATE:   $5,000
IV ATE:        $15,000
Frontdoor ATE:  $5,500
```
**Possible explanations**:
- IV estimate reflects **local average treatment effect (LATE)** for compliers (people whose education was affected by distance) — they may have higher returns
- IV instrument is **weak** (distance doesn't strongly predict education)
- IV **exclusion restriction violated** (distance affects earnings through other channels, e.g., urban/rural differences)

#### Scenario C: Frontdoor Much Smaller
```
Backdoor ATE:  $8,000
IV ATE:        $8,500
Frontdoor ATE: $3,000
```
**Possible explanation**:
- **Job skills don't fully mediate** the effect — education affects earnings through other pathways (signaling, networks) not captured by M
- Frontdoor assumption violated: the mechanism is incomplete

### Practical Guidance: Which One to Trust?

#### Decision Framework

1. **Evaluate assumptions for each strategy**:
   - Backdoor: Have I measured all confounders? (Often questionable)
   - Frontdoor: Is the mediator complete? Can I measure it fully? (Rarely true)
   - IV: Is the instrument truly exogenous and relevant? (Hard to verify)

2. **Prioritize based on credibility**:
   - If you have a **very credible IV** (natural experiment, randomized encouragement) → Trust IV most
   - If you have **rich covariate data** and believe confounders are observable → Trust backdoor
   - If the **mechanism is well-understood and measurable** → Trust frontdoor

3. **Use the others for robustness**:
   - Report all estimates
   - Discuss why they differ (if they do)
   - Acknowledge which assumptions you're most confident in

#### Example: What Leading Researchers Do

In practice, top econometrics papers often:

1. **Primary specification**: Use the most credible approach (often IV if they have a good natural experiment)

2. **Robustness checks**: Show estimates from alternative approaches:
   ```
   Table 2: Main Results (IV Estimates)
   Table 3: Robustness - Backdoor Adjustment
   Table 4: Robustness - Alternative Instruments
   Appendix: Frontdoor Analysis
   ```

3. **Discuss discrepancies**: If estimates differ, explain why and which is more credible

### Can You Ever Combine Them?

#### Yes, in Specific Cases:

**Case 1: Doubly Robust Estimation**

Combines backdoor (regression) and IPW (propensity scores):

```python
# Doubly robust: correct if EITHER outcome model OR propensity model is correct
from econml.dr import DRLearner

dr = DRLearner(model_regression=..., model_propensity=...)
dr.fit(Y=earnings, T=education, X=covariates)
ate_doubly_robust = dr.ate()
```

This isn't using backdoor + frontdoor + IV; it's a clever combination of two backdoor-related methods.

**Case 2: IV + Covariate Adjustment**

You can use IV while **also controlling for observed confounders**:

```python
# IV with additional controls
iv_model = IV2SLS(dependent=earnings,
                   exog=confounders,  # Still control for these
                   endog=education,
                   instruments=distance_to_college)
```

This strengthens IV by reducing variance, but the identification still relies on IV assumptions.

### Summary Table

| Question | Answer |
|----------|--------|
| Can I use backdoor, frontdoor, AND IV on the same problem? | Yes, for **robustness checking**, not as a single combined estimator |
| Should estimates be identical? | No — different assumptions often yield different estimates |
| What if they differ? | Investigate which assumptions are most credible in your context |
| Which one to trust? | The one whose assumptions are most defensible |
| Can I average them? | No — each targets potentially different estimands under different assumptions |

### Key Takeaway

Think of multiple strategies as **alternative paths to causal identification**, each relying on different assumptions. Use them to triangulate evidence and test robustness, not as a literal combination formula.

**If all three give similar answers**, you have strong evidence. **If they diverge**, you need to think carefully about which set of assumptions is most plausible in your specific problem.

---

## do-Calculus: The General Framework (Detailed Explanation)

### What is do-Calculus?

**do-Calculus** is a formal system of rules developed by Judea Pearl that allows us to derive whether a causal effect is identifiable from observational data, given a causal graph (DAG). It provides a mechanical way to transform causal queries (with the "do" operator) into statistical queries (without "do") that can be estimated from data.

### The Core Problem

We want to know: **P(Y | do(X = x))** — the probability distribution of Y when we intervene to set X to value x.

But we only have observational data, which gives us: **P(Y | X = x)** — the probability distribution of Y when we observe X = x (no intervention).

**These are different!** Observational data includes confounding; interventional data does not.

**do-Calculus provides three rules** that let us transform P(Y | do(X)) into expressions involving only observational probabilities P(·), if identification is possible.

---

### The Three Rules of do-Calculus

Before stating the rules, understand the notation:
- **P(y | do(x), z)** means: the probability of Y = y, given we intervene to set X = x and observe Z = z
- **G_X̄** means: the graph G with all arrows **into** X removed (simulating intervention on X)
- **G_X** means: the graph G with all arrows **out of** X removed
- **G_X̄Z** means: remove arrows into X and remove arrows into Z
- **(Y ⊥ Z | W)_G** means: Y is independent of Z given W in graph G

Now the three rules:

---

## Rule 1: Insertion/Deletion of Observations

**Statement:**
```
P(y | do(x), z, w) = P(y | do(x), w)  
  if (Y ⊥ Z | X, W) in G_X̄
```

**Plain English:**
If Z is independent of Y given X and W in the manipulated graph G_X̄ (where arrows into X are removed), then we can **ignore** Z when computing the effect of do(X) on Y.

**Intuition:**
Once we've intervened on X (cutting incoming arrows), if Z provides no additional information about Y beyond what X and W already tell us, then Z is irrelevant — we can drop it from our conditioning set.

### Concrete Example: Rule 1

**Scenario: Effect of Exercise (X) on Heart Health (Y)**

```
Causal Graph G:
    Age (Z) → Exercise (X) → Heart Health (Y)
            ↘               ↗
              Body Weight (W)
              
Age affects both exercise habits and heart health
Body Weight is affected by Age and affects Heart Health
```

**Question:** Does Age (Z) matter when estimating P(Y | do(X), W)?

**Step 1:** Create G_X̄ (remove arrows into X):
```
G_X̄:
    Age (Z)    Exercise (X) → Heart Health (Y)
            ↘               ↗
              Body Weight (W)
```

The arrow Age → Exercise is removed (we're intervening on Exercise).

**Step 2:** Check independence in G_X̄:
Is (Y ⊥ Z | X, W) in G_X̄?

Given Exercise level (X) and Body Weight (W), is Heart Health (Y) independent of Age (Z)?

Looking at G_X̄:
- Age → Body Weight → Heart Health (this path is blocked by conditioning on W)
- There's no other path from Age to Heart Health that isn't blocked

**Yes!** (Y ⊥ Z | X, W) in G_X̄

**Conclusion (by Rule 1):**
```
P(Y | do(X), Z, W) = P(Y | do(X), W)
```

We can **ignore Age** when estimating the effect of exercise on heart health, as long as we condition on Body Weight.

**Practical implication:** You don't need to collect or control for Age if you're already controlling for Body Weight when estimating this causal effect.

---

## Rule 2: Action/Observation Exchange

**Statement:**
```
P(y | do(x), do(z), w) = P(y | do(x), z, w)  
  if (Y ⊥ Z | X, W) in G_X̄Z
```

**Plain English:**
If Z is independent of Y given X and W in the graph G_X̄Z (where arrows into both X and Z are removed), then intervening on Z is the same as merely observing Z — we can replace do(Z) with observed Z.

**Intuition:**
If there are no confounders between Z and Y (after intervening on X and Z), then the observational association between Z and Y is the same as the causal effect. This lets us "downgrade" an intervention do(Z) to a passive observation Z.

### Concrete Example: Rule 2

**Scenario: Effect of Drug Dose (X) and Exercise (Z) on Recovery (Y)**

```
Causal Graph G:
    Severity (C) → Drug Dose (X) → Recovery (Y)
                 ↘                ↗
                   Exercise (Z)
                   
Severity confounds both Drug Dose and Exercise
Both Drug Dose and Exercise affect Recovery
```

**Question:** Can we replace P(Y | do(X), do(Z)) with P(Y | do(X), Z)?

**Step 1:** Create G_X̄Z (remove arrows into X and into Z):
```
G_X̄Z:
    Severity (C)    Drug Dose (X) → Recovery (Y)
                                   ↗
                      Exercise (Z)
```

Both arrows from Severity are removed (we've intervened on both X and Z).

**Step 2:** Check independence in G_X̄Z:
Is (Y ⊥ Z | X) in G_X̄Z?

Given Drug Dose (X), is Recovery (Y) independent of Exercise (Z)?

Looking at G_X̄Z:
- There's a direct path: Z → Y (NOT blocked by X)

**No!** Y is NOT independent of Z given X in G_X̄Z (there's a direct causal effect Z → Y).

**Wait — this seems like Rule 2 fails?**

Let me reconsider. Actually, for Rule 2, we need to check if the independence holds. In this case:
- Z directly causes Y, so they're NOT independent even after conditioning on X
- Rule 2 does NOT apply here

**Let's try a different example where Rule 2 DOES work:**

### Better Example for Rule 2

```
Causal Graph G:
    Genes (C) → Exercise (Z) → Fitness (M) → Recovery (Y)
              ↘                              ↗
                      Drug Dose (X) ──────────
                      
Genes confound Exercise and Recovery (through Fitness)
Drug Dose directly affects Recovery
Exercise affects Recovery only through Fitness
```

**Question:** Can we replace P(Y | do(X), do(Z), M) with P(Y | do(X), Z, M)?

**Step 1:** Create G_X̄Z (remove arrows into X and into Z):
```
G_X̄Z:
    Genes (C)    Exercise (Z) → Fitness (M) → Recovery (Y)
                                              ↗
                       Drug Dose (X) ──────────
```

**Step 2:** Check independence in G_X̄Z:
Is (Y ⊥ Z | X, M) in G_X̄Z?

Given Drug Dose (X) and Fitness level (M), is Recovery (Y) independent of Exercise (Z)?

Looking at G_X̄Z:
- Path Z → M → Y is blocked by conditioning on M
- No confounding path exists (arrow from Genes to Z was removed)
- X and Z don't interact in their effect on Y

**Yes!** (Y ⊥ Z | X, M) in G_X̄Z

**Conclusion (by Rule 2):**
```
P(Y | do(X), do(Z), M) = P(Y | do(X), Z, M)
```

**Practical implication:** If we're already intervening on Drug Dose and observing Fitness level, then we don't need to intervene on Exercise — just observing the exercise level is sufficient. This is because once we condition on Fitness (the mediator), Exercise's effect is captured, and there's no confounding.

---

## Rule 3: Insertion/Deletion of Actions

**Statement:**
```
P(y | do(x), do(z), w) = P(y | do(x), w)  
  if (Y ⊥ Z | X, W) in G_X̄Z̄(W)
```

Where G_X̄Z̄(W) means: remove arrows into X, remove arrows into Z, keep only arrows from W.

**Plain English:**
If Z is independent of Y given X and W in the graph where we've removed all incoming arrows to both X and Z (and kept only W's influence), then intervening on Z has no effect — we can completely remove do(Z).

**Intuition:**
If Z doesn't affect Y (even when we intervene on both X and Z), then the intervention on Z is irrelevant to estimating the effect on Y. This is the strongest rule — it lets us completely drop an intervention.

### Concrete Example: Rule 3

**Scenario: Effect of Medication (X) and Room Temperature (Z) on Recovery (Y)**

```
Causal Graph G:
    Severity (C) → Medication (X) → Recovery (Y)
                 ↘                
                   Room Temp (Z)
                   
Severity affects both Medication choice and Room Temperature
Medication affects Recovery
Room Temperature does NOT affect Recovery (just a spurious correlation)
```

**Question:** Can we ignore do(Z) when computing P(Y | do(X), do(Z))?

**Step 1:** Create G_X̄Z̄ (remove arrows into X and into Z):
```
G_X̄Z̄:
    Severity (C)    Medication (X) → Recovery (Y)
                                  
                      Room Temp (Z)
```

All arrows into X and Z are removed.

**Step 2:** Check independence in G_X̄Z̄:
Is (Y ⊥ Z | X) in G_X̄Z̄?

Given Medication (X), is Recovery (Y) independent of Room Temperature (Z)?

Looking at G_X̄Z̄:
- There's no path from Z to Y at all
- Z is completely disconnected from Y

**Yes!** (Y ⊥ Z | X) in G_X̄Z̄

**Conclusion (by Rule 3):**
```
P(Y | do(X), do(Z)) = P(Y | do(X))
```

**Practical implication:** Room temperature has no causal effect on recovery — intervening on it is useless. We can completely ignore it. The only reason room temperature might correlate with recovery in observational data is because of the common cause (severity), but once we intervene on medication, room temperature is irrelevant.

---

## Summary of the Three Rules

| Rule | What it does | When it applies | What you can do |
|------|-------------|-----------------|-----------------|
| **Rule 1: Insertion/Deletion of Observations** | Remove an observed variable from conditioning set | (Y ⊥ Z \| X, W) in G_X̄ | Drop Z from P(y \| do(x), z, w) → P(y \| do(x), w) |
| **Rule 2: Action/Observation Exchange** | Convert an intervention to an observation | (Y ⊥ Z \| X, W) in G_X̄Z | Change do(z) to z: P(y \| do(x), do(z), w) → P(y \| do(x), z, w) |
| **Rule 3: Insertion/Deletion of Actions** | Remove an intervention entirely | (Y ⊥ Z \| X, W) in G_X̄Z̄(W) | Drop do(z): P(y \| do(x), do(z), w) → P(y \| do(x), w) |

---

## How do-Calculus Helps with Identification

**The Complete Process:**

1. **Start with the causal query:** P(Y | do(X))
2. **Apply Rules 1, 2, and 3 iteratively** to transform the expression
3. **Goal:** Eliminate all "do" operators, leaving only observational probabilities
4. **If successful:** The causal effect is **identifiable** — you can estimate it from data
5. **If not:** The effect is **not identifiable** from the given graph and available data

### Example: Deriving the Backdoor Adjustment Formula

**Graph:**
```
    Confounder (C)
         ↓        ↓
    Treatment (X) → Outcome (Y)
```

**Goal:** Express P(Y | do(X)) in terms of observational probabilities.

**Step 1:** Expand using the law of total probability:
```
P(Y | do(X)) = Σ_c P(Y | do(X), C=c) · P(C=c | do(X))
```

**Step 2:** Apply Rule 2 to P(C | do(X)):
- Check if (C ⊥ X) in G_X̄ (graph with arrows into X removed)
- Yes! C has no parents, so it's independent of the intervention on X
- Therefore: P(C | do(X)) = P(C)

Now we have:
```
P(Y | do(X)) = Σ_c P(Y | do(X), C=c) · P(C)
```

**Step 3:** Apply Rule 2 to P(Y | do(X), C):
- Check if (Y ⊥ X | C) in G_X̄C (remove arrows into X and C)
- In G_X̄C, the arrow C→X is gone, and C has no incoming arrows
- The only remaining path is X→Y (direct causal effect)
- But wait — we need to check if observing X is the same as intervening
- Actually, after conditioning on C, the backdoor path is blocked
- So: P(Y | do(X), C) = P(Y | X, C)

**Final result:**
```
P(Y | do(X)) = Σ_c P(Y | X, C=c) · P(C)
```

This is the **backdoor adjustment formula** — derived using do-calculus!

---

## Key Insights

### 1. do-Calculus is Complete
Pearl proved that if a causal effect is identifiable from a graph, do-calculus can derive it. If do-calculus fails to identify it, it's truly non-identifiable.

### 2. Mechanical Application
You don't need to be clever — just apply the rules systematically. Software can do this automatically.

### 3. Generalizes All Previous Strategies
- Backdoor criterion → derivable via do-calculus
- Frontdoor criterion → derivable via do-calculus  
- Instrumental variables → derivable via do-calculus

### 4. Works for Complex Graphs
Even when backdoor/frontdoor/IV don't apply, do-calculus might still find a way to identify the effect.

---

## Practical Takeaway

**For most applications, you don't need to manually apply do-calculus.** Instead:

1. **Draw your causal graph** (DAG)
2. **Use software** (e.g., `dowhy` in Python, `dagitty` in R) to check identifiability
3. **The software applies do-calculus** behind the scenes
4. **You get back:** either an identification formula or a message that the effect is non-identifiable

**When to learn do-calculus deeply:**
- You're doing causal inference research
- You're designing new identification algorithms
- You want to deeply understand *why* certain effects are/aren't identifiable

**For practitioners:**
- Understand the intuition: it's about systematically removing "do" operators
- Know the three rules exist and what they do
- Use software tools that implement do-calculus for you

---

*These notes provide detailed explanations and examples to supplement the main identification strategies content.*

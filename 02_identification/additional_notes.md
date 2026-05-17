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

## Common Pitfalls: Concrete Examples

### 1. Assuming Identification Without Justification

**Example:**
```python
# Estimating effect of job training on wages
model = LinearRegression()
model.fit(data[['age', 'education', 'experience']], data['wage'])
training_effect = model.coef_[0]  # "This is the causal effect!"
```

**Problem:** No DAG was drawn. What if motivation affects both training enrollment and wages? What if prior employment affects training access and future wages? Controlling for age, education, and experience may not be sufficient.

---

### 2. Controlling for Everything

**Example:**
```python
# Effect of education on income
# "Let me control for everything to be safe"
controls = ['age', 'parent_income', 'ability_test', 
            'first_job_salary',  # ← Mediator! (caused by education)
            'spouse_education',  # ← Collider! (caused by income)
            'current_city']      # ← Post-treatment! (caused by education)

model.fit(data[controls + ['education']], data['income'])
```

**Problem:** 
- `first_job_salary` is a mediator (education → first job → income) — controlling blocks the causal path
- `spouse_education` is a collider (education → spouse education ← income) — controlling creates bias
- `current_city` is post-treatment (education → career → city choice) — controlling blocks mechanism

**Result:** Severely biased estimate, likely underestimating the true effect.

---

### 3. Assuming IV Validity Without Evidence

**Example:**
```python
# Effect of exercise on weight loss
# "I'll use gym proximity as an instrument!"
iv_model = IV2SLS(dependent=data['weight_loss'],
                   endog=data['exercise_hours'],
                   instruments=data['distance_to_gym'])
```

**Problem:**
- **Relevance:** Maybe okay (closer to gym → more exercise)
- **Exclusion restriction violation:** Distance to gym might affect weight loss directly through walking/biking to work, neighborhood walkability, income level (wealthy neighborhoods have closer gyms AND healthier food)
- **Independence violation:** People who live near gyms might be health-conscious and would lose weight regardless

**No justification provided** for why exclusion restriction holds.

---

### 4. Ignoring Non-Identification

**Example:**
```python
# DAG: U → Treatment → Outcome
#      U → Outcome
# where U is unmeasured

# Analyst proceeds anyway:
model = LinearRegression()
model.fit(data[['treatment']], data['outcome'])
effect = model.coef_[0]

print(f"Causal effect: {effect:.2f}")  # Report with confidence!
```

**Problem:** With unmeasured confounder U and no valid instrument, the effect is **not identified**. The estimate is biased no matter how much data you have. Should report "effect is not identifiable from available data" instead.

---

### 5. Confusing Identification with Estimation

**Example:**
```python
# Effect of drug on recovery, with unmeasured confounding
model = LogisticRegression()
model.fit(data[['drug']], data['recovery'])

# Get a p-value < 0.05
p_value = 0.003
print(f"Statistically significant (p={p_value})! This proves causation!")
```

**Problem:** 
- **Identification issue:** Unmeasured confounding (severity affects both drug prescription and recovery)
- **Statistical significance** just means the *association* is not due to sampling error
- You've precisely estimated a *biased* quantity
- The true causal effect remains unknown

**Correct interpretation:** "We found a strong association (p=0.003), but without controlling for disease severity, we cannot make causal claims."

---

*These notes provide detailed explanations and examples to supplement the main identification strategies content. For detailed do-Calculus explanations with concrete examples, see the do-Calculus section in `01_identification_strategies.md`.*

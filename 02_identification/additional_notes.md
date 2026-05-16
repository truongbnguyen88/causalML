# Additional Notes: Strategy #4 - Ignorability/Unconfoundedness

## The Core Concept

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

*These notes provide detailed explanations and examples to supplement the main identification strategies content.*

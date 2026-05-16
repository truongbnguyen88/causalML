# Causal Identification: When Can We Estimate Causal Effects?

## Overview

In Module 1, we learned about confounding and how it creates bias in causal estimates. Now we address the fundamental question of causal inference:

**When can we identify causal effects from observational data?**

**Identification** means we can, in principle, estimate a causal effect from data if we had infinite samples. It's about whether the causal quantity we care about can be expressed in terms of the observed data distribution.

This module covers the main strategies for identifying causal effects when randomized experiments aren't possible.

---

## The Identification Problem

### What is Identification?

A causal effect is **identified** if we can express it as a function of the observed data distribution.

**Formally:**
- We want to know: P(Y | do(X = x)) — the outcome distribution if we *intervened* to set X = x
- We observe: P(Y | X = x) — the outcome distribution among those who *happen* to have X = x
- **Identification**: Can we compute P(Y | do(X)) from P(Y, X, Z)?

**Key insight:** Observational association ≠ Causal effect (unless certain conditions hold)

### Why Identification Matters

1. **Precedes estimation**: Must establish identifiability before worrying about statistical estimation
2. **Reveals what data you need**: Tells you what variables to measure
3. **Makes assumptions explicit**: Forces you to state what you're assuming
4. **Prevents futile analysis**: If effect isn't identified, no amount of data helps

**The hierarchy:**
1. **Identification** (theoretical): Can we compute the causal effect from the data distribution?
2. **Estimation** (statistical): Given finite data, how do we estimate it?
3. **Inference** (statistical): What's the uncertainty around our estimate?

---

## Core Identification Strategies

There are several main approaches to identifying causal effects:

| Strategy | Key Idea | When to Use | Requirements |
|----------|----------|-------------|--------------|
| **Backdoor Adjustment** | Control for confounders | Confounders are measurable | Block all backdoor paths |
| **Frontdoor Criterion** | Use mediators | Confounders unmeasurable but mediator is | Specific graph structure |
| **Instrumental Variables** | Use exogenous variation | Confounders unmeasurable | Valid instrument exists |
| **Randomization** | Break confounding by design | Can run experiment | Random treatment assignment |
| **Regression Discontinuity** | Exploit threshold rules | Treatment based on cutoff | Sharp discontinuity |
| **Difference-in-Differences** | Use parallel trends | Panel data with treatment timing variation | Parallel trends assumption |

In this module, we focus on the first three (backdoor, frontdoor, IV). Later modules cover experimental designs and other strategies.

---

## Strategy 1: Backdoor Criterion (Adjustment for Confounders)

### The Idea

If we can measure all confounders and block all backdoor paths from treatment to outcome, we can identify the causal effect by "adjusting" for those confounders.

### The Backdoor Criterion (Pearl, 1995)

A set of variables Z **satisfies the backdoor criterion** relative to (X, Y) if:

1. **No descendant of X**: Z contains no descendants of X (don't control for mediators or colliders caused by X)
2. **Blocks all backdoor paths**: Z blocks every path from X to Y that has an arrow into X

**If Z satisfies the backdoor criterion:**

$$P(Y | do(X = x)) = \sum_z P(Y | X = x, Z = z) \cdot P(Z = z)$$

This is the **adjustment formula**. It says: we can compute the causal effect by stratifying on Z and averaging.

### Example 1: Single Confounder

```
Z (Age)
 ↓    ↓
X → Y
(Smoking) (Lung Cancer)
```

**Backdoor paths from X to Y:**
- X ← Z → Y

**Adjustment set:** {Z}
- Blocks the backdoor path ✓
- Not a descendant of X ✓

**Causal effect identified:** Yes! Control for Age.

**Formula:**
$$P(\text{Cancer} | do(\text{Smoking} = 1)) = \sum_{\text{age}} P(\text{Cancer} | \text{Smoking} = 1, \text{Age} = \text{age}) \cdot P(\text{Age} = \text{age})$$

### Example 2: Multiple Confounders

```
    Z1    Z2
    ↓ ×  ↓
      X → Y
```

**Backdoor paths:**
- X ← Z1 → Y
- X ← Z2 → Y

**Adjustment set:** {Z1, Z2}

**Causal effect identified:** Yes! Control for both.

### Example 3: Mediator (Don't Control!)

```
X → M → Y
```

**Backdoor paths:** None!

**Adjustment set:** Empty set {}
- No backdoor paths to block
- M is a mediator (descendant of X), so don't control for it

**Causal effect identified:** Yes! No adjustment needed (just compare treated vs control).

### Example 4: Collider (Don't Control!)

```
X → C ← Y
```

**Backdoor paths:** None! (C is a collider, naturally blocks the path)

**Adjustment set:** Empty set {}

**Causal effect identified:** Yes! Don't adjust for C (would create bias).

### Finding Minimal Adjustment Sets

Often multiple sets of variables satisfy the backdoor criterion. We prefer **minimal** sets (fewest variables) because:
- Easier to measure
- More efficient estimation
- Less risk of measurement error
- Avoid over-controlling

**Example:**

```
Z1 → X → Y ← Z2
     ↓       ↑
     Z3 ------
```

**Backdoor paths:**
- X ← Z1 → ... (if Z1 also affects Y)

**Valid adjustment sets:**
- {Z1} - minimal ✓
- {Z1, Z3} - also valid but not minimal
- {Z2} - blocks nothing, invalid ✗

**Use the minimal set:** {Z1}

### Limitations of Backdoor Adjustment

**Won't work when:**
1. **Unmeasured confounders**: Can't control for variables you didn't measure
2. **No valid adjustment set exists**: Some DAG structures don't allow backdoor adjustment
3. **Measurement error**: Can't perfectly measure confounders
4. **Post-treatment confounding**: Confounders affected by treatment

**When backdoor fails → Try frontdoor or IV**

---

## Strategy 2: Frontdoor Criterion (Using Mediators)

### The Idea

Sometimes we can't measure confounders, but we CAN measure how the treatment works (the mediator). If the mediator fully captures the treatment's effect, we can identify the causal effect through a two-step process.

### The Frontdoor Criterion (Pearl, 1995)

A set of variables M **satisfies the frontdoor criterion** relative to (X, Y) if:

1. **M intercepts all directed paths from X to Y**: All causal pathways go through M
2. **No backdoor paths from X to M**: No confounding of X → M
3. **X blocks all backdoor paths from M to Y**: X d-separates M and Y given X

**If M satisfies the frontdoor criterion:**

$$P(Y | do(X = x)) = \sum_m P(M = m | X = x) \sum_{x'} P(Y | M = m, X = x') \cdot P(X = x')$$

This is the **frontdoor adjustment formula**.

### Classic Example: Smoking → Tar → Lung Cancer

```
    U (Genetics)
    ↓           ↓
Smoking → Tar → Lung Cancer
```

**Problem:** U (genetics) is unmeasured and confounds Smoking → Lung Cancer

**Backdoor adjustment:** Can't control for U (unmeasured) ✗

**But notice:**
- Smoking → Tar has no backdoor path (no confounding)
- Tar → Cancer: backdoor path Tar ← Smoking ← U → Cancer is blocked by Smoking

**Frontdoor criterion satisfied!**

**Two-step identification:**
1. Estimate effect of Smoking on Tar: P(Tar | Smoking) (no confounding)
2. Estimate effect of Tar on Cancer, controlling for Smoking: P(Cancer | Tar, Smoking)
3. Combine using frontdoor formula

**Intuition:**
- We can't directly estimate Smoking → Cancer (confounded)
- But we CAN estimate Smoking → Tar (unconfounded)
- And we CAN estimate Tar → Cancer controlling for Smoking (blocks the backdoor)
- Multiply these together to get total effect!

### When to Use Frontdoor

**Use when:**
- Direct path is confounded by unmeasured variables
- You can measure the mediator (mechanism)
- The mechanism fully captures the effect

**Rare in practice because:**
- Requires complete mediation (all effect through M)
- Hard to verify mechanism is complete
- Often other paths exist

**Common applications:**
- Mediation analysis in psychology
- Mechanism studies in medicine
- When mechanism is well-understood theoretically

---

## Strategy 3: Instrumental Variables (Using Exogenous Variation)

### The Idea

An **instrumental variable** (IV) is a variable that:
1. Affects the treatment
2. Doesn't affect the outcome except through treatment
3. Isn't affected by confounders

It provides "as-if random" variation in treatment that we can exploit.

### Instrumental Variable Requirements

A variable Z is a valid instrument for estimating the effect of X on Y if:

1. **Relevance**: Z affects X
   - Cor(Z, X) ≠ 0
   - Can be tested from data ✓

2. **Exclusion Restriction**: Z affects Y only through X
   - No direct path Z → Y
   - Cannot be fully tested (assumption) ⚠️

3. **Independence**: Z is independent of confounders
   - No backdoor paths Z ← U → Y
   - Cannot be fully tested (assumption) ⚠️

**DAG for valid IV:**

```
       U
       ↓  ↓
Z → X → Y
```

- Z → X (relevance)
- No Z → Y direct path (exclusion)
- No Z ← U → Y path (independence)

### Classic Examples

**Example 1: Vietnam Draft Lottery**

```
Draft Lottery Number → Military Service → Earnings
                              ↑
                           (ability, family background, etc.)
```

- **Instrument (Z)**: Draft lottery number (random)
- **Treatment (X)**: Military service
- **Outcome (Y)**: Lifetime earnings
- **Confounder (U)**: Ability, family background (unmeasured)

**Why it's a valid IV:**
1. **Relevance**: Low lottery number → more likely to serve ✓
2. **Exclusion**: Lottery number doesn't affect earnings except through service ✓
3. **Independence**: Lottery is random, uncorrelated with ability ✓

**Example 2: Distance to College**

```
Distance to College → College Attendance → Income
                              ↑
                          (ability, family wealth, etc.)
```

- **Instrument (Z)**: Distance to nearest college
- **Treatment (X)**: College attendance  
- **Outcome (Y)**: Income
- **Confounder (U)**: Ability, family background (unmeasured)

**Why it might be a valid IV:**
1. **Relevance**: Closer to college → more likely to attend ✓
2. **Exclusion**: Distance doesn't affect income except through education (debatable)
3. **Independence**: Distance isn't correlated with ability (questionable - families select location)

**Validity concerns:**
- Exclusion: Living near a college might affect income through networks, culture, etc.
- Independence: Wealthy families might live near universities

**Lesson:** IVs require strong assumptions and careful justification!

### IV Identification Formula

With a valid instrument Z:

$$\text{Causal Effect} = \frac{Cov(Y, Z)}{Cov(X, Z)}$$

**Intuition:**
- Numerator: How much does Y change with Z?
- Denominator: How much does X change with Z?
- Ratio: How much does Y change per unit change in X (using only Z-induced variation)

**This is called the Wald estimator** (for binary Z and X).

### When to Use IV

**Use when:**
- Unmeasured confounding prevents backdoor/frontdoor
- You have a credible source of exogenous variation
- Strong domain knowledge supports IV assumptions

**Challenges:**
- Finding valid instruments is hard
- Exclusion restriction is untestable
- Weak instruments → large standard errors
- Estimates only **Local Average Treatment Effect (LATE)** for compliers, not full ATE

---

## Strategy 4: Ignorability/Unconfoundedness

### The Assumption

The **ignorability** (or **unconfoundedness**) assumption states:

$$(Y(1), Y(0)) \perp X | Z$$

**In words:** Conditional on Z, treatment assignment is independent of potential outcomes.

**Equivalent statements:**
- "No unmeasured confounding"
- "Selection on observables"
- "Conditional independence assumption (CIA)"

### What It Means

After controlling for Z:
- Treated and control groups are comparable (as-if randomized)
- Treatment assignment doesn't depend on potential outcomes
- No hidden confounders remain

**This is the assumption underlying backdoor adjustment!**

### When Is It Plausible?

**More plausible when:**
- Rich set of measured covariates
- Domain knowledge suggests you measured all confounders
- Pre-treatment variables that determine treatment
- Administrative data with comprehensive records

**Less plausible when:**
- Measured variables are limited
- Treatment is self-selected based on expectations
- Unobservable characteristics matter (ability, motivation, health)
- No clear selection process

### Testing Ignorability

**Cannot fully test** (potential outcomes are never observed), but can do:

1. **Balance checks**: Are treated/control groups similar on observables?
2. **Placebo tests**: Does treatment "affect" pre-treatment outcomes?
3. **Sensitivity analysis**: How robust to unmeasured confounding?
4. **Over-identification tests**: If multiple adjustment sets exist, do they agree?

**Ultimately requires subject-matter judgment!**

**Note:** See `additional_notes.md` for a detailed concrete example of ignorability with the online bootcamp scenario.

---

## Comparing Identification Strategies

| Criterion | Backdoor | Frontdoor | IV |
|-----------|----------|-----------|-----|
| **What you need** | Measure all confounders | Measure mediator | Find valid instrument |
| **Main assumption** | Ignorability | Complete mediation | Exclusion restriction |
| **Testability** | Partially (balance) | Partially | Relevance only |
| **Estimand** | ATE | ATE | LATE (for compliers) |
| **Efficiency** | Best | Good | Often poor (weak IV) |
| **When to use** | Can measure confounders | Can't measure confounders but know mechanism | Can't measure confounders but have exogenous variation |

**General guidance:**
1. **Try backdoor first** (easiest if confounders measurable)
2. **Try frontdoor if** mechanism is known and complete
3. **Try IV if** you have credible exogenous variation
4. **If none work** → Consider experimental design or give up on causal claims

**Note:** See `additional_notes.md` for detailed discussion on using multiple identification strategies simultaneously for robustness checking.

---

## do-Calculus: The General Framework

### What is do-Calculus?

**do-calculus** is a formal system of rules developed by Judea Pearl that allows us to derive whether a causal effect is identifiable from observational data, given a causal graph (DAG). It provides a mechanical way to transform causal queries (with the "do" operator) into statistical queries (without "do") that can be estimated from data.

### The Core Problem

We want to know: **P(Y | do(X = x))** — the probability distribution of Y when we intervene to set X to value x.

But we only have observational data, which gives us: **P(Y | X = x)** — the probability distribution of Y when we observe X = x (no intervention).

**These are different!** Observational data includes confounding; interventional data does not.

**do-Calculus provides three rules** that let us transform P(Y | do(X)) into expressions involving only observational probabilities P(·), if identification is possible.

### The Three Rules of do-Calculus

Before stating the rules, understand the notation:
- **P(y | do(x), z)** means: the probability of Y = y, given we intervene to set X = x and observe Z = z
- **G_X̄** means: the graph G with all arrows **into** X removed (simulating intervention on X)
- **G_X** means: the graph G with all arrows **out of** X removed
- **G_X̄Z** means: remove arrows into X and remove arrows into Z
- **(Y ⊥ Z | W)_G** means: Y is independent of Z given W in graph G

---

### Rule 1: Insertion/Deletion of Observations

**Statement:**
$$P(Y | do(X), Z, W) = P(Y | do(X), W) \text{ if } (Y \perp Z | X, W) \text{ in } G_{\overline{X}}$$

**Plain English:** If Z is independent of Y given X and W in the manipulated graph G_X̄ (where arrows into X are removed), then we can **ignore** Z when computing the effect of do(X) on Y.

**Intuition:** Once we've intervened on X (cutting incoming arrows), if Z provides no additional information about Y beyond what X and W already tell us, then Z is irrelevant — we can drop it from our conditioning set.

#### Concrete Example: Rule 1 - Exercise and Heart Health

**Scenario:** Effect of Exercise (X) on Heart Health (Y)

```
Causal Graph G:
    Age (Z) → Exercise (X) → Heart Health (Y)
            ↘               ↗
              Body Weight (W)
```

Age affects both exercise habits and heart health; Body Weight is affected by Age and affects Heart Health.

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
$$P(Y | do(X), Z, W) = P(Y | do(X), W)$$

We can **ignore Age** when estimating the effect of exercise on heart health, as long as we condition on Body Weight.

**Practical implication:** You don't need to collect or control for Age if you're already controlling for Body Weight when estimating this causal effect.

---

### Rule 2: Action/Observation Exchange

**Statement:**
$$P(Y | do(X), do(Z), W) = P(Y | do(X), Z, W) \text{ if } (Y \perp Z | X, W) \text{ in } G_{\overline{X}, \overline{Z}}$$

**Plain English:** If Z is independent of Y given X and W in the graph G_X̄Z (where arrows into both X and Z are removed), then intervening on Z is the same as merely observing Z — we can replace do(Z) with observed Z.

**Intuition:** If there are no confounders between Z and Y (after intervening on X and Z), then the observational association between Z and Y is the same as the causal effect. This lets us "downgrade" an intervention do(Z) to a passive observation Z.

#### Concrete Example: Rule 2 - Drug, Exercise, and Recovery

**Scenario:** Effect of Drug Dose (X) and Exercise (Z) on Recovery (Y)

```
Causal Graph G:
    Genes (C) → Exercise (Z) → Fitness (M) → Recovery (Y)
              ↘                              ↗
                      Drug Dose (X) ──────────
```

Genes confound Exercise and Recovery (through Fitness); Drug Dose directly affects Recovery; Exercise affects Recovery only through Fitness.

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
$$P(Y | do(X), do(Z), M) = P(Y | do(X), Z, M)$$

**Practical implication:** If we're already intervening on Drug Dose and observing Fitness level, then we don't need to intervene on Exercise — just observing the exercise level is sufficient. This is because once we condition on Fitness (the mediator), Exercise's effect is captured, and there's no confounding.

---

### Rule 3: Insertion/Deletion of Actions

**Statement:**
$$P(Y | do(X), do(Z), W) = P(Y | do(X), W) \text{ if } (Y \perp Z | X, W) \text{ in } G_{\overline{X}, \overline{Z(W)}}$$

Where G_X̄Z̄(W) means: remove arrows into X, remove arrows into Z, keep only arrows from W.

**Plain English:** If Z is independent of Y given X and W in the graph where we've removed all incoming arrows to both X and Z (and kept only W's influence), then intervening on Z has no effect — we can completely remove do(Z).

**Intuition:** If Z doesn't affect Y (even when we intervene on both X and Z), then the intervention on Z is irrelevant to estimating the effect on Y. This is the strongest rule — it lets us completely drop an intervention.

#### Concrete Example: Rule 3 - Medication and Room Temperature

**Scenario:** Effect of Medication (X) and Room Temperature (Z) on Recovery (Y)

```
Causal Graph G:
    Severity (C) → Medication (X) → Recovery (Y)
                 ↘                
                   Room Temp (Z)
```

Severity affects both Medication choice and Room Temperature; Medication affects Recovery; Room Temperature does NOT affect Recovery (just a spurious correlation).

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
$$P(Y | do(X), do(Z)) = P(Y | do(X))$$

**Practical implication:** Room temperature has no causal effect on recovery — intervening on it is useless. We can completely ignore it. The only reason room temperature might correlate with recovery in observational data is because of the common cause (severity), but once we intervene on medication, room temperature is irrelevant.

---

### Summary of the Three Rules

| Rule | What it does | When it applies | What you can do |
|------|-------------|-----------------|-----------------|
| **Rule 1: Insertion/Deletion of Observations** | Remove an observed variable from conditioning set | (Y ⊥ Z \| X, W) in G_X̄ | Drop Z from P(y \| do(x), z, w) → P(y \| do(x), w) |
| **Rule 2: Action/Observation Exchange** | Convert an intervention to an observation | (Y ⊥ Z \| X, W) in G_X̄Z | Change do(z) to z: P(y \| do(x), do(z), w) → P(y \| do(x), z, w) |
| **Rule 3: Insertion/Deletion of Actions** | Remove an intervention entirely | (Y ⊥ Z \| X, W) in G_X̄Z̄(W) | Drop do(z): P(y \| do(x), do(z), w) → P(y \| do(x), w) |

### Why It Matters

do-calculus allows you to:
1. **Prove identifiability** for complex DAGs
2. **Derive identification formulas** algorithmically
3. **Unify backdoor, frontdoor, and IV** as special cases

#### Example: Deriving the Backdoor Adjustment Formula

**Graph:**
```
    Confounder (C)
         ↓        ↓
    Treatment (X) → Outcome (Y)
```

**Goal:** Express P(Y | do(X)) in terms of observational probabilities.

**Step 1:** Expand using the law of total probability:
$$P(Y | do(X)) = \sum_c P(Y | do(X), C=c) \cdot P(C=c | do(X))$$

**Step 2:** Apply Rule 2 to P(C | do(X)):
- Check if (C ⊥ X) in G_X̄ (graph with arrows into X removed)
- Yes! C has no parents, so it's independent of the intervention on X
- Therefore: P(C | do(X)) = P(C)

Now we have:
$$P(Y | do(X)) = \sum_c P(Y | do(X), C=c) \cdot P(C)$$

**Step 3:** Apply Rule 2 to P(Y | do(X), C):
- After conditioning on C, the backdoor path is blocked
- So: P(Y | do(X), C) = P(Y | X, C)

**Final result:**
$$P(Y | do(X)) = \sum_c P(Y | X, C=c) \cdot P(C)$$

This is the **backdoor adjustment formula** — derived using do-calculus!

### Practical Use

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

**Key insight:** Pearl proved that do-calculus is **complete** — if a causal effect is identifiable from a graph, do-calculus can derive it. If do-calculus fails to identify it, it's truly non-identifiable.

---

## Identification Checklist

Before analyzing observational data, ask:

### 1. Draw the DAG
- [ ] What's the treatment?
- [ ] What's the outcome?
- [ ] What are potential confounders?
- [ ] What's the causal structure?

### 2. Check for Backdoor Paths
- [ ] Are there paths from X to Y with arrows into X?
- [ ] Can you measure variables that block all backdoor paths?
- [ ] Do any variables violate the backdoor criterion (descendants of X)?

### 3. Identify Valid Adjustment Set
- [ ] What's the minimal set that satisfies backdoor?
- [ ] Can you measure all variables in the set?
- [ ] Is ignorability plausible conditional on these variables?

### 4. If Backdoor Fails, Try Alternatives
- [ ] **Frontdoor**: Is there a measured mediator? Complete mediation?
- [ ] **IV**: Is there exogenous variation? Valid instrument?
- [ ] **Other**: RDD, DiD, or experimental design possible?

### 5. State Your Assumptions
- [ ] What are you assuming about the DAG?
- [ ] What are you assuming about unmeasured variables?
- [ ] How plausible are these assumptions?

### 6. Plan Sensitivity Analyses
- [ ] How robust are results to violations of assumptions?
- [ ] What alternative DAGs are plausible?
- [ ] Can you test predictions of your assumptions?

---

## Common Pitfalls

### 1. Assuming Identification Without Justification

**Error:** "I'll control for X, Y, Z and get a causal effect"

**Problem:** 
- How do you know that's sufficient?
- What if there are unmeasured confounders?
- What if you're controlling for mediators or colliders?

**Solution:** Draw the DAG, apply backdoor criterion formally

### 2. Controlling for Everything

**Error:** "I'll control for all available variables to be safe"

**Problem:**
- May control for mediators (blocks causal path)
- May control for colliders (creates bias)
- Over-controlling reduces efficiency

**Solution:** Only control for variables that satisfy backdoor criterion

### 3. Assuming IV Validity Without Evidence

**Error:** "I'll use Z as an instrument"

**Problem:**
- Exclusion restriction is untestable
- Relevance might be weak
- Independence might not hold

**Solution:** Provide strong domain-knowledge arguments for each IV assumption

### 4. Ignoring Non-Identification

**Error:** Proceeding with analysis even when effect isn't identified

**Problem:** 
- Estimates are biased no matter how much data you have
- Results are uninterpretable

**Solution:** If not identified, acknowledge it! Don't report causal estimates.

### 5. Confusing Identification with Estimation

**Error:** "I got a statistically significant result, so it's causal"

**Problem:**
- Statistical significance ≠ causal identification
- Precise estimate of biased quantity is still wrong

**Solution:** Establish identification before worrying about estimation

---

## Summary

### Key Takeaways

1. **Identification comes first**: Before estimating, ask if the causal effect is identified
2. **Multiple strategies exist**: Backdoor, frontdoor, IV, experiments
3. **All require assumptions**: Make them explicit and justify them
4. **DAGs are essential**: Visualize causal structure to reason about identification
5. **No free lunch**: Observational causal inference always requires untestable assumptions

### The Identification Hierarchy

1. **Best: Randomized experiment** 
   - Breaks all confounding by design
   - No assumptions needed (except SUTVA)

2. **Good: Backdoor with measured confounders**
   - Assumes ignorability
   - Can partially test (balance)

3. **Harder: Frontdoor or IV**
   - Stronger assumptions
   - Less testable
   - More complex estimation

4. **Last resort: Sensitivity analysis**
   - Acknowledge non-identification
   - Bound the bias
   - Report range of estimates

### Moving Forward

In the next notebooks, we'll:
- **02_backdoor_adjustment.ipynb**: Apply backdoor criterion to real examples
- **03_frontdoor_criterion.ipynb**: Work through frontdoor identification
- **04_instrumental_variables.ipynb**: Understand IV estimation and LATE

You'll learn to **implement** these identification strategies and **estimate** causal effects using real data.

---

## Further Reading

### Essential Papers

**Identification Theory:**
- Pearl, J. (1995). "Causal diagrams for empirical research." *Biometrika*.
- Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Chapters 3-4.

**Ignorability/Backdoor:**
- Rosenbaum, P. R., & Rubin, D. B. (1983). "The central role of the propensity score."
- Imbens, G. W. (2004). "Nonparametric estimation of average treatment effects under exogeneity."

**Instrumental Variables:**
- Angrist, J. D., Imbens, G. W., & Rubin, D. B. (1996). "Identification of causal effects using instrumental variables."
- Angrist, J. D., & Pischke, J.-S. (2009). *Mostly Harmless Econometrics*. Chapter 4.

**Frontdoor:**
- Pearl, J. (2009). "Causal inference in statistics: An overview." *Statistics Surveys*.

### Textbooks

- Hernán, M. A., & Robins, J. M. (2020). *Causal Inference: What If*. Chapters 1-7.
- Pearl, J., Glymour, M., & Jewell, N. P. (2016). *Causal Inference in Statistics: A Primer*. Chapters 3-4.
- Cunningham, S. (2021). *Causal Inference: The Mixtape*. Chapters 3-5.

### Software

- **DAGitty**: Online tool for drawing DAGs and checking identification (dagitty.net)
- **DoWhy** (Python): Implements identification algorithms
- **causaleffect** (R): Implements do-calculus

---

**Next:** [Backdoor Adjustment](02_backdoor_adjustment.ipynb) — Apply the backdoor criterion with code examples

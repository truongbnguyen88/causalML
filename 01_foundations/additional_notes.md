# Additional Notes: Common Pitfalls Explained

Supplementary explanations for [01_intro_causality.md](01_intro_causality.md)

---

## Pitfall 4: "Causation flows from correlation + time order"

### The Core Issue

**Misconception**: If X and Y are correlated, and X happens before Y, then X causes Y.

**Reality**: Temporal ordering is **necessary but not sufficient** for causation. This is one of the most common mistakes in interpreting data.

### Why Time Order Isn't Enough

The fundamental problem is that **confounders can exist before the treatment**, creating spurious correlations even when the time order is correct.

#### Example: Education and Income

Consider this timeline:
```
Time 1: Family wealth (Z)
Time 2: Years of education (X) 
Time 3: Income (Y)
```

**What we observe**:
- Education (X) clearly precedes income (Y) ✓
- Education and income are strongly correlated ✓
- More education → Higher income

**Why we can't conclude causation**:

Family wealth at Time 1 affects both education and income:
- **Wealthy families → More education**: Can afford college, no need to work early, better schools, parental expectations
- **Wealthy families → Higher income**: Inheritance, business connections, social networks, access to high-paying jobs

So even though education comes before income, some (or all) of the correlation might be due to family wealth creating a spurious association. If you intervened to increase education without changing family wealth, the effect might be smaller than the correlation suggests.

This is a **time-ordered confounder** - it satisfies temporal ordering but still creates confounding:
```
Family Wealth (Time 1)
    ↓           ↓
Education → Income
(Time 2)   (Time 3)
```

#### Other Time-Ordered Confounders

Multiple confounders can exist before the treatment decision:

**Innate ability** (exists from birth):
- Smart people tend to pursue more education
- Smart people tend to earn more, even without additional education
- Creates correlation between education and income that's not purely causal

**Motivation and personality** (develops in childhood):
- Motivated individuals pursue more education
- Motivated individuals work harder and earn more
- Again, creates non-causal correlation

**Geographic location** (determined by family):
- Living in areas with good schools → More education attained
- Living in areas with strong economies → Higher income opportunities
- Location affects both independently

The key insight: All these confounders **precede** the education decision and satisfy temporal ordering, yet they still confound the relationship.

#### Problem 2: Anticipation and Forward-Looking Behavior

Sometimes the temporal order can be misleading when people anticipate future events.

**Example: Stock prices and earnings**

Timeline:
```
Time 1: Stock price drops
Time 2: Company announces poor earnings
```

Observations:
- Stock price drop precedes the announcement ✓
- They're correlated ✓

But the stock price didn't **cause** poor earnings. Instead, investors anticipated the poor earnings (based on signals like declining sales, industry trends, etc.) and sold the stock before the announcement. The actual poor earnings were determined by business operations that occurred even earlier.

This shows how temporal ordering can be tricky when agents have information and can act on expectations.

### What Temporal Ordering Does and Doesn't Tell You

**What it DOES tell you**:
- Y cannot cause X if X happens first (eliminates reverse causation)
- The causal direction, if there is one, must be X → Y

**What it DOESN'T tell you**:
- Whether earlier variables confound the X-Y relationship
- How much of the observed correlation is actually causal
- Whether X has any causal effect at all on Y

### What You Actually Need

To establish causation from observational data, you need:

1. ✓ **Temporal ordering** (X before Y) - Necessary but not sufficient
2. ✓ **Correlation** (X and Y associated) - Shows relationship exists
3. ✗ **No confounding** - No common causes affecting both X and Y (This is the hard part!)
4. ✗ **No selection bias** - Treatment assignment not related to potential outcomes
5. ✗ **Correct causal model** - Proper assumptions about the data-generating process

Items 3-5 are what causal inference methods help you achieve through:
- **Randomization**: Breaks confounding by making treatment assignment independent of everything
- **Control for confounders**: Include all confounders in your analysis (requires measuring them all)
- **Instrumental variables**: Use exogenous variation unrelated to confounders
- **Natural experiments**: Find quasi-random variation in treatment assignment
- **Sensitivity analysis**: Test how robust conclusions are to potential unmeasured confounding

### Bottom Line

Temporal ordering + correlation is **suggestive evidence** but not **conclusive proof** of causation. The reason: confounders can precede both the treatment and outcome, creating spurious correlations despite correct time order. You need additional design features or assumptions to move from correlation to causation.

---

## Pitfall 5: "Causal inference is just for experiments"

### The Core Issue

**Misconception**: You can only establish causation with randomized controlled trials (RCTs). Without randomization, you're stuck with mere correlations and can't make causal claims.

**Reality**: While RCTs are the gold standard, many powerful methods exist for causal inference with observational data. Most causal knowledge in medicine, economics, and policy comes from observational studies.

### Why Randomization Is Powerful

First, let's understand why RCTs are so valuable:

**How randomization works**:
```
Population → Random Assignment → Treatment or Control → Measure Outcomes
```

**Why it's powerful**: Random assignment ensures that, on average, the treatment and control groups are identical in all characteristics - both measured and unmeasured. This includes:
- Demographics (age, gender, education)
- Health status, genetics, ability
- Motivation, preferences, personality
- Everything else, even factors we don't know about or can't measure

Because the groups are balanced on everything except treatment, any difference in outcomes can be attributed to the treatment (within sampling error). No confounding, no selection bias - just clean causal effects.

### Why We Can't Always Do Experiments

Despite the power of RCTs, many important causal questions cannot be answered experimentally:

#### 1. Ethical Constraints
We cannot randomly assign harmful exposures:
- Can't make people smoke for 30 years to study lung cancer
- Can't randomly deny children education
- Can't expose communities to pollution
- Can't randomly assign people to poverty

These questions are crucial for public health and policy, but experiments would be unethical.

#### 2. Feasibility Issues
Some experiments are simply impractical:
- **Too expensive**: Evaluating national-level policies
- **Too long**: Studying effects that take decades to materialize
- **Not scalable**: Can't randomize macroeconomic policies across countries
- **Political resistance**: Governments won't randomly assign welfare benefits

#### 3. External Validity Concerns
Even when RCTs are possible, they have limitations:
- **Selection**: People who volunteer for studies may differ from the general population
- **Artificial settings**: Controlled trial conditions may not reflect real-world behavior
- **Context dependency**: Effects may vary across different settings, cultures, or time periods

#### 4. Historical Questions
Many important questions involve events that already occurred:
- Did a historical policy change affect outcomes?
- What was the effect of a natural disaster?
- How did a technology adoption pattern emerge?

You can't randomize the past.

### Powerful Methods for Observational Causal Inference

The field has developed sophisticated methods to approximate experimental conditions using observational data:

#### 1. Natural Experiments

**Core idea**: Find situations where nature or policy creates quasi-random variation in treatment assignment.

**Example - Vietnam War Draft Lottery**:
In 1969-1972, the U.S. used a lottery based on birthdates to determine draft eligibility. Men born on certain dates were drafted; others weren't. The lottery number assignment was essentially random.

Researchers used this to study: Does military service affect lifetime earnings? By comparing men with draft-eligible vs. non-eligible lottery numbers, they could estimate causal effects. The lottery mimics randomization - being born on one date vs. another is random with respect to potential outcomes.

**Why it works**: The "treatment assignment" (lottery number) is unrelated to any characteristics that would affect outcomes. It's "as-if" randomized.

#### 2. Instrumental Variables (IV)

**Core idea**: Find a variable (the instrument) that:
- Affects treatment assignment (relevance)
- Doesn't directly affect the outcome except through treatment (exclusion restriction)
- Isn't correlated with confounders (exogeneity)

**Example - Compulsory Schooling Laws**:
Research question: Does education cause higher earnings, or is the correlation due to ability?

Problem: Ability confounds education → earnings (smart people get more education AND earn more regardless of education).

Instrument: Compulsory schooling laws. Some states/countries require students to stay in school longer. These laws:
- Affect years of education (some people get more schooling due to the law)
- Don't directly affect earnings except through the additional schooling
- Aren't related to individual ability (laws apply to everyone)

By using variation in education caused only by the laws (not by ability), researchers can estimate the causal effect of education on earnings.

#### 3. Regression Discontinuity Design (RDD)

**Core idea**: When treatment is assigned based on a cutoff in a continuous variable, units just above and below the threshold are very similar except for treatment status.

**Example - Financial Aid and College Attendance**:
Students with GPA ≥ 3.0 receive a scholarship; those with GPA < 3.0 don't.

Compare students with GPAs of 2.98, 2.99 vs. 3.01, 3.02. These students are nearly identical in ability and other characteristics - the GPA difference is tiny. But one group gets aid, the other doesn't. By comparing outcomes just around the cutoff, we approximate a randomized experiment in that local region.

**Why it works**: Units near the cutoff are so similar that assignment is "as-if" random locally.

#### 4. Difference-in-Differences (DiD)

**Core idea**: Compare the change over time in a treatment group to the change in a control group.

**Example - Minimum Wage Study (Card & Krueger, 1994)**:
Research question: Does raising minimum wage reduce employment?

Setting: New Jersey raised its minimum wage in 1992; neighboring Pennsylvania didn't.

Analysis: Compare employment changes in NJ fast-food restaurants (treatment) vs. PA restaurants (control):
- Employment in NJ: Before vs. After wage increase
- Employment in PA: Before vs. After (same time period)
- DiD estimate: (NJ After - NJ Before) - (PA After - PA Before)

**Key assumption**: Parallel trends - NJ and PA would have trended similarly in the absence of the policy change.

**Why it works**: Differences out time trends and fixed differences between the states.

#### 5. Matching and Propensity Scores

**Core idea**: Create comparable treatment and control groups by matching on observable characteristics.

**Example - Job Training Program**:
Can't randomize who receives training. Instead, for each trainee, find a non-trainee who is similar in:
- Age, education, work history
- Prior earnings
- Location, industry
- Other relevant characteristics

Then compare earnings of matched pairs. If matching is done well on all confounders, this approximates randomization.

**Limitation**: Only works if all confounders are measured and matched. Unmeasured confounding remains a threat.

#### 6. Synthetic Control Methods

**Core idea**: When you have one treated unit (like a state or country), create a "synthetic control" from a weighted combination of untreated units that closely matches the treated unit's pre-treatment trajectory.

**Example - German Reunification**:
Question: What was the economic effect of reunification on West Germany?

Problem: Only one West Germany - can't randomize countries!

Solution: Create "synthetic West Germany" as a weighted average of other countries (e.g., Austria, Netherlands, Switzerland) that matched West Germany's economic trends before reunification. After reunification, compare actual West Germany to this synthetic control.

### When Do Observational Methods Work?

These methods succeed when assumptions are credible:

1. **All confounders measured** (for matching): You have data on everything that affects both treatment and outcome
2. **Valid instruments exist** (for IV): The instrument truly doesn't affect outcomes except through treatment
3. **Parallel trends** (for DiD): Treatment and control would have evolved similarly without intervention
4. **Discontinuity is sharp** (for RDD): Treatment is truly determined by the cutoff
5. **Domain knowledge**: Biological mechanisms, institutional rules, or prior research support your assumptions

### Key Historical Examples

**1. Smoking and Lung Cancer (1950s-1960s)**
- No RCT (unethical to make people smoke)
- Evidence: Cohort studies controlling for confounders, dose-response relationship, temporal consistency, biological mechanism
- Result: Causal link firmly established through observational methods

**2. John Snow and Cholera (1854)**
- Predates modern statistics and RCTs
- Natural experiment: Different water suppliers in London neighborhoods
- Compared cholera rates by water source
- Result: Identified contaminated water as cause, leading to public health interventions

### Bottom Line

**RCTs are wonderful but not necessary for causal inference.**

Observational methods require **stronger assumptions** than randomization, but these assumptions are often justifiable with:
- Domain expertise and institutional knowledge
- Careful research design
- Sensitivity analyses testing robustness
- Triangulation (using multiple methods)

Quote from Joshua Angrist:
> "Randomization is not the only path to credible causal inference."

Most causal knowledge in medicine, economics, and policy comes from observational studies using these methods. The key is being transparent about assumptions, testing their plausibility, and assessing how sensitive conclusions are to violations.

---

## Further Reading

**On temporal ordering and confounding**:
- Pearl, J., Glymour, M., & Jewell, N. P. (2016). *Causal Inference in Statistics: A Primer*. Chapter 3

**On observational methods**: 
- Angrist, J. D., & Pischke, J. S. (2009). *Mostly Harmless Econometrics*. Chapters 3-6
- Cunningham, S. (2021). *Causal Inference: The Mixtape*

**Classic papers**:
- Rosenbaum, P. R., & Rubin, D. B. (1983). "The central role of the propensity score in observational studies for causal effects"
- Card, D., & Krueger, A. B. (1994). "Minimum wages and employment: A case study of the fast-food industry in New Jersey and Pennsylvania"

---

## Simpson's Paradox

### Definition

**Simpson's Paradox** occurs when a trend or association that appears in several subgroups **reverses or disappears** when the subgroups are combined. This happens due to a confounding variable that affects both the treatment and outcome differently across groups.

**In causal inference terms**: The naive (unadjusted) estimate and the adjusted estimate (controlling for a confounder) have **opposite signs** or substantially different magnitudes.

### Classic Example: UC Berkeley Admissions (1973)

**Setup**: UC Berkeley was sued for gender bias in graduate admissions.

**Overall data** (Combined):
- Men: 44% admitted
- Women: 35% admitted
- **Conclusion**: Appears biased against women!

**Department-level data** (Subgroups):

| Department | Men Applied | Men Admitted | Women Applied | Women Admitted |
|------------|-------------|--------------|---------------|----------------|
| A          | 825         | 62%          | 108           | 82%            |
| B          | 560         | 63%          | 25            | 68%            |
| C          | 325         | 37%          | 593           | 34%            |
| D          | 417         | 33%          | 375           | 35%            |
| E          | 191         | 28%          | 393           | 24%            |
| F          | 373         | 6%           | 341           | 7%             |

**Within each department**: Women have similar or **higher** admission rates than men!

**The Paradox**: 
- Overall: Men admitted more (bias appears to favor men)
- By department: Women admitted at similar/higher rates (no bias or favors women)

**Explanation** (The Confounder):
- **Department** is the confounder
- Women applied more to competitive departments (C, E, F) with low admission rates
- Men applied more to less competitive departments (A, B) with high admission rates
- The different application patterns created the spurious overall association

**The reversal**: Controlling for department reverses the apparent bias.

This is Simpson's Paradox: the aggregate data suggests one conclusion, but the disaggregated data shows the opposite.

---

## Why Controlling for Mediators Blocks the Causal Effect

### The Core Issue

When you control for a mediator, you're blocking the causal pathway you want to measure.

### Example: Drug → Blood Pressure → Heart Attack

If you control for blood pressure in a regression:
- You're asking: "What's the effect of the drug, **holding blood pressure constant**?"
- But the drug **works through** lowering blood pressure
- By forcing blood pressure to be the same in treated and control groups, you eliminate the mechanism by which the drug operates

**Result**: You'll find no effect (or a much smaller effect), not because the drug doesn't work, but because you blocked the pathway through which it works.

### General Principle

**Structure**: Treatment → Mediator → Outcome

- Controlling for the mediator removes the indirect effect
- You only capture the direct effect (if any exists)

### When to Control for Mediators

Only if you specifically want to measure the **direct effect** while shutting down the indirect pathway. For **total causal effect**, don't control for mediators.

### Contrast with Confounders

- **Confounder** (Z → Treatment, Z → Outcome): **Control** to remove bias
- **Mediator** (Treatment → M → Outcome): **Don't control** if you want total effect

---

## Why You Should Never Control for Colliders

### The Core Issue

A **collider** is a variable that is caused by two other variables. In the structure X → C ← Y, the variable C is a collider because both X and Y point into it.

**Key principle**: When X and Y are initially independent (no arrow between them), conditioning on their common effect C creates a spurious association between them.

### The Mechanism: Explaining Away

When you observe the collider C, you create an informational dependency between its causes:

- If you learn that X is high, this "explains" the observed value of C, making Y less likely to be high
- If you learn that Y is high, this "explains" C, making X less likely to be high

The causes compete to explain the observed effect - this is called **explaining away**.

### Example: NBA Players

**Setup:**
- **Talent** → NBA Player ← **Height**
- In the general population, talent and height are independent (correlation ≈ 0)
- Both increase your chances of making the NBA

**What happens when we condition on being an NBA player?**

Among NBA players, talent and height become **negatively correlated**:
- Very tall players may have made it with moderate talent
- Shorter players probably have exceptional talent to compensate

This creates spurious negative correlation where none existed in the population!

### Example: Exercise and Heart Disease (Backdoor Path)

**Setup:**
```
Exercise → Heart_Disease (true causal: exercise PREVENTS disease)
   ↓              ↓
   → Hospitalization ←
```

**The Question:** Does exercise reduce heart disease?

**The Collider:** Hospitalization is caused by both Exercise and Heart_Disease
- Exercise → Hospitalization (injuries, accidents)
- Heart_Disease → Hospitalization (cardiac events)

**Without controlling for Hospitalization:**

Study the general population:
- The path Exercise → Hospitalization ← Heart_Disease is **BLOCKED** (collider blocks it)
- Exercisers have lower heart disease rates ✓
- Non-exercisers have higher heart disease rates ✓
- You correctly see that exercise prevents heart disease

**When controlling for Hospitalization (studying only hospitalized patients):**

The path Exercise → **[Hospitalization]** ← Heart_Disease becomes **OPEN** (conditioning unblocks the collider).

This creates a **backdoor path** that introduces selection bias:

Among hospitalized patients:
- **Exercisers** are likely hospitalized for injuries/accidents (NOT heart disease)
  - Healthy heart, but hospitalized for other reasons
- **Non-exercisers** are likely hospitalized for heart disease
  - Unhealthy heart, that's why they're there

**Result:** Among hospitalized patients, exercisers appear to have LESS heart disease than the true causal effect suggests, or the relationship might even reverse!

**The backdoor path:** Exercise → Hospitalization ← Heart_Disease
- Blocked naturally (when not controlling) → no bias ✓
- Opens when controlling for Hospitalization → creates selection bias ✗

**Why it's called a "backdoor path":**
- The "front door" = Exercise → Heart_Disease (causal pathway)
- The "back door" = Exercise → Hospitalization ← Heart_Disease (non-causal, spurious)
- Controlling for the collider "opens the back door" allowing bias to flow through

### Statistical Mechanism

**Before conditioning**: P(X, Y) = P(X) × P(Y) — they're independent

**After conditioning on C**: P(X, Y | C) ≠ P(X | C) × P(Y | C) — they're now dependent

The conditioning breaks the independence by creating selection on a variable that both X and Y influence.

### What Does "Controlling" Mean?

"Controlling for a variable" means making statistical adjustments to compare units that have the same value of that variable. Common methods include:

**1. Regression Adjustment** (Most Common)
- Include the variable as a covariate in your model
- Example: `Y ~ X + C` instead of `Y ~ X`
- You're asking: "What's the effect of X, **holding C constant**?"

**2. Stratification**
- Divide data into groups based on the variable
- Analyze within each group, then combine results
- Example: Analyze separately for C=low, C=medium, C=high

**3. Matching**
- For each treated unit, find controls with the same value of the variable
- Compare only matched pairs
- Example: Match treated and control units on C

**4. Conditioning/Filtering**
- Restrict analysis to a specific value of the variable
- Example: Only analyze data where C = 5

**The key**: All these methods compare units with the same (or similar) value of the controlled variable.

### Why This Creates Selection Bias

If you're trying to estimate the causal effect of X on Y and you control for collider C:

**Correct approach:**
- Don't control for C
- X and Y remain independent (no confounding, no bias)

**Wrong approach:**
- Control for C (include as covariate in regression, stratify by C, match on C, etc.)
- Creates spurious association between X and Y
- Your causal estimate is now biased by the induced correlation

**Why controlling for a collider creates bias:**
- Without controlling: You compare all X values to all Y values (independent)
- When controlling: You compare X and Y **within each level of C**
- Since C is caused by both X and Y, conditioning on C creates an informational dependency
- If C is high and X is low, then Y must be high to "explain" C
- This induced dependency creates spurious correlation between X and Y

### Contrast with Confounders

This is opposite to confounders:

- **Confounder** (X ← Z → Y): You **must** control for it to block bias
- **Collider** (X → C ← Y): You **must not** control for it to avoid creating bias

### The DAG Rule

**Never control for:**
1. Colliders themselves (X → C ← Y)
2. Descendants of colliders (anything caused by C)

Doing so opens a "backdoor path" through the collider, creating bias where none existed before.

---

*Return to [01_intro_causality.md](01_intro_causality.md)*

# Introduction to Causal Inference

## Learning Objectives

By the end of this reading, you will be able to:
- Distinguish between correlation and causation with concrete examples
- Understand why causal questions are fundamentally different from predictive questions
- Recognize the importance of causal reasoning in data science
- Identify situations where causal inference is necessary
- Appreciate the challenges in establishing causality from observational data

---

## Why Causal Inference Matters

As a data scientist, you've likely built many predictive models. You can predict customer churn, forecast sales, or classify images with high accuracy. But consider these questions:

- **Will** offering a discount **cause** customers to buy more?
- **Does** a new drug **cause** patients to recover faster?
- **Would** hiring more engineers **cause** the company to ship products faster?

These questions are fundamentally different from prediction. They ask about **intervention** and **causation**, not just association. Answering them requires causal inference.

### The Difference: Prediction vs Causation

**Predictive Question**: "Given that a customer received a discount, how likely are they to purchase?"
- Uses: P(Purchase | Discount)
- Goal: Forecast what will happen
- Method: Standard machine learning

**Causal Question**: "If we give a customer a discount, will it cause them to purchase?"
- Uses: P(Purchase | do(Discount))
- Goal: Understand what would happen under intervention
- Method: Causal inference

The key difference is the **do()** operator, introduced by Judea Pearl. It represents an intervention—actively setting a variable to a value—rather than just observing it.

---

## Correlation Does Not Imply Causation

You've heard this phrase countless times. But why exactly is it true? Let's explore with concrete examples.

### Example 1: Ice Cream and Drowning

**Observation**: Ice cream sales and drowning deaths are strongly correlated.

**Does ice cream cause drowning?** No. Both are caused by a third variable: **temperature**.
- Hot weather → People buy more ice cream
- Hot weather → People swim more → More drowning incidents

This is a classic case of **confounding**. Temperature is a **confounder**—it affects both ice cream sales and drowning rates, creating a spurious correlation.

```
Temperature
    ↓      ↓
Ice Cream  Drowning
```

If you intervened to ban ice cream sales, drowning deaths wouldn't decrease. The correlation exists, but there's no causal relationship.

### Example 2: Coffee and Lung Cancer

**Observation**: Coffee drinkers have higher rates of lung cancer.

**Does coffee cause lung cancer?** No. The real culprit is **smoking**.
- In the past, smokers were more likely to drink coffee (social/behavioral association)
- Smoking causes lung cancer
- Coffee consumption is merely associated with smoking

```
Smoking
   ↓     ↓
Coffee  Lung Cancer
```

This is another confounder scenario. Once you control for smoking status, the coffee-cancer association disappears.

### Example 3: Education and Income

**Observation**: People with more education earn higher incomes.

**Does education cause higher income?** Maybe, but it's complicated.

Possible explanations:
1. **Direct causation**: Education → Skills → Higher income
2. **Confounding**: Ability, family background, socioeconomic status affect both education and income
3. **Reverse causation**: Wealthier families can afford more education
4. **Selection bias**: People who choose to pursue education differ from those who don't

```
Family Background
       ↓          ↓
   Education → Income
       ↑
   Ability (unmeasured)
```

This example shows that real-world causal questions are often complex, with multiple pathways and confounders.

---

## When Correlation Does Suggest Causation

While correlation doesn't **prove** causation, it's often the starting point. Under certain conditions, we can infer causation from correlation:

### 1. Randomized Controlled Trials (RCTs)

**Gold Standard**: Randomly assign treatment, measure outcomes.

Example: Drug trial
- Randomly assign patients to drug vs placebo
- Randomization ensures treatment and control groups are similar on average
- Any difference in outcomes can be attributed to the drug

**Why it works**: Randomization breaks the link between confounders and treatment assignment.

### 2. Natural Experiments

**Idea**: Nature or policy creates quasi-random assignment.

Example: Lottery for military draft (Vietnam War)
- Draft lottery numbers randomly assigned by birthdate
- Compare outcomes of those drafted vs not drafted
- Approximates random assignment

### 3. Strong Background Knowledge

**Domain expertise** can help establish causation:
- Biological mechanisms (smoking damages lung tissue)
- Temporal ordering (treatment precedes outcome)
- Dose-response relationship (more smoking → higher cancer risk)
- Consistency across studies

However, these alone aren't sufficient without proper causal analysis.

---

## The Fundamental Challenge: The Counterfactual Problem

Here's the core challenge of causal inference:

**To know if treatment X causes outcome Y for person i, we need to compare:**
- Y<sub>i</sub>(1) = outcome for person i **with** treatment
- Y<sub>i</sub>(0) = outcome for person i **without** treatment

**The problem**: We can only observe **one** of these for any given person.

### A Concrete Example

Suppose we want to know if a job training program causes higher earnings.

**Person Alice**:
- We observe: Alice took the program → Earns $50,000
- We don't observe: What Alice would earn without the program

**Person Bob**:
- We observe: Bob didn't take the program → Earns $40,000
- We don't observe: What Bob would earn with the program

Can we compare Alice ($50k, with program) to Bob ($40k, without program) and conclude the program causes a $10k increase?

**No!** Alice and Bob likely differ in many ways:
- Motivation (Alice chose to enroll)
- Prior skills
- Job opportunities
- Personal circumstances

This is called **selection bias**. People who select into treatment differ from those who don't.

### The Fundamental Problem of Causal Inference

**We can never observe both potential outcomes for the same individual at the same time.**

This is why causal inference is challenging. We need methods to estimate what **would have happened** under different treatments—the counterfactual outcomes we can't observe.

---

## Types of Causal Questions

Different questions require different approaches:

### 1. Average Treatment Effect (ATE)

**Question**: What is the average effect of treatment across the population?

**Example**: On average, how much does the job training program increase earnings?

**Notation**: E[Y(1) - Y(0)]

### 2. Treatment Effect on the Treated (ATT)

**Question**: What is the effect for those who actually received treatment?

**Example**: For people who enrolled in the program, how much did it increase their earnings?

**Notation**: E[Y(1) - Y(0) | T = 1]

### 3. Conditional Average Treatment Effect (CATE)

**Question**: How does the treatment effect vary by characteristics?

**Example**: Does the program work better for younger vs older workers?

**Notation**: E[Y(1) - Y(0) | X = x]

### 4. Individual Treatment Effect (ITE)

**Question**: What is the effect for a specific individual?

**Example**: How much would the program increase Alice's earnings?

**Notation**: Y<sub>i</sub>(1) - Y<sub>i</sub>(0)

**Note**: ITE is generally not identifiable (we can't observe both outcomes), but CATE and ATE often are.

---

## Approaches to Causal Inference

There are several frameworks for causal reasoning:

### 1. Potential Outcomes Framework (Rubin Causal Model)

**Key idea**: Each unit has potential outcomes for each treatment level.
- Focus: Counterfactual reasoning
- Developed by: Donald Rubin
- Strength: Clear definition of causal effects
- Used in: Experimental design, matching methods, propensity scores

*We'll explore this in detail in the next section.*

### 2. Graphical Models (Pearl's Approach)

**Key idea**: Use directed graphs (DAGs) to represent causal relationships.
- Focus: Causal structure and identification
- Developed by: Judea Pearl
- Strength: Visual reasoning about confounding and paths
- Used in: Identifying adjustment sets, understanding bias

*We'll cover DAGs in depth in upcoming notebooks.*

### 3. Structural Equation Models

**Key idea**: Express outcomes as functions of causes plus noise.
- Focus: Functional relationships
- Strength: Can model mechanisms and mediation
- Used in: Economics, social sciences

These frameworks are complementary and often used together in modern causal inference.

---

## Key Concepts Summary

### Correlation vs Causation
- **Correlation**: X and Y tend to occur together
- **Causation**: Changing X causes a change in Y
- Correlation can arise from causation, confounding, reverse causation, or chance

### Confounding
A variable that affects both treatment and outcome, creating spurious association.

### Selection Bias
Treatment and control groups differ systematically in ways that affect the outcome.

### Counterfactual
The outcome that would have occurred under a different treatment.

### Identification
Determining whether a causal effect can be estimated from data given assumptions.

### Randomization
The gold standard for causal inference—random assignment breaks confounding.

---

## Common Pitfalls and Misconceptions

### Pitfall 1: "Controlling for everything"
**Misconception**: If I include all variables in my regression, I'll get the causal effect.

**Reality**: 
- You can't control for unmeasured confounders
- Controlling for the wrong variables (colliders, mediators) can introduce bias
- More variables ≠ better causal estimates

### Pitfall 2: "It's statistically significant, so it's causal"
**Misconception**: A p-value < 0.05 proves causation.

**Reality**:
- Statistical significance measures whether an association is likely due to chance
- It says nothing about whether the association is causal
- Confounding can produce highly significant but non-causal associations

### Pitfall 3: "Prediction models can answer causal questions"
**Misconception**: If my model predicts well, it captures causal relationships.

**Reality**:
- Prediction uses P(Y|X)—what happens when we observe X
- Causation needs P(Y|do(X))—what happens when we intervene on X
- These can be very different (e.g., the ice cream example)

### Pitfall 4: "Causation flows from correlation + time order"
**Misconception**: If X precedes Y, and they're correlated, X causes Y.

**Reality**:
- Temporal ordering is necessary but not sufficient
- Confounders can precede both X and Y
- Example: Family wealth → Education → Income (time-ordered but confounded)

### Pitfall 5: "Causal inference is just for experiments"
**Misconception**: Without an RCT, you can't do causal inference.

**Reality**:
- Many causal methods work with observational data
- Natural experiments, instrumental variables, regression discontinuity
- We need strong assumptions, but they're often justifiable

---

## Real-World Applications of Causal Inference

### Medicine and Public Health
- Does a drug reduce symptoms? (Clinical trials)
- Do mask mandates reduce COVID-19 transmission? (Policy evaluation)
- Does air pollution cause asthma? (Environmental epidemiology)

### Economics and Policy
- Does raising minimum wage reduce employment? (Difference-in-differences)
- Do job training programs increase earnings? (Matching, IV)
- Does education improve economic mobility? (Instrumental variables)

### Technology and Business
- Does a new feature increase user engagement? (A/B testing)
- Will a discount cause customers to purchase? (Uplift modeling)
- Does showing an ad increase sales? (Observational causal inference)

### Social Sciences
- Does violent media cause aggressive behavior? (Natural experiments)
- Do social programs reduce crime? (Regression discontinuity)
- Does discrimination affect wages? (Mediation analysis)

---

## The Path Forward

Causal inference is both an art and a science. It requires:

1. **Clear causal questions**: What exactly are you trying to learn?
2. **Domain knowledge**: What are plausible confounders and mechanisms?
3. **Appropriate methods**: What design or technique fits your setting?
4. **Careful assumptions**: What must be true for your analysis to be valid?
5. **Transparent reporting**: What are the limitations of your conclusions?

In the following sections of this module, you'll learn:
- **Potential outcomes framework**: How to precisely define causal effects
- **Directed Acyclic Graphs (DAGs)**: How to visualize and reason about causal structures
- **Confounding and bias**: How to identify and address threats to causal inference

These foundations will prepare you for the estimation methods in later modules.

---

## Key Takeaways

1. **Causal questions differ fundamentally from predictive questions**
   - Prediction: What is? Causation: What if?
   
2. **Correlation ≠ Causation due to confounding, selection bias, and reverse causation**
   - Always ask: What else could explain this association?

3. **The fundamental challenge is the counterfactual problem**
   - We can't observe what would have happened under a different treatment

4. **Multiple frameworks exist for causal reasoning**
   - Potential outcomes, DAGs, and structural equations are complementary

5. **Causal inference is possible with observational data**
   - But requires careful design, assumptions, and sensitivity analysis

6. **Avoid common pitfalls**
   - Statistical significance ≠ causation
   - Controlling for everything can make things worse
   - Prediction models don't answer causal questions

---

## Further Reading

### Accessible Introductions
- Pearl, J., & Mackenzie, D. (2018). *The Book of Why*. Chapter 1: "The Ladder of Causation"
  - Accessible introduction to causal thinking and the three levels of causation

- Cunningham, S. (2021). *Causal Inference: The Mixtape*. Chapter 1-2
  - Applied introduction with code examples and clear intuition

### Technical References
- Hernán, M. A., & Robins, J. M. (2020). *Causal Inference: What If*. Chapter 1
  - Rigorous but readable introduction to potential outcomes

- Imbens, G. W., & Rubin, D. B. (2015). *Causal Inference for Statistics, Social, and Biomedical Sciences*. Chapter 1
  - The definitive potential outcomes reference

### Classic Papers
- Holland, P. W. (1986). "Statistics and Causal Inference." *Journal of the American Statistical Association*, 81(396), 945-960.
  - Foundational paper on the challenges of causal inference

---

## Reflection Questions

Before moving to the next section, consider:

1. Think of a correlation you've seen in your work. What are three alternative explanations besides causation?

2. For a causal question in your domain, what would the counterfactual outcomes be? Why can't you observe them?

3. What are potential confounders in your domain? How might they create spurious associations?

4. When would you need average treatment effects vs individual treatment effects in your work?

---

**Next**: [Potential Outcomes Framework](02_potential_outcomes.ipynb) - Learn to precisely define and reason about causal effects using the potential outcomes framework.

---

*This material is part of the Causal Inference & Causal ML learning repository.*
*For questions or feedback, see the main repository README.*

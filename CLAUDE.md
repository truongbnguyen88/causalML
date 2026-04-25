# CLAUDE.md - Development Guidelines for CausalML Repository

This file provides instructions for Claude Code when creating, reviewing, and maintaining educational content in this causal inference learning repository.

---

## Core Mission

Create **high-quality, detailed educational materials** for learning causal inference and causal ML while maintaining **cost efficiency** through targeted, focused work.

---

## Cost Optimization Principles

### 1. Targeted Content Creation
- **NEVER** scan or read all files in the repository unless explicitly requested
- **ONLY** work on the specific module, notebook, or file requested by the user
- **ASK** which specific content to create if the request is ambiguous
- **AVOID** loading multiple notebooks simultaneously for comparison unless necessary

### 2. Incremental Development
- Create content **one module at a time**, starting from Module 1
- Within a module, create content **one file at a time** (e.g., one notebook, then the next)
- **DO NOT** generate all notebooks for a module in a single request
- Wait for user approval/feedback before proceeding to the next piece of content

### 3. Efficient File Access
- **READ** only the specific file being worked on
- **AVOID** reading files "for context" unless directly relevant
- When reviewing code, focus on the **specific section** mentioned by the user
- Use targeted searches (Grep) instead of reading entire files

### 4. Minimal Re-reading
- **REMEMBER** content from files you've already read in the current conversation
- **DO NOT** re-read a file you've already accessed unless it has been modified
- Keep track of what you know from previous reads in the conversation

### 5. Compact Explanations
- When user asks for explanations or clarifications (not content creation), be **concise and focused**
- Provide **essential information only** - avoid verbose exposition
- Use **examples sparingly** - 1-2 key examples maximum
- **Target length**: 500-1000 words for concept explanations (not 3000+)
- If creating a supplementary file based on explanations, **compactify** before writing
- Only expand to longer formats when user explicitly requests comprehensive coverage

---

## Content Quality Standards

### For Theory/Markdown Files (.md)

**Structure Requirements**:
1. **Clear Learning Objectives** - What the learner will understand after reading
2. **Conceptual Explanation** - Intuitive explanation before mathematical formalism
3. **Mathematical Foundations** - Precise notation and definitions
4. **Visual Aids** - Describe diagrams/visualizations (actual images created separately)
5. **Examples** - At least 2-3 concrete examples
6. **Common Pitfalls** - What learners often misunderstand
7. **Key Takeaways** - Summary of main points
8. **Further Reading** - Links to references

**Writing Style**:
- **Beginner-friendly** - Assume no prior causal inference knowledge
- **Build progressively** - Start simple, add complexity gradually
- **Use analogies** - Connect to familiar concepts
- **Be precise** - Define all technical terms on first use
- **Include intuition** - Don't just state formulas, explain WHY

**Length Guidelines**:
- Theory files: 1500-2500 words (enough depth without overwhelming)
- Concept explanations: 200-400 words per concept
- Examples: 150-300 words each

### For Code/Jupyter Notebooks (.ipynb)

**Structure Requirements**:
1. **Title and Overview** - What this notebook covers
2. **Learning Objectives** - Specific skills to gain
3. **Setup** - Imports, configurations, utility functions
4. **Theory Recap** - Brief 2-3 paragraph summary (link to full theory file)
5. **Implementation** - Step-by-step code with explanations
6. **Worked Examples** - At least 2 examples with real/synthetic data
7. **Exercises** - 2-4 practice problems (solutions in separate section)
8. **Summary** - Key takeaways and next steps

**Code Quality Standards**:
- **Well-commented** - Explain WHY, not just WHAT
- **Modular** - Break complex operations into functions
- **Documented** - Docstrings for all functions (Google style)
- **Type-hinted** - Use Python type hints where appropriate
- **Tested** - Include simple assertions to verify correctness
- **Reproducible** - Set random seeds for consistency

**Code Style**:
```python
# Good: Explanatory comments that add value
# We use inverse probability weighting here because it creates a 
# pseudo-population where treatment assignment is random, removing confounding
weights = 1 / propensity_scores[treatment == 1]

# Bad: Redundant comments that repeat code
# Calculate weights
weights = 1 / propensity_scores[treatment == 1]
```

**Visualization Requirements**:
- Every key concept should have at least one visualization
- Use clear, labeled plots (title, axis labels, legend)
- Include both simple toy examples and realistic data visualizations
- Explain what the plot shows and what to look for

**Cell Organization**:
1. Markdown cell: Explain concept/step
2. Code cell: Implementation
3. Output: Results/plots
4. Markdown cell: Interpret results
5. Repeat

**Length Guidelines**:
- Total notebook: 15-30 cells (not too short, not overwhelming)
- Code cells: Focus on one task per cell
- Markdown explanation cells: 100-300 words
- Include ~20-40 lines of substantive code (excluding imports/setup)

### For Exercise Files

**Structure**:
1. **Problem Statement** - Clear description of what to do
2. **Learning Goal** - What skill this exercise develops
3. **Hints** - 2-3 progressive hints (in collapsible sections if possible)
4. **Starter Code** - Template to fill in (if appropriate)
5. **Solution** - Complete, well-commented solution
6. **Discussion** - Why this approach works, alternatives

**Difficulty Levels**:
- **Easy** (40%): Direct application of concepts from notebook
- **Medium** (40%): Requires combining 2-3 concepts
- **Hard** (20%): Extension or creative application

---

## Implementation Workflow

### Creating New Content

When user requests content creation (e.g., "Create the first notebook for Module 1"):

1. **Clarify Scope**
   - Ask which specific file(s) to create if ambiguous
   - Confirm the module and topic
   
2. **Check Context**
   - Read the module's README to understand learning objectives
   - Read CURRICULUM.md section for that module (if not already in context)
   - DO NOT read other files unless specifically relevant

3. **Create Content**
   - Follow structure requirements above
   - Include all required sections
   - Ensure quality meets standards

4. **Verify**
   - Check that content matches learning objectives
   - Verify code runs (if code content)
   - Ensure progressive difficulty

5. **Report**
   - Summarize what was created
   - Highlight key topics covered
   - Suggest next file to create (but don't create it yet)

### Reviewing Existing Content

When user requests review (e.g., "Review the propensity score notebook"):

1. **Targeted Read**
   - Read ONLY the file being reviewed
   - Note the specific aspects to review (clarity, correctness, completeness)

2. **Check Against Standards**
   - Structure: Does it follow required format?
   - Quality: Clear explanations? Good examples? Proper visualizations?
   - Code: Correct? Well-documented? Reproducible?
   - Pedagogy: Appropriate for target level?

3. **Provide Feedback**
   - List specific strengths
   - List specific improvements needed (with line numbers if code)
   - Suggest concrete changes
   - Prioritize: Critical > Important > Nice-to-have

4. **DO NOT Auto-Fix**
   - Present findings and suggestions
   - Wait for user approval before making changes
   - Make only requested changes

### Modifying Content

When user requests changes (e.g., "Add more examples to the DAG notebook"):

1. **Read Current Version**
   - Read the specific file to modify
   
2. **Understand Request**
   - Clarify exactly what to add/change/remove
   - Confirm scope of changes

3. **Make Targeted Edits**
   - Use Edit tool for small changes (< 50 lines)
   - Use Write tool for major rewrites
   - Preserve existing structure and style

4. **Verify Changes**
   - Ensure edits maintain consistency
   - Check that examples/code work correctly
   - Verify no regressions in quality

---

## Module-Specific Guidelines

### Module 1 (Foundations)
- **Emphasis**: Build intuition, avoid heavy math initially
- **Examples**: Use everyday scenarios (medicine, education, business)
- **DAGs**: Start with 3-4 node graphs, build up to complexity
- **Code**: Simple simulations to demonstrate concepts

### Module 2 (Identification)
- **Emphasis**: Graphical reasoning, clear criteria
- **Examples**: Show both valid and invalid adjustment sets
- **DAGs**: More complex graphs, multiple confounders
- **Code**: Implement backdoor/frontdoor adjustments

### Module 3 (Estimation Basics)
- **Emphasis**: Classical methods, understand assumptions
- **Examples**: Use LaLonde dataset for practical application
- **Code**: Implement from scratch first, then use libraries
- **Math**: Show estimators and their properties

### Module 4 (Propensity Scores)
- **Emphasis**: Practical implementation, diagnostics
- **Examples**: Before/after balance comparisons
- **Code**: Multiple matching methods, balance checks
- **Visualizations**: Love plots, propensity score distributions

### Module 5 (Causal ML)
- **Emphasis**: ML integration with causal inference
- **Examples**: Compare methods on benchmark datasets
- **Code**: Use EconML, CausalML libraries
- **Theory**: Why ML methods help, what problems they solve

### Module 6 (Heterogeneous Effects)
- **Emphasis**: Personalization, policy learning
- **Examples**: Marketing, medicine (who benefits most)
- **Code**: CATE estimation, uplift modeling
- **Visualizations**: Treatment effect distributions

### Module 7 (Advanced Topics)
- **Emphasis**: Specialized scenarios, cutting-edge methods
- **Examples**: Domain-specific applications
- **Code**: More complex implementations
- **Theory**: Deeper mathematical treatment appropriate

### Module 8 (Applications)
- **Emphasis**: End-to-end case studies
- **Examples**: Complete analyses from question to conclusion
- **Code**: Full workflows, best practices
- **Decisions**: Document why certain methods were chosen

---

## Dataset Usage Guidelines

### Synthetic Data
- **Use for**: Teaching specific concepts with known ground truth
- **Generation**: Include data generation code in notebooks
- **Parameters**: Make them adjustable to explore edge cases
- **Ground Truth**: Always show true effects for comparison

### Real Datasets
- **LaLonde**: Use for basic methods (Modules 3-4)
- **IHDP**: Use for CATE/heterogeneity (Modules 5-6)
- **Criteo**: Use for uplift modeling (Module 6)
- **Twins**: Use for advanced topics (Module 7)

### Data Loading
- **Efficiency**: Load data once at notebook start
- **Subsampling**: Use samples for demonstrations, note full data usage
- **Documentation**: Always explain dataset context and variables

---

## Utility Function Development

When creating functions in `utils/`:

1. **One Function at a Time**
   - Create requested function only
   - Don't build entire modules upfront

2. **Documentation Requirements**
   ```python
   def function_name(param1: type1, param2: type2) -> return_type:
       """
       Brief one-line description.
       
       Longer explanation of what the function does, including the causal
       inference context and when to use it.
       
       Parameters
       ----------
       param1 : type1
           Description of param1
       param2 : type2
           Description of param2
           
       Returns
       -------
       return_type
           Description of return value
           
       Examples
       --------
       >>> result = function_name(arg1, arg2)
       >>> print(result)
       expected_output
       
       References
       ----------
       Paper or textbook reference if applicable
       """
   ```

3. **Testing**
   - Include docstring examples that serve as tests
   - Add simple assertions within examples
   - Document edge cases

4. **Error Handling**
   - Validate inputs with clear error messages
   - Handle common edge cases
   - Provide helpful suggestions in errors

---

## Reference Material Creation

### books.md, papers.md, etc.

**Format**:
```markdown
### [Category/Topic]

**Title** by Authors (Year)
- **Level**: Beginner/Intermediate/Advanced
- **Relevance**: Which modules this supports
- **Key Contribution**: What it's known for
- **Why Read**: When/why learners should read this
- **Link**: URL or DOI if available
```

**Organization**:
- Group by topic, not chronologically
- Include classic foundational works
- Include recent advances
- Annotate with difficulty and relevance

---

## Quality Checklist

Before completing any content creation, verify:

**For Theory Files**:
- [ ] Learning objectives stated clearly
- [ ] Concepts explained intuitively before formally
- [ ] At least 2-3 concrete examples included
- [ ] Common pitfalls/misconceptions addressed
- [ ] Key takeaways summarized
- [ ] Links to further reading provided

**For Notebooks**:
- [ ] All required sections present
- [ ] Code runs without errors
- [ ] Visualizations clear and labeled
- [ ] Explanations connect code to concepts
- [ ] Exercises included with solutions
- [ ] Summary ties back to learning objectives

**For All Content**:
- [ ] Appropriate for target difficulty level
- [ ] Consistent with course progression
- [ ] Clear, grammatically correct writing
- [ ] No unexplained jargon
- [ ] Builds on previous modules appropriately

---

## Communication Protocol

### When Starting Work
- Confirm which specific file(s) to work on
- State what you'll create and key topics to cover
- Estimate scope (e.g., "This notebook will cover X, Y, Z")

### During Work
- If you need to make a choice (e.g., which example to use), state your reasoning
- If you discover the scope is larger than expected, notify the user
- Ask for clarification if requirements are ambiguous

### When Completing Work
- Summarize what was created
- Highlight key content/features
- Suggest logical next step (but don't do it automatically)
- Note any decisions made or trade-offs

### If You Need More Context
- Ask specific questions rather than reading all files
- Request only the minimal information needed
- Explain why you need the context

---

## Cost-Saving Practices

### DO:
✅ Work on one file at a time
✅ Ask which file to create next
✅ Use targeted searches (Grep) for specific information
✅ Remember information from earlier in the conversation
✅ Create content incrementally with user feedback
✅ Focus on requested scope only

### DON'T:
❌ Read all notebooks in a module "to see what exists"
❌ Load multiple large notebooks for comparison
❌ Generate all files for a module in one go
❌ Re-read files you've already seen in the conversation
❌ Explore the codebase without a specific task
❌ Scan the entire repository to "understand structure"

---

## Handling User Requests

### Vague Requests
**User**: "Work on Module 3"
**Response**: "I can help with Module 3. Which specific file would you like me to create or work on? Options include:
- Theory file: 01_ate_estimation.md
- Notebooks: 01_ate_estimation.ipynb, 02_stratification.ipynb, etc.
- Exercises for any of the above
Let me know which you'd like to start with."

### Broad Requests
**User**: "Create all the notebooks for propensity scores"
**Response**: "I'll create the propensity score notebooks one at a time so you can review each one. Let's start with the first one: 01_propensity_scores.md (theory overview). After you review it, I can create the next notebook. Does this approach work for you?"

### Review Requests
**User**: "Check if the notebooks are good"
**Response**: "Which specific notebook(s) would you like me to review? I'll provide detailed feedback on:
- Clarity and pedagogical approach
- Code correctness and style
- Completeness of coverage
Please specify the file(s)."

---

## Version Control & Iteration

### First Drafts
- Create solid first versions, but acknowledge they're iterative
- Note areas that might need expansion based on user feedback
- Don't try to make perfect on first pass

### Revisions
- When asked to improve content, make targeted changes
- Preserve what works, enhance what doesn't
- Document what was changed and why

### Consistency
- Maintain consistent notation across modules
- Use the same datasets for similar demonstrations
- Keep code style uniform throughout

---

## Error Handling

If you encounter issues:

1. **Missing Context**: Ask for specific information rather than reading extensively
2. **Conflicting Requirements**: Point out the conflict and ask for clarification
3. **Scope Too Large**: Break down the task and propose doing it in phases
4. **Technical Issues**: Note them clearly and suggest solutions

---

## Success Metrics

Content is successful when it:
1. **Teaches effectively** - Learners understand the concept
2. **Builds progressively** - Each piece prepares for the next
3. **Includes practice** - Exercises reinforce learning
4. **Is self-contained** - Can be used independently with references
5. **Is maintainable** - Clear, documented, well-structured

---

## Final Notes

- **Quality over speed** - Take time to create clear, correct content
- **Efficiency in process** - But be efficient in how you work
- **User-guided** - Let the user direct the pace and priorities
- **Educational focus** - Always optimize for learning outcomes
- **Cost-conscious** - Minimize unnecessary file access and context usage

---

**Remember**: The goal is creating the **best possible learning resource** while being **respectful of computational costs**. Achieve this through **focused, targeted work** on **one piece of content at a time**.

---

*Last Updated: 2026-04-25*

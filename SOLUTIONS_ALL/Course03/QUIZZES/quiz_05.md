# Module 05 Quiz: Probabilities and Statistical Inference

**Instructions**: Answer the following questions. Check your answers with the solutions provided.

## Part 1: Conceptual Questions

### Question 1
**Why are probabilities important in machine learning?**
- [ ] A) They make code faster
- [ ] B) They quantify uncertainty in predictions
- [ ] C) They're required by Python
- [ ] D) They're optional

**Answer**: B

**Explanation**: Probabilities help us understand and quantify uncertainty in model predictions.

---

### Question 2
**What is a confidence interval?**
- [ ] A) A single number
- [ ] B) A range of values with a certain confidence level
- [ ] C) A matrix
- [ ] D) A function

**Answer**: B

**Explanation**: A confidence interval is a range of values that likely contains the true value.

---

### Question 3
**What does a p-value tell us?**
- [ ] A) The probability the result is correct
- [ ] B) The probability of observing the result if null hypothesis is true
- [ ] C) The probability of error
- [ ] D) Random number

**Answer**: B

**Explanation**: P-value is the probability of observing the result (or more extreme) if the null hypothesis is true.

---

### Question 4
**What is hypothesis testing used for in ML?**
- [ ] A) Testing code
- [ ] B) Comparing models and determining if differences are significant
- [ ] C) Testing data
- [ ] D) Random testing

**Answer**: B

**Explanation**: Hypothesis testing helps determine if model improvements are statistically significant.

---

### Question 5
**What does a 95% confidence interval mean?**
- [ ] A) 95% chance the value is in the interval
- [ ] B) If we repeated the experiment many times, 95% of intervals would contain true value
- [ ] C) 95% of data is in interval
- [ ] D) Random concept

**Answer**: B

**Explanation**: 95% confidence means that in repeated experiments, 95% of intervals would contain the true value.

---

## Part 2: Code Understanding

### Question 6
**What does this statistical test do?**
```python
t_stat, p_value = stats.ttest_ind(model_a_scores, model_b_scores)
```

- [ ] A) Tests if two models perform significantly differently
- [ ] B) Tests if models are the same
- [ ] C) Tests if data is correct
- [ ] D) Random test

**Answer**: A

**Explanation**: Two-sample t-test compares means of two groups to see if difference is significant.

---

### Question 7
**If p-value < 0.05, what does this mean?**
- [ ] A) No significant difference
- [ ] B) Significant difference (reject null hypothesis)
- [ ] C) Models are identical
- [ ] D) Can't tell

**Answer**: B

**Explanation**: p < 0.05 means the difference is statistically significant at 5% level.

---

## Part 3: Application Questions

### Question 8
**Which module provides statistical foundations that this module extends?**
- [ ] A) Module 01
- [ ] B) Module 02
- [ ] C) Module 03 (Statistics)
- [ ] D) Module 04

**Answer**: C

**Explanation**: Module 03 introduces statistical measures, Module 05 extends to inference.

---

### Question 9
**What is Bayesian inference?**
- [ ] A) Forward pass
- [ ] B) Updating probabilities based on evidence
- [ ] C) Data storage
- [ ] D) Random operation

**Answer**: B

**Explanation**: Bayesian inference updates prior beliefs with new evidence using Bayes' theorem.

---

### Question 10
**Why do we need statistical inference in ML?**
- [ ] A) It's optional
- [ ] B) To make confident decisions about models and predictions
- [ ] C) To make code faster
- [ ] D) It's only for research

**Answer**: B

**Explanation**: Statistical inference helps us make confident, data-driven decisions about models.

---

## Scoring

- **9-10 correct**: Excellent! You understand probabilities and inference.
- **7-8 correct**: Good! Review the concepts you missed.
- **5-6 correct**: Review the module and try again.
- **Below 5**: Study the module more carefully before proceeding.

---

## Next Steps

After completing this quiz:
1. Review any questions you got wrong
2. Complete the exercises in `exercises/`
3. Complete the final exam to test all modules together!


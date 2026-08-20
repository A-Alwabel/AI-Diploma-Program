# Quiz 2: Bias, Justice, and Discrimination in AI

**Time Limit:** 30 minutes | **Marks:** 30 points

---

## Part 1: Multiple Choice (10 points)

### Question 1 (2 points)
What is demographic parity?
- A) Equal accuracy across all groups
- B) Equal positive prediction rates across groups
- C) Equal false positive rates
- D) Equal model complexity

---

### Question 2 (2 points)
What is equalized odds?
- A) Equal positive rates across groups
- B) Equal true positive and false positive rates across groups
- C) Equal accuracy
- D) Equal model performance

---

### Question 3 (2 points)
What is the main source of bias in machine learning models?
- A) Algorithm design
- B) Biased training data
- C) Model complexity
- D) Computing power

---

### Question 4 (2 points)
What is fairness through unawareness?
- A) Removing protected attributes from data
- B) Adding more protected attributes
- C) Using only protected attributes
- D) Ignoring fairness completely

---

### Question 5 (2 points)
What is a common limitation of fairness through unawareness?
- A) It always works perfectly
- B) Protected attributes can be inferred from other features (proxy discrimination)
- C) It's too expensive
- D) It's too slow

---

## Part 2: Short Answer (10 points)

### Question 6 (5 points)
Explain the difference between demographic parity and equalized odds. When would you use each?

**Demographic Parity:**
- Requires equal positive prediction rates across groups
- P(Ŷ=1 | Group=A) = P(Ŷ=1 | Group=B)
- Focuses on outcomes, not accuracy
- Use when: Equal opportunity in outcomes is the priority

**Equalized Odds:**
- Requires equal true positive and false positive rates across groups
- P(Ŷ=1 | Y=1, Group=A) = P(Ŷ=1 | Y=1, Group=B)
- P(Ŷ=1 | Y=0, Group=A) = P(Ŷ=1 | Y=0, Group=B)
- Focuses on accuracy fairness
- Use when: Equal accuracy across groups is the priority

**Trade-off:** Often cannot achieve both simultaneously.

---

### Question 7 (5 points)
Describe three techniques for mitigating bias in machine learning models.

**1. Pre-processing (Data-level):**
- Collect diverse, representative training data
- Remove or correct biased historical data
- Balance datasets across groups
- Example: Oversampling underrepresented groups

**2. In-processing (Algorithm-level):**
- Modify algorithms to optimize for fairness
- Add fairness constraints to objective function
- Use adversarial debiasing
- Example: Fairness-aware loss functions

**3. Post-processing (Prediction-level):**
- Adjust predictions to meet fairness criteria
- Reject option classification
- Calibrated equalized odds
- Example: Threshold adjustment per group

---

## Part 3: Case Analysis (10 points)

### Question 8 (5 points)
A hiring AI system shows the following results:
- Group A: 80% hired, 85% accuracy
- Group B: 40% hired, 85% accuracy

What fairness issues exist? How would you address them?

**Issues:**
1. **Demographic Parity Violation**: Group A has 2x higher hiring rate
2. **Potential Bias**: Despite equal accuracy, outcomes differ significantly
3. **Possible Proxy Discrimination**: Model may use features correlated with group membership

**Solutions:**
1. **Audit the Model**: Check for proxy variables (e.g., zip code, education institution)
2. **Apply Fairness Constraints**: Use demographic parity or equalized odds
3. **Re-train with Fairness**: Include fairness in objective function
4. **Post-processing**: Adjust thresholds to achieve demographic parity
5. **Regular Monitoring**: Continuously audit for bias

---

### Question 9 (5 points)
What are the key metrics used to measure fairness in AI systems? Explain each.

**Key Fairness Metrics:**

1. **Demographic Parity (Statistical Parity):**
   - Equal positive rates: P(Ŷ=1 | A) = P(Ŷ=1 | B)
   - Measures: Equal outcomes
   - Limitation: Ignores actual qualifications

2. **Equalized Odds:**
   - Equal TPR and FPR: P(Ŷ=1 | Y=1, A) = P(Ŷ=1 | Y=1, B)
   - Measures: Equal accuracy across groups
   - Limitation: May conflict with demographic parity

3. **Calibration:**
   - Equal prediction accuracy: P(Y=1 | Ŷ=p, A) = P(Y=1 | Ŷ=p, B)
   - Measures: Predictions are equally reliable
   - Use: When probabilities matter (risk assessment)

4. **Individual Fairness:**
   - Similar individuals get similar predictions
   - Measures: Consistency in treatment
   - Challenge: Defining "similar"

5. **Counterfactual Fairness:**
   - Prediction unchanged if protected attribute changed
   - Measures: Causal fairness
   - Use: When causal relationships are known

---

## Grading Rubric

- **90-100% (27-30 points):** Excellent understanding
- **80-89% (24-26 points):** Good understanding
- **70-79% (21-23 points):** Satisfactory
- **60-69% (18-20 points):** Needs improvement
- **Below 60% (<18 points):** Requires additional study
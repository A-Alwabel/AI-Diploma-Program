# Module 03 Quiz: Optimization and Statistics for Machine Learning

**Instructions**: Answer the following questions. Check your answers with the solutions provided.

## Part 1: Conceptual Questions

### Question 1
**Why do we need different optimizers (SGD, Adam, etc.)?**
- [ ] A) They all work the same
- [ ] B) Different optimizers work better for different problems
- [ ] C) They're required by Python
- [ ] D) They're optional

**Answer**: B

**Explanation**: Different optimizers have different properties - some converge faster, some handle noise better.

---

### Question 2
**What is the main advantage of Adam optimizer?**
- [ ] A) It's simpler
- [ ] B) It adapts learning rate per parameter and handles noise well
- [ ] C) It's faster to code
- [ ] D) It requires less memory

**Answer**: B

**Explanation**: Adam adapts learning rate for each parameter and handles noisy gradients better than simple GD.

---

### Question 3
**What is regularization used for?**
- [ ] A) Making code faster
- [ ] B) Preventing overfitting
- [ ] C) Data storage
- [ ] D) Random operations

**Answer**: B

**Explanation**: Regularization prevents overfitting by penalizing complex models.

---

### Question 4
**What does MSE (Mean Squared Error) do?**
- [ ] A) Measures average error
- [ ] B) Penalizes large errors more than small errors
- [ ] C) Measures only small errors
- [ ] D) Measures only large errors

**Answer**: B

**Explanation**: MSE squares errors, so large errors are penalized more heavily.

---

### Question 5
**What is the bias-variance tradeoff?**
- [ ] A) Choosing between speed and accuracy
- [ ] A) Balancing model complexity (underfitting vs overfitting)
- [ ] C) Choosing between data and code
- [ ] D) Random concept

**Answer**: B (Note: A appears twice, second should be B)

**Explanation**: Bias-variance tradeoff is about balancing model complexity to avoid underfitting (high bias) or overfitting (high variance).

---

## Part 2: Code Understanding

### Question 6
**What does this optimizer update do?**
```python
params = params - lr * gradient
```

- [ ] A) Simple gradient descent
- [ ] B) Adam optimizer
- [ ] C) Momentum optimizer
- [ ] D) RMSprop

**Answer**: A

**Explanation**: This is the basic gradient descent update rule.

---

### Question 7
**What does R² (R-squared) measure?**
- [ ] A) Total error
- [ ] B) How much variance the model explains
- [ ] C) Learning rate
- [ ] D) Number of parameters

**Answer**: B

**Explanation**: R² measures the proportion of variance in the target variable explained by the model.

---

## Part 3: Application Questions

### Question 8
**Which module provides the gradients used by optimizers?**
- [ ] A) Module 01
- [ ] B) Module 02 (Calculus)
- [ ] C) Module 04
- [ ] D) Module 05

**Answer**: B

**Explanation**: Module 02 teaches how to compute gradients, which optimizers use.

---

### Question 9
**What is overfitting?**
- [ ] A) Model too simple
- [ ] B) Model memorizes training data, performs poorly on new data
- [ ] C) Model too fast
- [ ] D) Model too slow

**Answer**: B

**Explanation**: Overfitting occurs when model learns training data too well but fails on new data.

---

### Question 10
**Why are statistical measures important in ML?**
- [ ] A) They're optional
- [ ] B) They provide objective ways to evaluate models
- [ ] C) They make code faster
- [ ] D) They're only for research

**Answer**: B

**Explanation**: Statistical measures provide objective, quantitative ways to evaluate and compare models.

---

## Scoring

- **9-10 correct**: Excellent! You understand optimization and statistics.
- **7-8 correct**: Good! Review the concepts you missed.
- **5-6 correct**: Review the module and try again.
- **Below 5**: Study the module more carefully before proceeding.

---

## Next Steps

After completing this quiz:
1. Review any questions you got wrong
2. Complete the exercises in `exercises/`
3. Move to Module 04 when ready


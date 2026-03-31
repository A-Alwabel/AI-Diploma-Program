# Final Exam: Mathematics and Probabilities for Machine Learning

**Course**: 113 AIAT - Mathematics and Probabilities for Machine Learning  
**Duration**: 60 minutes  
**Total Points**: 100

**Instructions**:
- Answer all questions
- Show your work for code questions
- Review all modules before taking the exam
- Good luck!

---

## Part 1: Module 01 - Linear Algebra (20 points)

### Question 1 (5 points)
Explain why linear algebra is the foundation of machine learning. Give 3 specific examples.

**Answer**: 
- All data in ML is represented as vectors/matrices
- Neural networks use matrix multiplication for transformations
- Eigenvalues/eigenvectors are used in PCA
- Gradients are vectors
- All ML operations use linear algebra

### Question 2 (5 points)
If you have a data matrix of shape (1000, 50), what does this mean?
- [ ] A) 1000 features, 50 samples
- [ ] B) 1000 samples, 50 features ✓
- [ ] C) 1000x50 = 50,000 total values
- [ ] D) Both B and C ✓

**Answer**: D

### Question 3 (5 points)
What is the result of this matrix multiplication?
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5], [6]])
result = A @ B
```

**Answer**: 
```
[[1*5 + 2*6], [3*5 + 4*6]]
= [[17], [39]]
```

### Question 4 (5 points)
What are eigenvalues and eigenvectors used for in Module 04?

**Answer**: PCA (Principal Component Analysis) uses eigenvalue decomposition to find principal components (directions of maximum variance).

---

## Part 2: Module 02 - Calculus (20 points)

### Question 5 (5 points)
Why do we need gradients in machine learning?

**Answer**: Gradients tell us which direction to adjust parameters to minimize the loss function. This is how ML models learn.

### Question 6 (5 points)
What is the relationship between gradients and optimization?

**Answer**: Optimization algorithms (like gradient descent) use gradients to find optimal parameters. Gradients point toward steepest increase, so we move opposite to minimize loss.

### Question 7 (5 points)
What is backpropagation?

**Answer**: Backpropagation is the chain rule applied to neural networks. It computes gradients through multiple layers by multiplying gradients backward.

### Question 8 (5 points)
If the gradient of a loss function at point x=5 is 10, and learning rate is 0.1, what is the next value of x in gradient descent?

**Answer**: 
```
x_new = x - lr * gradient
x_new = 5 - 0.1 * 10
x_new = 5 - 1
x_new = 4
```

---

## Part 3: Module 03 - Optimization and Statistics (20 points)

### Question 9 (5 points)
What is the main advantage of Adam optimizer over simple gradient descent?

**Answer**: Adam adapts learning rate per parameter and handles noisy gradients better, leading to faster and more stable convergence.

### Question 10 (5 points)
What is overfitting and how does regularization help?

**Answer**: Overfitting is when model memorizes training data but fails on new data. Regularization penalizes complex models, preventing overfitting.

### Question 11 (5 points)
What does R² (R-squared) measure?

**Answer**: R² measures the proportion of variance in the target variable explained by the model. Higher R² = better model fit.

### Question 12 (5 points)
What is the bias-variance tradeoff?

**Answer**: Balancing model complexity to avoid underfitting (high bias, too simple) or overfitting (high variance, too complex).

---

## Part 4: Module 04 - Dimensionality Reduction (20 points)

### Question 13 (5 points)
What is the curse of dimensionality?

**Answer**: As dimensions increase, the amount of data needed grows exponentially. High-dimensional data becomes sparse.

### Question 14 (5 points)
What mathematical concepts from Module 01 does PCA use?

**Answer**: PCA uses eigenvalue decomposition - specifically eigenvalues and eigenvectors of the covariance matrix.

### Question 15 (5 points)
If PCA reduces 100 features to 10 components and explains 85% variance, is this good? Why?

**Answer**: Yes, this is good. Reduced dimensions by 90% while preserving 85% of information. This improves efficiency significantly.

### Question 16 (5 points)
How does Module 03 (optimization) connect to PCA?

**Answer**: PCA finds components that maximize variance, which is an optimization problem. Optimization techniques help find optimal reduced dimensions.

---

## Part 5: Module 05 - Probabilities and Inference (20 points)

### Question 17 (5 points)
Why are probabilities important in machine learning?

**Answer**: Probabilities quantify uncertainty in predictions, help make confident decisions, and enable Bayesian methods.

### Question 18 (5 points)
What does a 95% confidence interval mean?

**Answer**: If we repeated the experiment many times, 95% of the computed intervals would contain the true value.

### Question 19 (5 points)
If a statistical test comparing two models gives p-value = 0.03, what does this mean?

**Answer**: p < 0.05 means the difference is statistically significant. We reject the null hypothesis and conclude models perform differently.

### Question 20 (5 points)
How do all 5 modules work together in a complete ML pipeline?

**Answer**: 
1. Module 01: Data as matrices
2. Module 02: Compute gradients
3. Module 03: Use gradients for optimization
4. Module 04: Reduce dimensions (uses Module 01 + 03)
5. Module 05: Statistical evaluation and inference

---

## Bonus Question (10 points)

**Describe the complete learning flow from Module 01 to Module 05, explaining how each module builds on previous ones.**

**Answer**:
- **Module 01** provides foundation: vectors, matrices, eigenvalues
- **Module 02** builds on Module 01: uses vectors for gradients, matrices for Jacobians
- **Module 03** uses Module 02: optimizers use gradients to train models
- **Module 04** combines Module 01 + 03: PCA uses eigenvalues (Module 01) + optimization (Module 03)
- **Module 05** extends Module 03: statistical inference for evaluation and decision-making

All modules work together: Data (01) → Gradients (02) → Optimization (03) → Dimensionality Reduction (04) → Statistical Evaluation (05)

---

## Scoring Guide

- **90-100 points**: Excellent! You've mastered all concepts.
- **80-89 points**: Very good! Review areas you missed.
- **70-79 points**: Good! Study the modules you struggled with.
- **60-69 points**: Passing, but review all modules.
- **Below 60**: Review all modules before retaking.

---

## Answer Key

All answers are provided above. Review your responses and study any concepts you missed.

**Congratulations on completing the course!** 🎉


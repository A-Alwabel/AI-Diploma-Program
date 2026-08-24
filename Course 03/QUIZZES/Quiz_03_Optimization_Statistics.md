# Quiz 03: Optimization and Statistics

**Time Limit:** 45 minutes | **Marks:** 100 points

---

## Part 1: Optimizers (25 points)

### Question 1 (5 points)
What is the main difference between SGD and Adam optimizer?
- A) SGD is faster
- B) Adam adapts learning rate per parameter, SGD uses fixed learning rate
- C) SGD uses momentum
- D) They are the same

---

### Question 2 (5 points)
What is momentum in optimization?
- A) A technique that uses past gradients to accelerate convergence
- B) The speed of convergence
- C) The learning rate
- D) The number of iterations

---

### Question 3 (5 points)
What is the advantage of Adam optimizer?
- A) It's always faster
- B) It uses less memory
- C) It adapts learning rates automatically and handles sparse gradients well
- D) It's simpler

---

### Question 4 (10 points)
Explain the difference between batch, mini-batch, and stochastic gradient descent.

**Batch Gradient Descent:**
- Uses entire dataset to compute gradient
- More stable, but slower
- Requires all data in memory
- One update per epoch

**Mini-Batch Gradient Descent:**
- Uses small batches (e.g., 32, 64, 128 samples)
- Balance between stability and speed
- Most common in practice
- Multiple updates per epoch

**Stochastic Gradient Descent (SGD):**
- Uses single sample per update
- Very fast updates, but noisy gradients
- Can escape local minima
- Many updates per epoch

**Trade-offs:**
- Batch: Stable but slow, good for small datasets
- Mini-batch: Good balance, standard for deep learning
- SGD: Fast but noisy, good for large datasets

---

## Part 2: Loss Functions (25 points)

### Question 5 (5 points)
What is a loss function?
- A) A metric to evaluate model performance
- B) A data structure
- C) An optimization algorithm
- D) A function that measures the difference between predictions and actual values

---

### Question 6 (5 points)
When would you use Mean Squared Error (MSE)?
- A) For classification problems
- B) For regression problems
- C) For clustering
- D) Always

---

### Question 7 (5 points)
When would you use Cross-Entropy Loss?
- A) For regression problems
- B) For clustering
- C) For classification problems
- D) Never

---

### Question 8 (10 points)
Compare MSE and MAE. When would you use each?

**Mean Squared Error (MSE):**
- Formula: MSE = (1/n)Σ(y - ŷ)²
- Penalizes large errors more (squared term)
- Differentiable everywhere
- Sensitive to outliers
- Use: When large errors are very costly, normal distribution assumed

**Mean Absolute Error (MAE):**
- Formula: MAE = (1/n)Σ|y - ŷ|
- Treats all errors equally
- Less sensitive to outliers
- Not differentiable at zero
- Use: When outliers are present, robust regression

**Example:**
- Prediction errors: [1, 2, 10]
- MSE = (1² + 2² + 10²)/3 = (1 + 4 + 100)/3 = 35
- MAE = (1 + 2 + 10)/3 = 4.33
- MSE heavily penalizes the large error (10)

---

## Part 3: Statistical Measures (25 points)

### Question 9 (5 points)
What is the mean of a dataset?
- A) The middle value
- B) The range
- C) The most common value
- D) The average value

---

### Question 10 (5 points)
What is standard deviation?
- A) A measure of how spread out the data is
- B) The average
- C) The median
- D) The maximum value

---

### Question 11 (5 points)
What is the difference between population and sample statistics?
- A) Population uses all data, sample uses subset; sample uses n-1 for variance
- B) They are the same
- C) Sample is always larger
- D) Population is always smaller

---

### Question 12 (10 points)
Explain variance and why we use n-1 in sample variance.

**Variance:**
- Measures spread of data around the mean
- Formula: σ² = (1/n)Σ(xᵢ - μ)²
- Average squared deviation from mean

**Sample Variance (n-1):**
- When estimating population variance from sample
- Formula: s² = (1/(n-1))Σ(xᵢ - x̄)²
- Uses n-1 instead of n (Bessel's correction)

**Why n-1?**
1. **Unbiased Estimator:** Using n-1 makes sample variance an unbiased estimator of population variance
2. **Degrees of Freedom:** We lose one degree of freedom by estimating the mean
3. **Mathematical Proof:** E[s²] = σ² when using n-1, but E[s²] < σ² when using n

**Example:**
- Sample: [1, 2, 3, 4, 5], mean = 3
- Using n: variance = ((1-3)² + (2-3)² + (3-3)² + (4-3)² + (5-3)²)/5 = 2
- Using n-1: variance = ((1-3)² + (2-3)² + (3-3)² + (4-3)² + (5-3)²)/4 = 2.5
- n-1 gives better estimate of population variance

---

## Part 4: Applications (25 points)

### Question 13 (10 points)
How are optimization and statistics used together in machine learning?

**Integration:**

1. **Loss Function as Statistical Measure:**
   - Loss functions often based on statistical measures (MSE, cross-entropy)
   - Measure discrepancy between predictions and true values
   - Statistical foundation for optimization

2. **Optimization Minimizes Statistical Error:**
   - Gradient descent minimizes loss (statistical error)
   - Find parameters that minimize expected error
   - Statistical learning theory guides optimization

3. **Regularization:**
   - Statistical concepts (bias-variance tradeoff) guide regularization
   - L1/L2 regularization based on statistical priors
   - Prevents overfitting (high variance)

4. **Model Selection:**
   - Statistical tests (t-test, F-test) for feature selection
   - Cross-validation (statistical resampling) for model selection
   - AIC, BIC for model comparison

5. **Uncertainty Quantification:**
   - Statistics provide confidence intervals
   - Bayesian methods combine statistics and optimization
   - Uncertainty estimates from statistical distributions

**Example:**
- Linear regression: Minimize MSE (statistical measure) using gradient descent (optimization)
- Regularization: Add L2 penalty (statistical prior) to optimization objective
- Result: Optimal parameters that balance fit and complexity

---

### Question 14 (15 points)
Explain the bias-variance tradeoff and its relationship to optimization and statistics.

**Bias-Variance Decomposition:**
- Total Error = Bias² + Variance + Irreducible Error
- Bias: Error from overly simplistic assumptions
- Variance: Error from sensitivity to training set variations
- Irreducible Error: Noise in data

**Relationship to Statistics:**
- **Bias:** Systematic error, related to model complexity
  - High bias: Model too simple (underfitting)
  - Low bias: Model can capture patterns
- **Variance:** Variability of predictions
  - High variance: Model too complex (overfitting)
  - Low variance: Stable predictions

**Relationship to Optimization:**
- **Optimization Goal:** Minimize total error
- **Challenge:** Reducing bias increases variance, and vice versa
- **Solution:** Find optimal balance through:
  - Regularization (penalize complexity)
  - Cross-validation (estimate generalization error)
  - Early stopping (prevent overfitting)

**Examples:**
1. **Linear Regression (High Bias, Low Variance):**
   - Simple model, stable predictions
   - May miss non-linear patterns
   - Optimization: Minimize MSE with L2 regularization

2. **Complex Neural Network (Low Bias, High Variance):**
   - Can capture complex patterns
   - Sensitive to training data
   - Optimization: Regularization, dropout, early stopping

3. **Optimal Model:**
   - Balance between bias and variance
   - Good generalization to new data
   - Achieved through proper optimization and statistical validation

**Practical Approach:**
- Use cross-validation to estimate bias and variance
- Adjust model complexity based on results
- Use regularization in optimization to control tradeoff
- Monitor training vs validation error

---

## Grading Rubric

- **90-100 points:** Excellent understanding
- **80-89 points:** Good understanding
- **70-79 points:** Satisfactory
- **60-69 points:** Needs improvement
- **Below 60:** Review required

---

**Created:** 2025  
**For:** 113 AIAT - Mathematics and Probabilities for Machine Learning

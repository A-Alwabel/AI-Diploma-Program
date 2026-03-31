# Test 1: Regression Analysis
## امتحان 1: تحليل الانحدار

**Time Limit:** 90 minutes | **Marks:** 50 points

---

## Instructions
- Answer all questions
- Show your work for code questions
- Use proper comments in your code
- You may use pandas, numpy, sklearn, and matplotlib

---

## Part 1: Multiple Choice (15 points)

### Question 1 (3 points)
What does R² (R-squared) measure?
- A) The correlation between features
- B) The proportion of variance explained by the model
- C) The mean squared error
- D) The residual sum of squares

**Answer:** B

---

### Question 2 (3 points)
In linear regression, what does the coefficient represent?
- A) The intercept
- B) The change in target variable per unit change in feature
- C) The error term
- D) The correlation coefficient

**Answer:** B

---

### Question 3 (3 points)
What is overfitting?
- A) Model performs well on training but poorly on test data
- B) Model performs poorly on both training and test data
- C) Model performs well on both training and test data
- D) Model has too few parameters

**Answer:** A

---

### Question 4 (3 points)
Which evaluation metric is most sensitive to outliers in regression?
- A) MAE (Mean Absolute Error)
- B) MSE (Mean Squared Error)
- C) R² Score
- D) Accuracy

**Answer:** B

---

### Question 5 (3 points)
When would you use polynomial regression instead of linear regression?
- A) When data shows linear relationship
- B) When data shows non-linear relationship
- C) When you have categorical features
- D) When you have missing values

**Answer:** B

---

## Part 2: Code Implementation (25 points)

### Question 6 (10 points)
Complete the following code to implement a complete regression pipeline:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Given: df is a dataframe with features and 'target' column

# TODO 1: Split into X and y
# Your code here

# TODO 2: Split into train/test (80/20)
# Your code here

# TODO 3: Scale the features
# Your code here

# TODO 4: Train a Linear Regression model
# Your code here

# TODO 5: Make predictions and calculate MSE and R²
# Your code here

# TODO 6: Create a scatter plot: Actual vs Predicted
# Your code here
```

**Answer:**
```python
# TODO 1: Split into X and y
X = df.drop('target', axis=1)
y = df['target']

# TODO 2: Split into train/test (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TODO 3: Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# TODO 4: Train a Linear Regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# TODO 5: Make predictions and calculate MSE and R²
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse:.4f}, R²: {r2:.4f}")

# TODO 6: Create a scatter plot: Actual vs Predicted
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], 
         [y_test.min(), y_test.max()], 'r--', linewidth=2)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted')
plt.grid(True, alpha=0.3)
plt.show()
```

**Grading:**
- Correct split: 1 point
- Correct train_test_split: 2 points
- Correct scaling: 2 points
- Correct model training: 2 points
- Correct evaluation: 2 points
- Correct plot: 1 point

---

### Question 7 (10 points)
Write a function that:
1. Takes X_train, y_train, X_test, y_test as parameters
2. Trains polynomial regression models with degrees 1, 2, 3, 4
3. Evaluates each model and returns a dictionary with degrees as keys and R² scores as values
4. Identifies the best degree

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def find_best_polynomial_degree(X_train, y_train, X_test, y_test):
    """
    Find the best polynomial degree for regression.
    
    Returns:
        dict: Dictionary with degrees and R² scores
        int: Best degree
    """
    # Your code here
    pass
```

**Answer:**
```python
def find_best_polynomial_degree(X_train, y_train, X_test, y_test):
    results = {}
    best_degree = 1
    best_score = -float('inf')
    
    for degree in [1, 2, 3, 4]:
        # Create polynomial features
        poly_features = PolynomialFeatures(degree=degree)
        X_train_poly = poly_features.fit_transform(X_train)
        X_test_poly = poly_features.transform(X_test)
        
        # Train model
        model = LinearRegression()
        model.fit(X_train_poly, y_train)
        
        # Evaluate
        y_pred = model.predict(X_test_poly)
        r2 = r2_score(y_test, y_pred)
        
        results[degree] = r2
        
        # Track best
        if r2 > best_score:
            best_score = r2
            best_degree = degree
    
    return results, best_degree
```

**Grading:**
- Function structure: 2 points
- Polynomial features: 3 points
- Model training: 2 points
- Evaluation: 2 points
- Best degree logic: 1 point

---

### Question 8 (5 points)
Write code to analyze residuals:
1. Calculate residuals (y_test - y_pred)
2. Plot histogram of residuals
3. Plot residuals vs predicted values

**Answer:**
```python
# Calculate residuals
residuals = y_test - y_pred

# Histogram
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(residuals, bins=20, edgecolor='black', alpha=0.7)
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Residuals Distribution')
plt.axvline(0, color='r', linestyle='--')

plt.subplot(1, 2, 2)
plt.scatter(y_pred, residuals, alpha=0.6)
plt.axhline(0, color='r', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Predicted')

plt.tight_layout()
plt.show()
```

**Grading:**
- Residuals calculation: 1 point
- Histogram: 2 points
- Residuals vs predicted: 2 points

---

## Part 3: Analysis and Explanation (10 points)

### Question 9 (5 points)
A student trained a linear regression model and got:
- Training R² = 0.95
- Test R² = 0.65

Explain what this indicates and suggest solutions.

**Answer:**
This indicates **overfitting**:
- The model learned the training data too well (high training R²)
- But fails to generalize to new data (low test R²)
- Gap of 0.30 suggests significant overfitting

**Solutions:**
1. Use regularization (Ridge or Lasso)
2. Reduce model complexity (fewer features)
3. Get more training data
4. Use cross-validation
5. Try simpler models

---

### Question 10 (5 points)
Explain the difference between:
- Simple Linear Regression
- Multiple Linear Regression
- Polynomial Regression

Give examples of when to use each.

**Answer:**

1. **Simple Linear Regression:**
   - One feature, one target
   - y = b₀ + b₁x
   - Use: Single feature analysis, simple relationships

2. **Multiple Linear Regression:**
   - Multiple features, one target
   - y = b₀ + b₁x₁ + b₂x₂ + ...
   - Use: Multiple factors affect target, complex real-world problems

3. **Polynomial Regression:**
   - Non-linear relationships
   - y = b₀ + b₁x + b₂x² + ...
   - Use: Curved relationships, when linear doesn't fit

---

## Answer Key Summary

**Part 1:** 15 points (5 questions × 3 points)
**Part 2:** 25 points (Questions 6-8)
**Part 3:** 10 points (Questions 9-10)

**Total: 50 points**

---

## Grading Rubric

- **90-100% (45-50 points):** Excellent - Mastery of concepts
- **80-89% (40-44 points):** Good - Strong understanding
- **70-79% (35-39 points):** Satisfactory - Basic understanding
- **60-69% (30-34 points):** Passing - Needs improvement
- **Below 60% (<30 points):** Fail - Requires retaking

---

## Time Management Tips

- Part 1 (Multiple Choice): 15 minutes
- Part 2 (Code): 50 minutes
- Part 3 (Analysis): 20 minutes
- Review: 5 minutes


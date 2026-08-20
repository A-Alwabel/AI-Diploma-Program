# Quiz 4: Machine Learning Introduction

**Time Limit:** 30 minutes | **Marks:** 30 points

---

## Part 1: Multiple Choice (10 points)

### Question 1 (2 points)
What is the difference between supervised and unsupervised learning?
- A) Supervised uses labels, unsupervised doesn't
- B) Supervised is faster
- C) Unsupervised uses more data
- D) They are the same

---

### Question 2 (2 points)
What does accuracy measure?
- A) The proportion of correct predictions
- B) The average error
- C) The model complexity
- D) The training time

---

### Question 3 (2 points)
What is overfitting?
- A) Model performs well on training but poorly on test data
- B) Model performs poorly on both training and test data
- C) Model is too simple
- D) Model trains too slowly

---

### Question 4 (2 points)
What is the purpose of train_test_split?
- A) To speed up training
- B) To evaluate model performance on unseen data
- C) To reduce data size
- D) To remove outliers

---

### Question 5 (2 points)
What does a confusion matrix show?
- A) Model training time
- B) True positives, false positives, true negatives, false negatives
- C) Feature importance
- D) Model parameters

---

## Part 2: Code Writing (10 points)

### Question 6 (5 points)
Write code to train a simple linear regression model:
1. Import necessary libraries
2. Split data into train/test
3. Train the model
4. Make predictions and calculate accuracy

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# Assuming X (features) and y (target) are defined
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse}, R²: {r2}")
```

---

### Question 7 (5 points)
Write code to train a classification model and evaluate it:
1. Import classification model (e.g., LogisticRegression)
2. Train the model
3. Make predictions
4. Calculate accuracy and show confusion matrix

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

# Assuming X and y are defined
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{cm}")
```

---

## Part 3: Short Answer (10 points)

### Question 8 (5 points)
Explain the bias-variance tradeoff. How does it relate to overfitting and underfitting?

**Bias-Variance Tradeoff:**
- **Bias**: Error from overly simplistic assumptions (underfitting)
  - High bias: Model too simple, can't capture patterns
  - Example: Linear model for non-linear data
  
- **Variance**: Error from sensitivity to small fluctuations (overfitting)
  - High variance: Model too complex, memorizes training data
  - Example: Deep tree that captures noise

**Tradeoff:**
- Reducing bias increases variance (more complex models)
- Reducing variance increases bias (simpler models)
- Goal: Find optimal balance for best generalization

**Solutions:**
- Regularization (L1/L2) to reduce variance
- Cross-validation to find optimal complexity
- Ensemble methods to balance both

---

### Question 9 (5 points)
What are the main evaluation metrics for classification and regression? When would you use each?

**Classification Metrics:**
1. **Accuracy**: Overall correctness (use when classes are balanced)
2. **Precision**: True positives / (True positives + False positives) - use when false positives are costly
3. **Recall**: True positives / (True positives + False negatives) - use when false negatives are costly
4. **F1-Score**: Harmonic mean of precision and recall - use for balanced measure
5. **ROC-AUC**: Area under ROC curve - use for binary classification with imbalanced data

**Regression Metrics:**
1. **MSE (Mean Squared Error)**: Average squared errors - penalizes large errors
2. **RMSE (Root Mean Squared Error)**: Square root of MSE - in same units as target
3. **MAE (Mean Absolute Error)**: Average absolute errors - less sensitive to outliers
4. **R² Score**: Proportion of variance explained - use to compare models

---

## Grading Rubric

- **90-100% (27-30 points):** Excellent understanding
- **80-89% (24-26 points):** Good understanding
- **70-79% (21-23 points):** Satisfactory
- **60-69% (18-20 points):** Needs improvement
- **Below 60% (<18 points):** Requires additional study

"""
Unit 2 - Exercise 2: Cross-Validation Practice
تقنيات الانحدار المتقدمة - تمرين 2: ممارسة التحقق المتقاطع

Instructions:
1. Load the provided dataset
2. Implement K-Fold cross-validation manually
3. Use sklearn's KFold for cross-validation
4. Compare single train-test split vs K-Fold CV
5. Calculate mean and std of CV scores
6. Understand why CV gives more reliable estimates

Dataset: Regression dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# Generate sample regression data
np.random.seed(123)
X = np.random.randn(300, 5)
y = 2 * X[:, 0] + 1.5 * X[:, 1] - X[:, 2] + 3 * X[:, 3] + np.random.normal(0, 0.5, 300)

df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(5)])
df['target'] = y

print("Dataset loaded!")
print(f"Shape: {df.shape}")

# TODO: Write your code here
# TODO: اكتب الكود الخاص بك هنا

# Task 1: Single train-test split (baseline)
print("\n" + "="*60)
print("Task 1: Single train-test split")
print("="*60)
# Split data 80/20
# Train Linear Regression
# Evaluate on test set
# Print MSE and R²
# Your code here...

# Task 2: Manual K-Fold cross-validation (K=5)
print("\n" + "="*60)
print("Task 2: Manual K-Fold CV (K=5)")
print("="*60)
# Split data into 5 folds manually
# For each fold:
#   - Train on 4 folds, test on 1 fold
#   - Calculate MSE and R²
# Store all scores
# Print mean and std of scores
# Your code here...

# Task 3: Use sklearn's KFold
print("\n" + "="*60)
print("Task 3: sklearn KFold")
print("="*60)
# Use KFold(n_splits=5, shuffle=True, random_state=123)
# Implement CV loop using KFold
# Calculate mean and std of scores
# Your code here...

# Task 4: Use cross_val_score
print("\n" + "="*60)
print("Task 4: cross_val_score")
print("="*60)
# Use sklearn's cross_val_score function
# Much simpler than manual implementation!
# Print mean and std
# Your code here...

# Task 5: Compare single split vs CV
print("\n" + "="*60)
print("Task 5: Compare single split vs CV")
print("="*60)
# Show that CV gives more reliable estimate
# Single split: One score (might be lucky/unlucky)
# CV: Multiple scores, mean gives better estimate
# Your code here...

# Task 6: Visualize CV score distribution
print("\n" + "="*60)
print("Task 6: Visualize CV scores")
print("="*60)
# Plot histogram of CV scores
# Show mean and std
# Your code here...

print("\n" + "="*60)
print("Exercise 2 Complete!")
print("اكتمل التمرين 2!")
print("="*60)


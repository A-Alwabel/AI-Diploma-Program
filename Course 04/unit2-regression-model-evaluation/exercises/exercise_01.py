"""
Unit 2 - Exercise 1: Ridge and Lasso Regression Practice
تقنيات الانحدار المتقدمة - تمرين 1: ممارسة الانحدار ريدج ولاسو

Instructions:
1. Load the provided dataset
2. Apply Ridge and Lasso regression with different alpha values
3. Compare the results with Linear Regression
4. Visualize the coefficient shrinkage
5. Find the optimal alpha value for both methods
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# Generate sample data with multicollinearity
np.random.seed(42)
n_samples = 300

X = np.random.randn(n_samples, 8)
# Make some features correlated
X[:, 2] = X[:, 0] + 0.3 * np.random.randn(n_samples)
X[:, 3] = X[:, 1] + 0.3 * np.random.randn(n_samples)

y = (2 * X[:, 0] + 1.5 * X[:, 1] - X[:, 2] + 3 * X[:, 3] + 
     0.5 * X[:, 4] + np.random.normal(0, 0.5, n_samples))

df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(8)])
df['target'] = y

print("Dataset loaded!")
print(f"Shape: {df.shape}")

# TODO: Write your code here
# TODO: اكتب الكود الخاص بك هنا

# Task 1: Split the data and scale features
print("\nTask 1: Split and scale data")
# Your code here...

# Task 2: Train Linear Regression, Ridge, and Lasso models
print("\nTask 2: Train models")
# Your code here...

# Task 3: Compare coefficients
print("\nTask 3: Compare coefficients")
# Your code here...

# Task 4: Find optimal alpha for Ridge and Lasso
print("\nTask 4: Find optimal alpha")
# Your code here...

print("\nExercise 1 Complete!")
print("اكتمل التمرين 1!")


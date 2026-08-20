"""
Unit 1 - Exercise 3: Polynomial Regression Practice
أساليب معالجة البيانات - تمرين 3: ممارسة الانحدار متعدد الحدود

Instructions:
1. Load the provided dataset
2. Create polynomial regression models with different degrees
3. Detect overfitting by comparing train vs test performance
4. Find the optimal polynomial degree
5. Visualize the results
6. Understand the bias-variance tradeoff

Use the provided dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate sample non-linear data
np.random.seed(123)
X = np.linspace(0, 10, 200).reshape(-1, 1)
# Create non-linear relationship: y = 2*x^2 - 3*x + 1 + noise
y = 2 * X.flatten()**2 - 3 * X.flatten() + 1 + np.random.normal(0, 2, 200)

df = pd.DataFrame({'x': X.flatten(), 'y': y})

print("Dataset Info:")
print(f"Shape: {df.shape}")
print(df.head())

# TODO: Write your code here
# TODO: اكتب الكود الخاص بك هنا

# Task 1: Split the data into train and test sets (80/20)
print("\n" + "="*60)
print("Task 1: Split data")
print("="*60)
# Your code here...

# Task 2: Train polynomial regression with degree 1 (linear)
print("\n" + "="*60)
print("Task 2: Polynomial Regression (degree=1)")
print("="*60)
# Use PolynomialFeatures with degree=1
# Train LinearRegression
# Evaluate on both train and test
# Your code here...

# Task 3: Train polynomial regression with degree 2
print("\n" + "="*60)
print("Task 3: Polynomial Regression (degree=2)")
print("="*60)
# Use PolynomialFeatures with degree=2
# Train and evaluate
# Your code here...

# Task 4: Train polynomial regression with degree 5
print("\n" + "="*60)
print("Task 4: Polynomial Regression (degree=5)")
print("="*60)
# Use PolynomialFeatures with degree=5
# Train and evaluate
# Notice overfitting (high train accuracy, lower test accuracy)
# Your code here...

# Task 5: Find optimal degree using validation
print("\n" + "="*60)
print("Task 5: Find optimal polynomial degree")
print("="*60)
# Test degrees from 1 to 10
# Plot degree vs MSE (both train and test)
# Find degree with best test performance
# Your code here...

# Task 6: Visualize results
print("\n" + "="*60)
print("Task 6: Visualize polynomial fits")
print("="*60)
# Plot original data
# Plot polynomial fits for different degrees
# Show how higher degrees can overfit
# Your code here...

print("\n" + "="*60)
print("Exercise 3 Complete!")
print("اكتمل التمرين 3!")
print("="*60)


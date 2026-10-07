"""
Unit 5 - Exercise 2: Boosting Algorithms Practice
Model selection and boosting - Exercise 2: Practising boosting algorithms

Instructions:
1. Load the provided dataset
2. Train XGBoost model (if available)
3. Train LightGBM model (if available)
4. Compare with Random Forest (bagging)
5. Compare boosting algorithms with each other
6. Interpret feature importance
7. Understand boosting vs bagging

Dataset: Binary classification dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_auc_score, roc_curve
)
from sklearn.datasets import load_breast_cancer

# Load real-world Breast Cancer dataset
cancer_data = load_breast_cancer()
X = cancer_data.data
y = cancer_data.target

df = pd.DataFrame(X, columns=cancer_data.feature_names)
df['target'] = y

print("Dataset loaded!")
print(f"Shape: {df.shape}")
print(f"\nClass distribution:")
print(df['target'].value_counts())

# TODO: Write your code here
# TODO: write your code here

# Task 1: Split the data
print("\n" + "="*60)
print("Task 1: Split data")
print("="*60)
# Your code here...

# Task 2: Train Random Forest (bagging - for comparison)
print("\n" + "="*60)
print("Task 2: Train Random Forest (bagging)")
print("="*60)
# Train RandomForestClassifier
# Evaluate and print metrics
# Your code here...

# Task 3: Try to import and train XGBoost
print("\n" + "="*60)
print("Task 3: Train XGBoost (if available)")
print("="*60)
# Try: import xgboost as xgb
# If available: Train XGBClassifier
# Evaluate and print metrics
# If not available: Print installation instructions
# Your code here...

# Task 4: Try to import and train LightGBM
print("\n" + "="*60)
print("Task 4: Train LightGBM (if available)")
print("="*60)
# Try: import lightgbm as lgb
# If available: Train LGBMClassifier
# Evaluate and print metrics
# If not available: Print installation instructions
# Your code here...

# Task 5: Compare all models
print("\n" + "="*60)
print("Task 5: Compare models")
print("="*60)
# Create comparison table
# Show: Random Forest vs XGBoost vs LightGBM
# Show which performs best
# Your code here...

# Task 6: Feature importance comparison
print("\n" + "="*60)
print("Task 6: Feature importance")
print("="*60)
# Get feature importance from all models
# Visualize and compare
# Show which features are most important
# Your code here...

# Task 7: Understand boosting vs bagging
print("\n" + "="*60)
print("Task 7: Boosting vs Bagging")
print("="*60)
# Explain the difference:
# - Bagging (RF): Models trained in parallel, then averaged
# - Boosting (XGBoost/LightGBM): Models trained sequentially, each learns from mistakes
# Your code here...

print("\n" + "="*60)
print("Exercise 2 Complete!")
print("Exercise 2 complete.")
print("="*60)


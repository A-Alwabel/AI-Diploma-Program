"""
Unit 3 - Exercise 3: Support Vector Machine (SVM) Practice
Advanced classification techniques - Exercise 3: Practising support vector machines (SVM)

Instructions:
1. Load the provided dataset
2. Train SVM models with different kernels (Linear, RBF, Polynomial)
3. Compare their performance
4. Tune hyperparameters (C and gamma for RBF)
5. Visualize decision boundaries (if 2D) or compare metrics
6. Find the best kernel and hyperparameters

Dataset: Binary classification dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_auc_score
)

# Generate sample classification data
np.random.seed(123)
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=500,
    n_features=8,
    n_informative=5,
    n_redundant=2,
    n_classes=2,
    random_state=123
)

df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(8)])
df['target'] = y

print("Dataset loaded!")
print(f"Shape: {df.shape}")
print(f"\nClass distribution:")
print(df['target'].value_counts())

# TODO: Write your code here
# TODO: write your code here

# Task 1: Split the data and scale features (CRITICAL for SVM!)
print("\n" + "="*60)
print("Task 1: Split and scale data")
print("="*60)
# Your code here...

# Task 2: Train Linear SVM
print("\n" + "="*60)
print("Task 2: Train Linear SVM")
print("="*60)
# Train SVM with kernel='linear', C=1.0
# Evaluate and print metrics
# Your code here...

# Task 3: Train RBF SVM
print("\n" + "="*60)
print("Task 3: Train RBF SVM")
print("="*60)
# Train SVM with kernel='rbf', C=1.0, gamma='scale'
# Evaluate and print metrics
# Your code here...

# Task 4: Train Polynomial SVM
print("\n" + "="*60)
print("Task 4: Train Polynomial SVM")
print("="*60)
# Train SVM with kernel='poly', degree=3, C=1.0
# Evaluate and print metrics
# Your code here...

# Task 5: Compare all three kernels
print("\n" + "="*60)
print("Task 5: Compare kernels")
print("="*60)
# Create a comparison table or visualization
# Show which kernel performs best
# Your code here...

# Task 6: Tune C parameter for RBF kernel
print("\n" + "="*60)
print("Task 6: Tune C parameter for RBF")
print("="*60)
# Try different C values: [0.1, 1.0, 10.0, 100.0]
# Find the best C value
# Your code here...

# Task 7: (Optional) Tune gamma parameter for RBF
print("\n" + "="*60)
print("Task 7: (Optional) Tune gamma parameter")
print("="*60)
# Try different gamma values: ['scale', 'auto', 0.01, 0.1, 1.0]
# Find the best gamma value
# Your code here...

print("\n" + "="*60)
print("Exercise 3 Complete!")
print("Exercise 3 complete.")
print("="*60)


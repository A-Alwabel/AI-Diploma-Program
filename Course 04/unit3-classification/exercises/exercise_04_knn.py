"""
Unit 3 - Exercise 4: K-Nearest Neighbors (KNN) Practice
Advanced classification techniques - Exercise 4: Practising k-nearest neighbours (KNN)

Instructions:
1. Load the provided dataset
2. Scale the features (CRITICAL for KNN!)
3. Train KNN models with different K values
4. Find the optimal K value using validation
5. Evaluate the final model with optimal K
6. Compare KNN with and without feature scaling (demonstrate importance)

Dataset: Binary classification dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix
)
from sklearn.datasets import make_classification

# Generate sample classification data
np.random.seed(123)
X, y = make_classification(
    n_samples=800,
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

# Task 1: Split the data
print("\n" + "="*60)
print("Task 1: Split data")
print("="*60)
# Your code here...

# Task 2: Demonstrate why scaling is critical
print("\n" + "="*60)
print("Task 2: Compare KNN with and without scaling")
print("="*60)
# Train KNN WITHOUT scaling (use original data)
# Train KNN WITH scaling (use StandardScaler)
# Compare accuracies - show the difference!
# Your code here...

# Task 3: Find optimal K value
print("\n" + "="*60)
print("Task 3: Find optimal K value")
print("="*60)
# Test K values from 1 to 30 (odd numbers only)
# Plot K vs Accuracy (both train and test)
# Find the K with best test accuracy
# Your code here...

# Task 4: Train final KNN model with optimal K
print("\n" + "="*60)
print("Task 4: Train final model with optimal K")
print("="*60)
# Train KNN with the best K value found
# Evaluate with all metrics (accuracy, precision, recall, F1)
# Your code here...

# Task 5: Create confusion matrix
print("\n" + "="*60)
print("Task 5: Confusion Matrix")
print("="*60)
# Create and visualize confusion matrix
# Your code here...

# Task 6: (Optional) Compare KNN with other classifiers
print("\n" + "="*60)
print("Task 6: (Optional) Compare with other classifiers")
print("="*60)
# Compare KNN with Logistic Regression or Decision Tree
# Show which performs better on this dataset
# Your code here...

print("\n" + "="*60)
print("Exercise 4 Complete!")
print("Exercise 4 complete.")
print("="*60)


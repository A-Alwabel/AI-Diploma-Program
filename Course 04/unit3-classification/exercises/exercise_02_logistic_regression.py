"""
Unit 3 - Exercise 2: Logistic Regression Practice
Advanced classification techniques - Exercise 2: Practising logistic regression

Instructions:
1. Load the provided dataset
2. Train a Logistic Regression classifier
3. Calculate and display all classification metrics (accuracy, precision, recall, F1)
4. Create and visualize a confusion matrix
5. Create and visualize an ROC curve
6. Experiment with different thresholds
7. Handle class imbalance using class weights

Dataset: Binary classification dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_curve, roc_auc_score, classification_report
)
from sklearn.datasets import make_classification

# Generate sample classification data
np.random.seed(123)
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=6,
    n_redundant=2,
    n_classes=2,
    random_state=123
)

df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(10)])
df['target'] = y

print("Dataset loaded!")
print(f"Shape: {df.shape}")
print(f"\nClass distribution:")
print(df['target'].value_counts())

# TODO: Write your code here
# TODO: write your code here

# Task 1: Split the data into train and test sets (80/20, use stratify)
print("\n" + "="*60)
print("Task 1: Split data")
print("="*60)
# Your code here...

# Task 2: Scale the features (important for logistic regression!)
print("\n" + "="*60)
print("Task 2: Scale features")
print("="*60)
# Your code here...

# Task 3: Train a Logistic Regression model (default parameters)
print("\n" + "="*60)
print("Task 3: Train Logistic Regression model")
print("="*60)
# Your code here...

# Task 4: Make predictions and calculate metrics
print("\n" + "="*60)
print("Task 4: Calculate classification metrics")
print("="*60)
# Calculate: accuracy, precision, recall, F1-score
# Your code here...

# Task 5: Create and visualize confusion matrix
print("\n" + "="*60)
print("Task 5: Confusion Matrix")
print("="*60)
# Create confusion matrix and visualize it with seaborn heatmap
# Your code here...

# Task 6: Get prediction probabilities and create ROC curve
print("\n" + "="*60)
print("Task 6: ROC Curve")
print("="*60)
# Get probabilities using .predict_proba()
# Calculate ROC curve (fpr, tpr, thresholds)
# Calculate AUC score
# Plot ROC curve with AUC value
# Your code here...

# Task 7: Train model with class weights to handle imbalance
print("\n" + "="*60)
print("Task 7: Handle class imbalance with class weights")
print("="*60)
# Train new model with class_weight='balanced'
# Compare metrics with previous model
# Your code here...

print("\n" + "="*60)
print("Exercise 2 Complete!")
print("Exercise 2 complete.")
print("="*60)


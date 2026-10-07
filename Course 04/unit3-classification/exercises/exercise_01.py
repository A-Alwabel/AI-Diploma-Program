"""
Unit 3 - Exercise 1: Classification Practice
Advanced classification techniques - Exercise 1: Practising classification

Instructions:
1. Load the provided dataset
2. Train a Decision Tree classifier
3. Train a Random Forest classifier
4. Evaluate both models using appropriate metrics
5. Compare feature importance
6. Visualize decision boundaries (if 2D) or feature importance
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                            confusion_matrix)
from sklearn.datasets import make_classification

# Generate sample classification data
np.random.seed(42)
X, y = make_classification(
    n_samples=800,
    n_features=8,
    n_informative=5,
    n_redundant=2,
    random_state=42
)

df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(8)])
df['target'] = y

print("Dataset loaded!")
print(f"Shape: {df.shape}")

# TODO: Write your code here
# TODO: write your code here

# Task 1: Split the data
print("\nTask 1: Split data")
# Your code here...

# Task 2: Train Decision Tree
print("\nTask 2: Train Decision Tree")
# Your code here...

# Task 3: Train Random Forest
print("\nTask 3: Train Random Forest")
# Your code here...

# Task 4: Evaluate both models
print("\nTask 4: Evaluate models")
# Your code here...

# Task 5: Compare feature importance
print("\nTask 5: Feature importance")
# Your code here...

print("\nExercise 1 Complete!")
print("Exercise 1 complete.")


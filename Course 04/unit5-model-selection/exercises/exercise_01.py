"""
Unit 5 - Exercise 1: Model Selection Practice
Model selection and boosting - Exercise 1: Practising model selection

Instructions:
1. Load the provided dataset
2. Use Grid Search to find best hyperparameters for Random Forest
3. Compare with default Random Forest
4. (Optional) Try XGBoost if available
5. Evaluate and compare results
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import make_classification

# Generate sample classification data
np.random.seed(42)
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=5,
    random_state=42
)

df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(10)])
df['target'] = y

print("Dataset loaded!")
print(f"Shape: {df.shape}")

# TODO: Write your code here
# TODO: write your code here

# Task 1: Split the data
print("\nTask 1: Split data")
# Your code here...

# Task 2: Train default Random Forest
print("\nTask 2: Default Random Forest")
# Your code here...

# Task 3: Grid Search for Random Forest
print("\nTask 3: Grid Search")
# Your code here...

# Task 4: Compare results
print("\nTask 4: Compare")
# Your code here...

print("\nExercise 1 Complete!")
print("Exercise 1 complete.")


"""
Unit 4 - Exercise 2: Principal Component Analysis (PCA) Practice
Clustering and dimensionality reduction - Exercise 2: Practising principal component analysis (PCA)

Instructions:
1. Load the provided dataset
2. Apply PCA to reduce dimensionality
3. Analyze explained variance
4. Choose optimal number of components
5. Visualize data in reduced dimensions
6. Compare original vs PCA-transformed data

Dataset: Multi-dimensional dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# Load Iris dataset (4 features, 3 classes)
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names

df = pd.DataFrame(X, columns=feature_names)
df['target'] = y

print("Dataset loaded!")
print(f"Shape: {df.shape}")
print(f"Features: {feature_names}")
print(f"\nClass distribution:")
print(df['target'].value_counts())

# TODO: Write your code here
# TODO: write your code here

# Task 1: Scale the data (CRITICAL for PCA!)
print("\n" + "="*60)
print("Task 1: Scale data")
print("="*60)
# Use StandardScaler
# Your code here...

# Task 2: Apply PCA with all components
print("\n" + "="*60)
print("Task 2: Apply PCA (all components)")
print("="*60)
# Create PCA object
# Fit and transform the data
# Your code here...

# Task 3: Analyze explained variance
print("\n" + "="*60)
print("Task 3: Explained variance analysis")
print("="*60)
# Get explained_variance_ratio_ for each component
# Calculate cumulative explained variance
# Print: Each component's variance, cumulative variance
# Your code here...

# Task 4: Visualize explained variance
print("\n" + "="*60)
print("Task 4: Visualize explained variance")
print("="*60)
# Plot: Component number vs Explained variance
# Plot: Component number vs Cumulative explained variance
# Your code here...

# Task 5: Reduce to 2D for visualization
print("\n" + "="*60)
print("Task 5: Reduce to 2D")
print("="*60)
# Apply PCA with n_components=2
# Transform data to 2D
# Visualize in 2D (color by original class labels)
# Your code here...

# Task 6: Find optimal number of components
print("\n" + "="*60)
print("Task 6: Find optimal number of components")
print("="*60)
# Find number of components that explain 95% of variance
# Find number of components that explain 99% of variance
# Your code here...

# Task 7: Compare original vs PCA-transformed
print("\n" + "="*60)
print("Task 7: Compare original vs PCA")
print("="*60)
# Show: Original has 4 features, PCA can reduce to 2-3
# Show: PCA preserves most information with fewer features
# Your code here...

print("\n" + "="*60)
print("Exercise 2 Complete!")
print("Exercise 2 complete.")
print("="*60)


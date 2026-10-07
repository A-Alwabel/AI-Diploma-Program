"""
Unit 4 - Exercise 1: Clustering Practice
Clustering and dimensionality reduction - Exercise 1: Practising clustering

Instructions:
1. Load the provided dataset
2. Apply K-Means clustering with different K values
3. Use the Elbow Method to find optimal K
4. Apply Hierarchical clustering
5. Visualize the clusters
6. Compare results
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Generate sample data
np.random.seed(42)

cluster1 = np.random.normal([2, 2], 0.6, (80, 2))
cluster2 = np.random.normal([6, 6], 0.6, (80, 2))
cluster3 = np.random.normal([2, 6], 0.6, (80, 2))

X = np.vstack([cluster1, cluster2, cluster3])
indices = np.random.permutation(len(X))
X = X[indices]

df = pd.DataFrame(X, columns=['feature_1', 'feature_2'])

print("Dataset loaded!")
print(f"Shape: {df.shape}")

# TODO: Write your code here
# TODO: write your code here

# Task 1: Scale the data
print("\nTask 1: Scale data")
# Your code here...

# Task 2: Apply K-Means with K=3
print("\nTask 2: K-Means (K=3)")
# Your code here...

# Task 3: Elbow Method to find optimal K
print("\nTask 3: Elbow Method")
# Your code here...

# Task 4: Apply Hierarchical Clustering
print("\nTask 4: Hierarchical Clustering")
# Your code here...

# Task 5: Visualize clusters
print("\nTask 5: Visualize")
# Your code here...

print("\nExercise 1 Complete!")
print("Exercise 1 complete.")


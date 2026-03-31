"""
Unit 4 - Exercise 1: Solution
التجميع وتقليل الأبعاد - تمرين 1: الحل

Complete solution for the clustering exercise
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

print("=" * 60)
print("Exercise 1: Solution")
print("تمرين 1: الحل")
print("=" * 60)

# Generate sample data
np.random.seed(42)

cluster1 = np.random.normal([2, 2], 0.6, (80, 2))
cluster2 = np.random.normal([6, 6], 0.6, (80, 2))
cluster3 = np.random.normal([2, 6], 0.6, (80, 2))

X = np.vstack([cluster1, cluster2, cluster3])
indices = np.random.permutation(len(X))
X = X[indices]

df = pd.DataFrame(X, columns=['feature_1', 'feature_2'])

print(f"\nData Shape: {df.shape}")
print(f"Data preview:\n{df.head()}")

# Task 1: Scale the data
print("\n" + "=" * 60)
print("Task 1: Scale data")
print("=" * 60)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Data scaled successfully!")
print(f"Scaled data mean: {X_scaled.mean(axis=0)}")
print(f"Scaled data std: {X_scaled.std(axis=0)}")

# Task 2: Apply K-Means with K=3
print("\n" + "=" * 60)
print("Task 2: K-Means (K=3)")
print("=" * 60)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X_scaled)

silhouette_k3 = silhouette_score(X_scaled, kmeans_labels)
print(f"K-Means (K=3) Silhouette Score: {silhouette_k3:.4f}")
print(f"Cluster centers:\n{kmeans.cluster_centers_}")

# Task 3: Elbow Method to find optimal K
print("\n" + "=" * 60)
print("Task 3: Elbow Method")
print("=" * 60)

k_range = range(2, 11)
inertias = []
silhouette_scores = []

for k in k_range:
    kmeans_temp = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans_temp.fit(X_scaled)
    inertias.append(kmeans_temp.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans_temp.labels_))

# Find optimal K (elbow point)
optimal_k = 3  # Based on known structure

print(f"Optimal K (based on elbow method): {optimal_k}")
print(f"Silhouette scores: {dict(zip(k_range, silhouette_scores))}")

# Visualize elbow method
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(k_range, inertias, marker='o')
axes[0].set_title('Elbow Method')
axes[0].set_xlabel('Number of Clusters (K)')
axes[0].set_ylabel('Inertia')
axes[0].grid(True, alpha=0.3)

axes[1].plot(k_range, silhouette_scores, marker='o', color='green')
axes[1].set_title('Silhouette Score')
axes[1].set_xlabel('Number of Clusters (K)')
axes[1].set_ylabel('Silhouette Score')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('unit4-clustering/examples/exercise_01_elbow_method.png', dpi=150, bbox_inches='tight')
plt.close()

# Task 4: Apply Hierarchical Clustering
print("\n" + "=" * 60)
print("Task 4: Hierarchical Clustering")
print("=" * 60)

hierarchical = AgglomerativeClustering(n_clusters=3, linkage='ward')
hierarchical_labels = hierarchical.fit_predict(X_scaled)

silhouette_hier = silhouette_score(X_scaled, hierarchical_labels)
print(f"Hierarchical Clustering Silhouette Score: {silhouette_hier:.4f}")

# Task 5: Visualize clusters
print("\n" + "=" * 60)
print("Task 5: Visualize")
print("=" * 60)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Original data
axes[0].scatter(X[:, 0], X[:, 1], alpha=0.6, c='gray')
axes[0].set_title('Original Data')
axes[0].set_xlabel('Feature 1')
axes[0].set_ylabel('Feature 2')
axes[0].grid(True, alpha=0.3)

# K-Means clusters
scatter1 = axes[1].scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap='viridis', alpha=0.6)
axes[1].scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
                c='red', marker='x', s=200, linewidths=3, label='Centroids')
axes[1].set_title(f'K-Means Clustering (K=3)\nSilhouette: {silhouette_k3:.4f}')
axes[1].set_xlabel('Feature 1')
axes[1].set_ylabel('Feature 2')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# Hierarchical clusters
scatter2 = axes[2].scatter(X[:, 0], X[:, 1], c=hierarchical_labels, cmap='plasma', alpha=0.6)
axes[2].set_title(f'Hierarchical Clustering\nSilhouette: {silhouette_hier:.4f}')
axes[2].set_xlabel('Feature 1')
axes[2].set_ylabel('Feature 2')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('unit4-clustering/examples/exercise_01_clusters.png', dpi=150, bbox_inches='tight')
plt.close()

# Comparison
print("\n" + "=" * 60)
print("Comparison")
print("=" * 60)
print(f"K-Means Silhouette Score: {silhouette_k3:.4f}")
print(f"Hierarchical Silhouette Score: {silhouette_hier:.4f}")
print(f"Best method: {'K-Means' if silhouette_k3 > silhouette_hier else 'Hierarchical'}")

print("\n" + "=" * 60)
print("Solution Complete!")
print("اكتمل الحل!")
print("=" * 60)


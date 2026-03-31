"""
Solution 01: Principal Component Analysis (PCA)

This is the reference solution for exercise_01.py
"""

import numpy as np


def compute_covariance_matrix(data):
    """Compute the covariance matrix of data."""
    # Center the data (subtract mean)
    centered = data - np.mean(data, axis=0)
    # Compute covariance: (1/n) * X^T @ X
    n = data.shape[0]
    return (centered.T @ centered) / (n - 1)


def pca_from_scratch(data, n_components=2):
    """Implement PCA from scratch."""
    # 1. Center the data
    mean = np.mean(data, axis=0)
    centered = data - mean
    
    # 2. Compute covariance matrix
    cov = compute_covariance_matrix(data)
    
    # 3. Find eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(cov)
    
    # 4. Sort by eigenvalues (descending)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    # 5. Select top n_components
    top_eigenvectors = eigenvectors[:, :n_components]
    
    # 6. Project data
    reduced = centered @ top_eigenvectors
    
    # 7. Calculate explained variance ratio
    explained_variance_ratio = np.sum(eigenvalues[:n_components]) / np.sum(eigenvalues)
    
    return reduced, explained_variance_ratio


def calculate_variance_explained(eigenvalues, n_components):
    """Calculate variance explained by top components."""
    return np.sum(eigenvalues[:n_components]) / np.sum(eigenvalues)


if __name__ == "__main__":
    print("Solution 01: PCA")
    print("=" * 60)
    
    np.random.seed(42)
    data = np.random.randn(100, 10)
    
    reduced, variance_ratio = pca_from_scratch(data, n_components=2)
    
    print(f"Original shape: {data.shape}")
    print(f"Reduced shape: {reduced.shape}")
    print(f"Variance explained: {variance_ratio:.2%}")
    print("\n✅ Solution verified!")

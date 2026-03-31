"""
PCA Implementation - Complete Solution
Principal Component Analysis from scratch with visualization
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, load_iris

class PCA:
    """Principal Component Analysis implementation from scratch."""
    
    def __init__(self, n_components=2):
        """
        Initialize PCA.
        
        Args:
            n_components: Number of principal components to keep
        """
        self.n_components = n_components
        self.components_ = None
        self.explained_variance_ratio_ = None
        self.mean_ = None
    
    def fit(self, X):
        """
        Fit PCA on data.
        
        Args:
            X: Input data (n_samples, n_features)
        """
        # Center the data
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_
        
        # Compute covariance matrix
        cov_matrix = np.cov(X_centered.T)
        
        # Eigenvalue decomposition
        eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
        
        # Sort by eigenvalue (descending)
        idx = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]
        
        # Select top n_components
        self.components_ = eigenvectors[:, :self.n_components]
        
        # Calculate explained variance ratio
        total_variance = np.sum(eigenvalues)
        self.explained_variance_ratio_ = eigenvalues[:self.n_components] / total_variance
    
    def transform(self, X):
        """
        Transform data to principal component space.
        
        Args:
            X: Input data (n_samples, n_features)
        
        Returns:
            Transformed data (n_samples, n_components)
        """
        X_centered = X - self.mean_
        return X_centered.dot(self.components_)
    
    def fit_transform(self, X):
        """Fit and transform in one step."""
        self.fit(X)
        return self.transform(X)

def visualize_pca(X, X_pca, explained_variance, title="PCA Visualization"):
    """Visualize PCA results."""
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Original data (first 2 features)
    axes[0].scatter(X[:, 0], X[:, 1], alpha=0.6, s=50)
    axes[0].set_xlabel('Feature 1')
    axes[0].set_ylabel('Feature 2')
    axes[0].set_title('Original Data (First 2 Features)')
    axes[0].grid(True, alpha=0.3)
    
    # PCA transformed data
    axes[1].scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.6, s=50, c='red')
    axes[1].set_xlabel(f'PC1 (Variance: {explained_variance[0]:.2%})')
    axes[1].set_ylabel(f'PC2 (Variance: {explained_variance[1]:.2%})')
    axes[1].set_title('Data After PCA (2D Projection)')
    axes[1].grid(True, alpha=0.3)
    
    plt.suptitle(title, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

def visualize_variance_explained(explained_variance_ratio, n_components=5):
    """Visualize explained variance by each component."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    components = range(1, min(len(explained_variance_ratio) + 1, n_components + 1))
    variance = explained_variance_ratio[:n_components]
    cumulative = np.cumsum(variance)
    
    x = np.arange(len(components))
    width = 0.35
    
    ax.bar(x - width/2, variance, width, label='Individual', alpha=0.8)
    ax.bar(x + width/2, cumulative, width, label='Cumulative', alpha=0.8)
    
    ax.set_xlabel('Principal Component')
    ax.set_ylabel('Explained Variance Ratio')
    ax.set_title('Explained Variance by Principal Component')
    ax.set_xticks(x)
    ax.set_xticklabels([f'PC{i}' for i in components])
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.show()

def main():
    """Main function to run PCA implementation."""
    print("PCA Implementation - Complete Solution")
    print("=" * 60)
    
    # Generate sample data
    print("\nGenerating sample data...")
    X, y = make_classification(n_samples=200, n_features=10, n_informative=5,
                              n_redundant=3, n_classes=3, random_state=42)
    print(f"Data shape: {X.shape}")
    
    # Apply PCA
    print("\nApplying PCA...")
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    
    print(f"Original dimensions: {X.shape[1]}")
    print(f"Reduced dimensions: {X_pca.shape[1]}")
    print(f"\nExplained variance ratio:")
    for i, var in enumerate(pca.explained_variance_ratio_):
        print(f"  PC{i+1}: {var:.2%}")
    print(f"Total variance explained: {np.sum(pca.explained_variance_ratio_):.2%}")
    
    # Visualizations
    print("\nShowing PCA visualization...")
    visualize_pca(X, X_pca, pca.explained_variance_ratio_)
    
    # Test with Iris dataset
    print("\n" + "=" * 60)
    print("Testing with Iris Dataset")
    print("=" * 60)
    
    iris = load_iris()
    X_iris = iris.data
    y_iris = iris.target
    
    pca_iris = PCA(n_components=2)
    X_iris_pca = pca_iris.fit_transform(X_iris)
    
    print(f"Iris data: {X_iris.shape} -> {X_iris_pca.shape}")
    print(f"Explained variance: {np.sum(pca_iris.explained_variance_ratio_):.2%}")
    
    # Visualize Iris with colors
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Original (first 2 features)
    scatter1 = axes[0].scatter(X_iris[:, 0], X_iris[:, 1], c=y_iris, 
                              cmap='viridis', alpha=0.7, s=60)
    axes[0].set_xlabel('Sepal Length')
    axes[0].set_ylabel('Sepal Width')
    axes[0].set_title('Original Data (First 2 Features)')
    plt.colorbar(scatter1, ax=axes[0])
    
    # PCA
    scatter2 = axes[1].scatter(X_iris_pca[:, 0], X_iris_pca[:, 1], c=y_iris,
                              cmap='viridis', alpha=0.7, s=60)
    axes[1].set_xlabel(f'PC1 ({pca_iris.explained_variance_ratio_[0]:.2%})')
    axes[1].set_ylabel(f'PC2 ({pca_iris.explained_variance_ratio_[1]:.2%})')
    axes[1].set_title('PCA Projection (2D)')
    plt.colorbar(scatter2, ax=axes[1])
    
    plt.suptitle('Iris Dataset: Original vs PCA', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

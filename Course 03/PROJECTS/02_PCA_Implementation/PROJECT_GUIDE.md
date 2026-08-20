# Complete Project Guide: 02 Pca Implementation

---

## 🎯 Real-World Application

---

## 🚀 Quick Start (For Experienced Students)

> 💡 **New to this project?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.

## Step-by-Step Implementation

---

## 📚 Complete Tutorial (For Beginners)

> 💡 **Already familiar with this?** See [Quick Start](#-quick-start-for-experienced-students) section above.

### Step 1: Understand PCA (Day 1)

**What is PCA?**
Principal Component Analysis:
- Finds the most important directions in data
- Reduces dimensions while keeping information
- Like compressing a photo without losing quality

**Example:**
```
Original Image: 1000x1000 pixels = 1,000,000 values
After PCA: 100 principal components = 100 values
Compression: 99.99% reduction!
Quality: Still recognizable
```

---

### Step 2: Set Up Project (Day 1)

**Create structure:**
```
pca_project/
├── pca_implementation.py
├── visualizer.py
├── image_compression.py
├── test.py
└── README.md
```

**Install:**
```bash
pip install numpy matplotlib scikit-learn pillow
```

---

### Step 3: Implement PCA Core (Day 2-3)

**File: `pca_implementation.py`**

```python
import numpy as np

class PCA:
    """Principal Component Analysis from scratch"""
    
    def __init__(self, n_components=2):
        self.n_components = n_components
        self.components = None
        self.mean = None
        self.explained_variance_ratio_ = None
    
    def fit(self, X):
        """Fit PCA to data"""
        # Step 1: Center the data (subtract mean)
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean
        
        # Step 2: Calculate covariance matrix
        # Covariance shows how features vary together
        n_samples = X_centered.shape[0]
        covariance_matrix = np.dot(X_centered.T, X_centered) / (n_samples - 1)
        
        # Step 3: Eigenvalue decomposition
        # Eigenvectors = principal components (directions)
        # Eigenvalues = variance explained (importance)
        eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
        
        # Step 4: Sort by eigenvalues (descending)
        # Higher eigenvalue = more important component
        idx = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]
        
        # Step 5: Select top n components
        self.components = eigenvectors[:, :self.n_components]
        
        # Calculate explained variance ratio
        total_variance = eigenvalues.sum()
        self.explained_variance_ratio_ = eigenvalues[:self.n_components] / total_variance
        
        print(f"✅ PCA fitted: {self.n_components} components")
        print(f"   Explained variance: {self.explained_variance_ratio_.sum():.2%}")
        
        return self
    
    def transform(self, X):
        """Transform data to lower dimensions"""
        X_centered = X - self.mean
        return np.dot(X_centered, self.components)
    
    def fit_transform(self, X):
        """Fit and transform in one step"""
        return self.fit(X).transform(X)
    
    def inverse_transform(self, X_reduced):
        """Reconstruct original data from reduced dimensions"""
        return np.dot(X_reduced, self.components.T) + self.mean
```

---

### Step 4: Create Visualizer (Day 4)

**File: `visualizer.py`**

```python
import matplotlib.pyplot as plt
import numpy as np

class PCAVisualizer:
    """Visualize PCA process"""
    
    def plot_original_vs_reduced(self, X_original, X_reduced, labels=None):
        """Compare original and reduced data"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Original data (first 2 features)
        axes[0].scatter(X_original[:, 0], X_original[:, 1], 
                       c=labels, cmap='viridis', alpha=0.6)
        axes[0].set_title('Original Data (First 2 Features)')
        axes[0].set_xlabel('Feature 1')
        axes[0].set_ylabel('Feature 2')
        axes[0].grid(True, alpha=0.3)
        
        # Reduced data (PCA components)
        axes[1].scatter(X_reduced[:, 0], X_reduced[:, 1],
                       c=labels, cmap='viridis', alpha=0.6)
        axes[1].set_title('PCA Reduced Data (2 Components)')
        axes[1].set_xlabel('First Principal Component')
        axes[1].set_ylabel('Second Principal Component')
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('results/original_vs_reduced.png', dpi=300)
        plt.close()
    
    def plot_variance_explained(self, pca):
        """Plot variance explained by each component"""
        plt.figure(figsize=(10, 6))
        
        components = range(1, len(pca.explained_variance_ratio_) + 1)
        variance = pca.explained_variance_ratio_
        cumulative = np.cumsum(variance)
        
        plt.bar(components, variance, alpha=0.7, label='Individual')
        plt.plot(components, cumulative, 'ro-', label='Cumulative')
        plt.xlabel('Principal Component')
        plt.ylabel('Explained Variance Ratio')
        plt.title('Variance Explained by Principal Components')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('results/variance_explained.png', dpi=300)
        plt.close()
    
    def plot_components(self, pca, feature_names):
        """Visualize principal components"""
        n_components = pca.components.shape[1]
        fig, axes = plt.subplots(1, n_components, figsize=(5*n_components, 5))
        
        if n_components == 1:
            axes = [axes]
        
        for i in range(n_components):
            component = pca.components[:, i]
            axes[i].barh(feature_names, component)
            axes[i].set_title(f'Principal Component {i+1}')
            axes[i].set_xlabel('Component Value')
        
        plt.tight_layout()
        plt.savefig('results/components.png', dpi=300)
        plt.close()
```

---

### Step 5: Image Compression Example (Day 5)

**File: `image_compression.py`**

```python
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from pca_implementation import PCA

class ImageCompressor:
    """Compress images using PCA"""
    
    def load_image(self, filepath):
        """Load image as numpy array"""
        img = Image.open(filepath)
        img_array = np.array(img)
        return img_array
    
    def compress_image(self, img_array, n_components=50):
        """Compress image using PCA"""
        # Reshape image: (height, width, channels) -> (height*width, channels)
        h, w, c = img_array.shape
        img_2d = img_array.reshape(-1, c)
        
        # Apply PCA to each channel separately
        compressed_channels = []
        pca_models = []
        
        for channel in range(c):
            channel_data = img_2d[:, channel:channel+1]
            pca = PCA(n_components=n_components)
            compressed = pca.fit_transform(channel_data)
            compressed_channels.append(compressed)
            pca_models.append(pca)
        
        # Reconstruct image
        reconstructed_channels = []
        for channel, pca in zip(compressed_channels, pca_models):
            reconstructed = pca.inverse_transform(channel)
            reconstructed_channels.append(reconstructed)
        
        # Combine channels
        reconstructed_2d = np.hstack(reconstructed_channels)
        reconstructed_img = reconstructed_2d.reshape(h, w, c)
        
        # Clip values to valid range
        reconstructed_img = np.clip(reconstructed_img, 0, 255).astype(np.uint8)
        
        return reconstructed_img, pca_models
    
    def compare_images(self, original, compressed):
        """Compare original and compressed images"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 7))
        
        axes[0].imshow(original)
        axes[0].set_title('Original Image')
        axes[0].axis('off')
        
        axes[1].imshow(compressed)
        axes[1].set_title('Compressed Image (PCA)')
        axes[1].axis('off')
        
        plt.tight_layout()
        plt.savefig('results/image_comparison.png', dpi=300)
        plt.close()
```

---

### Step 6: Create Main Program (Day 6)

**File: `main.py`**

```python
import numpy as np
from sklearn.datasets import load_iris
from pca_implementation import PCA
from visualizer import PCAVisualizer

def main():
    print("=" * 60)
    print("PCA Implementation and Visualization")
    print("=" * 60)
    
    # Example 1: Iris dataset
    print("\n[Example 1] Iris Dataset")
    data = load_iris()
    X = data.data
    y = data.target
    
    # Apply PCA
    pca = PCA(n_components=2)
    X_reduced = pca.fit_transform(X)
    
    print(f"Original shape: {X.shape}")
    print(f"Reduced shape: {X_reduced.shape}")
    print(f"Variance explained: {pca.explained_variance_ratio_}")
    
    # Visualize
    viz = PCAVisualizer()
    viz.plot_original_vs_reduced(X, X_reduced, y)
    viz.plot_variance_explained(pca)
    
    # Example 2: Image compression (if image available)
    print("\n[Example 2] Image Compression")
    try:
        from image_compression import ImageCompressor
        compressor = ImageCompressor()
        # img = compressor.load_image('data/image.jpg')
        # compressed, pca_models = compressor.compress_image(img, n_components=50)
        # compressor.compare_images(img, compressed)
        print("   (Add an image file to test compression)")
    except:
        print("   (Image compression example skipped)")
    
    print("\n✅ PCA implementation complete!")

if __name__ == "__main__":
    main()
```

---

---
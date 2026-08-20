# Complete Project Guide: 01 Algorithms From Scratch

---

## 🎯 Real-World Application

---

## 🚀 Quick Start (For Experienced Students)

> 💡 **New to this project?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.

## Step-by-Step Implementation

---

## 📚 Complete Tutorial (For Beginners)

> 💡 **Already familiar with this?** See [Quick Start](#-quick-start-for-experienced-students) section above.

### Step 1: Understand the Goal (Day 1)

**What is "From Scratch"?**
Implementing algorithms using only:
- NumPy (for arrays and math)
- Basic Python (no ML libraries)
- Your own code (no scikit-learn)

**Why?**
- Understand how algorithms work
- Learn the mathematics
- Customize for your needs
- Impress employers!

---

### Step 2: Set Up Project (Day 1)

**Create structure:**
```
algorithms_from_scratch/
├── linear_regression.py
├── logistic_regression.py
├── pca.py
├── test.py
└── README.md
```

**Install:**
```bash
pip install numpy matplotlib
```

---

### Step 3: Implement Linear Regression (Day 2-3)

**File: `linear_regression.py`**

```python
import numpy as np

class LinearRegression:
    """Linear Regression from scratch"""
    
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        """Train the model using gradient descent"""
        # Initialize parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Gradient descent
        for i in range(self.iterations):
            # Predictions
            y_pred = np.dot(X, self.weights) + self.bias
            
            # Calculate gradients
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)
            
            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            
            # Print progress every 100 iterations
            if i % 100 == 0:
                cost = np.mean((y_pred - y) ** 2)
                print(f"Iteration {i}: Cost = {cost:.4f}")
    
    def predict(self, X):
        """Make predictions"""
        return np.dot(X, self.weights) + self.bias
    
    def score(self, X, y):
        """Calculate R² score"""
        y_pred = self.predict(X)
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        return 1 - (ss_res / ss_tot)
```

---

### Step 4: Implement Logistic Regression (Day 4-5)

**File: `logistic_regression.py`**

```python
import numpy as np

class LogisticRegression:
    """Logistic Regression from scratch"""
    
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = None
    
    def sigmoid(self, z):
        """Sigmoid activation function"""
        return 1 / (1 + np.exp(-np.clip(z, -250, 250)))
    
    def fit(self, X, y):
        """Train the model"""
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for i in range(self.iterations):
            # Forward pass
            linear_model = np.dot(X, self.weights) + self.bias
            y_pred = self.sigmoid(linear_model)
            
            # Calculate gradients
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)
            
            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
    
    def predict(self, X):
        """Make predictions"""
        linear_model = np.dot(X, self.weights) + self.bias
        y_pred = self.sigmoid(linear_model)
        return (y_pred >= 0.5).astype(int)
    
    def predict_proba(self, X):
        """Get probability predictions"""
        linear_model = np.dot(X, self.weights) + self.bias
        return self.sigmoid(linear_model)
```

---

### Step 5: Implement PCA (Day 6-7)

**File: `pca.py`**

```python
import numpy as np

class PCA:
    """Principal Component Analysis from scratch"""
    
    def __init__(self, n_components=2):
        self.n_components = n_components
        self.components = None
        self.mean = None
    
    def fit(self, X):
        """Fit PCA to data"""
        # Center the data
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean
        
        # Calculate covariance matrix
        covariance_matrix = np.cov(X_centered.T)
        
        # Eigenvalue decomposition
        eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
        
        # Sort by eigenvalues (descending)
        idx = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]
        
        # Select top n components
        self.components = eigenvectors[:, :self.n_components]
        
        # Explained variance
        self.explained_variance_ratio_ = eigenvalues[:self.n_components] / eigenvalues.sum()
        
        return self
    
    def transform(self, X):
        """Transform data to lower dimensions"""
        X_centered = X - self.mean
        return np.dot(X_centered, self.components)
    
    def fit_transform(self, X):
        """Fit and transform in one step"""
        return self.fit(X).transform(X)
```

---

### Step 6: Test Your Implementations (Day 8)

**File: `test.py`**

```python
import numpy as np
from sklearn.datasets import make_regression, make_classification
from linear_regression import LinearRegression
from logistic_regression import LogisticRegression
from pca import PCA

# Test Linear Regression
print("Testing Linear Regression...")
X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)
lr = LinearRegression(learning_rate=0.01, iterations=1000)
lr.fit(X, y)
print(f"R² Score: {lr.score(X, y):.4f}")

# Test Logistic Regression
print("\nTesting Logistic Regression...")
X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)
lr_clf = LogisticRegression(learning_rate=0.01, iterations=1000)
lr_clf.fit(X, y)
predictions = lr_clf.predict(X)
accuracy = np.mean(predictions == y)
print(f"Accuracy: {accuracy:.4f}")

# Test PCA
print("\nTesting PCA...")
X = np.random.randn(100, 10)
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)
print(f"Original shape: {X.shape}")
print(f"Reduced shape: {X_reduced.shape}")
print(f"Explained variance: {pca.explained_variance_ratio_}")

print("\n✅ All tests passed!")
```

---

---
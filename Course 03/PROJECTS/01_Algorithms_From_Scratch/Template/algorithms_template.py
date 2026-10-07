"""
ML Algorithms from Scratch Template
Project 01 Template

Fill in the functions marked with TODO comments.
Use ONLY NumPy - no scikit-learn for core implementations!
"""

import numpy as np
import matplotlib.pyplot as plt


class LinearRegression:
    """Linear Regression from scratch."""
    
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = None
        self.cost_history = []
    
    def fit(self, X, y):
        """
        Train linear regression using gradient descent.
        
        TODO: Implement gradient descent
        """
        # TODO: Initialize weights and bias
        # m, n = X.shape
        # self.weights = np.zeros(n)
        # self.bias = 0
        
        # TODO: Gradient descent loop
        # for i in range(self.iterations):
        #     # Calculate predictions
        #     y_pred = X.dot(self.weights) + self.bias
        #     
        #     # Calculate gradients
        #     dw = (1/m) * X.T.dot(y_pred - y)
        #     db = (1/m) * np.sum(y_pred - y)
        #     
        #     # Update weights and bias
        #     self.weights -= self.learning_rate * dw
        #     self.bias -= self.learning_rate * db
        #     
        #     # Calculate and store cost
        #     cost = self.cost(y, y_pred)
        #     self.cost_history.append(cost)
        pass
    
    def predict(self, X):
        """
        Make predictions.
        
        TODO: Implement prediction
        """
        # TODO: y_pred = X.dot(self.weights) + self.bias
        # return y_pred
        pass
    
    def cost(self, y_true, y_pred):
        """
        Calculate mean squared error.
        
        TODO: Implement MSE cost function
        """
        # TODO: mse = (1/(2*len(y_true))) * np.sum((y_pred - y_true)**2)
        # return mse
        pass


class LogisticRegression:
    """Logistic Regression from scratch."""
    
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = None
        self.cost_history = []
    
    def sigmoid(self, z):
        """
        Sigmoid activation function.
        
        TODO: Implement sigmoid function
        """
        # TODO: return 1 / (1 + np.exp(-z))
        pass
    
    def fit(self, X, y):
        """
        Train logistic regression using gradient descent.
        
        TODO: Implement gradient descent with sigmoid
        """
        # TODO: Initialize weights and bias
        # TODO: Gradient descent loop
        # TODO: Calculate predictions using sigmoid
        # TODO: Calculate gradients
        # TODO: Update weights and bias
        # TODO: Calculate and store cost
        pass
    
    def predict(self, X):
        """
        Make binary predictions.
        
        TODO: Implement prediction with threshold
        """
        # TODO: Calculate probabilities using sigmoid
        # TODO: Return binary predictions (threshold = 0.5)
        pass
    
    def cost(self, y_true, y_pred_proba):
        """
        Calculate binary cross-entropy loss.
        
        TODO: Implement BCE loss
        """
        # TODO: bce = -np.mean(y_true * np.log(y_pred_proba) + 
        #                      (1 - y_true) * np.log(1 - y_pred_proba))
        # return bce
        pass


class PCA:
    """Principal Component Analysis from scratch."""
    
    def __init__(self, n_components=None):
        self.n_components = n_components
        self.components = None
        self.mean = None
    
    def fit(self, X):
        """
        Fit PCA by finding principal components.
        
        TODO: Implement PCA fitting
        """
        # TODO: Standardize data (subtract mean)
        # self.mean = np.mean(X, axis=0)
        # X_centered = X - self.mean
        
        # TODO: Calculate covariance matrix
        # cov_matrix = np.cov(X_centered.T)
        
        # TODO: Calculate eigenvalues and eigenvectors
        # eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
        
        # TODO: Sort by eigenvalues (descending)
        # TODO: Select top n_components
        # self.components = eigenvectors[:, :self.n_components]
        pass
    
    def transform(self, X):
        """
        Transform data to lower dimensions.
        
        TODO: Project data onto principal components
        """
        # TODO: Center data
        # X_centered = X - self.mean
        
        # TODO: Project onto principal components
        # return X_centered.dot(self.components)
        pass
    
    def fit_transform(self, X):
        """Fit and transform in one step."""
        self.fit(X)
        return self.transform(X)


def main():
    """
    Main execution function.
    
    TODO: Test all algorithms
    """
    # TODO: Generate or load test data
    # TODO: Test LinearRegression
    # TODO: Test LogisticRegression
    # TODO: Test PCA
    # TODO: Compare with scikit-learn (for verification)
    
    print("Algorithms from scratch complete!")


if __name__ == "__main__":
    main()


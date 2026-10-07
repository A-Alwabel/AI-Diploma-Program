"""
Gradient Descent Visualizer Template
Project 03 Template

Fill in the functions marked with TODO comments.
Requires: pip install matplotlib numpy
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation


def cost_function(w, b, X, y):
    """
    Calculate cost (MSE) for linear regression.
    
    TODO: Implement cost function
    """
    # TODO: Calculate predictions
    # y_pred = X.dot(w) + b
    
    # TODO: Calculate MSE
    # mse = np.mean((y_pred - y)**2)
    # return mse
    pass


def gradient(w, b, X, y):
    """
    Calculate gradients.
    
    TODO: Implement gradient calculation
    """
    # TODO: Calculate predictions
    # y_pred = X.dot(w) + b
    
    # TODO: Calculate gradients
    # dw = (1/len(y)) * X.T.dot(y_pred - y)
    # db = (1/len(y)) * np.sum(y_pred - y)
    # return dw, db
    pass


class GradientDescent:
    """Gradient Descent implementation."""
    
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.cost_history = []
        self.parameter_history = []
    
    def fit(self, X, y, w_init=None, b_init=0):
        """
        Train using gradient descent.
        
        TODO: Implement gradient descent algorithm
        """
        # TODO: Initialize parameters
        # if w_init is None:
        #     w = np.zeros(X.shape[1])
        # else:
        #     w = w_init.copy()
        # b = b_init
        
        # TODO: Gradient descent loop
        # for i in range(self.iterations):
        #     # Calculate cost
        #     cost = cost_function(w, b, X, y)
        #     self.cost_history.append(cost)
        #     self.parameter_history.append((w.copy(), b))
        #     
        #     # Calculate gradients
        #     dw, db = gradient(w, b, X, y)
        #     
        #     # Update parameters
        #     w -= self.learning_rate * dw
        #     b -= self.learning_rate * db
        
        # return w, b
        pass


class GradientDescentVisualizer:
    """Visualizes gradient descent."""
    
    def plot_cost_surface(self, X, y, w_range, b_range):
        """
        Plot 3D cost surface.
        
        TODO: Create 3D surface plot of cost function
        """
        # TODO: Create meshgrid for w and b
        # W, B = np.meshgrid(w_range, b_range)
        
        # TODO: Calculate cost for each point
        # Cost = np.zeros_like(W)
        # for i in range(len(w_range)):
        #     for j in range(len(b_range)):
        #         Cost[j, i] = cost_function(W[j, i], B[j, i], X, y)
        
        # TODO: Create 3D surface plot
        pass
    
    def plot_cost_history(self, cost_history):
        """
        Plot cost vs iterations.
        
        TODO: Create line plot of cost over iterations
        """
        # TODO: Plot cost_history
        pass
    
    def plot_contour_with_path(self, X, y, parameter_history, w_range, b_range):
        """
        Plot contour of cost function with gradient descent path.
        
        TODO: Create contour plot with descent path
        """
        # TODO: Create contour plot of cost function
        # TODO: Plot gradient descent path
        pass
    
    def animate_descent(self, X, y, parameter_history, w_range, b_range):
        """
        Animate gradient descent on cost surface.
        
        TODO: Create animation of gradient descent
        """
        # TODO: Set up figure
        # TODO: Create animation function
        # TODO: Use FuncAnimation
        pass


def compare_gd_variants(X, y):
    """
    Compare different gradient descent variants.
    
    TODO: Implement and compare:
    - Batch Gradient Descent
    - Stochastic Gradient Descent
    - Mini-batch Gradient Descent
    """
    # TODO: Implement SGD
    # TODO: Implement Mini-batch GD
    # TODO: Compare convergence
    pass


def main():
    """
    Main execution function.
    
    TODO: Implement complete gradient descent visualization
    """
    # TODO: Generate or load data
    # TODO: Initialize GradientDescent
    # TODO: Train model
    # TODO: Create visualizations
    # TODO: Animate descent
    # TODO: Compare variants
    
    print("Gradient descent visualization complete!")


if __name__ == "__main__":
    main()


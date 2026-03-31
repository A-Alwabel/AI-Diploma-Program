"""
Gradient Descent Visualizer - Complete Solution
Animated visualization of gradient descent optimization
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

def cost_function(w, b, X, y):
    """Calculate MSE cost for linear regression."""
    y_pred = X.dot(w) + b
    mse = np.mean((y_pred - y)**2)
    return mse

def gradient(w, b, X, y):
    """Calculate gradients for w and b."""
    m = len(y)
    y_pred = X.dot(w) + b
    dw = (1/m) * X.T.dot(y_pred - y)
    db = (1/m) * np.sum(y_pred - y)
    return dw, db

class GradientDescent:
    """Gradient Descent implementation with visualization."""
    
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.cost_history = []
        self.parameter_history = []
    
    def fit(self, X, y, w_init=None, b_init=0):
        """Train using gradient descent."""
        if w_init is None:
            w = np.random.randn(X.shape[1]) * 0.1
        else:
            w = w_init.copy()
        b = b_init
        
        for i in range(self.iterations):
            cost = cost_function(w, b, X, y)
            self.cost_history.append(cost)
            self.parameter_history.append((w.copy(), b))
            
            dw, db = gradient(w, b, X, y)
            w -= self.learning_rate * dw
            b -= self.learning_rate * db
        
        return w, b

def visualize_2d(gd, X, y, w_final, b_final):
    """2D visualization of gradient descent."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Plot 1: Data and fitted line
    ax1.scatter(X[:, 0], y, alpha=0.5, label='Data')
    x_line = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
    y_line = w_final[0] * x_line + b_final
    ax1.plot(x_line, y_line, 'r-', linewidth=2, label='Fitted Line')
    ax1.set_xlabel('X')
    ax1.set_ylabel('y')
    ax1.set_title('Linear Regression Fit')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Cost function over iterations
    ax2.plot(gd.cost_history, 'b-', linewidth=2)
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel('Cost (MSE)')
    ax2.set_title('Cost Function Convergence')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def visualize_3d_animated(gd, X, y):
    """3D animated visualization of gradient descent."""
    # Create parameter space
    w_range = np.linspace(-2, 2, 50)
    b_range = np.linspace(-2, 2, 50)
    W, B = np.meshgrid(w_range, b_range)
    
    # Calculate cost surface
    Cost = np.zeros_like(W)
    for i in range(W.shape[0]):
        for j in range(W.shape[1]):
            w_temp = np.array([W[i, j]])
            Cost[i, j] = cost_function(w_temp, B[i, j], X, y)
    
    # Create figure
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot surface
    surf = ax.plot_surface(W, B, Cost, cmap='viridis', alpha=0.6)
    
    # Extract parameter history
    w_history = [p[0][0] for p in gd.parameter_history[::10]]  # Sample every 10th
    b_history = [p[1] for p in gd.parameter_history[::10]]
    cost_history = gd.cost_history[::10]
    
    # Initialize line for path
    line, = ax.plot([], [], [], 'r-', linewidth=3, label='Gradient Descent Path')
    point, = ax.plot([], [], [], 'ro', markersize=10)
    
    ax.set_xlabel('Weight (w)')
    ax.set_ylabel('Bias (b)')
    ax.set_zlabel('Cost')
    ax.set_title('Gradient Descent Animation')
    
    def animate(frame):
        if frame < len(w_history):
            w_vals = w_history[:frame+1]
            b_vals = b_history[:frame+1]
            c_vals = cost_history[:frame+1]
            
            line.set_data(w_vals, b_vals)
            line.set_3d_properties(c_vals)
            
            if len(w_vals) > 0:
                point.set_data([w_vals[-1]], [b_vals[-1]])
                point.set_3d_properties([c_vals[-1]])
        
        return line, point
    
    anim = animation.FuncAnimation(fig, animate, frames=len(w_history), 
                                   interval=100, blit=True, repeat=True)
    plt.show()
    return anim

def main():
    """Main function to run gradient descent visualizer."""
    print("Gradient Descent Visualizer")
    print("=" * 60)
    
    # Generate sample data
    np.random.seed(42)
    X = np.random.randn(100, 1) * 2
    y = 3 * X.flatten() + 2 + np.random.randn(100) * 0.5
    
    # Normalize X
    X = (X - X.mean()) / X.std()
    
    print(f"\nData shape: X={X.shape}, y={y.shape}")
    print(f"True relationship: y = 3x + 2 + noise")
    
    # Create and train
    gd = GradientDescent(learning_rate=0.1, iterations=100)
    w_final, b_final = gd.fit(X, y)
    
    print(f"\nFinal parameters:")
    print(f"  Weight (w): {w_final[0]:.4f}")
    print(f"  Bias (b): {b_final:.4f}")
    print(f"  Final cost: {gd.cost_history[-1]:.4f}")
    
    # Visualizations
    print("\nShowing 2D visualization...")
    visualize_2d(gd, X, y, w_final, b_final)
    
    print("\nShowing 3D animated visualization...")
    print("(Close the window to continue)")
    visualize_3d_animated(gd, X, y)

if __name__ == "__main__":
    main()

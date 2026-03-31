"""
Solution 01: Derivatives and Gradients

This is the reference solution for exercise_01.py
"""

import numpy as np
from scipy.misc import derivative


def compute_derivative(func, x, h=1e-6):
    """
    Compute the derivative of a function at a point.
    
    WHY: Derivatives tell us the direction to minimize loss
    HOW: Use the definition of derivative: (f(x+h) - f(x)) / h
    """
    return (func(x + h) - func(x)) / h


def compute_gradient(func, point):
    """
    Compute the gradient of a multivariable function.
    
    WHY: ML models have many parameters - need direction for each
    HOW: Gradient = vector of partial derivatives
    """
    h = 1e-6
    grad = np.zeros_like(point)
    
    for i in range(len(point)):
        # Create points for computing partial derivative
        point_plus = point.copy()
        point_plus[i] += h
        point_minus = point.copy()
        point_minus[i] -= h
        
        # Partial derivative: ∂f/∂x_i ≈ (f(x+h) - f(x-h)) / (2h)
        grad[i] = (func(point_plus) - func(point_minus)) / (2 * h)
    
    return grad


def gradient_descent_step(func, x, learning_rate=0.1):
    """
    Perform one step of gradient descent.
    
    WHY: Find optimal parameters that minimize loss
    HOW: Move in direction opposite to gradient
    """
    h = 1e-6
    # Compute gradient numerically
    grad = (func(x + h) - func(x - h)) / (2 * h)
    # Move in opposite direction
    return x - learning_rate * grad


# Test the solution
if __name__ == "__main__":
    print("Solution 01: Derivatives and Gradients")
    print("=" * 60)
    
    # Test 1: Derivative
    print("\n1. compute_derivative:")
    def f(x):
        return x**2 + 3*x + 2
    
    x0 = 2.0
    deriv = compute_derivative(f, x0)
    analytical = 2*x0 + 3
    print(f"   Function: f(x) = x² + 3x + 2")
    print(f"   At x = {x0}:")
    print(f"   Numerical derivative: {deriv:.4f}")
    print(f"   Analytical derivative: {analytical:.4f}")
    print(f"   Difference: {abs(deriv - analytical):.6f}")
    
    # Test 2: Gradient
    print("\n2. compute_gradient:")
    def multivariable_func(point):
        x, y = point
        return x**2 + y**2 + x*y
    
    point = np.array([1.0, 2.0])
    grad = compute_gradient(multivariable_func, point)
    print(f"   Function: f(x, y) = x² + y² + xy")
    print(f"   At point ({point[0]}, {point[1]}):")
    print(f"   Gradient: {grad}")
    print(f"   Explanation:")
    print(f"   - ∂f/∂x = 2x + y = {2*point[0] + point[1]:.2f}")
    print(f"   - ∂f/∂y = 2y + x = {2*point[1] + point[0]:.2f}")
    
    # Test 3: Gradient descent step
    print("\n3. gradient_descent_step:")
    def loss_func(x):
        return (x - 3)**2
    
    x = 5.0
    x_new = gradient_descent_step(loss_func, x, learning_rate=0.1)
    print(f"   Loss function: f(x) = (x - 3)² (minimum at x = 3)")
    print(f"   Starting at x = {x}")
    print(f"   After one step: x = {x_new:.4f}")
    print(f"   Moved closer to minimum: {abs(x_new - 3) < abs(x - 3)}")
    
    print("\n" + "=" * 60)
    print("✅ Solution verified!")

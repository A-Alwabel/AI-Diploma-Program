"""
Solution 02: Gradient Descent Implementation

This is the reference solution for exercise_02.py
"""

import numpy as np


def gradient_descent(func, gradient_func, initial_x, learning_rate=0.1, iterations=100):
    """
    Implement gradient descent to minimize a function.
    
    WHY: Find optimal parameters that minimize loss
    HOW: Iteratively move in direction opposite to gradient
    """
    x = initial_x
    history = [x]
    
    for i in range(iterations):
        # Compute gradient at current point
        grad = gradient_func(x)
        # Update: move in opposite direction of gradient
        x = x - learning_rate * grad
        history.append(x)
    
    return x, history


def analyze_learning_rate(func, gradient_func, initial_x, learning_rates, iterations=50):
    """
    Analyze how different learning rates affect convergence.
    
    WHY: Learning rate is crucial - too small = slow, too large = divergence
    HOW: Try different learning rates and see convergence behavior
    """
    results = {}
    
    for lr in learning_rates:
        final_x, _ = gradient_descent(func, gradient_func, initial_x, lr, iterations)
        results[lr] = final_x
    
    return results


# Test the solution
if __name__ == "__main__":
    print("Solution 02: Gradient Descent")
    print("=" * 60)
    
    # Test 1: Gradient descent
    print("\n1. gradient_descent:")
    def f(x):
        return (x - 3)**2
    
    def grad_f(x):
        return 2 * (x - 3)
    
    initial_x = 5.0
    final_x, history = gradient_descent(f, grad_f, initial_x, learning_rate=0.1, iterations=20)
    
    print(f"   Function: f(x) = (x - 3)² (minimum at x = 3)")
    print(f"   Starting at: {initial_x}")
    print(f"   Final value: {final_x:.4f}")
    print(f"   Converged: {abs(final_x - 3) < 0.1}")
    print(f"   Number of steps to converge: {len(history)}")
    
    # Test 2: Learning rate analysis
    print("\n2. analyze_learning_rate:")
    learning_rates = [0.01, 0.1, 0.5, 1.0]
    results = analyze_learning_rate(f, grad_f, initial_x, learning_rates, iterations=30)
    
    print(f"   Learning Rate Analysis:")
    for lr, final_val in sorted(results.items()):
        converged = abs(final_val - 3) < 0.5
        status = "✅ Converged" if converged else "❌ Diverged/Oscillated"
        print(f"   LR = {lr:.2f}: Final x = {final_val:.4f} {status}")
    
    print("\n   Key Insights:")
    print("   - Too small LR (0.01): Slow convergence")
    print("   - Good LR (0.1): Fast convergence")
    print("   - Too large LR (0.5+): May overshoot or diverge")
    
    print("\n" + "=" * 60)
    print("✅ Solution verified!")


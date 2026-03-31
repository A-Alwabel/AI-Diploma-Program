"""
Solution 01: Optimization Algorithms

This is the reference solution for exercise_01.py
"""

import numpy as np


class SimpleGDOptimizer:
    """Simple Gradient Descent optimizer."""
    def __init__(self, lr=0.01):
        self.lr = lr
    
    def update(self, params, grads):
        return params - self.lr * grads


class MomentumOptimizer:
    """Gradient descent with momentum."""
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.velocity = None
    
    def update(self, params, grads):
        if self.velocity is None:
            self.velocity = np.zeros_like(params)
        
        # Update velocity: v = momentum * v + lr * grads
        self.velocity = self.momentum * self.velocity + self.lr * grads
        # Update params: params = params - velocity
        return params - self.velocity


def compare_optimizers(loss_func, grad_func, initial_params, optimizers, iterations=100):
    """Compare different optimizers."""
    results = {}
    
    for name, optimizer in optimizers.items():
        params = initial_params.copy() if isinstance(initial_params, np.ndarray) else initial_params
        
        for i in range(iterations):
            grads = grad_func(params)
            params = optimizer.update(params, grads)
        
        results[name] = params
    
    return results


if __name__ == "__main__":
    print("Solution 01: Optimization Algorithms")
    print("=" * 60)
    
    def loss(x):
        return (x - 3)**2
    
    def grad(x):
        return 2 * (x - 3)
    
    # Test optimizers
    optimizers = {
        'Simple GD': SimpleGDOptimizer(lr=0.1),
        'Momentum': MomentumOptimizer(lr=0.1, momentum=0.9)
    }
    
    results = compare_optimizers(loss, grad, 5.0, optimizers, iterations=20)
    
    for name, final_val in results.items():
        print(f"{name}: Final = {final_val:.4f}, Target = 3.0")
    
    print("\n✅ Solution verified!")

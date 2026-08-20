# Complete Project Guide: 03 Gradient Descent Visualizer

---

## 🎯 Real-World Application

---

## 🚀 Quick Start (For Experienced Students)

> 💡 **New to this project?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.

## Step-by-Step Implementation

---

## 📚 Complete Tutorial (For Beginners)

> 💡 **Already familiar with this?** See [Quick Start](#-quick-start-for-experienced-students) section above.

### Step 1: Understand Gradient Descent (Day 1)

**What is Gradient Descent?**
An optimization algorithm that:
- Finds the minimum of a function
- Uses gradients (slopes) to move downhill
- Like finding the bottom of a valley by always going downhill

**Example:**
```
Function: f(x) = x²
Goal: Find x where f(x) is minimum
Start: x = 5, f(5) = 25
Step 1: Move downhill → x = 3, f(3) = 9
Step 2: Move downhill → x = 1, f(1) = 1
Step 3: Move downhill → x = 0, f(0) = 0 (minimum!)
```

---

### Step 2: Set Up Project (Day 1)

**Create structure:**
```
gradient_descent_visualizer/
├── gradient_descent.py
├── optimizers.py
├── visualizer.py
├── main.py
└── README.md
```

**Install:**
```bash
pip install numpy matplotlib
```

---

### Step 3: Implement Basic Gradient Descent (Day 2)

**File: `gradient_descent.py`**

```python
import numpy as np

class GradientDescent:
    """Basic gradient descent optimizer"""
    
    def __init__(self, learning_rate=0.01, max_iterations=1000):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.history = []  # Store path
    
    def gradient(self, x):
        """Calculate gradient of f(x) = x²"""
        return 2 * x
    
    def optimize_1d(self, start_x=5.0):
        """Optimize 1D function"""
        x = start_x
        self.history = [(x, x**2)]
        
        for i in range(self.max_iterations):
            # Calculate gradient
            grad = self.gradient(x)
            
            # Update position (move downhill)
            x = x - self.learning_rate * grad
            
            # Store history
            self.history.append((x, x**2))
            
            # Check convergence
            if abs(grad) < 1e-6:
                print(f"Converged at iteration {i}")
                break
        
        return x, self.history
    
    def optimize_2d(self, start_point, loss_function, gradient_function):
        """Optimize 2D function"""
        x, y = start_point
        self.history = [(x, y, loss_function(x, y))]
        
        for i in range(self.max_iterations):
            # Calculate gradient
            grad_x, grad_y = gradient_function(x, y)
            
            # Update position
            x = x - self.learning_rate * grad_x
            y = y - self.learning_rate * grad_y
            
            # Store history
            loss = loss_function(x, y)
            self.history.append((x, y, loss))
            
            # Check convergence
            if np.sqrt(grad_x**2 + grad_y**2) < 1e-6:
                print(f"Converged at iteration {i}")
                break
        
        return (x, y), self.history
```

---

### Step 4: Implement Different Optimizers (Day 3)

**File: `optimizers.py`**

```python
import numpy as np

class MomentumGradientDescent:
    """Gradient descent with momentum"""
    
    def __init__(self, learning_rate=0.01, momentum=0.9, max_iterations=1000):
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.max_iterations = max_iterations
        self.velocity = 0
        self.history = []
    
    def optimize_1d(self, start_x=5.0):
        """Optimize with momentum"""
        x = start_x
        self.velocity = 0
        self.history = [(x, x**2)]
        
        for i in range(self.max_iterations):
            grad = 2 * x
            
            # Update velocity (momentum)
            self.velocity = self.momentum * self.velocity - self.learning_rate * grad
            
            # Update position
            x = x + self.velocity
            
            self.history.append((x, x**2))
            
            if abs(grad) < 1e-6:
                break
        
        return x, self.history

class AdamOptimizer:
    """Adam optimizer (adaptive learning rate)"""
    
    def __init__(self, learning_rate=0.01, beta1=0.9, beta2=0.999, max_iterations=1000):
        self.learning_rate = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.max_iterations = max_iterations
        self.m = 0  # First moment
        self.v = 0  # Second moment
        self.history = []
    
    def optimize_1d(self, start_x=5.0):
        """Optimize with Adam"""
        x = start_x
        self.m = 0
        self.v = 0
        self.history = [(x, x**2)]
        
        for i in range(1, self.max_iterations + 1):
            grad = 2 * x
            
            # Update biased first moment
            self.m = self.beta1 * self.m + (1 - self.beta1) * grad
            
            # Update biased second moment
            self.v = self.beta2 * self.v + (1 - self.beta2) * grad**2
            
            # Bias correction
            m_hat = self.m / (1 - self.beta1**i)
            v_hat = self.v / (1 - self.beta2**i)
            
            # Update position
            x = x - self.learning_rate * m_hat / (np.sqrt(v_hat) + 1e-8)
            
            self.history.append((x, x**2))
            
            if abs(grad) < 1e-6:
                break
        
        return x, self.history
```

---

### Step 5: Create Visualizer (Day 4-5)

**File: `visualizer.py`**

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class GradientDescentVisualizer:
    """Visualize gradient descent process"""
    
    def plot_1d_optimization(self, optimizer_history, title="Gradient Descent"):
        """Plot 1D optimization path"""
        x_values = [h[0] for h in optimizer_history]
        y_values = [h[1] for h in optimizer_history]
        
        # Plot function
        x_range = np.linspace(min(x_values) - 1, max(x_values) + 1, 100)
        y_range = x_range**2
        
        plt.figure(figsize=(12, 6))
        plt.plot(x_range, y_range, 'b-', linewidth=2, label='f(x) = x²')
        
        # Plot path
        plt.plot(x_values, y_values, 'ro-', markersize=8, linewidth=2, label='Optimization Path')
        
        # Mark start and end
        plt.plot(x_values[0], y_values[0], 'go', markersize=15, label='Start')
        plt.plot(x_values[-1], y_values[-1], 'rs', markersize=15, label='End')
        
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(title)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'results/{title.replace(" ", "_")}.png', dpi=300)
        plt.close()
    
    def plot_2d_contour(self, loss_function, history, title="2D Gradient Descent"):
        """Plot 2D optimization on contour"""
        # Create grid
        x_range = np.linspace(-5, 5, 100)
        y_range = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x_range, y_range)
        Z = loss_function(X, Y)
        
        # Extract path
        x_path = [h[0] for h in history]
        y_path = [h[1] for h in history]
        
        plt.figure(figsize=(10, 8))
        
        # Plot contour
        contour = plt.contour(X, Y, Z, levels=20, alpha=0.6)
        plt.clabel(contour, inline=True, fontsize=8)
        
        # Plot path
        plt.plot(x_path, y_path, 'ro-', markersize=6, linewidth=2, label='Path')
        plt.plot(x_path[0], y_path[0], 'go', markersize=15, label='Start')
        plt.plot(x_path[-1], y_path[-1], 'rs', markersize=15, label='End')
        
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(title)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'results/{title.replace(" ", "_")}.png', dpi=300)
        plt.close()
    
    def plot_loss_history(self, histories, labels, title="Loss History"):
        """Compare loss histories of different optimizers"""
        plt.figure(figsize=(12, 6))
        
        for history, label in zip(histories, labels):
            losses = [h[1] if len(h) > 1 else h[0] for h in history]
            plt.plot(losses, label=label, linewidth=2)
        
        plt.xlabel('Iteration')
        plt.ylabel('Loss')
        plt.title(title)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.yscale('log')  # Log scale for better visualization
        plt.tight_layout()
        plt.savefig(f'results/{title.replace(" ", "_")}.png', dpi=300)
        plt.close()
    
    def plot_3d_surface(self, loss_function, history, title="3D Loss Surface"):
        """Plot 3D loss surface with path"""
        x_range = np.linspace(-5, 5, 50)
        y_range = np.linspace(-5, 5, 50)
        X, Y = np.meshgrid(x_range, y_range)
        Z = loss_function(X, Y)
        
        x_path = [h[0] for h in history]
        y_path = [h[1] for h in history]
        z_path = [loss_function(x, y) for x, y in zip(x_path, y_path)]
        
        fig = plt.figure(figsize=(14, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Plot surface
        ax.plot_surface(X, Y, Z, alpha=0.5, cmap='viridis')
        
        # Plot path
        ax.plot(x_path, y_path, z_path, 'ro-', markersize=8, linewidth=2, label='Path')
        
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('Loss')
        ax.set_title(title)
        plt.tight_layout()
        plt.savefig(f'results/{title.replace(" ", "_")}.png', dpi=300)
        plt.close()
```

---

### Step 6: Create Main Program (Day 6)

**File: `main.py`**

```python
import numpy as np
from gradient_descent import GradientDescent
from optimizers import MomentumGradientDescent, AdamOptimizer
from visualizer import GradientDescentVisualizer

def loss_function_2d(x, y):
    """Example 2D loss function"""
    return (x - 1)**2 + (y - 2)**2 + 0.5 * np.sin(2*x) * np.cos(2*y)

def gradient_2d(x, y):
    """Gradient of 2D loss function"""
    grad_x = 2*(x - 1) + np.cos(2*x) * np.cos(2*y)
    grad_y = 2*(y - 2) - np.sin(2*x) * np.sin(2*y)
    return grad_x, grad_y

def main():
    print("=" * 60)
    print("Gradient Descent Visualizer")
    print("=" * 60)
    
    viz = GradientDescentVisualizer()
    
    # Example 1: 1D optimization
    print("\n[Example 1] 1D Gradient Descent")
    gd = GradientDescent(learning_rate=0.1, max_iterations=50)
    x_opt, history = gd.optimize_1d(start_x=5.0)
    print(f"Optimal x: {x_opt:.6f}, f(x) = {x_opt**2:.6f}")
    viz.plot_1d_optimization(history, "1D Gradient Descent")
    
    # Example 2: Compare optimizers
    print("\n[Example 2] Compare Optimizers")
    gd = GradientDescent(learning_rate=0.1, max_iterations=50)
    momentum = MomentumGradientDescent(learning_rate=0.1, momentum=0.9, max_iterations=50)
    adam = AdamOptimizer(learning_rate=0.1, max_iterations=50)
    
    _, history_gd = gd.optimize_1d(5.0)
    _, history_momentum = momentum.optimize_1d(5.0)
    _, history_adam = adam.optimize_1d(5.0)
    
    viz.plot_loss_history(
        [history_gd, history_momentum, history_adam],
        ['Gradient Descent', 'Momentum', 'Adam'],
        "Optimizer Comparison"
    )
    
    # Example 3: 2D optimization
    print("\n[Example 3] 2D Gradient Descent")
    gd_2d = GradientDescent(learning_rate=0.1, max_iterations=100)
    (x_opt, y_opt), history_2d = gd_2d.optimize_2d(
        start_point=(4.0, 4.0),
        loss_function=loss_function_2d,
        gradient_function=gradient_2d
    )
    print(f"Optimal point: ({x_opt:.4f}, {y_opt:.4f})")
    print(f"Loss: {loss_function_2d(x_opt, y_opt):.6f}")
    
    viz.plot_2d_contour(loss_function_2d, history_2d, "2D Gradient Descent")
    viz.plot_3d_surface(loss_function_2d, history_2d, "3D Loss Surface")
    
    print("\n✅ Visualization complete!")

if __name__ == "__main__":
    main()
```

---

---
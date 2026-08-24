# Quiz 02: Calculus for Machine Learning

**Time Limit:** 45 minutes | **Marks:** 100 points

---

## Part 1: Derivatives Basics (25 points)

### Question 1 (5 points)
What is a derivative?
- A) The rate of change of a function with respect to a variable
- B) A function
- C) An integral
- D) A matrix

---

### Question 2 (5 points)
What does the derivative f'(x) represent geometrically?
- A) The area under the curve
- B) The x-intercept
- C) The y-intercept
- D) The slope of the tangent line at point x

---

### Question 3 (5 points)
What is the derivative of f(x) = x²?
- A) x
- B) 2x
- C) x²
- D) 2

---

### Question 4 (10 points)
Calculate the derivative of f(x) = 3x³ + 2x² - 5x + 1

f'(x) = d/dx(3x³) + d/dx(2x²) - d/dx(5x) + d/dx(1)
     = 3(3x²) + 2(2x) - 5(1) + 0
     = 9x² + 4x - 5

---

## Part 2: Gradients and Multivariable Calculus (30 points)

### Question 5 (5 points)
What is a gradient?
- A) A single number
- B) A matrix
- C) A vector of partial derivatives
- D) A function

---

### Question 6 (5 points)
What does the gradient point toward?
- A) The minimum of the function
- B) The maximum value
- C) The origin
- D) The direction of steepest ascent

---

### Question 7 (10 points)
For the function f(x, y) = x² + 2xy + y², calculate the gradient ∇f.

∂f/∂x = 2x + 2y
∂f/∂y = 2x + 2y

∇f = [2x + 2y, 2x + 2y]

---

### Question 8 (10 points)
What is the chain rule? Give an example of how it's used in neural networks.

**Chain Rule:**
- For composite functions: if z = f(g(x)), then dz/dx = (dz/dg) × (dg/dx)
- Allows computing derivatives of nested functions
- Essential for backpropagation in neural networks

**Neural Network Example:**
In a neural network:
- Input x → Hidden layer h = σ(W₁x + b₁) → Output y = W₂h + b₂
- To compute ∂y/∂x, use chain rule:
  - ∂y/∂x = (∂y/∂h) × (∂h/∂x)
  - ∂y/∂h = W₂
  - ∂h/∂x = σ'(W₁x + b₁) × W₁
  - Therefore: ∂y/∂x = W₂ × σ'(W₁x + b₁) × W₁

This is how backpropagation computes gradients through layers.

---

## Part 3: Gradient Descent (25 points)

### Question 9 (5 points)
What is gradient descent?
- A) A method to find the maximum of a function
- B) An optimization algorithm that finds the minimum by following the negative gradient
- C) A data structure
- D) A type of neural network

---

### Question 10 (5 points)
What is the learning rate in gradient descent?
- A) The speed of convergence
- B) The number of iterations
- C) The step size used when updating parameters
- D) The initial value

---

### Question 11 (5 points)
What happens if the learning rate is too large?
- A) The algorithm may overshoot and fail to converge
- B) Convergence is faster
- C) Nothing changes
- D) It always works

---

### Question 12 (10 points)
Write pseudocode for gradient descent algorithm:

```
1. Initialize parameters θ (e.g., randomly)
2. Set learning rate α
3. Repeat until convergence:
   a. Compute gradient: ∇θ = ∂J/∂θ
   b. Update parameters: θ = θ - α × ∇θ
   c. Check convergence (e.g., gradient magnitude < threshold)
4. Return optimal parameters θ
```

**Python-like pseudocode:**
```python
def gradient_descent(J, gradient_J, initial_theta, learning_rate, max_iterations):
    theta = initial_theta
    for i in range(max_iterations):
        grad = gradient_J(theta)
        theta = theta - learning_rate * grad
        if np.linalg.norm(grad) < threshold:
            break
    return theta
```

---

## Part 4: Applications (20 points)

### Question 13 (10 points)
Explain how calculus is used in machine learning. Give at least 3 examples.

**Applications:**

1. **Optimization:**
   - Gradient descent to minimize loss functions
   - Finding optimal model parameters
   - Used in training neural networks, linear regression, etc.

2. **Backpropagation:**
   - Chain rule to compute gradients through neural network layers
   - Enables training of deep networks
   - Efficient gradient computation

3. **Loss Function Minimization:**
   - Derivatives to find minimum of cost functions
   - Mean squared error, cross-entropy, etc.
   - Critical for model training

4. **Feature Engineering:**
   - Derivatives to understand feature importance
   - Sensitivity analysis
   - Understanding model behavior

5. **Regularization:**
   - Derivatives of penalty terms (L1, L2)
   - Gradient-based optimization with constraints
   - Preventing overfitting

---

### Question 14 (10 points)
What is the relationship between gradients and optimization in machine learning?

**Relationship:**

1. **Gradients Guide Optimization:**
   - Gradient points in direction of steepest ascent
   - Negative gradient points toward minimum
   - Used to update parameters iteratively

2. **Loss Function Minimization:**
   - Goal: Minimize J(θ) where θ are model parameters
   - Gradient ∇J(θ) shows how to change θ to reduce loss
   - Update: θ_new = θ_old - α∇J(θ)

3. **Convergence:**
   - When gradient ≈ 0, we're at a critical point (minimum/maximum/saddle)
   - Gradient magnitude indicates how far from optimum
   - Used as convergence criterion

4. **Efficiency:**
   - Gradients computed efficiently using automatic differentiation
   - Enables training of large models
   - Backpropagation uses chain rule for efficiency

5. **Challenges:**
   - Local minima vs global minima
   - Saddle points
   - Learning rate selection
   - Gradient vanishing/exploding in deep networks

**Example:**
In linear regression: J(θ) = (1/2m)Σ(y - θᵀx)²
- Gradient: ∇J(θ) = -(1/m)Σ(y - θᵀx)x
- Update: θ = θ - α∇J(θ)
- Iteratively moves toward optimal θ that minimizes J

---

## Grading Rubric

- **90-100 points:** Excellent understanding
- **80-89 points:** Good understanding
- **70-79 points:** Satisfactory
- **60-69 points:** Needs improvement
- **Below 60:** Review required

---

**Created:** 2025  
**For:** 113 AIAT - Mathematics and Probabilities for Machine Learning

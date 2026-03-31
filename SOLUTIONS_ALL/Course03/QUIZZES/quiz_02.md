# Module 02 Quiz: Calculus for Machine Learning

**Instructions**: Answer the following questions. Check your answers with the solutions provided.

## Part 1: Conceptual Questions

### Question 1
**Why are derivatives important in machine learning?**
- [ ] A) They make code faster
- [ ] B) They tell us which direction to adjust parameters to minimize loss
- [ ] C) They are required by Python
- [ ] D) They are optional

**Answer**: B

**Explanation**: Derivatives tell us the direction to minimize loss functions, which is how ML models learn.

---

### Question 2
**What is a gradient?**
- [ ] A) A single number
- [ ] B) A vector of partial derivatives
- [ ] C) A matrix
- [ ] D) A function

**Answer**: B

**Explanation**: A gradient is a vector containing partial derivatives with respect to each parameter.

---

### Question 3
**What does the chain rule enable in neural networks?**
- [ ] A) Faster computation
- [ ] B) Backpropagation (computing gradients through layers)
- [ ] C) Data storage
- [ ] D) Random operations

**Answer**: B

**Explanation**: The chain rule allows us to compute gradients through multiple layers, which is backpropagation.

---

### Question 4
**In gradient descent, why do we move in the opposite direction of the gradient?**
- [ ] A) It's faster
- [ ] B) The gradient points in direction of steepest increase, we want decrease
- [ ] C) It's required
- [ ] D) Random choice

**Answer**: B

**Explanation**: Gradient points toward steepest increase. To minimize, we move opposite (steepest decrease).

---

### Question 5
**What happens if the learning rate is too large?**
- [ ] A) Training is faster
- [ ] B) May overshoot or diverge
- [ ] C) Training is slower
- [ ] D) Nothing

**Answer**: B

**Explanation**: Too large learning rate can cause the algorithm to overshoot the minimum or diverge.

---

## Part 2: Code Understanding

### Question 6
**What does this gradient descent step do?**
```python
x = x - learning_rate * gradient
```

- [ ] A) Moves in direction of gradient
- [ ] B) Moves opposite to gradient (toward minimum)
- [ ] C) Multiplies by gradient
- [ ] D) Divides by gradient

**Answer**: B

**Explanation**: Subtracting `learning_rate * gradient` moves opposite to gradient, toward the minimum.

---

### Question 7
**For a function f(x, y), how many partial derivatives does the gradient have?**
- [ ] A) 0
- [ ] B) 1
- [ ] C) 2 (one for x, one for y)
- [ ] D) Infinite

**Answer**: C

**Explanation**: Gradient has one partial derivative for each variable: [∂f/∂x, ∂f/∂y].

---

## Part 3: Application Questions

### Question 8
**Which module will use the gradients you learned here?**
- [ ] A) Module 01
- [ ] B) Module 03 (Optimization)
- [ ] C) Module 04
- [ ] D) Module 05

**Answer**: B

**Explanation**: Module 03 uses gradients from Module 02 for optimization algorithms.

---

### Question 9
**What is backpropagation?**
- [ ] A) Forward pass through network
- [ ] B) Chain rule applied to compute gradients through layers
- [ ] C) Data storage
- [ ] D) Random operation

**Answer**: B

**Explanation**: Backpropagation is the chain rule applied to neural networks to compute gradients.

---

### Question 10
**Why do we need gradients for ML?**
- [ ] A) They're optional
- [ ] B) They enable model training through optimization
- [ ] C) They make code faster
- [ ] D) They're only for neural networks

**Answer**: B

**Explanation**: Gradients enable optimization, which is how all ML models learn from data.

---

## Scoring

- **9-10 correct**: Excellent! You understand calculus for ML.
- **7-8 correct**: Good! Review the concepts you missed.
- **5-6 correct**: Review the module and try again.
- **Below 5**: Study the module more carefully before proceeding.

---

## Next Steps

After completing this quiz:
1. Review any questions you got wrong
2. Complete the exercises in `exercises/`
3. Move to Module 03 when ready


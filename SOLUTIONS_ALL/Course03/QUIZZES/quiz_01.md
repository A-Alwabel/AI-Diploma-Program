# Module 01 Quiz: Linear Algebra for Machine Learning

**Instructions**: Answer the following questions. Check your answers with the solutions provided.

## Part 1: Conceptual Questions

### Question 1
**Why are vectors and matrices fundamental to machine learning?**
- [ ] A) They make code run faster
- [ ] B) All ML data is represented as vectors/matrices
- [ ] C) They are required by Python
- [ ] D) They are optional

**Answer**: B

**Explanation**: All data in ML is represented as vectors (single data points) or matrices (multiple data points). This is the fundamental data structure.

---

### Question 2
**What does matrix multiplication represent in neural networks?**
- [ ] A) Data storage
- [ ] B) Data transformation through layers
- [ ] C) Data deletion
- [ ] D) Data copying

**Answer**: B

**Explanation**: Matrix multiplication transforms data as it flows through neural network layers. Each layer applies a transformation matrix.

---

### Question 3
**What are eigenvalues and eigenvectors used for in ML?**
- [ ] A) Data storage
- [ ] B) Principal Component Analysis (PCA)
- [ ] C) Data deletion
- [ ] D) Random operations

**Answer**: B

**Explanation**: Eigenvalues and eigenvectors are the mathematical foundation of PCA, which finds the most important directions in data.

---

### Question 4
**In a data matrix, what does each row represent?**
- [ ] A) A feature
- [ ] B) A data point (sample)
- [ ] C) A label
- [ ] D) An error

**Answer**: B

**Explanation**: In ML, each row = one data point (sample), each column = one feature.

---

### Question 5
**What is the dot product used for in neural networks?**
- [ ] A) Data storage
- [ ] B) Computing weighted sums of inputs
- [ ] C) Data deletion
- [ ] D) Random operations

**Answer**: B

**Explanation**: The dot product computes weighted sums, which is how neural network layers combine inputs with weights.

---

## Part 2: Code Understanding

### Question 6
**What does this code do?**
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = A @ B
```

- [ ] A) Adds matrices A and B
- [ ] B) Multiplies matrices A and B
- [ ] C) Subtracts B from A
- [ ] D) Divides A by B

**Answer**: B

**Explanation**: `@` is the matrix multiplication operator in NumPy.

---

### Question 7
**What does `matrix.T` do?**
- [ ] A) Deletes the matrix
- [ ] B) Transposes the matrix (rows become columns)
- [ ] C) Multiplies by 2
- [ ] D) Nothing

**Answer**: B

**Explanation**: `.T` computes the transpose, swapping rows and columns.

---

## Part 3: Application Questions

### Question 8
**If you have 1000 data points with 50 features, what shape is your data matrix?**
- [ ] A) (50, 1000)
- [ ] B) (1000, 50)
- [ ] C) (1000, 1000)
- [ ] D) (50, 50)

**Answer**: B

**Explanation**: Shape is (samples, features) = (1000, 50).

---

### Question 9
**Which module will use eigenvalues/eigenvectors from this module?**
- [ ] A) Module 02
- [ ] B) Module 03
- [ ] C) Module 04 (PCA)
- [ ] D) Module 05

**Answer**: C

**Explanation**: Module 04 (Dimensionality Reduction) uses eigenvalues/eigenvectors for PCA.

---

### Question 10
**Why is linear algebra the foundation of ML?**
- [ ] A) It's easy to learn
- [ ] B) All ML operations use linear algebra
- [ ] C) It's optional
- [ ] D) It's only for neural networks

**Answer**: B

**Explanation**: Every ML algorithm uses linear algebra operations - it's the mathematical foundation.

---

## Scoring

- **9-10 correct**: Excellent! You understand linear algebra fundamentals.
- **7-8 correct**: Good! Review the concepts you missed.
- **5-6 correct**: Review the module and try again.
- **Below 5**: Study the module more carefully before proceeding.

---

## Next Steps

After completing this quiz:
1. Review any questions you got wrong
2. Complete the exercises in `exercises/`
3. Move to Module 02 when ready


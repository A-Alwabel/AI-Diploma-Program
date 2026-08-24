# Quiz 01: Linear Algebra for Machine Learning

**Time Limit:** 45 minutes | **Marks:** 100 points

---

## Part 1: Vectors and Matrices Basics (25 points)

### Question 1 (5 points)
What is a vector in the context of machine learning?
- A) A single number
- B) An ordered collection of numbers (1D array)
- C) A 2D array
- D) A function

---

### Question 2 (5 points)
What is a matrix?
- A) A single number
- B) A 1D array
- C) A 2D array of numbers arranged in rows and columns
- D) A function

---

### Question 3 (5 points)
What is the shape of a matrix with 3 rows and 4 columns?
- A) (4, 3)
- B) (3, 4)
- C) (12,)
- D) (3, 3)

---

### Question 4 (10 points)
Write NumPy code to:
1. Create a vector [1, 2, 3, 4, 5]
2. Create a 2x3 matrix with values 1-6
3. Get the shape of both

```python
import numpy as np

# Create vector
vector = np.array([1, 2, 3, 4, 5])
print(f"Vector: {vector}")
print(f"Vector shape: {vector.shape}")

# Create matrix
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Matrix:\n{matrix}")
print(f"Matrix shape: {matrix.shape}")
```

---

## Part 2: Matrix Operations (30 points)

### Question 5 (5 points)
What is matrix addition?
- A) Adding corresponding elements
- B) Multiplying elements
- C) Concatenating matrices
- D) Transposing matrices

---

### Question 6 (5 points)
When can two matrices be multiplied?
- A) Always
- B) When they have the same shape
- C) When number of columns in first equals number of rows in second
- D) When they are square matrices

---

### Question 7 (10 points)
What is the result of matrix multiplication A × B where:
```
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]
```

Show your calculation.

---

### Question 8 (10 points)
Write NumPy code to:
1. Create two 2x2 matrices A and B
2. Perform matrix multiplication
3. Perform element-wise multiplication
4. Calculate the transpose of A

```python
import numpy as np

# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
C = np.dot(A, B)  # or A @ B
print(f"Matrix multiplication:\n{C}")

# Element-wise multiplication
D = A * B
print(f"Element-wise multiplication:\n{D}")

# Transpose
A_transpose = A.T
print(f"Transpose of A:\n{A_transpose}")
```

---

## Part 3: Eigenvalues and Eigenvectors (25 points)

### Question 9 (5 points)
What is an eigenvalue?
- A) A vector
- B) A scalar that represents how a vector is scaled by a transformation
- C) A matrix
- D) A function

---

### Question 10 (5 points)
What is an eigenvector?
- A) A vector that changes direction under transformation
- B) A vector that doesn't change direction under transformation
- C) A scalar
- D) A matrix

---

### Question 11 (5 points)
Why are eigenvalues and eigenvectors important in machine learning?
- A) They make calculations faster
- B) They help in dimensionality reduction (PCA) and understanding transformations
- C) They reduce memory usage
- D) They improve accuracy

---

### Question 12 (10 points)
Write NumPy code to find eigenvalues and eigenvectors of a matrix:

```python
import numpy as np

# Create a matrix
A = np.array([[4, 2], [1, 3]])

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}")
```

---

## Part 4: Applications (20 points)

### Question 13 (10 points)
Explain how linear algebra is used in machine learning. Give at least 3 examples.

**Applications:**

1. **Data Representation:**
   - Data points as vectors
   - Datasets as matrices
   - Features as columns, samples as rows

2. **Linear Regression:**
   - Model: y = Xw + b (matrix form)
   - Solution: w = (X^T X)^(-1) X^T y
   - Uses matrix operations for predictions

3. **Dimensionality Reduction (PCA):**
   - Uses eigenvalues/eigenvectors
   - Finds principal components
   - Reduces feature space

4. **Neural Networks:**
   - Weight matrices for layers
   - Matrix multiplication for forward propagation
   - Efficient computation

5. **Image Processing:**
   - Images as matrices
   - Transformations using matrix operations
   - Convolution operations

---

### Question 14 (10 points)
What is the dot product? How is it used in machine learning?

**Dot Product:**
- Sum of element-wise products of two vectors
- Formula: a · b = Σ(a_i × b_i)
- Result is a scalar

**Properties:**
- Measures similarity between vectors
- Related to cosine similarity
- Used in distance calculations

**ML Applications:**
1. **Similarity Measures:** Compare feature vectors
2. **Linear Models:** y = w · x + b (dot product of weights and features)
3. **Neural Networks:** Each neuron computes dot product of inputs and weights
4. **Kernel Methods:** Many kernels use dot products
5. **Recommendation Systems:** User-item similarity

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

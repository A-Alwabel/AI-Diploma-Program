"""
Solution 01: Vector and Matrix Operations

This is the reference solution for exercise_01.py
"""

import numpy as np


def create_data_matrix(samples, features):
    """
    Create a data matrix representing ML data.
    
    In ML, data is organized as a matrix where:
    - Each row = one data point (sample)
    - Each column = one feature
    """
    return np.random.randn(samples, features)


def compute_dot_product(v1, v2):
    """
    Compute the dot product of two vectors.
    
    The dot product is used in neural networks for weighted sums.
    """
    return np.dot(v1, v2)
    # Alternative: return v1 @ v2


def matrix_multiplication(A, B):
    """
    Perform matrix multiplication.
    
    This is the core operation in neural network layers.
    """
    return np.dot(A, B)
    # Alternative: return A @ B


def compute_transpose(matrix):
    """
    Compute the transpose of a matrix.
    
    Transpose is used when computing gradients in ML.
    """
    return matrix.T
    # Alternative: return np.transpose(matrix)


# Test the solution
if __name__ == "__main__":
    print("Solution 01: Vector and Matrix Operations")
    print("=" * 60)
    
    # Test 1: Create data matrix
    print("\n1. create_data_matrix:")
    data = create_data_matrix(5, 3)
    print(f"   Created matrix shape: {data.shape}")
    print(f"   Matrix:\n{data}")
    
    # Test 2: Dot product
    print("\n2. compute_dot_product:")
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    result = compute_dot_product(v1, v2)
    print(f"   v1: {v1}")
    print(f"   v2: {v2}")
    print(f"   Dot product: {result}")
    print(f"   Explanation: (1×4) + (2×5) + (3×6) = {result}")
    
    # Test 3: Matrix multiplication
    print("\n3. matrix_multiplication:")
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    result = matrix_multiplication(A, B)
    print(f"   A:\n{A}")
    print(f"   B:\n{B}")
    print(f"   A @ B:\n{result}")
    print(f"   Explanation:")
    print(f"   - First row: [1×5+2×7, 1×6+2×8] = [{result[0,0]}, {result[0,1]}]")
    print(f"   - Second row: [3×5+4×7, 3×6+4×8] = [{result[1,0]}, {result[1,1]}]")
    
    # Test 4: Transpose
    print("\n4. compute_transpose:")
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    result = compute_transpose(matrix)
    print(f"   Original:\n{matrix}")
    print(f"   Shape: {matrix.shape}")
    print(f"   Transposed:\n{result}")
    print(f"   Shape: {result.shape}")
    print(f"   Explanation: Rows become columns, columns become rows")
    
    print("\n" + "=" * 60)
    print("✅ Solution verified!")

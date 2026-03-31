"""
Solution 02: Matrix Properties and Operations

This is the reference solution for exercise_02.py
"""

import numpy as np


def compute_determinant(matrix):
    """
    Compute the determinant of a square matrix.
    
    The determinant tells us if a transformation is invertible.
    """
    return np.linalg.det(matrix)


def compute_matrix_inverse(matrix):
    """
    Compute the inverse of a matrix.
    
    Matrix inverse is used in solving linear systems and some ML algorithms.
    """
    return np.linalg.inv(matrix)


def compute_eigenvalues_eigenvectors(matrix):
    """
    Compute eigenvalues and eigenvectors of a matrix.
    
    This is crucial for PCA (Module 04) and understanding data transformations.
    """
    eigenvals, eigenvecs = np.linalg.eig(matrix)
    return eigenvals, eigenvecs


def verify_inverse(matrix, inverse):
    """
    Verify that a matrix and its inverse multiply to identity.
    """
    identity = np.eye(matrix.shape[0])
    result = matrix @ inverse
    return np.allclose(result, identity)


# Test the solution
if __name__ == "__main__":
    print("Solution 02: Matrix Properties")
    print("=" * 60)
    
    # Test 1: Determinant
    print("\n1. compute_determinant:")
    matrix = np.array([[1, 2], [3, 4]])
    det = compute_determinant(matrix)
    print(f"   Matrix:\n{matrix}")
    print(f"   Determinant: {det:.2f}")
    print(f"   Explanation: det = ad - bc = (1×4) - (2×3) = {det:.2f}")
    print(f"   Meaning: {'Invertible' if det != 0 else 'Not invertible'}")
    
    # Test 2: Matrix inverse
    print("\n2. compute_matrix_inverse:")
    inv = compute_matrix_inverse(matrix)
    print(f"   Original matrix:\n{matrix}")
    print(f"   Inverse:\n{inv}")
    
    # Test 3: Verify inverse
    print("\n3. verify_inverse:")
    is_valid = verify_inverse(matrix, inv)
    print(f"   Matrix @ Inverse:\n{matrix @ inv}")
    print(f"   Is identity: {is_valid}")
    
    # Test 4: Eigenvalues and eigenvectors
    print("\n4. compute_eigenvalues_eigenvectors:")
    matrix = np.array([[2, 1], [1, 2]])
    eigenvals, eigenvecs = compute_eigenvalues_eigenvectors(matrix)
    print(f"   Matrix:\n{matrix}")
    print(f"   Eigenvalues: {eigenvals}")
    print(f"   Eigenvectors:\n{eigenvecs}")
    print(f"   Explanation:")
    print(f"   - Eigenvalues show how much variance in each direction")
    print(f"   - Eigenvectors show the directions of maximum variance")
    print(f"   - This is used in PCA (Module 04)!")
    
    print("\n" + "=" * 60)
    print("✅ Solution verified!")


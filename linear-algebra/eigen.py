# With Numpy

import numpy as np

# Step 2: Define the Matrix
A = np.array([[4, 3],
              [2, 1]])

# Step 3: Compute Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
determinant = np.linalg.det(A)

# Step 4: Display Results
print("Determinant:")
print(determinant)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)


# Without numpy


"""
Matrix Operations
"""

def scalar_multiplication(scalar, matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            matrix[row][column] *= scalar
    return matrix


def matrix_addition(matrixA, matrixB):
    """
    Only for square matrices
    """
    for row in range(len(matrixA)):
        for column in range(len(matrixA[0])):
            matrixA[row][column] += matrixB[row][column]
    return matrixA


def matrix_multiplication(matrixA, matrixB):
    """
    Only for square matrices
    """
    for row in range(len(matrixA)):
        for column in range(len(matrixA[0])):
            matrixA[row][column] *= matrixB[row][column]
    return matrixA


def find_order_of_matrix(matrix):
    print(f"order of matrix is {len(matrix)} x {len(matrix[0])}")

# Example matrices 
matrixA = [[1,1,1],
           [1,1,1],
           [1,1,1]]

matrixB = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matrix = [[1,2,3],
           [4,5,6],
           [7,8,9]]

scalar = 2

result_for_scalar_multiplication = scalar_multiplication(scalar=scalar, matrix=matrix)
result_for_matrix_addition = matrix_addition(matrixA=matrixA, matrixB=matrixB)
result_for_matrix_multiplication = matrix_multiplication(matrixA=matrixA, matrixB=matrix)

# print the result
for row in result_for_matrix_multiplication:
    print(row)


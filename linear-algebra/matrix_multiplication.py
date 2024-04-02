def matrix_multiply(A, B):
    """
    Performs matrix multiplication of matrices A and B.
    """
    # Get the dimensions of matrices A and B
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Check if the matrices can be multiplied
    if cols_A != rows_B:
        raise ValueError("Number of columns in matrix A must be equal to the number of rows in matrix B")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    # Perform matrix multiplication
    for i in range(rows_A):
        print("\n")
        print("i: ",i)
        for j in range(cols_B):
            print("\tj: ",j)
            for k in range(cols_A):
                print("\t\tk: ",k)
                print(f"\t\t\t A == {A[i][k]}, B == {B[k][j]}")
                result[i][j] += A[i][k] * B[k][j]
            print("\n Result currently: " ,result, "\n")

    return result

# Example matrices A and B
A = [[2, 4, 6],
     [3, 4, 5]]

B = [[1, 2],
     [3, 8],
     [5, 12]]

# Multiply matrices A and B
result = matrix_multiply(A, B)

# Print the result
for row in result:
    print(row)

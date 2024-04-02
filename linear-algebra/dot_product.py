def dot_product(vectorA, vectorB):
    """
    Note: input must always be vectors
    """
    if len(vectorA) != len(vectorB):
        raise ValueError("Vectors should have same length")
    
    result = 0
    for i in range(len(vectorA)):
        result += vectorA[i] * vectorB[i]
    return result

vecA = [1,2,3]
vecB = [2,4,6]

print(dot_product(vectorA=vecA, vectorB=vecB))
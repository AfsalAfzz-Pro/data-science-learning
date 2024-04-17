import numpy as np

# an np array with 2 axes, axis 1: len == 3 and axis 2: len == 5
array = np.array([[1,2,3,4,5], 
                  [6,7,8,9,10],
                  [11,12,13,14,15]])
# print(array[0][:2]) # slicing
# print(array)
print()


# an np array wiith zeroes
array1 = np.zeros((5, 5))
# print(array1)
print()


# an np array with oness
array2 = np.ones((5,5), dtype=np.int64)
# print(array2)
print()


# an np arrray which is empty
array3 = np.empty((5,5))
# print(array3)
print()


# np one-dimensiona array with a range
array4 = np.arange(4, 10)
# print(array4)
print()
array4a = np.arange(2, 9, 2)
# print(array4a)
print()


# np array with evenly spaced elements
array5 = np.linspace(0, 10, 5)
# print(array5)


# sorting an np array
array6 = [10,5,9,7,8,6,3,1,2]
array6a = np.sort(array6)
# print(array6a)
print()


# concatenating np arrays
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.concatenate((a, b))
# print(c)
print()


x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
z = np.concatenate((x, y), axis=0)
# print(z)

data = np.array([2,4,6,8])
to_add = np.array([2,2,2,2])
result = np.add(data, to_add)
print(result)

# finding eigen values and eigen vectors
print(np.linalg.eig(x))

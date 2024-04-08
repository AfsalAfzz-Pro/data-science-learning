import math
"""
program to find mean
"""

matrix = [[12, 0.27],
          [13, 0.25],
          [14, 0.18],
          [15, 0.15],
          [16, 0.15]]

for row in matrix:
    print(row)

mean_list = []
for row in range(len(matrix)):
    mean = 1
    for column in range(len(matrix[0])):
        mean *= matrix[row][column]
    mean_list.append(mean)

# mean for individual rows
print(mean_list)

# final mean
meanU = sum(mean_list)
print("\nMean: ", meanU)





"""
program to find variance and standard deviation
"""
x_sqr_list = []
for row in range(len(matrix)):
    x_sqr = matrix[row][0]**2
    x_sqr_list.append(x_sqr)
# print()
# print(x_sqr_list)

p_of_x = []
for i in range(len(matrix)):
    mean = matrix[i][1]
    p_of_x.append(mean)
# print(p_of_x)

product_list = []
for i in range(len(x_sqr_list)):
    product = x_sqr_list[i] * p_of_x[i]
    product_list.append(product)
# print(product_list)

sigma_sqr = sum(product_list) - meanU**2
print("\nVariance: ",sigma_sqr)

standard_deviation = math.sqrt(sigma_sqr)
print("\nstandard_deviation", standard_deviation)




""" 
program to find median
"""
x = []
for i in range(len(matrix)):
    mean = matrix[i][0]
    x.append(mean)

x = [4,5,16,32,64,128]
n = len(x)
if n % 2 != 0:
    median = x[n//2]
else:
    # print(n//2)    
    # print((n-1)//2)    
    median = (x[n//2] + x[(n-1)//2])/2
    print("\nmedian: ",median)


"""
program to find mode
"""
array = [1,1,1,4,4,4,4,5,5,5,6,6,6,6,6]
frequency = {}
for num in array:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
# print(frequency)

greatest = 0

for k, v in frequency.items():
    # print(f"key: {k}, value: {v}, greatest: {greatest}")
    if v > greatest:
        key = k
        greatest = v
        # print(greatest)

print("\nMode: ", key)
print()


"""mean again"""

arr = [85, 90, 75, 92, 88, 79, 83, 95, 87, 91, 78, 86, 89, 94, 82, 80, 84, 93, 88, 81]
mean = sum(arr)/len(arr)
print("new mean: ", mean)

"""variance again"""
variance = sum([(x-mean)**2 for x in arr])/len(arr)

print("variance: ", variance)

std_dev = math.sqrt(variance)
print("std_dev: ",std_dev)
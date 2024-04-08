import numpy as np
import math

# Example data: Height (in inches) and Weight (in pounds)
height = [65, 68, 70, 61, 72]
weight = [150, 170, 175, 140, 180]
weight.reverse()

# Calculate covariance
covariance = np.cov(height, weight)[0][1]

# Calculate correlation
correlation = np.corrcoef(height, weight)[0][1]

print("Covariance between Height and Weight:", covariance)
print("Correlation between Height and Weight:", correlation)


print()
print("height: ", height)
print("weight: ",weight)


# checking mean
meanH = sum(height)/len(height)
meanW = sum(weight)/len(weight)
# print(meanH)
# print(meanW)

if len(height) == len(weight):
    length = len(height)

mean_list = []
for i in range(length):
    x = height[i] - meanH
    y = weight[i] - meanW
    m = x * y
    mean_list.append(m)

print()
print(mean_list)

cov = sum(mean_list)/length
print("\ncovariance: ",cov)

varH = sum([(x-meanH)**2 for x in height])/length
varW = sum([(x-meanW)**2 for x in weight])/length

std_H = math.sqrt(varH)
std_W = math.sqrt(varW)

corr = cov/(std_H*std_W)
print("correlation: ", corr)



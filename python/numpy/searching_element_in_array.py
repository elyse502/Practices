# Searchinng for an Element in an Array
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr == 4)
print(x)

# Find the indexes where the values are even
x = np.where(arr % 2 == 0)
print(x)

# Find the indexes where the values are odd
x = np.where(arr % 2 == 1)
print(x)

# Splitting an Array
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = np.array_split(arr, 2)
print(newarr)
print()

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)
print()

arr = np.array([1, 2, 3, 4, 5, 6, 7])
newarr = np.array_split(arr, 3)
print(newarr)
print()

arr = np.array([1, 2, 3, 4, 5, 6, 7])
newarr = np.array_split(arr, 4)
print(newarr)

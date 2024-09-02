# Joining Two Arrays
import numpy as np

# Join two arrays 1D
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)
# Order matters
arr = np.concatenate((arr2, arr1))
print(arr)
print()

# Join two arrays 2D
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=0)
print(arr)
print()
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)


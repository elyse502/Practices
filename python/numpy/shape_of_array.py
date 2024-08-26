# Finding Shape of an Array
import numpy as np

# Matrix -> Order -> rowsize X colsize
# 1D array
arr = np.array([1, 2, 3, 4, 5])
print(arr.shape)
print()

# 2D array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr.shape)
print()

# 3D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr.shape)

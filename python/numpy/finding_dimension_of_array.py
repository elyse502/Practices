import numpy as np

# 1D array
b = np.array([1, 2, 3])
print(b)
print("Dimension of array: ", b.ndim)  # dimension of array(arrayName.ndim)
print()

# 2D array
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print("Dimension of array: ", a.ndim)  # dimension of array(arrayName.ndim)
print()

# 3D array
c = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(c)
print("Dimension of array: ", c.ndim)

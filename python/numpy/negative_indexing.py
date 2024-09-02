import numpy as np

# 1D array
a = np.array([1,2,3,4,5])
print(a[-1])  # a[4] = a[-1] = 5
print(a[-2])  # a[3] = a[-2] = 4
print()

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b[-1])
print(b[-2])
print()

# 2D array
c = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(c[1,-1])

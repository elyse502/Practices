import numpy as np

# Iterating 1D array
arr = np.array([1, 2, 3, 4, 5])
for x in arr:
    print(x)
print()

# Iterating 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(y)


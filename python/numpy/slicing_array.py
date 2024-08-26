import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])  # [2 3 4 5]
print(arr[1:5:])  # [2 3 4 5]
print(arr[4:])  # [5 6 7]
print(arr[:4])  # [1 2 3 4]
print(arr[-3:-1])  # [4 5]
print()

# step size
print(arr[1:5:2])  # [2 4]
print(arr[1:5:3])  # [2]

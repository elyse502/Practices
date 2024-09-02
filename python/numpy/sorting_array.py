# Sorting an Array
import numpy as np

arr = np.array([3, 2, 0, 1])
arr = np.sort(arr)
print(arr)
print()

arr = np.array([3, 2, 0, 1])
arr = np.sort(arr)[::-1]
print(arr)
print()

arr = np.array([3, 2, 0, 1])
arr.sort()
print(arr)
print()

arr = np.array([3, 2, 0, 1])
arr.sort()
print(arr[::-1])
print()

# String Sorting
arr = np.array(["banana", "cherry", "apple"])
arr.sort()
print(arr)
print(np.sort(arr))
print()

arr = np.array(["banana", "cherry", "apple"])
arr.sort()
print(arr[::-1])
print(np.sort(arr)[::-1])
print()

# 2D Array Sorting
arr = np.array([[3, 2, 1], [7, 6, 5]])
print(np.sort(arr))

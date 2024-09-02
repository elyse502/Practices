# Filtering an Array by using a boolean index list
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
x = [True, False, True, False, True, True, False]
newarr = arr[x]
print(newarr)

# Working with series in Pandas along with Numpy
import pandas as pd
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 100])
print(arr)
print()

s = pd.Series(arr)
print(s)
print()

t = np.sqrt(s)
print(t)
print()

# Create a series with custom index using numpy array
index = np.array(['a', 'b', 'c', 'd', 'e'])
arr1 = np.array([10, 20, 30, 40, 50])

s1 = pd.Series(arr1, index=index)
print(s1)

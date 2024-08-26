import numpy as np

a = np.array([1, 2, 3, 4, 5])
x = a.copy()

print("Original array a: ", a)
print("Copied array x: ", x)
print()

# change in x will not reflect in a
x[0] = 10
print("After changing x: ", x)
print("After changing a: ", a)
print()


b = np.array([[1, 2, 3], [4, 5, 6]])
y = b.copy()

print("Original array b: ", b)
print("Copied array y: ", y)
print()

# change in y will not reflect in b
y[0][0] = 10
print("After changing y: ", y)
print("After changing b: ", b)

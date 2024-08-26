import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a.dtype)

b = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
print(b.dtype)

c = np.array([1, 2, 3, 4, 5], dtype="i4")
print(c.dtype)

d = np.array([1, 2, 3, 4, 5], dtype="f")
print(d.dtype)

e = np.array([1, 2, 3, 4, 5], dtype="U")
print(e.dtype)

f = np.array([1, 2, 3, 4, 5], dtype="S")
print(f.dtype)

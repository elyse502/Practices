# Tutorial 38-Python Matrix Implementation

# a is 2-D matrix with integers
a = [['Roy', 80, 75, 85, 90, 95],
     ['John', 75, 80, 75, 85, 100],
     ['Dave', 80, 80, 80, 90, 95]]

# b is a nested list but not a matrix
b = [['Roy', 80, 75, 85, 90, 95],
     ['John', 75, 80, 75],
     ['Dave', 80, 80, 80, 90, 95]]

print(a)
print()
print(b)


# Creating a dynamic matrix using for loop in python
n = 3
m = 4
a = [0] * n
print(a)
for i in range(n):
    a[i] = [0] * m
print(a)

# Accessing elements from a matrix
print(a)
print(a[0])
print(a[0][1])
print(a[1][2])

# Negative Indexing
print(a)
print(a[-1])
print(a[-1][-2])
print(a[-2][-3])

# Change elements of a matrix in python
print(a)
b=a[0]
print(b)

b[1]=75
print(b)
print(a)

a[2]=['Sam',82,79,88,97,99]
print(a)
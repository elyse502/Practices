# Tutorial 7-Python Tuples

# Creating an empty tuple
tuple1 = ()
print(tuple1)


# Creating tuples with integer elements
tuple2 = (1, 2, 3)
print(tuple2)


# tuple with mixed datatypes
tuple3 = (101, "Anirban", 20000.00, "HR Dept")
print(tuple3)


# Creation of nested tuple
tuple4 = ("points", [1, 4, 3], (7, 8, 6))
print(tuple4)


# tuple can be created without any parenthesis
# also called tuple packing
tuple5 = 101, "Anirban", 20000.00, "HR Dept"
print(tuple5)


# tuple unpacking is also possible
empid, empname, empsal, empdept = tuple5
print(empid)
print(empname)
print(empsal)
print(empdept)

print(type(tuple5))


# accessing elements in a tuple
tuple1 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
print(tuple1)
print(tuple1[1])
print(tuple1[3])
print(tuple1[5])


# nested tuple
nest_tuple2 = ("point", [1, 3, 4], (8, 7, 9))
print(nest_tuple2)
print(nest_tuple2[0][3])
print(nest_tuple2[1][2])
print(nest_tuple2[2][2])


# slicing tuple contents
tuple1 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')

print(tuple1[1:3])

print(tuple1[:-3])

print(tuple1[3:])

print(tuple1[:])


# tuple elements are immutable
tuple1 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
print(tuple1)
# tuple1[2] = 'x'   # error


# tuples can be reassigned
tuple1 =('g', 'o', 'o', 'd', 'b', 'y', 'e')
print(tuple1)


# concatenation of tuples
tuple2 = ('w', 'e', 'l')
tuple3 = ('c', 'o', 'm', 'e')
print(tuple2)
print(tuple3)
print(tuple2 + tuple3)

print(("again",) * 4)


# deletion operation on a tuple
tuple4 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')

# as immutable so elements can not be deleted
# del tuple4[2]

# but can delete entire tuple
del tuple4
# print(tuple4) # NameError: name 'tuple4' is not defined


# tuple methods
tuple5 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
print(tuple5.count('e'))
print(tuple5.index('c'))


# tuple operations
tuple6 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
print(tuple6)

# membership
print('c' in tuple6)
print('c' not in tuple6)
print('a' in tuple6)
print('a' not in tuple6)


# iteration through tuple elements
tuple6 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
for letters in tuple6:
    print("letter is -> ", letters)


# built-in functions with tuple
tuple7 = (22, 33, 55, 44, 77, 66, 11)
print(tuple7)

print(max(tuple7))
print(min(tuple7))
print(sorted(tuple7))
print(len(tuple7))

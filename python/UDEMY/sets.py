# Tutorial 8-Python sets

# creating sets
# set of integers
my_set1 = {11, 33, 66, 55, 44, 22}
print(my_set1)


# set of mixed datatypes
my_set2 = {101, "Agnibha", (21, 2, 1994)}
print(my_set2)


# duplicate values are not allowed
my_set3 = {11, 22, 33, 33, 44, 22}
print(my_set3)


# set cannot have mutable items
# my_set4 = {1, 2, [3, 4]}


# we can make set from a list
my_set5 = set([1, 2, 3, 2])
print(my_set5)
print(type(my_set5))


# we can make list from a set
my_list1 = list({11, 22, 33, 44})
print(my_list1)
print(type(my_list1))


# operatios on sets
my_set1 = {11, 33, 44, 66, 55}
print(my_set1)

# 'set' object does not support indexing

# my_set1[0]

# add an element to a set
my_set1.add(77)
print(my_set1)

# add multiple elements to a set
my_set1.update([88, 99, 22])
print(my_set1)

# add list and set
my_set1.update([100, 102], {103, 104, 105})
print(my_set1)

# remove and discard
# initialize my_set
my_set1 = {11, 33, 44, 55, 66}
print(my_set1)

# discard an element which is not present, no error
my_set1.discard(4)
print(my_set1)

# remove an element which is not present, error raised
# my_set1.remove(6)
print(my_set1)

# discard an element
my_set1.discard(44)
print(my_set1)
my_set1.remove(55)
print(my_set1)

# using pop
# initialize my_set
my_set1 = {11, 33, 44, 55, 66}
print(my_set1)

# pop an element
print(my_set1.pop())

# pop another element
print(my_set1.pop())
print(my_set1)

# clear my_set
my_set1.clear()
print(my_set1)

# set operations - union
myset1 = {0, 1, 2, 3, 4, 5}
myset2 = {4, 5, 6, 7, 8, 9}
print(myset1)
print(myset2)


# use | operator for union
print(myset1 | myset2)
print(myset2 | myset1)
print(myset1.union(myset2))
print(myset2.union(myset1))


# set operations - intersection
myset1 = {0, 1, 2, 3, 4, 5}
myset2 = {4, 5, 6, 7, 8, 9}
print(myset1)
print(myset2)

# use & operator for intersection
print(myset1 & myset2)
print(myset2 & myset1)
print(myset1.intersection(myset2))
print(myset2.intersection(myset1))


# set operations - set difference
myset1 = {0, 1, 2, 3, 4, 5}
myset2 = {4, 5, 6, 7, 8, 9}
print(myset1)
print(myset2)

# use - operator for set difference
print(myset1 - myset2)
print(myset2 - myset1)
print(myset1.difference(myset2))
print(myset2.difference(myset1))


# set operations - symmetric difference
myset1 = {0, 1, 2, 3, 4, 5}
myset2 = {4, 5, 6, 7, 8, 9}
print(myset1)
print(myset2)

# use ^ operator for symmetric difference
print(myset1 ^ myset2)
print(myset2 ^ myset1)
print(myset1.symmetric_difference(myset2))
print(myset2.symmetric_difference(myset1))


# set membership
myset1 = {0, 1, 2, 3, 4, 5}
print(2 in myset1)
print(6 in myset1)
print(2 not in myset1)
print(6 not in myset1)


# iterating through a set
for letter in set("welcome"):
    print(letter)


# built-in functions with set
myset1 = {0, 1, 2, 3, 4, 5}
print(len(myset1))
print(max(myset1))
print(min(myset1))
print(sum(myset1))
print(sorted(myset1))


# python frozenset
# Frozenset is a new class that has the characteristics
# of a set, but its elements cannot be changed once assigned.
# while tuples are immutable lists, frozensets are immutable sets.
# initialize A and B
myset1 = frozenset([1, 2, 3, 4])
myset2 = frozenset([3, 4, 5, 6])
print(myset1)
print(myset2)
print(myset1.difference(myset2))
print(myset1.union(myset2))
print(myset1.intersection(myset2))
print(myset1.symmetric_difference(myset2))
# myset1.add(10)

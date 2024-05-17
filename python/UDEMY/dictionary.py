# Tutorial 11- Python Dictionary
new_dict = {1:"Hello", 2:"Hi", 3:"Hola"}
print(new_dict)
print(new_dict[1])
# print(new_dict[10]) # KeyError: 10
print(new_dict.get(2))
print(new_dict.get(20)) # None


# Updating value
new_dict[1] = "Hey"
print(new_dict)


# Adding value
new_dict[4] = "Namaste"
print(new_dict)


# Creating a new dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares)


# remove a particular item
print(squares.pop(4))
print(squares)


# remove an arbitrary item
print(squares.popitem())
print(squares)


# delete a particular item
del squares[1]

print(squares)


# Creating a new dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares)


# remove all items
squares.clear()


# Output: {}
print(squares)


# delete the dictionary itself
del squares


# Throws Error as the dictionary has been deleted
# print(squares) # NameError: name 'squares' is not defined


#  Creating a ne dictionary using Comprenhension
squares = {x: x*x for x in range(6)}
print(squares)


# Dictionary Membership test
squares = {1:1, 3:9, 5:25, 7:49, 9:81}

print(1 in squares)

print(2 not in squares)

# membership tests for key only not value
print(49 in squares)


# Iterating through a dictionary
squares = {1:1, 3:9, 5:25, 7:49, 9:81}
for i in squares:
    print(squares[i])


# Using built-in functions in a dictionary
squares = {1:1, 3:9, 5:25, 7:49, 9:81}

print(len(squares)) # Prints the length of the dictionary

print(sorted(squares)) # Prints the dictionary in sorted order
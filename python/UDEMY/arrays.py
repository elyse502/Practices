# Tutorial 5-Python Array Implementation

# Defining and declaring an array
arr = [10, 20, 30, 40, 50]
print(arr)

# Accessing array elements
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1])  # Negative Indexing
print(arr[-2])  # Negative Indexing


brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
print(brands)

# Finding the length of the array
num_brands = len(brands)
print(num_brands)

# Adding an element to an array using append()
brands.append("Intel")
print(brands)


# Removing elements from an array
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
print(colors)

del colors[4]
print(colors)

colors.remove("blue")
print(colors)

colors.pop(3)
print(colors)


# Modifying elements of an array using indexing
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits)

fruits[1] = "Pinapple"
print(fruits)

fruits[-1] = "Guava"
print(fruits)


# Concatenating two arrays using + operator
concat = [1, 2, 3]
print(concat)

concat + [4, 5, 6]
print(concat)

concat = concat + [4, 5, 6]
print(concat)


# Repeating element in an array
repeat = ["a"]
print(repeat)

repeat = repeat * 5
print(repeat)


# Slicing an array
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits)
print(fruits[1:4])
print(fruits[ : 3])
print(fruits[-4:])
print(fruits[-3:-1])


# Declaring and defining multi-dimensional arrays
multd = [[1,2], [3,4], [5,6], [7,8]]
print(multd)
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])
# Tutorial 19-Python Iterations Using for

# Printing all the elements present in a set
a = [1, 2, 3, 4, 5]
for i in a:
    print(i, end="")
    print(" Hello")


# Using range in for loop
for i in range(6, 11, 2):
    print(i)


# Using for loop for printing the values present in the
# tuple and using the else command in the for loop
b = (11, 12, 13, 14, 15)
for i in b:
    print(i)
else:
    print("Printing Completed!")
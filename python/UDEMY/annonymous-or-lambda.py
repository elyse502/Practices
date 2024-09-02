# Tutorial 44-Python Lamda Function

a = lambda x:x*2
            # In python, anonymous function is a function that is defined without a name.
            # It is defined by lambda.

print("Double of 10 is", a(10))
print()


# Making a new list by taking only the even numbers from the old list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
            # filter function is called with all the items in the list and a new list 
            # is returned which contains items for which the function evaluates to True.
# Output: [4, 6, 8, 12]
print(new_list)
print()


# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x*2, my_list))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)
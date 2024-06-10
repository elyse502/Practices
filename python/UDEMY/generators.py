# Tutorial 34-Python Generators

# A simple generator function
def my_generator():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

a = my_generator()
# Iterrating using next
next(a)
next(a)
next(a)

print("Using for loop...")
# Iterating using for
for item in my_generator():
    print(item)


# Generatiors with a loop
def reverse_string(my_string):
    length = len(my_string)
    for i in range(length - 1, -1, -1):
        yield my_string[i]

# For loop to reverse the string
for char in reverse_string("WORLD"):
    print(char)
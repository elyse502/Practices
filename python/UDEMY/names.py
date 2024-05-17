# Name (also called identifier) is simply a name given to objects.

# We can get the address (in RAM) of some object through the built-infunction, id().
# Note: You may get different value of id

a = 2
# Output: id(2) = 10919424
print('id(2) =', id(2))

# Output: id(a) = 10919424
print('id(a) =', id(a))

a = 2
# Output: id(a) = 10919424
print('id(a) =', id(a))

a = a+1
# Output: id(a) = 10919456
print('id(a) =', id(a))

# Output: id(3) = 10919456
print('id(3) =', id(3))

b = 2
# Output: id(b) = 10919424
print('id(2) =', id(2))
print('id(b) =', id(b))


# Scope
def outer_function():
    global a
    a= 20

    def inner_function():
        global a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

a = 10
print('a =', a)
outer_function()
print('a =', a)
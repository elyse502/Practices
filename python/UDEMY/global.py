# Tutorial 16-Python global local nonlocal

# Global and local variable with different name
x = "global"    # Global variable can be accessed from anywhere in the program

def funct1():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

print("Global x = ", x)
funct1()
print("Global x = ", x)


# Global and local variable with same name
a = 5

def funct2():
    a = 10  # Local variables are accessed from the block where it is defined only
    print("local a:", a)

print("global a:", a)
funct2()
print("global a:", a)

# Creating and using a Non-local variable

def outer():
    x = "local"

    def inner():
        # nonlocal x  # Nonlocal variable are used in nested function
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
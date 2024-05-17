# Tutorial 23-Python Functions

def hello1():   # Function without a return statement
    print("Hello! I love to code in Python.")

def hello2():   # Function with a return statement
    return "Hello! I love to code in Python."
    # Return commands returns back the control to the caller.
    # Mainly used to return a value to the caller of the function.

hello1()
print(hello2())


def myAddition(x, y):
    print("Performing the addirion operation...")
    return x + y
def mySubtraction(x, y):
    print("Performing the subtraction operation...")
    return x - y
def myMultiplication(x, y):
    print("Performing the multiplication operation...")
    return x * y
def myDivision(x, y):
    print("Performing the division operation...")
    return x / y
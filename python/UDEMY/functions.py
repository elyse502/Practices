# Tutorial 23-Python Functions

def hello1():   # Function without a return statement
    print("Hello! I love to code in Python.")

def hello2():   # Function with a return statement
    """
    This is 
    a multiline 
    text"""
    return "Hello! I love to code in Python."
    # Return commands returns back the control to the caller.
    # Mainly used to return a value to the caller of the function.

hello1()
print(hello2())
print(hello2.__doc__)


def myAddition(x, y):
    print("Performing the addition operation...")
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
def myMenu():
    print("Main Menu...")
    print("1 > Addition operation...")
    print("2 > Subtraction operation...")
    print("3 > Multiplication operation...")
    print("4 > Division operation...")
    choice = int(input("Please enter your option number..."))
    return choice
def calculation():
    ch = myMenu()
    num1 = int(input("Please enter the first number..."))
    num2 = int(input("Please enter the second number..."))
    if ch == 1:
        result = myAddition(num1, num2)
    elif ch == 2:
        result = mySubtraction(num1, num2)
    elif ch == 3:
        result = myMultiplication(num1, num2)
    elif ch == 4:
        result = myDivision(num1, num2)
    print("So result = ", result)

calculation()
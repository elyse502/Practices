# Tutorial 26-Python Errors And Exceptions

try:
    """
    The code which can give rise to an exception is written here
    """
    # a = "hi"   # This will give rise to an exception
    a = "100"
    b = int(a)
    print("I am here...")
    print("b = ",b)
except:
    print("Exception caught!")


# Catching specific exception
try:
    a = 5
    b = 0
    c = a/b
except ZeroDivisionError:
    print("Division by zero is not possible")


# Exceptions can be raised also
try:
    raise TypeError
except TypeError:
    print("TypeError Exception caught!")


# try..finally
try:
    print("In try block")
    raise TypeError
except:
    print("In except block")
finally:
    print("In finally block")
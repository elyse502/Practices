#!/usr/bin/python3

# Factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the factorial function
if __name__ == "__main__":
    num = 5
    print(f">> The factorial of {num} is {factorial(num)}")
    # Test with a larger number
    num = 10
    print(f">> The factorial of {num} is {factorial(num)}")
    # Test with a negative number
    num = -5
    try:
        print(f">> The factorial of {num} is {factorial(num)}")
    except RecursionError:
        print(f">> RecursionError: Factorial of negative number {num} is not defined.")
    # Test with zero
    num = 0
    print(f">> The factorial of {num} is {factorial(num)}")
    # Test with one
    num = 1
    print(f">> The factorial of {num} is {factorial(num)}")
    # Test with a large number
    num = 1000
    try:
        print(f">> The factorial of {num} is {factorial(num)}")
    except RecursionError:
        print(f">> RecursionError: Factorial of large number {num} caused a recursion error.")

#!/usr/bin/python3
# Factorial of a number using recursion
def factorial(n):
    """Less efficient recursive function. 
    With O(2^n) time complexity."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Using Memoization or Dynamic Programming to optimize the recursive factorial function
def memoize(func):
    """More efficient recursive function 
    using memoization. With O(n) time complexity."""
    memo = {}
    def helper(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]
    return helper    

# Test the factorial function
if __name__ == "__main__":
    print("\n{:^94}\n".format("- Testing the factorial function:"))
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

    # Test with memoization
    print("\n{}\n\n\n{:^94}\n".format("="*94, "- Testing with memoization:"))
    num = 5
    memoized_factorial = memoize(factorial)
    print(f">> The memoized factorial of {num} is {memoized_factorial(num)}")
    # Test with a larger number using memoization
    num = 10
    print(f">> The memoized factorial of {num} is {memoized_factorial(num)}")
    # Test with a negative number using memoization
    num = -5
    try:
        print(f">> The memoized factorial of {num} is {memoized_factorial(num)}")
    except RecursionError:
        print(f">> RecursionError: Memoized factorial of negative number {num} is not defined.")
    # Test with zero using memoization
    num = 0
    print(f">> The memoized factorial of {num} is {memoized_factorial(num)}")
    # Test with one using memoization
    num = 1
    print(f">> The memoized factorial of {num} is {memoized_factorial(num)}")
    # Test with a large number using memoization
    num = 1000
    try:
        print(f">> The memoized factorial of {num} is {memoized_factorial(num)}")
    except RecursionError:
        print(f">> RecursionError: Memoized factorial of large number {num} caused a recursion error.")

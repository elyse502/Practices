# Tutorial 41-Python Recursion

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

print("Factorial of 5 is", fact(5))
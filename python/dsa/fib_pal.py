#!/usr/bin/python3

title = "PYTHON CLASS"
print("{:_^24}".format(title), end="\n\n")

""" FIBONACCI """
n = 10
a, b = 0, 1

print(a, b, end=" ")

for i in range(n - 2):
    c = a + b
    print(c, end=" ")
    
    a = b
    b = c
# Fibonacci Function
def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1

    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]

print(f"\n>> {fibonacci(40)}")
   
""" SWAPPING TWO NUMS """ 
x = 10
y = 20
print(f"\n\n>> Before swap: {x=} {y=}")
x, y = y, x
print(f">> After swap: {x=} {y=}", end="\n\n")

""" ARGS & KWARGS """
def summation(*nums):
    return sum(nums)
    
print(f"SUM = {summation(1, 2, 3, 4)}")

def personDetails(**info):
    for key, value in info.items():
        print(">> {}: {}".format(key, value))
    
personDetails(name="Elysee", age=24)
print()

""" PALINDROME """
def isPalindrome(string):
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    
    if string == reversed_string:
        print(f">> {string} is Palindrome.")
    else:
        print(f">> {string} is not Palindrome.")
        
isPalindrome("reviver")

def is_palindrome(number):
    originalNumber = number
    reversedNumber = 0
    
    if number < 0:
        return False
    while number > 0:
        lastDigit = number % 10
        reversedNumber = reversedNumber * 10 + lastDigit
        number //= 10
    if originalNumber == reversedNumber:
        print(f">> {originalNumber} is Palindrome.")
    else:
        print(f">> {originalNumber} is not Palindrome.")

is_palindrome(1221)

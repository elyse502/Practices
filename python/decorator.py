#!/usr/bin/python3
"""Basic Decorator"""
title = "BASIC DECORATOR"
print(f"{title:_^46}\n")
def my_decorator(func):
    def wrapper():
        print(">> Before the Function!")
        func()
        print(">> After the Function!")
    return wrapper
    
@my_decorator
def say_hello():
    print(">> Hello!")

say_hello()
print("\n______________________________________________\n")

title = "DECORATOR WITH ARGUMENTS"
print(f"{title:_^46}\n")
def greet_decorator(func):
    def wrapper(name):
        print(">> Welcome!")
        func(name)
        print(">> Have a nice day!")
    return wrapper
    
@greet_decorator
def greet(name):
    print(f">> Hello, {name}.")
    
greet("Elysee NIYIBIZI")
print("\n______________________________________________\n")

title = "LOGGING WITH DECORATORS"
print(f"{title:_^46}\n")
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f">> Function '{func.__name__}' called with arguments {args}")
        result = func(*args, **kwargs)
        print(f">> Function '{func.__name__}' returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 5)



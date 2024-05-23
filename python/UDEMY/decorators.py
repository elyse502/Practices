# Tutorial 35-Python Decorators

# Demonstration
def make_decorated(func):
    def inner_function():
        print("I got decorated")
        func()
    return inner_function

@make_decorated
def simple_func():
    print("I am a simple function")

#decor = make_decorated(simple_func)
#decor()

simple_func()


# Another example
def my_smart_div(func):
    def inner_func(x, y):
        print("I am dividing ", x, " and ", y)
        if y == 0:
            print("Oops! Division by ZERO is illegal...!!!")
            return
        
        return func(x, y)
    return inner_func

@my_smart_div
def go_divide(a, b):    # Generally, we decorate a function and reassign it as, 
    return a / b        # go_divide = my_smart_div(go_divide)

print(go_divide(20, 2))
print(go_divide(20, 0))
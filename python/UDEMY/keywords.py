# Tutorial 6-Python Keywords And Identifiers

# True False
print(5 == 5)
print(5 > 5)


# None
print(None == 0)
print(None == False)
print(None == [])
print(None == None)


def a_void_function():
    a = 1
    b = 2
    c = a + b
    # return (c)

x = a_void_function()
print(x)


# and, or, not
print(True and False)
print(True or False)
print(not False)

print(True and True)
print(True or True)
print(not True)


# as
import math as myMath
print(myMath.cos(myMath.pi))


# assert
# assert 5 > 5 # AssertionError
assert 5 > 4
assert 5 == 5


# break
for i in range(1, 11):
    if i == 5:
        break
    print(i)


# continue
for i in range(1, 8):
    if i == 5:
        continue
    print(i)


# class
class ExampleClass:
    def function1(parameters):
        print("function1() executing...")

    def function2(parameters):
        print("function2() executing...")


ob1 = ExampleClass()
ob1.function1()
ob1.function2()


# def
def function_name(parameters):
    pass
function_name(10)


# del
a = 10
print(a)
del a
# print(a) # NameError: name 'a' is not defined


# if...elif...else
num = 4
if num == 1:
    print('One')
elif num == 2:
    print('Two')
elif num == 3:
    print('Three')
else:
    print('Something else')


# try...raise...catch...finally
try:
    x = 9
    # raise ZeroDivisionError
except ZeroDivisionError:
    print("Division cannot be performed")
finally:
    print("Execution Successfully")


# for
for i in range(1, 10, 1):
    print(i)


# frrom..import
import math
from math import cos
print(cos(10))


# global
globvar = 10
def read1():
    print(globvar)
def write1():
    global globvar
    globvar = 5
def write2():
    globvar = 15
read1()
write1()
read1()
write2()
read1()


# in
a = [1, 2, 3, 4]
print(4 in a)
print(44 in a)
print(44 not in a)


# is
print(True is True)


# lambda
a = lambda x: x*2
for i in range(1, 6):
    print(i, a(i))


# nonlocal
def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("Inner function: ", a)
    inner_function()
    print("Outer function: ", a)

outer_function()


# pass
def function(args):
    pass
function(10)


# return
def func_return():
    a = 10
    return a
print(func_return())


# while
i = 5
while i > 0:
    print(i)
    i -= 1


# with
with open('example.txt', 'w') as my_file:
    my_file.write('Hello World!\n')


# yield
def generator():
    for i in range(6):
        yield i*i

g = generator()
for i in g:
    print(i)

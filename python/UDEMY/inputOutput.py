# Tutorial 42-Python Input, Output And Import

# print function and it's usage
print('This sentence is output to the screen')
# Output: This sentence is output to the screen

a = 5

print('The value of a is', a)
# Output: The value of a is 5

print(1,2,3,4)
# Output: 1 2 3 4

print(1,2,3,4, sep='*')
# Output: 1*2*3*4

print(1,2,3,4, sep='#', end='&')
# Output: 1#2#3#4&
print()

print('I love {} and {}'.format('bread','butter'))
print('I love {0} and {1}'.format('bread','butter'))
# Output: I love bread and butter

print('I love {1} and {0}'.format('bread','butter'))
# Output: I love butter and bread
print()


# input
x = input('Please enter any number : ')
print(x)
y = int(input('Please enter any number : '))
print(y)
print(int(x) + y)
print()


# Importing module
import math     # mainly done at the top of the program
x = 100
print(math.pow(int(x), 2))
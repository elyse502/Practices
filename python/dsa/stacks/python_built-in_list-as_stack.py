#!/usr/bin/python3

my_stack = []

my_stack.append(1)
my_stack.append(2)
my_stack.append(3)
my_stack.append(4)
my_stack.append(5)

print(">> Stack before popping:", my_stack)

if len(my_stack) > 0:
    popped_item = my_stack.pop()
    print(">> Popped item:", popped_item)
    print(">> Stack after popping:", my_stack)
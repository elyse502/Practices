#!/usr/bin/python3

my_set = {1, 2, 3}
print(">> Original set:", my_set)
print()
my_set.add(4)  # Adding an element
print(">> After adding 4:", my_set)
print()
my_set.remove(2)  # Removing an element
print(">> After removing 2:", my_set)
print()
my_set.discard(3)  # Discarding an element (does not raise an error if not found)
# Note: The remove method raises a KeyError if the element is not found
my_set.discard(5)  # Discarding an element that doesn't exist
print(">> After discarding 3:", my_set)
print()
print(">> Is 4 in the set?", 4 in my_set)  # Checking if an element is in the set
print()
print(">> Is set empty?", not my_set)
print()
my_set.clear()  # Clearing the set
print(">> After clearing the set:", my_set)
print()
print(">> Is set empty?", not my_set)

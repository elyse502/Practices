#!/usr/bin/python3

# Example 1: Creating a set with no duplicate elements
unique_numbers = {1, 2, 3, 4, 5}
print(">> Unique Numbers:", unique_numbers)
print()

# Example 2: Using set() constructor to create a set
programming_languages = set(["Python", "Java", "C++"])
programming_languages.add("JavaScript")  # Adding an element to the set
"""
programming_languages.remove("Java")  # Removing an element from the set
# The discard method does not raise an error if the element is not found
programming_languages.discard("C#")  # Discarding an element that doesn't exist
"""
print(">> Programming Languages:", programming_languages)
print()

# Example 3: Creating an empty set
empty_set = set()
print(">> Empty Set:", empty_set)
print()

# Example 4: Creating an immutable set (frozenset)
immutable_set = frozenset([10, 20, 30])
# Note: You cannot modify a frozenset after it's created
# immutable_set.add(40)  # This will raise an AttributeError
# immutable_set.remove(20)  # This will also raise an AttributeError
print(">> Immutable Set (frozenset):", immutable_set)

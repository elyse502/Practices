#!/usr/bin/python3
# Example usage
numbers = [38, 27, 43, 3, 9, 82, 10]
print(f"- Original array:", numbers)
numbers.sort()
print("\n>> Sorted array:", numbers)

# Sorting a list of strings
print("\n\n", "-" * 80, "\n\n\n{:_^80}".format("List of strings example:"))
arr_str = ["Zucchini", "Banana", "Apple", "Pineapple", "Orange", "Grape"]
print(f"\n- Original array: {arr_str}")
arr_str.sort()
print(f"\n>> Sorted array: {arr_str}")

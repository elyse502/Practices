#!/usr/bin/python3
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    # Ensure the array is sorted
    arr.sort()  # Sort the array if not already sorted
    print(f"\n- Sorted array: {arr}")
    
    # Binary search algorithm
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found in the array

# Example usage
array = [10, 2, 7, 5, 3, 1, 4, 9, 8, 6]
print(f"\n- Array: {array}")

# Searching for different targets
targeted_lement = 7
result = binary_search(array, targeted_lement)
print(f"\n>> Target {targeted_lement} found at index {result}.")
targeted_lement = 11
result = binary_search(array, targeted_lement)
print(f"\n>> Target {targeted_lement} found at index {result}.")

# List of strings example
print("\n\n", "-" * 80, "\n\n\n{:_^80}".format("List of strings example:"))
array = ["Zion", "Jane", "Passy", "Nolan", "Ange", "Eric", "Zachary", "Marry", "Peter", "Naomi", "Logan"]
print(f"\n- Array: {array}\n")

# Searching for different targets
targeted_lement = "Marry"
result = binary_search(array, targeted_lement)
print()
print(dict(enumerate(array)))
print("\n- Names with respective index:")
for idx, name in enumerate(array):
    print(f"\t\t\t{idx}. {name}")
print(f"\n>> Target '{targeted_lement}' found at index {result}.")
targeted_lement = "John"
result = binary_search(array, targeted_lement) 
print(f"\n>> Target '{targeted_lement}' found at index {result}.")

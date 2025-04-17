#!/usr/bin/python3
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            # Target found, return the index
            return i
    # Target not found in the array
    return -1

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    target = 3
    result = linear_search(arr, target)
    print(f">> Target {target} found at index {result}.")
    target = 6
    result = linear_search(arr, target)
    print(f">> Target {target} found at index {result}.")

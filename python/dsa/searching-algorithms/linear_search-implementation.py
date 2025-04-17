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
    # List of integers example
    arr = [10, 2, 7, 5, 3, 1, 4]
    print(f"Array: {arr}")

    # Searching for different targets
    target = 3
    result = linear_search(arr, target)
    print(f"\n>> Target {target} found at index {result}.")
    target = 6
    result = linear_search(arr, target)
    print(f">> Target {target} found at index {result}.")

    # List of strings example
    print("\n\n", "-" * 80, "\n\n\n{:_^80}".format("List of strings example:"))
    arr = ["Eric", "Passy", "Ange", "Jane", "Peter", "Marry"]
    print(f"\nArray: {arr}")

    # Searching for different targets
    target = "Jane"
    result = linear_search(arr, target)
    print(list(enumerate(arr)))
    print("\n- Names with respective index:")
    for idx, name in enumerate(arr):
        print(f"\t\t\t{idx}. {name}")
    print(f"\n>> Target {target} found at index {result}.")
    target = "John"
    result = linear_search(arr, target)
    print(f">> Target {target} found at index {result}.")

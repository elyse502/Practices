#!/usr/bin/python3
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break
    
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"- Array: {arr}")
sorted_arr = bubble_sort(arr)
print(f"\n>> Sorted array: {sorted_arr}")

# Bubble sort on a list of strings
print("\n\n", "-" * 80, "\n\n\n{:_^80}".format("List of strings example:"))
arr_str = ["Zucchini", "Banana", "Apple", "Pineapple", "Orange", "Grape"]
print(f"\n- Array: {arr_str}")
sorted_arr_str = bubble_sort(arr_str)
print(f"\n>> Sorted array: {sorted_arr_str}")

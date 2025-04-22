#!/usr/bin/python3
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_element = arr[i]

        j = i - 1
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current_element

    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"- Array: {arr}")
sorted_arr = insertion_sort(arr)
print(f"\n>> Sorted array: {sorted_arr}")

# Insertion sort on a list of strings
print("\n\n", "-" * 80, "\n\n\n{:_^80}".format("List of strings example:"))
arr_str = ["Zucchini", "Banana", "Apple", "Pineapple", "Orange", "Grape"]
print(f"\n- Array: {arr_str}")
sorted_arr_str = insertion_sort(arr_str)
print(f"\n>> Sorted array: {sorted_arr_str}")

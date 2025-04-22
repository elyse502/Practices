#!/usr/bin/python3
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"- Array: {arr}")
sorted_arr = selection_sort(arr)
print(f"\n>> Sorted array: {sorted_arr}")

# Selection sort on a list of strings
print("\n\n", "-" * 80, "\n\n\n{:_^80}".format("List of strings example:"))
arr_str = ["Zucchini", "Banana", "Apple", "Pineapple", "Orange", "Grape"]
print(f"\n- Array: {arr_str}")
sorted_arr_str = selection_sort(arr_str)
print(f"\n>> Sorted array: {sorted_arr_str}")

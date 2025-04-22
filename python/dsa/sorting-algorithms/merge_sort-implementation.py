#!/usr/bin/python3
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two sorted halves
        merge(arr, left_half, right_half)

def merge(arr, left_half, right_half):
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1


# Example usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print(f"- Original array:", arr)
    merge_sort(arr)
    print("\n>> Sorted array:", arr)

    # Merge sort on a list of strings
    print("\n\n", "-" * 80, "\n\n\n{:_^80}".format("List of strings example:"))
    arr_str = ["Zucchini", "Banana", "Apple", "Pineapple", "Orange", "Grape"]
    print(f"\n- Original array: {arr_str}")
    merge_sort(arr_str)
    print(f"\n>> Sorted array: {arr_str}")

#!/usr/bin/python3
"""Time complexity of the 
following code is O(2n) = O(n)
        AND
Space complexity of the 
following code is O(2n) = O(n) too.
"""
def loop_twice(arr):
    arr_copy_1 = list()
    arr_copy_2 = list()

    for i in arr:
        print(i)
        arr_copy_1.append(i)

    for i in arr:
        print(i)
        arr_copy_2.append(i)

input_arr = [1, 2, 3]
loop_twice(input_arr)
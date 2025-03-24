#!/usr/bin/python3
"""The total runtime complexity of the 
   following code is O(n^2 + n) = O(n^2).

   So n^2 is the dominant factor and n is 
   the non-dominant factor, and we always drop 
   the non-dominant factors in the big o claculation 
   because they have insignificant effect on the total 
   runtime or space complexity.
"""
def nested_loop_and_count(arr):
    result = list()
    counter = 0

    for i in arr:
        for j in arr:
            counter += 1
            result.append(counter)
            print(counter)
    print("")
    for k in arr:
        print(k)

    return result

input_arr = [1, 2, 3]
output = nested_loop_and_count(input_arr)
print(output)
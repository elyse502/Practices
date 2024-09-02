import numpy as np
# [1,2,3]
# [4,5,6]
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

print("First element of array: ", arr[0][0])
print("Last element of array: ", arr[1][2])

for x in arr:
    # print(x)
    for y in x:
        print(y)


# Tutorial 43-Python Shallow And Deep Copy

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = list1
print("List1 -> ", list1)
print("List2 -> ", list2)
print("id of List1 -> ", id(list1))
print("id of List2 -> ", id(list2))

list1.append([10, 11, 12])
print("List1 -> ", list1)
print("List2 -> ", list2)
print()


# Creating a copy using Shallow Copy
import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list: ", old_list)
print("New list: ", new_list)
print("id of Old list: ", id(old_list))
print("id of New list: ", id(new_list))

# Adding elements to the old_list using shallow copy
old_list.append([4, 4, 4])
print("Old list: ", old_list)
print("New list: ", new_list)

# Adding new nested object using shallow copy
old_list[1][1] = 'AA'
print("Old list: ", old_list)
print("New list: ", new_list)
old_list[3][1] = 'BB'
print("Old list: ", old_list)
print("New list: ", new_list)
print()


# Copying a list using deepcopy()
import copy
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list: ", old_list)
print("New list: ", new_list)
print("id of Old list: ", id(old_list))
print("id of New list: ", id(new_list))

# Adding a new nested object in the list using Deep Copy
old_list[1][0] = 'BB'
print("Old list: ", old_list)
print("New list: ", new_list)
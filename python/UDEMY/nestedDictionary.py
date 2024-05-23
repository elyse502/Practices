# Tutorial 30-Python Nested Dictionary Implementation

# Declaring and defining a nested dictionary
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
            2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people)

# Accessing elements of the dictionary

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])

people[3] = {}
# Adding elements to a dictionary
people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'

print(people)

# Adding dictionary to a nested dictionary
people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
print(people[4])

print(people)


# Deleting elements from a dictionary
print(people[3])
print(people[4])

del people[3]['married']
del people[4]['married']

print(people[3])
print(people[4])


people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}

print(people)

# Deleting dictionary from nested dictionary
del people[3], people[4]
print(people)


# Iterating through a nested dictionary
print(people.items())

for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)

    for key in p_info:
        print(key + ':', p_info[key])
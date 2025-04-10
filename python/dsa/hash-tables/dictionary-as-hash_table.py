#!/usr/bin/python3
grades_table = {}

grades_table["Alice"] = 85
grades_table["Bob"] = 92
grades_table["Emma"] = 95

# Retrieving a value from the hash table
retrieved_grade = grades_table["Emma"]
print(f">> Emma's grade: {retrieved_grade}")

# Updating a value in the hash table
grades_table["Emma"] = 90
print(f">> Updated Emma's grade: {grades_table['Emma']}")

# Checking if a key exists in the hash table
if "Alice" in grades_table:
    print("\nKey found") 
else:
    print("\nKey not found")
print("Alicee" in grades_table)  # True

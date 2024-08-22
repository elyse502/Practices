# Working with series in Pandas
import pandas as pd
s1 = pd.Series([1.25, 1.75, 2.25, 2.75, 3.25], index=['a', 'b', 'c', 'd', 'e'])
print(s1)
print()

# Accessing elements
print(s1['a'])
print(s1[2])
print(s1[1:4])
print()

# Perfoming some operations
print(">> s1 elements:")
print(s1)

s2 = s1 + 5
print("\n>> s2 elements:")
print(s2)

s3 = s1 * 2
print("\n>> s3 elements:")
print(s3)

# Perform filtering
s4 = s1[s1 > 2]
print("\n>> s4 elements:")
print(s4)

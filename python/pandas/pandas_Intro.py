"""Series: an indexed 1D array"""
import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)
print()

# Explicit index
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
print(data)
print()

# Access data
print(data['b'])
print(data[1])
print(data[1:3])
print()

# Can work as a dictionary
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}

population = pd.Series(population_dict)
print(population)
print()
# Concatenation of DataFrames
import pandas as pd

dict1 = {'id': [10, 18, 7],
    'Name': ['Elysée', 'Clement', 'Placide']
    }
df1 = pd.DataFrame(dict1)
print(">> df1 is :\n", df1)
print()

dict2 = {'id': [45, 42],
    'Name': ['NIYIBIZI', 'TUYISHIME']
    }
df2 = pd.DataFrame(dict2)
print(">> df2 is :\n", df2)
print()

df3 = pd.concat([df1, df2])
print(">> After concatenation, df3 is :\n", df3)


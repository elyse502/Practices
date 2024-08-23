# Boolean Indexing in Data Frame
import pandas as pd

dic = {'Name': ['Elysée', 'Clement', 'Placide'],
       'Age': [20, 21, 22]}
df = pd.DataFrame(dic, index = [True, False, True])
print(df)
print()

# Displaying only rows whose index is True
print(df.loc[True])
print("\nOR.......\n")
df1 = df[df.index == True]
print(df1)

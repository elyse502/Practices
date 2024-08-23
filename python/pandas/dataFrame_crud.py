# Add, Rename and Delete a column
import pandas as pd

s = pd.Series([10, 15, 18, 22, 26, 30])
df = pd.DataFrame(s)
df.columns = ['List1']
print(df)
print()

# Creating a new column and adding it to the particular table representation
# df['List2'] = [1, 2, 3, 4, 5, 6]
df['List2'] = 20
df['List3'] = df['List1'] + df['List2']
# print(df)

# Deleting a column
df.pop('List2')
# del df['List2']
print(df)

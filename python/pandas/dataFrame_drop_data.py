# Delete a column using dropr() method
import pandas as pd

s = pd.Series([10, 15, 18, 22, 26, 30])
df = pd.DataFrame(s)
df.columns = ['List1']
df['List2'] = 20
df['List3'] = df['List1'] + df['List2']
print(df)
print()

# axis=0 for row and axis=1 for column
df1 = df.drop('List2', axis=1)
print(df1)
print()
# Deleting row using drop() method
# df2 = df.drop(3, axis=0)
df2 = df.drop(index=[2, 4], axis=0)
print(df2)

# Creating an empty DataFrame
import pandas as pd
df = pd.DataFrame()
print(df)
print()

# Creating DataFrame from series
s = pd.Series(['a', 'b', 'c', 'd', 'e'])
df = pd.DataFrame(s)
print(df)
print()

# Creating DataFrame from dictionary
name = pd.Series(['Elysée', 'Placide', 'Yves'])
team = pd.Series(['FCB', 'RFC','MUFC'])
dic = {'Name': name, 'Team': team}
df = pd.DataFrame(dic)
print(df)
print()

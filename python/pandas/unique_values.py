# Displaying unique values in a series
import pandas as pd
# unique()
s1 = pd.Series([10, 20, 30, 40, 10, 20, 30, 40, 50])
print(">> Original Series is :\n")
print(s1)
print()
print("----------------------------------------\n\n>> Unique values in series is : \n")
print(s1.unique())
print()
print("----------------------------------------\n\n>> Number of Unique values in series is : ", s1.nunique())
print()

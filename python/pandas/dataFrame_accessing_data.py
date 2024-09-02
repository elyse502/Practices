# Accessing data row wise and column wise in DataFrame
import pandas as pd

l = [{'Name': 'Elysée', 'SurName': 'NIYIBIZI'},
     {'Name': 'Clement', 'SurName': 'TUYISHIME'},
     {'Name': 'Placide', 'SurName': 'SHEMA'}]
df = pd.DataFrame(l)
print(df)
print()

# iterrows()
print("(1) Accessing data row wise:\n_______________________________")
for (row_index, row_value) in df.iterrows():
    print("\n>> Row index is :", row_index)
    print(">> Row value is :\n\n", row_value)
    print("\n----------------------------------------")
print()

# items()
print("(2) Accessing data column wise:\n_______________________________")
for (column_index, column_value) in df.items():
    print("\n>> Column index is :", column_index)
    print(">> Column value is :\n\n", column_value)
    print("\n----------------------------------------")

# Creating Dataframe from List of dictionaries
import pandas as pd

l = [{'Name': 'Elysée', 'SurName': 'NIYIBIZI'},
     {'Name': 'Clement', 'SurName': 'TUYISHIME'},
     {'Name': 'Placide', 'SurName': 'SHEMA'}]
df = pd.DataFrame(l)
print(df)

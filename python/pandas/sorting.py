# Sorting a series
import pandas as pd
# sort_values()
s1 = pd.Series([90, 10, 30, 20, 60, 80, 50, 70, 40])
print(">> Original Series is :\n")
print(s1)
print()
print("----------------------------------------\n\n>> \
Sorted series is :\n")
print(s1.sort_values())

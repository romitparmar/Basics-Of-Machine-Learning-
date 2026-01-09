import pandas as pd

s1 = pd.Series([6,4,8,3,2,1])
sort = pd.Series.sort_values(s1)

print(sort.values)
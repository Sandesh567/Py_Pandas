#Exploring data sets.
#head(n)- default 5 rows from beginning, n means how many rows
#tail(n) -default 5 rows from end or last, n means how many rows

import pandas as pd

df = pd.read_json("sample_Data.json")

print("First 10 row of first")
print(df.head(10))

print("Last 10 row of last")
print(df.tail(10))


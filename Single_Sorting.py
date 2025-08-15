#sorting data like in alphabetical order
# SORTING DATA IN 1 COLUMN. sort_values()

#syntax:  df.sort_values(by="column_name",TRUE / FALSE, inplace = True)
#true = ascending false= descending

import pandas as pd

data = {
"Name": [
    "Alice", "Laura", "Michael","George" , "Kevin",
    "Fiona", "Nina", "Hannah", "Ian", "Julia",
    "Ethan", "Bob", "Diana", "Oscar","Charlie"
    ],
    "Salary":[
    75000, 65000, 55000, 70000, 60000,
        58000, 67000, 52000, 72000, 50000,
        56000, 48000, 80000, 61000, 85000
],
        "Department": [
        "HR", "IT", "Finance", "IT", "Marketing",
        "Finance", "IT", "HR", "IT", "Marketing",
        "Finance", "HR", "IT", "Marketing", "Finance"
    ],
}

df = pd.DataFrame(data)
print(df)



df.sort_values("Salary", ascending = False, inplace = True)

print("Sorted employees with highest salary")
print(df)

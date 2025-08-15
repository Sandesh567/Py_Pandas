# Multiple column sorting

import pandas as pd

data={
    "Name": [
        "Alice", "Laura", "Michael", "George", "Kevin",
        "Fiona", "Nina", "Hannah", "Ian", "Julia",
        "Ethan", "Bob", "Diana", "Oscar", "Charlie"
    ],
    "Salary": [
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

#if we want to sort multiple columns then we have to pass as list values
df.sort_values(by=["Name","Salary"],ascending=[True,False],inplace=True)
print("Name in ascending and salary in descending order")
print(df)
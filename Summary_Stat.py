#Summary Statistics provides numerical values such as
# mean , min & max value, sum ,count, std etc.
# df["column name].sum()
# df["column name"].mean
# df["column name"].min
# df["column name"].max



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

}

df = pd.DataFrame(data)
print(df)

#finding out average salary

ave_salary = df['Salary'].mean()
print(f"Average Salary is  {ave_salary}")
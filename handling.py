#Handling missing values by deleting it.

#dropna() - deletes data

# df.dropna(axis=0/1, inplace = True)

# axis = 0 means delete rows with missing value
# axis = 1 means delete column with missing value

import pandas as pd

data = {
    "Name": ['Sandesh', None, 'Abhishek', 'Marshall', 'Jermaine Cole', 'Mukesh', 'Suresh', 'Lokesh', 'Shiv', 'Hari'],
    "Age": [21, None, 23, 50, 40, 60, 56, 34, 56, 22],
    "Salary": [25000, None, 45000, 54000, 56000, 78000, 90000, 23000, 34000, 50000],
    "Performance_Score": [85, None, 88, 90, 92, 98, 67, 89, 90, 98]
}

df = pd.DataFrame(data)
print(df)


df.dropna(inplace=True)
print("Removing missing values")
print(df)



#Handling missing data represents as NaN or None (for object type)

#   isnull() - method is used to detect data
#   returns boolean value
#   if true - NaN is missing
#   if false then value is present


import pandas as pd

data = {
    "Name": ['Sandesh', None, 'Abhishek', 'Marshall', 'Jermaine Cole', 'Mukesh', 'Suresh', 'Lokesh', 'Shiv', 'Hari'],
    "Age": [21, None, 23, 50, 40, 60, 56, 34, 56, 22],
    "Salary": [25000, None, 45000, 54000, 56000, 78000, 90000, 23000, 34000, 50000],
    "Performance_Score": [85, None, 88, 90, 92, 98, 67, 89, 90, 98]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())  #this returns true if data is missing

print(df.isnull().sum()) #this return the number of missing data in each column


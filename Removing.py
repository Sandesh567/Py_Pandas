#Removing columns and rows

import pandas as pd

data = {
    "Name": ['Sandesh', 'Anuj', 'Abhishek', 'Marshall', 'Jermaine Cole', 'Mukesh', 'Suresh', 'Lokesh', 'Shiv', 'Hari'],
    "Age": [21, 22, 23, 50, 40, 60, 56, 34, 56, 22],
    "Salary": [25000, 34000, 45000, 54000, 56000, 78000, 90000, 23000, 34000, 50000],
    "Performance_Score": [85, 65, 88, 90, 92, 98, 67, 89, 90, 98]
}

df = pd.DataFrame(data)
print(df)

#df.drop[columns = ["Columnname"], inplace = True

# inplace true means modifies the original data frame

#Removing performance score column

print("Modified Data")


#Removes a single column

# df.drop(columns=["Performance_Score"], inplace=True)
# print(df)


#Removing Multiple column
df.drop(columns=["Performance_Score","Age"], inplace=True)
print(df)
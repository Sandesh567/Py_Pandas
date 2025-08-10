#Adding column to the data

import pandas as pd

#Creating data frame
data = {
    "Name":['Sandesh','Anuj','Avishek','Marshall','Jermaine Cole','Mukesh','Sukesh','Lokesh','Shiv','Hari'],
    "Age" : [21,22,23,50,40,60,56,34,56,22],
    "Salary":[25000,34000,45000,54000,56000,78000,90000,23000,34000,50000],
    "Performance_Score":[85,65,88,90,92,98,67,89,90,98]
}

df =pd.DataFrame(data)

print(df)

# 1. Adding new column . If adding to any position is valid then use this.

#New Bonus Column will be created

df["Bonus"] = df['Salary'] * 0.1
print(df)

# 2. Adding column using insert method. If adding to specific position use this.
#loc means position like if putting at first 0 position and like wise

#df.insert(loc,"Column_name", some_Data)

df.insert(0,"Employee ID" ,[10,20,30,40,50,60,70,80,90,100])
print(df)
import pandas as pd

data = {
    "Name":['Sandesh','Anuj','Abhishek','Marshall','Jermaine Cole','Mukesh','Suresh','Lokesh','Shiv','Hari'],
    "Age" : [21,22,23,50,40,60,56,34,56,22],
    "Salary":[25000,34000,45000,54000,56000,78000,90000,23000,34000,50000],
    "Performance_Score":[85,65,88,90,92,98,67,89,90,98]
}

df =pd.DataFrame(data)

print(df)

#Updating data in dataframe

# .loc[]
# df.loc[row_index,"Column_Name"] = new_Value

#updating Anuj salary
#row_index of anuj is 1 & column name we are changing salary so salary and assign new value.
df.loc[1 , 'Salary'] = 40000
print(df)
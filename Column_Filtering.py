#We will select the column single and multiple column data
#Creating Data converting to dataframe filtering single and multiple columns
import pandas as pd


#Creating data frame
data = {
    "Name":['Sandesh','Anuj','Avishek','Marshall','Jermaine Cole','Mukesh','Sukesh','Lokesh','Shiv','Hari'],
    "Age" : [21,22,23,50,40,60,56,34,56,22],
    "Salary":[25000,34000,45000,54000,56000,78000,90000,23000,34000,50000],
}

#Converting data into dataframe
df = pd.DataFrame(data)
print(df)


#Selecting single column
print("Name (Single column)")
name = df['Name']
print(name)

#Selecting multiple column
print("Multiple columns ")
multiple = df[['Name','Salary']]
print(multiple)
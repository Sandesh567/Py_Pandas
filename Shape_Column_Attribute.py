#Shape - returns a tuple that returns the  numbers of rows and columns
#Column - return the names of all the available columns


import pandas as pd

data = {
    "Name":['Sandesh','Anuj','Avishek','Marshall','Jermaine Cole','Mukesh','Sukesh','Lokesh','Shiv','Hari'],
    "Age" : [21,22,23,50,40,60,56,34,56,22],
    "Salary":[25000,34000,45000,54000,56000,78000,90000,23000,34000,50000],
}

df = pd.DataFrame(data)
print(df)

print(f'Shape:{df.shape}') #f acts as a template literals.
print(f'Columns:{df.columns}')

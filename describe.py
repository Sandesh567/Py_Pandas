#describe method returns description of the data in the dataframe
#helps in generative descriptive statistics of a dataframe or series
#count,mean, std, min. 25per, 50 per, 75per, max

import pandas as pd

data = {
    "Name":['Sandesh','Anuj','Avishek','Marshall','Jermaine Cole','Mukesh','Sukesh','Lokesh','Shiv','Hari'],
    "Age" : [21,22,23,50,40,60,56,34,56,22],
    "Salary":[25000,34000,45000,54000,56000,78000,90000,23000,34000,50000],
}

df = pd.DataFrame(data)
print(df)

print("Descriptive Statistics of Data:")
print(df.describe())
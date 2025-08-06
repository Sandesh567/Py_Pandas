#How to create dataframes and save.

import pandas as pd


#This creates a dataframe
data = {
    "Name":['Sandesh','Anuj','Avishek','Marshall','Jermaine Cole'],
    "Age" : [21,22,23,50,40],
    "City":['Dhangadhi','Dang','Kathmandu','USA','USA']
}

#using dataframe and passing data

df = pd.DataFrame(data)
print(df)

#Saving data to CSV file without index
df.to_csv("data.csv", index=False)
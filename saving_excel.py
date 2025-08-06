#saving dataframes to excel file
import pandas as pd


#creating data
data ={
    "Name":['Sandesh','Anuj','Avishek','Marshall','Jermaine Cole'],
    "Age" : [21,22,23,50,40],
    "City":['Dhangadhi','Dang','Kathmandu','USA','USA']
}

#adding it to dataframes

df = pd.DataFrame(data)
print(df)

#converting and saving to Excel file

#install package openpyxl to save it successfully
df.to_excel("people.xlsx",index=False)
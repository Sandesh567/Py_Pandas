##saving dataframes to json file
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

#converting and saving to json file

#
df.to_json("people.json",index=False)
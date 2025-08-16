#Joining row of multiple data based on common key values

import pandas as pd

#customer data frame

df_customers = pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['Sandesh','Anuj','Abhisek']
})

#order data frame

df_orders = pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmount':[250,350,550]
})

#merge the data frame

#inner  - It returns a Dataframe with only those rows that have common characteristics.
df_merged_inner = pd.merge(df_customers,df_orders,on="CustomerID",how="inner")
print("Inner Join")



#returns all the common data and those who are not matching it will show NaN.
df_merged_outer = pd.merge(df_customers,df_orders,on="CustomerID",how="outer")
print("Outer Join")

#All from left(1st DF) but only common from right(2nd DF) and uncommon will be filled with NaN
df_merged_left = pd.merge(df_customers,df_orders,on="CustomerID",how="left")
print("Left Join")

#All from right(2nd DF) but only common from left(1st DF) and uncommon will be filled with NaN
df_merged_right = pd.merge(df_customers,df_orders,on="CustomerID",how="right")
print(df_merged_right)
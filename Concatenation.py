#Combining data sets vertically or horizontally

#pd.concate([df1,df1] , axis = 0 ,ignore_index=True)

# [df1,df1] = list of data frames
# axis = 0 row / 1 Column
# ignore_index = True -  reset index

#vertically concatenating

import pandas as pd

#region 1

df_Region1 = pd.DataFrame({
    'CustomerID':[1,2],
    "Name":['Sandesh','Marshall']
})

#region 2

df_Region2 = pd.DataFrame({
    'CustomerID':[3,4],
    "Name":['Jermaine','Anuj']
})

#Concate vertically axis = 0 (Default)
df_concat_vertical = pd.concat([df_Region1,df_Region2],ignore_index=True)
print("vertical concat")



#Concate horizontally axis = 1
df_concat_horizontal = pd.concat([df_Region1,df_Region2],axis=1,ignore_index=True)
print(df_concat_horizontal)
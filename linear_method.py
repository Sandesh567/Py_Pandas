import pandas as pd

data = {
    "Time":[1,2,3,4,5,6],
    "Value":[10,20,None,40,None,60],
}

df = pd.DataFrame(data)
print("Before Interpolation data")
print(df)

df['Value'] = df['Value'].interpolate(method = "linear")
print("After Interpolation data")
print(df)


#Three major types: linear used for linear data, time used with time index datas, polynomial used with polynomial data
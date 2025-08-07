#info() method provides us

        # number of rows and columns
        # column names
        # data types
        # non-null counts
        # memory usage of the data frame
    #object data such as string like name city


import pandas as pd

df = pd.read_json("sample_Data.json")

print("Displaying the information of the datasets")

print(df.info())


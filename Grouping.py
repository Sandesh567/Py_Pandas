import pandas as pd

data = {
    "Name":['Sandesh','John','Anuj','Abhisek','Marshall'],
    "Age":[19,21,34,21,34],
    "Salary":[19000,21000,34000,21000,34000]
}

df = pd.DataFrame(data)

#Grouping the data

grouped= df.groupby("Age")["Salary"].sum()
print(grouped)

#there are two groups with same age ie; 21 and 34. So first the
# data is grouped based on age and salary then the data that was grouped,
# sum is performed. so adding salary of 21 of both people and same with 34

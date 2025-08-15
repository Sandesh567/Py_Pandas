import pandas as pd

data ={
    "Name":['Sandesh','John','Anuj','Abhisek','Marshall'],
    "Age":[19,21,34,21,34],
    "Salary":[19000,21000,34000,21000,34000]
}

df = pd.DataFrame(data)

grouped = df.groupby(["Age","Name"]) ["Salary"].sum()
print(grouped)

#name and age are grouped together then sum is performed.
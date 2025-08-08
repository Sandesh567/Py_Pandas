#Filtering rows according to different conditions

import pandas as pd

#Creating data frame
data = {
    "Name":['Sandesh','Anuj','Avishek','Marshall','Jermaine Cole','Mukesh','Sukesh','Lokesh','Shiv','Hari'],
    "Age" : [21,22,23,50,40,60,56,34,56,22],
    "Salary":[25000,34000,45000,54000,56000,78000,90000,23000,34000,50000],
    "Performance_Score":[85,65,88,90,92,98,67,89,90,98]
}

df = pd.DataFrame(data)

print(df)

#Filtering rows with a single condition

#Filtering rows based on condition where the salary is greater than 50k

high_Salary = df[df['Salary'] > 50000]
print("Employees with high salary")
print(high_Salary)



#Filtering with multiple condition

#Filtering rows based on data where the age is greater than 40 and salary greater than 50k
#using AND condition all true to return true

high_Salary_age= df[(df['Salary'] > 50000) & (df['Age'] > 40)]
print("Employees with high salary where age is greater than 40")
print(high_Salary_age)

#using OR where only one condition needs to be true to return value

high_performance_age= df[(df['Age'] > 35) | (df['Performance_Score'] > 90)]
print("Employees with Age greater than 35 where performance is greater than 90")
print(high_performance_age)





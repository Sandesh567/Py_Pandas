import pandas as pd

#read data from CSV file into a data file, also include encoding type
#1. reading CSV file
df_Csv = pd.read_csv("sales_data_sample.csv" , encoding="latin1")

#2.Reading excel file
#install xlrd package
df_Excel = pd.read_excel("SampleSuperstore.xlsx")

#3. Reading json file data
df_json = pd.read_json("sample_Data.json")
print(df_json)
# 📊 Reading Files with Pandas

This repository demonstrates how to use the [Pandas](https://pandas.pydata.org/) library in Python to read data from various file formats such 
as **CSV**, **Excel**, and **JSON**. Pandas makes it easy to load, explore, and manipulate structured data efficiently.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python and pip installed. You can install the required libraries using:

```bash
pip install pandas 


## Reading CSV File

## 1. Reading CSV file
df_Csv = pd.read_csv("sales_data_sample.csv" , encoding="latin1")

##read data from CSV file into a data file, also include encoding type

## 2. Reading excel file

##install xlrd package to run excel file

df_Excel = pd.read_excel("SampleSuperstore.xlsx")

## 3. Reading json file data

df_json = pd.read_json("sample_Data.json")














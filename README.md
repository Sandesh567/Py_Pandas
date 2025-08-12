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



#Topics
1. Saving data as different file format

2. info method

3. describe method

4. shape and column method

5. Column Filtering

6. Rows Filtering

7. Updating Data Frame

8. Adding New Column to the Data Frame

9. Removing column from the Data Frame

10. Detecting missing values using isnull().
    Returns boolean value true means value missing, false means not missing.
    isnull().sum() using this return the number of missing values.

11. Handling missing values by deleting it using dropna().

        # df.dropna(axis=0/1, inplace = True)
        # axis = 0 means delete rows with missing value
        # axis = 1 means delete column with missing value

                    df.dropna(inplace=True)
            It simply removes the missing value from the data frame.

12. Handling missing values by filling it rather than deleting it using fillna().

    #  We can fill it using default value : df.fillna(0, inplace=True), passing default value 0.

    #  We can use mean to fill the missing value.It is more like a calculated value approach
            df['Age'].fillna(df['Age'].mean(),inplace=True)

















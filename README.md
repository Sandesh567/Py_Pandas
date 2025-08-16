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

13. Handling missing values using interpolate linear method.

        df['Value'].interpolate(method = "linear")

                     #Value is column name
                     #Three major methods: linear, time , polynomial

14. Sorting Columns using sort_values()

        df.sort_values(by="column_name",TRUE / FALSE, inplace = True)  #single column sorting
            #true = ascending false= descending

        df.sort_values(by=["Name","Salary"],ascending=[True,False],inplace=True) #multiple column sorting
            
15. Grouping the data using groupby()
            df.groupby("Age")["Salary"].sum()  #single column grouping

        # Here first data is grouped based on age and salary then sum() function is performed.
        # person with same data is considered single data and added using sum().

            df.groupby(["Age","Name"]) ["Salary"].sum() #multiple column grouping

        # Here name and age is grouped together and salary is single grouped and sum is performed.


16. Summary Statistics

    #Provides a numerical statistics of data such as mean, max, min, count, std, sum
        ave_salary = df['Salary'].mean()

17. Merging
    #merging the dataframes using merge()

         df_merged_inner = pd.merge(df_customers,df_orders,on="CustomerID",how="inner")

        # df_customers, df_orders = data frames
        # on means which column to target
        # how means join type inner, right, left, outer

                        
18. Concatenation of DataFrames
        #Combining data sets vertically or horizontally

                #pd.concate([df1,df1] , axis = 0 ,ignore_index=True)

            # [df1,df1] = list of data frames
            # axis = 0 row / 1 Column
            # ignore_index = True -  reset index

#Concate vertically axis = 0 (Default)
df_concat_vertical = pd.concat([df_Region1,df_Region2],ignore_index=True)


#Concate horizontally axis = 1
df_concat_horizontal = pd.concat([df_Region1,df_Region2],axis=1,ignore_index=True)











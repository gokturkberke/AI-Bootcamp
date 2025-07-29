# Numpy
import numpy as np
l1 = [1,3,5,7]
l2 = [2,4,6,8]


lst = []
for i in range(len(l1)):
    lst.append(l1[i] + l2[i])
print(lst)

arr1 = np.array(l1)
arr2 = np.array(l2)
print(arr1 + arr2)

np.zeros((2, 3))  # Create a 2x3 array of zeros
np.arange(1,10,3)  # Create an array with values from 1 to 9 with a step of 3
np.linspace(1, 10, 5)  # Create an array with 5 evenly spaced values between 1 and 10
np.random.randint(0,100,size=5) # Create an array of 5 random integers between 0 and 100
np.random.normal(0, 1, size=5)  # Create an array of 5 random numbers from a normal distribution with mean 0 and std deviation 1


#Numpy Atrributes
arr1d = np.arange(1,10,2)
arr1d.shape # 1-dimensional array shape
arr1d.ndim  # Number of dimensions(boyut)
arr1d.size  # Total number of elements in the array

#to prevent random seed
np.random.seed(42)  # Set a random seed for reproducibility
#(Bir deney için rastgele veri oluşturmanız gerekiyor. np.random.seed(42) kullanırsanız, deneyinizi her tekrarladığınızda aynı rastgele veri setini kullanırsınız, bu da sonuçlarınızı karşılaştırmayı kolaylaştırır.)

arr1dd = np.array([1,2,3,4,5])
np.sum(arr1dd)  # Sum of all elements
np.mean(arr1dd)  # Mean of all elements
np.std(arr1dd)  # Standard deviation of all elements
np.var(arr1dd)  # Variance of all elements
print(arr1dd > 4)
print(arr1dd[arr1dd > 4]) # Elements greater than 4


# -----------------------------------------------------------------------------------------------------
# Pandas
import pandas as pd
arr = np.array([1, 2, 3, 4, 5])
ser = pd.Series(arr)
print(ser)
print(ser.shape)
print(ser.ndim)

import seaborn as sns
df = sns.load_dataset("tips")
print(df.head())
print(df.tail())

print(df.columns)  # Columns of the DataFrame
print(df.shape)    # Shape of the DataFrame
print(df.dtypes)   # Data types of each column
print(df.info())   # Summary of the DataFrame
print(df.describe())  # Statistical summary of the DataFrame
print(df.isnull().sum())  # Count of missing values in each column
print(df["day"].unique())  # Unique values in the 'day' column
print(df["day"].value_counts())  # Count of occurrences of each unique value in the

#loc dahil eder
print(df.loc[0:2])  # Select rows by label (inclusive of the last row)
print(df.iloc[0:2])  # Select rows by index (exclusive of the last)
# cogu zaman loc kullanilir
print(df.loc[df["total_bill"] > 20, ["smoker","size"]].head())  # Select smoker and size columns and all rows where total_bill is greater than 20

#groupby(tek cumle sorgulama da bu mantikli)
print(df.groupby("day")["total_bill"].mean())  # Group by 'day' and calculate the mean of 'total_bill'

#aggregate birden fazla fonksiyon icin mantikli olabilir
print(df.groupby("day", observed=True).agg({
    "total_bill" : ["mean", "sum"],
    "tip" : ["mean", "max"]
}))

#pivot_table
print(df.pivot_table(index="day",values="total_bill", aggfunc="mean"))  # Create a pivot table with 'day' as index and mean of 'total_bill'

print(df.pivot_table(
    index="day", 
    values=["total_bill","tip"], 
    aggfunc={
        "total_bill":["mean","sum"],
        "tip":"mean"
        }
))

# Exploratory Data Analysis
def check_df(dataframe, head=5):
    print("Shape of DataFrame:", dataframe.shape)
    print("Data Types:\n", dataframe.dtypes)
    print("First", head, "rows:\n", dataframe.head(head))
    print("Last", head, "rows:\n", dataframe.tail(head))
    print("Missing Values:\n", dataframe.isnull().sum())
    print("Statistical Summary:\n", dataframe.describe().T)
    
check_df(df)

cat_cols = ['sex','smoker','day','time']

def cat_summary(dataframe,col_name):
    print(pd.DataFrame({col_name : dataframe[col_name].value_counts(), "Ratio": 100 * dataframe[col_name].value_counts()/len(dataframe)}))

cat_summary(df,"day")


for col in cat_cols:
    cat_summary(df,col)
    
def num_summary(dataframe,numerical_col):
    quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,0.95,0.99]
    print(dataframe[numerical_col].describe(quantiles).T)
    
num_summary(df,"tip")

# Hedef Degisken Analizi

TARGET = "tip"

def target_summary_with_cat(dataframe,target,categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}), end = "\n\n\n")
    
for col in cat_cols:
    target_summary_with_cat(df, TARGET, col)
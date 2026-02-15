# ==========================================
# DATA ANALYSIS PROJECT USING PANDAS
# ==========================================

# 1️⃣ Import Required Libraries
import pandas as pd
import numpy as np

# 2️⃣ Load CSV Dataset into Pandas DataFrame
# Replace 'data.csv' with your dataset file name
df = pd.read_csv("data.csv")

print("Dataset Loaded Successfully!\n")


# 3️⃣ Explore Dataset
print("----- FIRST 5 ROWS -----")
print(df.head())

print("\n----- DATASET INFO -----")
print(df.info())

print("\n----- STATISTICAL SUMMARY -----")
print(df.describe())


# 4️⃣ Handle Missing Values

print("\n----- CHECKING MISSING VALUES -----")
print(df.isnull().sum())

# Option 1: Fill missing numerical values with mean
for column in df.select_dtypes(include=np.number):
    df[column].fillna(df[column].mean(), inplace=True)

# Option 2: Fill missing categorical values with mode
for column in df.select_dtypes(include="object"):
    df[column].fillna(df[column].mode()[0], inplace=True)

print("\nMissing values handled!")


# 5️⃣ Filter and Sort Data

# Example: Filter rows where Sales > 500
if "Sales" in df.columns:
    filtered_df = df[df["Sales"] > 500]
    print("\nFiltered Data (Sales > 500):")
    print(filtered_df.head())

# Example: Sort by Sales (descending)
if "Sales" in df.columns:
    sorted_df = df.sort_values(by="Sales", ascending=False)
    print("\nTop Sales Records:")
    print(sorted_df.head())


# 6️⃣ Group Data and Calculate Aggregates

# Example: Group by Category and calculate total & average Sales
if "Category" in df.columns and "Sales" in df.columns:
    group_data = df.groupby("Category")["Sales"].agg(["sum", "mean", "count"])
    print("\nGrouped Data (Category-wise Sales):")
    print(group_data)


# 7️⃣ Add New Calculated Columns

# Example: Add Profit Percentage column if Sales & Profit exist
if "Sales" in df.columns and "Profit" in df.columns:
    df["Profit_Percentage"] = (df["Profit"] / df["Sales"]) * 100
    print("\nNew Column Added: Profit_Percentage")


# 8️⃣ Export Cleaned Data to CSV

df.to_csv("cleaned_data.csv", index=False)
print("\nCleaned dataset exported as 'cleaned_data.csv'")


# 9️⃣ Interpret Insights (Basic Example)

print("\n----- INSIGHTS -----")

if "Sales" in df.columns:
    print(f"Average Sales: {df['Sales'].mean():.2f}")
    print(f"Maximum Sales: {df['Sales'].max():.2f}")

if "Profit" in df.columns:
    print(f"Average Profit: {df['Profit'].mean():.2f}")

print("\nData Analysis Completed Successfully!")

import pandas as pd

# Load CSV file into a Pandas DataFrame
df = pd.read_csv("01.Data Cleaning and Preprocessing.csv")

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Filtering data based on conditions
# Example: Filter rows where the 'ChipRate' column is greater than 15
filtered_df = df[df['ChipRate'] > 15]

# Display filtered DataFrame
print("\nFiltered DataFrame where ChipRate > 15:")
print(filtered_df.head())

# Handling missing values
# Check for missing values
print("\nMissing values in the DataFrame:")
print(df.isnull().sum())

# Replace missing values with a specific value (e.g., 0)
df.fillna(0, inplace=True)

# Alternatively, drop rows with missing values
# df.dropna(inplace=True)

# Calculating summary statistics
# Summary statistics for numerical columns
summary_stats = df.describe()

# Display summary statistics
print("\nSummary statistics:")
print(summary_stats)

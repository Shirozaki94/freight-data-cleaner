import pandas as pd

# File paths
input_file = "data/raw_freight_data.csv"
output_file = "data/clean_freight_data.csv"

# Read data
df = pd.read_csv(input_file)

# Basic cleaning
df.columns = df.columns.str.strip().str.lower()
df = df.dropna()

# Convert amount column to numeric if present
if "amount" in df.columns:
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

# Save cleaned data
df.to_csv(output_file, index=False)

print("Data cleaning completed successfully.")


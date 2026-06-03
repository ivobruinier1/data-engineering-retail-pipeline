import pandas as pd

# 1. Extract (data inlezen)
df = pd.read_csv("data/raw.csv")

# 2. Quick look
print("Original data:")
print(df.head())

# 3. Transform (cleaning)
df.columns = df.columns.str.lower().str.replace(" ", "_")

df = df.drop_duplicates()

df = df.dropna()

# 4. Load (save cleaned data)
df.to_csv("data/clean.csv", index=False)

print("ETL completed: clean.csv created")
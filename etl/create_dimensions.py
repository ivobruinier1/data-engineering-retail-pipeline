import pandas as pd

df = pd.read_csv("data/clean.csv")

# customer dimension
dim_customer = (
    df[["customer_id", "country"]]
    .drop_duplicates()
)

# product dimension
dim_product = (
    df[["stockcode", "description"]]
    .drop_duplicates()
)

# fact table
fact_sales = df.copy()


fact_sales["revenue"] = (
    fact_sales["quantity"] *
    fact_sales["price"]
)

dim_customer.to_csv(
    "data/dim_customer.csv",
    index=False
)

dim_product.to_csv(
    "data/dim_product.csv",
    index=False
)

fact_sales.to_csv(
    "data/fact_sales.csv",
    index=False
)

print("Dimensions and fact table created")
import pandas as pd
from sqlalchemy import create_engine, text

# =============================
# CONFIG
# =============================
DB_URL = "postgresql+psycopg2://postgres:ploekie22@localhost:5432/retail_dw"
engine = create_engine(DB_URL)

SAMPLE_SIZE = 1000

# =============================
# 1. CONNECTION CHECK
# =============================
print("🔌 Connecting to database...")

with engine.connect() as conn:
    conn.execute(text("SELECT 1"))

print("✔ Connection successful")

# =============================
# 2. TRUNCATE TABLES
# =============================
print("🧹 Clearing tables...")

with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE dim_customer RESTART IDENTITY CASCADE"))
    conn.execute(text("TRUNCATE TABLE dim_product RESTART IDENTITY CASCADE"))
    conn.execute(text("TRUNCATE TABLE fact_sales RESTART IDENTITY CASCADE"))

print("✔ Tables cleared")

# =============================
# 3. LOAD CSV
# =============================
print("📥 Loading CSV files...")

dim_customer = pd.read_csv("data/dim_customer.csv")
dim_product = pd.read_csv("data/dim_product.csv")
fact_sales = pd.read_csv("data/fact_sales.csv")

print("✔ CSV loaded")

# =============================
# 4. SAMPLE (🔥 IMPORTANT FOR TESTING)
# =============================
dim_customer = dim_customer.head(SAMPLE_SIZE)
dim_product = dim_product.head(SAMPLE_SIZE)
fact_sales = fact_sales.head(SAMPLE_SIZE)

print("\n🧪 USING SAMPLE DATA ONLY")
print("dim_customer:", dim_customer.shape)
print("dim_product:", dim_product.shape)
print("fact_sales:", fact_sales.shape)

# =============================
# 5. CLEAN DIM_CUSTOMER
# =============================
dim_customer = dim_customer.dropna(subset=["customer_id"])
dim_customer = dim_customer.drop_duplicates(subset=["customer_id"])
dim_customer["customer_id"] = dim_customer["customer_id"].astype(int)

# =============================
# 6. CLEAN DIM_PRODUCT
# =============================
dim_product = dim_product.dropna(subset=["stockcode"])
dim_product = dim_product.drop_duplicates(subset=["stockcode"])

# =============================
# 7. CLEAN FACT_SALES
# =============================
fact_sales = fact_sales.dropna(subset=["invoice", "stockcode", "customer_id","description"])

fact_sales["customer_id"] = fact_sales["customer_id"].astype(int)
fact_sales["stockcode"] = fact_sales["stockcode"].astype(str)

fact_sales["quantity"] = pd.to_numeric(fact_sales["quantity"], errors="coerce")
fact_sales["price"] = pd.to_numeric(fact_sales["price"], errors="coerce")

# fix datetime column name (IMPORTANT)
fact_sales = fact_sales.rename(columns={
    "invoicedate": "invoice_date"
})

fact_sales["invoice_date"] = pd.to_datetime(
    fact_sales["invoice_date"],
    errors="coerce"
)

fact_sales = fact_sales.dropna(subset=["quantity", "price"])

fact_sales["revenue"] = fact_sales["quantity"] * fact_sales["price"]

# 🔥 IMPORTANT: primary key fix
fact_sales = fact_sales.reset_index(drop=True)
fact_sales["sale_id"] = range(1, len(fact_sales) + 1)

print("✔ Data cleaned")

# =============================
# 8. LOAD TO POSTGRES
# =============================
print("\n📤 Loading SAMPLE into PostgreSQL...")

dim_customer.to_sql(
    "dim_customer",
    engine,
    if_exists="append",
    index=False
)

dim_product.to_sql(
    "dim_product",
    engine,
    if_exists="append",
    index=False
)

fact_sales.to_sql(
    "fact_sales",
    engine,
    if_exists="append",
    index=False,
    chunksize=1000,
    method="multi"
)

print("✔ Sample load complete")

# =============================
# 9. VERIFY
# =============================
with engine.connect() as conn:
    for table in ["dim_customer", "dim_product", "fact_sales"]:
        count = conn.execute(
            text(f"SELECT COUNT(*) FROM {table}")
        ).fetchone()[0]
        print(f"{table}: {count}")

print("\n🎉 SAMPLE PIPELINE DONE")
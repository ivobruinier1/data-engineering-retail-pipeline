import pandas as pd

print("\n🔍 ULTIMATE DATA CHECK START\n")

# =============================
# 1. LOAD CSV
# =============================
print("📥 Loading CSV...")

df = pd.read_csv("data/fact_sales.csv")

print("✔ Loaded")
print("Shape:", df.shape)

# =============================
# 2. COLUMN CHECK
# =============================
print("\n📌 Columns:")
for col in df.columns:
    print("-", col)

# check expected columns
expected = [
    "invoice",
    "stockcode",
    "description",
    "quantity",
    "invoicedate",
    "price",
    "customer_id",
    "country"
]

print("\n🧠 Missing columns check:")
for col in expected:
    if col not in df.columns:
        print("❌ MISSING:", col)
    else:
        print("✔ OK:", col)

# =============================
# 3. NULL CHECK
# =============================
print("\n🚨 NULL VALUES:")
print(df.isnull().sum())

# =============================
# 4. DUPLICATES CHECK
# =============================
print("\n🔁 DUPLICATES:")
print("Total duplicates:", df.duplicated().sum())

# =============================
# 5. DATA TYPES
# =============================
print("\n📊 DATA TYPES:")
print(df.dtypes)

# =============================
# 6. SAMPLE DATA
# =============================
print("\n👀 SAMPLE ROWS:")
print(df.head(10))

# =============================
# 7. SPECIFIC KEY CHECKS
# =============================
print("\n🔑 KEY FIELD TESTS:")

for col in ["invoice", "stockcode", "customer_id"]:
    if col in df.columns:
        print(f"{col} unique:", df[col].nunique())

# =============================
# 8. PROBLEM DETECTION
# =============================
print("\n⚠️ POTENTIAL ISSUES:")

if df.shape[0] == 0:
    print("❌ Dataset is EMPTY")

if df.duplicated().sum() > 0:
    print("⚠️ Duplicate rows detected")

if df.isnull().sum().sum() > 0:
    print("⚠️ NULL values exist")

print("\n🎯 CHECK COMPLETE")
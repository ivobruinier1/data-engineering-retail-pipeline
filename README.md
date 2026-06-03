# 📊 Retail Data Engineering Pipeline (PostgreSQL + Python ETL)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Data%20Warehouse-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-ETL-black.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red.svg)
![Status](https://img.shields.io/badge/Project-Completed-green.svg)
![ETL](https://img.shields.io/badge/Type-End--to--End%20ETL-orange.svg)

---

## 🚀 Project Overview

This project is a complete **end-to-end data engineering pipeline** that transforms raw e-commerce transactional data into a structured **PostgreSQL data warehouse** using Python.

It demonstrates:

- ETL pipeline design
- Data cleaning & transformation
- Star schema modeling
- Large-scale data loading
- Data quality checks

---

## 🏗️ Architecture

```
CSV → Python ETL → PostgreSQL → SQL Analytics
```

---

## 📦 Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- psycopg2

---

## 📁 Structure

```
etl/
data/
sql/
README.md
```

---

## ⚙️ ETL Flow

### Extract
Load CSV data using Pandas.

### Transform
- Remove duplicates
- Handle missing values
- Create revenue column
- Fix data types

### Load
Insert into PostgreSQL using SQLAlchemy.

---

## 🔍 Data Quality Checks

✔ Null checks  
✔ Duplicate checks  
✔ Row counts  
✔ Schema validation  

---

## 📊 Example Query

```sql
SELECT stockcode, SUM(quantity)
FROM fact_sales
GROUP BY stockcode
ORDER BY SUM(quantity) DESC
LIMIT 10;
```

---

## 🎯 Key Learnings

- ETL pipeline design
- PostgreSQL integration
- Data cleaning
- Star schema basics

---

## 👤 Author

Data engineering portfolio project.

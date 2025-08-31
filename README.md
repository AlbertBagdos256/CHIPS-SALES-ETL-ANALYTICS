# CHIPS-SALES-ETL-ANALYTICS
End-to-end pipeline that ingests chips sales from **AWS S3**, transforms with **Python (Pandas)** orchestrated by **Apache Airflow**, loads into **Snowflake**, and visualizes KPIs in **Power BI**.

## Stack
AWS S3 • Apache Airflow • Python • Snowflake • Power BI

## What It Does
- Extract CSVs from S3 (batched/daily)
- Clean + normalize (types, outliers, product catalog)
- Build warehouse schema (Dims + Fact)
- Publish Power BI dashboards (MoM, YTD, Top Brands)

## Key KPIs
- Total Sales, Quantity
- MoM & YoY Trends
- Top Brands / Products
- Basket Size, AOV

## Quick Start
1. `pip install -r requirements.txt`
2. Configure Airflow connections: `aws_default`, `snowflake_conn`
3. Create Snowflake schema: `sql/ddl/*.sql`
4. Trigger DAG: `dags/chips_etl_dag.py`
5. Connect Power BI to Snowflake (DirectQuery or Import)

## Warehouse Model
- `CHIP_DIM(Product_ID, Product_Name, Brand, Package_Size)`
- `CUSTOMERS_DIM(Customer_ID, Lifestage, Premium_Flag)`
- `TRANSACTIONS_FACT(Txn_ID, Customer_ID, Product_ID, Qty, Total_Sales, Txn_Date)`

## Screens
`/powerbi/screenshots/*`


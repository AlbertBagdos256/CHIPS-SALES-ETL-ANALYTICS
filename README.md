# 🥔 Chips Sales ETL & Analytics Pipeline  

## 📌 Overview  
This project demonstrates an **end-to-end ETL pipeline** for chips sales data. The pipeline extracts raw CSV files from **AWS S3**, performs **data cleaning and transformation** using **Python & Apache Airflow**, and loads the processed data into **Snowflake Data Warehouse**. Finally, the data is visualized in **Power BI** dashboards to track key performance indicators (KPIs) and business insights.  

The goal is to replicate a **real-world data engineering workflow**—from ingestion to reporting—ensuring **data quality, scalability, and actionable insights**.  

---

## ⚙️ Tech Stack  
- ☁️ **AWS S3** – Cloud storage for raw data  
- 🐍 **Python** – Data transformation & normalization  
- 🌬️ **Apache Airflow** – Workflow orchestration  
- ❄️ **Snowflake** – Cloud data warehouse  
- 📊 **Power BI** – Data visualization & KPI dashboards  

---

## 📊 KPIs Tracked  
- Total Sales Volume  
- Revenue by Region  
- Top-Selling Products  
- Month-over-Month Growth  
- Average Sales per Customer  

---

## 🔄 Data Flow  
```mermaid
flowchart LR
    A[S3: Raw Chips Sales Data] --> B[Airflow: ETL Orchestration]
    B --> C[Python: Data Cleaning & Normalization]
    C --> D[Snowflake: Data Warehouse]
    D --> E[Power BI: KPI Dashboards & Reports]

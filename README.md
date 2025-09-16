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
```
---
## 📊 Power BI Reports

<img width="2806" height="1526" alt="Screenshot 2025-09-15 224843" src="https://github.com/user-attachments/assets/f130d590-11e9-4081-a11b-845c45dc7af5" />
- Customers segmentation
<img width="2749" height="1521" alt="Screenshot 2025-09-15 224908" src="https://github.com/user-attachments/assets/939ff078-7b2f-47ad-8874-d5da2e59bb15" />
---

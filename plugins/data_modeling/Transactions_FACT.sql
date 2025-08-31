CREATE OR REPLACE TABLE CHIPS_DATA_MODEL.Transactions_FACT AS
SELECT TXN_ID AS Transaction_ID, 
       LYLTY_CARD_NBR AS Customer_ID, 
       PROD_NBR AS Product_ID, 
       PROD_QTY AS Product_Quantity, 
       TOT_SALES AS Total_Sales,
       DATEADD(DAY, Date, DATE '1899-12-30') AS Transaction_Date
FROM RAW_DATA.TRANSACTION_DATA 
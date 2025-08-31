CREATE OR REPLACE TABLE CHIPS_DATA_MODEL.CHIP_DIM AS
WITH chips_raw AS (
    SELECT DISTINCT 
        PROD_NBR AS Product_ID,
        REGEXP_REPLACE(PROD_NAME, '[0-9]+g', '') AS Product_Name,
        SPLIT_PART(PROD_NAME, ' ', 1) AS Brand_Name,
        REGEXP_SUBSTR(PROD_NAME, '[0-9]+') AS Package_Size
    FROM RAW_DATA.TRANSACTION_DATA
    WHERE NOT LOWER(PROD_NAME) LIKE '%sauce%'
      AND NOT LOWER(PROD_NAME) LIKE '%dip%'
      AND NOT LOWER(PROD_NAME) LIKE '%salsa%'
      AND NOT LOWER(PROD_NAME) LIKE '%mild%'
)
SELECT
    cr.Product_ID,
    cr.Product_Name,
    bm.clean_brand AS Product_Brand,
    cr.Package_Size AS Package_Size 
FROM chips_raw cr
LEFT JOIN CHIPS_DATA_MODEL.CLEAN_BRANDS bm
    ON cr.brand_name = bm.brand_name;

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from operators.extract_from_s3 import S3ToSnowflakeOperator
from operators.load_dimension import LoadDataModelOperator

# Default arguments
default_args = {
    'owner': 'albert',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Function Operator to send data from AWS s3 to Snowflake
def create_s3_to_snowflake_task(task_id, s3_key, table, schema='RAW_DATA', file_format='MY_CSV_FORMAT'):
    return S3ToSnowflakeOperator(
        task_id=task_id,
        aws_conn_id='aws_conn',# Airflow AWS connection ID
        snowflake_conn_id='snowflake_conn',
        s3_bucket='my-etl-csv-storage',# Your S3 bucket
        s3_key=s3_key,# Path in S3
        table=table, # Snowflake table
        file_format=file_format,# Snowflake file format
        schema=schema# Snowflake schema
    )


# DAG definition
with DAG(
    's3_to_snowflake_dag',
    default_args=default_args,
    description='Load data from S3 to Snowflake',
    schedule_interval=None,
    start_date=datetime(2025, 8, 12),
    catchup=False
) as dag:

    start_task = DummyOperator(task_id='start')
    # uploading raw csv file PURCHASE_BEHAVIOUR
    load_purchase_behaviour = create_s3_to_snowflake_task(
        task_id='load_purchase_behaviour',
        s3_key='QVI_purchase_behaviour.csv',
        table='PURCHASE_BEHAVIOUR'
    )
    # uploading raw csv file Transactions_data
    load_transactions = create_s3_to_snowflake_task(
        task_id='load_transactions',
        s3_key='QVI_transactions_data.csv',
        table='TRANSACTION_DATA'
    )
    # uploading Dimensional table of chips
    create_chip_dim = LoadDataModelOperator(
        task_id='create_chip_dim',
        snowflake_conn_id='snowflake_conn',
        sql_file_path='plugins/data_modeling/CHIPS_DIM.sql',
    )
    # uploading Dimensional table of sauses and dips
    create_sauces_dim = LoadDataModelOperator(
        task_id='create_sauces_dim',
        snowflake_conn_id='snowflake_conn',
        sql_file_path='plugins/data_modeling/Sauces_DIM.sql',
    )

    # uploading Dimensional table of customers's
    create_customers_dim = LoadDataModelOperator(
        task_id='create_customers_dim',
        snowflake_conn_id='snowflake_conn',
        sql_file_path='plugins/data_modeling/Customers_DIM.sql',
    )

    # uploading FACT table of transactions records
    create_transactions_fact = LoadDataModelOperator(
        task_id='create_transaction_fact',
        snowflake_conn_id='snowflake_conn',
        sql_file_path='plugins/data_modeling/Transactions_FACT.sql',
    )

    end_task = DummyOperator(task_id='end')
    
    
    # Define dependencies
    start_task >> [load_purchase_behaviour, load_transactions]
    load_purchase_behaviour >> [create_chip_dim, create_sauces_dim]
    load_transactions >> [create_chip_dim, create_sauces_dim]
    [create_chip_dim, create_sauces_dim] >> create_customers_dim
    create_customers_dim >> create_transactions_fact
    create_transactions_fact >> end_task



from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook

class LoadDataModelOperator(BaseOperator):
    """
    Custom Airflow operator to load dimension tables in Snowflake.
    Can execute either a SQL file or a raw SQL string.
    """
    
    def __init__(
        self,
        snowflake_conn_id: str = "",
        sql_query: str = None,     # Raw SQL string
        sql_file_path: str = None, # Path to .sql file
        table: str = None,         # Optional, only for logging
        *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.snowflake_conn_id = snowflake_conn_id
        self.sql_query = sql_query
        self.sql_file_path = sql_file_path
        self.table = table

    def execute(self, context):
        hook = SnowflakeHook(snowflake_conn_id=self.snowflake_conn_id)
        
        if self.sql_file_path:
            self.log.info(f"Reading SQL from file: {self.sql_file_path}")
            with open(self.sql_file_path, 'r') as f:
                sql_to_run = f.read()
        elif self.sql:
            sql_to_run = self.sql_query
        else:
            raise ValueError("Either 'sql' or 'sql_file_path' must be provided.")

        if self.table:
            self.log.info(f"Executing SQL for table: {self.table}")
        else:
            self.log.info("Executing SQL...")

        hook.run(sql_to_run)
        self.log.info("SQL execution completed.")

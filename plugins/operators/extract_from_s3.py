from airflow.models import BaseOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from airflow.exceptions import AirflowException


class S3ToSnowflakeOperator(BaseOperator):
    """
    Custom Airflow Operator to load data from AWS S3 into a Snowflake table
    using the COPY INTO command.
    """
    ui_color = '#87CEFA'  # Light blue in Airflow UI

    def __init__(self,
                 aws_conn_id: str,          # Airflow AWS connection ID
                 snowflake_conn_id: str,    # Airflow Snowflake connection ID
                 s3_bucket: str,
                 s3_key: str,
                 table: str,                # Snowflake target table
                 file_format: str,          # Snowflake file format name
                 schema: str,               # Snowflake schema
                 *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.aws_conn_id = aws_conn_id
        self.snowflake_conn_id = snowflake_conn_id
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.table = table
        self.file_format = file_format
        self.schema = schema

    def execute(self, context):
        self.log.info(f"Loading data from s3://{self.s3_bucket}/{self.s3_key} "
                      f"to Snowflake table {self.schema}.{self.table}")

        # Get AWS credentials from Airflow connection
        s3_hook = S3Hook(aws_conn_id=self.aws_conn_id)
        credentials = s3_hook.get_credentials()

        # Connect to Snowflake
        snowflake = SnowflakeHook(snowflake_conn_id=self.snowflake_conn_id)

        # Build COPY INTO command
        copy_sql = f"""
        COPY INTO {self.schema}.{self.table}
        FROM 's3://{self.s3_bucket}/{self.s3_key}'
        CREDENTIALS=(
            AWS_KEY_ID='{credentials.access_key}'
            AWS_SECRET_KEY='{credentials.secret_key}'
        )
        FILE_FORMAT = (FORMAT_NAME = {self.file_format})
        PURGE = FALSE;
        """

        self.log.info(f"Running COPY INTO SQL:\n{copy_sql}")
        try:
            snowflake.run(copy_sql)
            self.log.info(f"✅ Data successfully loaded into {self.schema}.{self.table}")
        except Exception as e:
            self.log.error(f"❌ Snowflake load failed: {e}")
            raise AirflowException(f"Snowflake load failed: {e}")

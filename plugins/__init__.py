from __future__ import division, absolute_import, print_function
from airflow.plugins_manager import AirflowPlugin
import operators
import data_modeling

# Define the plugin class
class ETLPlugin(AirflowPlugin):
    name = "my_etl_plugin"
    operators = [
        operators.S3ToSnowflakeOperator,
    ]
    helpers = [
        data_modeling.SqlQueries
    ]

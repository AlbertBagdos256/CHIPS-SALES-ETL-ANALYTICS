

class DataQualityOperator(BaseOperator):
    def __init__(self,
                 data_quality_checks = [],
                 aws_conn_id = "",
                 *args, **kwargs):
        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.data_quality_checks = data_quality_checks
        self.aws_conn_id = aws_conn_id
    def execute(self, context):
        pass



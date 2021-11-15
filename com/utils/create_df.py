from pyspark.sql.types import StructType,StructField, StringType, IntegerType

def get_df(spark):
    dept = [("Finance", 10),
            ("Marketing", 20),
            ("Sales", 30),
            ("IT", 40)
            ]
    deptColumns = StructType([
        StructField("dept_name", StringType(), True),
        StructField("count", IntegerType(), True),
    ])
    df1 = spark.createDataFrame(data=dept, schema=deptColumns)
    return df1
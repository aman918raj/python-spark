from com.utils.create_session import get_spark_session
from pyspark.sql.types import StructType,StructField, StringType, IntegerType

spark = get_spark_session("MyDatabricks-FirstJob")
dept = [("Finance",10),
        ("Marketing",20),
        ("Sales",30),
        ("IT",40)
      ]
deptColumns = StructType([
    StructField("dept_name", StringType(),True),
    StructField("count", IntegerType(),True),
])
df1 = spark.createDataFrame(data=dept, schema=deptColumns)
df1.show()
print(f"rec count : {df1.count()}")



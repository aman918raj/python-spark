from pyspark.sql import SparkSession
from create_df import get_df

spark = SparkSession.builder\
        .appName("databricks-Job")\
        .getOrCreate()



df1 = get_df(spark)
df1.show()
print(f"rec count : {df1.count()}")



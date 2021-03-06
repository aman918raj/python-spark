from pyspark.sql import SparkSession

spark = SparkSession.builder\
        .appName("databricks-Job")\
        .getOrCreate()

spark.sparkContext.addFile("dbfs:/FileStore/python-spark/com/utils/create_df.py")

from create_df import get_df

df1 = get_df(spark)
df1.show()
print(f"rec count : {df1.count()}")



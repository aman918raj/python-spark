from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import os
import sys
import subprocess


os.environ["hadoop.home.dir"] = "C:/Users/araj34/hadoop/bin/winutils.exe"
subprocess.run(["C:/Users/araj34/hadoop/bin/winutils.exe", "chmod", "777", "C:/tmp/hive"])
jdbc_driver_jar="C:/Users/araj34/Downloads/spark-mssql-connector_2.12-1.2.0.jar"
jdbc_url="jdbc:sqlserver://sql113372e1dv.database.windows.net:1433;database=sql113372e1dv;user=araj34@sql113372e1dv;password=Sep@2021;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30;"
spark = SparkSession.builder\
    .master("local")\
    .appName("Word Count")\
    .enableHiveSupport() \
    .config("spark.sql.warehouse.dir", "C:/Users/araj34/PycharmProjects/python-spark/spark-warehouse") \
    .config("spark.sql.shuffle.partitions", "10") \
    .config("spark.driver.extraClassPath", jdbc_driver_jar).getOrCreate()

input_path = "C:/Users/araj34/Documents/test.txt"

df1 = spark.read \
        .format("com.microsoft.sqlserver.jdbc.spark") \
        .option("url", jdbc_url) \
        .option("dbtable", "user_content_status") \
        .option("user", "araj34") \
        .option("password", "Sep@2021").load()

#df2 = df1.alias('df1_1').join(df1.alias('df1_2'), col('df1_1._c0') == col('df1_2._c0'), "inner")
df1.show()



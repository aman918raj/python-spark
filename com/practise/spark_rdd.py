from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import os
import sys
import subprocess


os.environ["HADOOP_HOME"] = "C:/Users/araj34/hadoop"
subprocess.run(["C:/Users/araj34/hadoop/bin/winutils.exe", "chmod", "777", "C:/tmp/hive"])
spark = SparkSession.builder\
    .appName("Word Count")\
    .enableHiveSupport() \
    .getOrCreate()

spark.sparkContext.addFile("file:///C:/Users/araj34/Downloads/utils.py")
from utils import hello_world

a = hello_world()
print(a)
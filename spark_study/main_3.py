import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName('rev').getOrCreate()
employee = [
    ("Radhika", 10),
    ("Kaavya", 20),
    ("Varnika", 30),
    ("Akshay", 40),
]

rdd = spark.sparkContext.parallelize(employee)

df = rdd.toDF()
df.printSchema()
df.show()

emp_columns = ["emp_name", "emp_id"]
df = rdd.toDF(emp_columns)
df.printSchema()
df.show(truncate=False)

emp_schema = StructType([
    StructField('emp_name', StringType(), True),
    StructField('emp_id', StringType(), True),
])

employee_df = spark.createDataFrame(data=employee, schema=emp_schema)
employee_df.printSchema()
employee_df.show(truncate=False)
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

import sys
sys.path.append('E:/retail-etl-platform/modules/')
import config

# 1. Start Spark Structured Streaming session: enables real-time windowed data processing
spark = SparkSession.builder.appName("Retail_Sales_Streaming_ETL").getOrCreate()

# 2. Define schema by reading one streaming input file - ensures all new files match
sample_file = config.STREAM_INPUT_DIR + 'sales_1970-01-01.csv'
schema = spark.read.csv(sample_file, header=True, inferSchema=True).schema

# 3. Set up a streaming DataFrame: watches folder for new CSV files
stream_df = spark.readStream.option("header", True).schema(schema).csv(config.STREAM_INPUT_DIR)

# 4. Streaming ETL transformation: aggregate sales by "MONTH" and "ITEM TYPE"
agg_df = stream_df.groupBy("YEAR", "MONTH", "ITEM TYPE")\
                  .agg(sum(col("RETAIL SALES")).alias("total_retail_sales"),
                       sum(col("WAREHOUSE SALES")).alias("total_warehouse_sales"),
                       sum(col("RETAIL TRANSFERS")).alias("total_retail_transfers"))

# 5. Output results to console for demo (swap to parquet/csv for production storage!)
query = agg_df.writeStream.outputMode("complete")\
    .format("console")\
    .option("truncate", False)\
    .start()

query.awaitTermination(120)  # Runs for 2 minutes: adjust as needed for demo/testing


# Optional: For persistent output, replace 'console' with 'parquet' and set a checkpoint location:
# .format("parquet").option("path", config.STREAM_OUTPUT).option("checkpointLocation", config.GCP_OUTPUT + "checkpoint/")

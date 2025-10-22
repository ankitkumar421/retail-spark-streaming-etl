import sys
sys.path.append('E:/retail-etl-platform/modules/')  # Add config folder to import path
import config                                      # Loads our central paths

from pyspark.sql import SparkSession

# Start Spark session: enables distributed data processing (cluster or local)
spark = SparkSession.builder.appName("Batch_ETL_Extract").getOrCreate()

# Step 1: Extract sales data
sales_df = spark.read.csv(config.SALES_FILE, header=True, inferSchema=True)
# Reads CSV as a distributed DataFrame for big-data scale.
# header=True uses CSV column headers; inferSchema=True auto-detects datatypes.

# Step 2: Extract customer data
customers_df = spark.read.csv(config.CUSTOMER_FILE, header=True, inferSchema=True)
# Also loads customers as its own DataFrame.

# Step 3: Show samples to confirm
print("Sales Data Sample:")
sales_df.show(5)         # Print first 5 rows of sales data

print("Customer Data Sample:")
customers_df.show(5)     # Print first 5 rows of customer data

# (Optional) Print schema for verification
sales_df.printSchema()      # Outputs column names and types for debugging
customers_df.printSchema()  # Shows structure of customer records

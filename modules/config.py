# config.py
# Centralizes all directory paths for your ETL pipelines

PROJECT_ROOT = 'E:/retail-etl-platform/'
DATA_DIR = "/home/jovyan/work/data/"
STREAM_INPUT_DIR = "/home/jovyan/work/data/streaming_input/"
AZURE_OUTPUT = PROJECT_ROOT + 'azure_blob/'
GCP_OUTPUT = "/home/jovyan/work/gcs_bucket/"
BATCH_OUTPUT = AZURE_OUTPUT + 'sales_analytics.parquet'
STREAM_OUTPUT = "/home/jovyan/work/data/streaming_output/"
CUSTOMER_FILE = DATA_DIR + 'customers.csv'
SALES_FILE = DATA_DIR + 'sales.csv'

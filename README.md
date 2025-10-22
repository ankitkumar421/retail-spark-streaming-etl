⚡ Retail Sales Streaming ETL
Real-Time ETL Pipeline with Apache Spark Structured Streaming

Build a real-time retail analytics pipeline using Spark Structured Streaming in JupyterLab.
This project ingests CSV files continuously, cleans and aggregates sales metrics, and streams instant insights — perfect for data teams who want live analytics with minimal latency.

✨ Features
Watches input folders for new CSV files automatically.

Parses timestamp columns for accurate time-based analytics.

Aggregates key metrics by item type and datetime in real time.

Runs seamlessly in Jupyter with an all-Python setup for flexible experimentation.

🏪 Use Case
Enable shop owners or analysts to view instant updates on sales, warehouse dispatches, and retail transfers — no waiting for daily batches or refresh cycles.

⚙️ How to Run
Start your Spark cluster and JupyterLab environment (or any Python setup with Spark installed).

Place new CSV files inside:

text
data/streaming_input/
Open and run the notebook:

text
retail_streaming_etl.ipynb
Watch your aggregated output stream live in the Jupyter console.

🧾 Example Input
text
YEAR,ITEM TYPE,RETAIL SALES,WAREHOUSE SALES,RETAIL TRANSFERS
2023-02-01 00:00:00.000002023,WINE,8,12,3
2023-02-01 00:00:00.000002023,BEER,2,5,1
📊 Example Output
text
+-------------------+---------+-------------------+---------------------+----------------------+
|SALE_DATETIME      |ITEM TYPE|total_retail_sales |total_warehouse_sales|total_retail_transfers|
+-------------------+---------+-------------------+---------------------+----------------------+
|2023-02-01 00:00:00|WINE     |8                  |12                   |3                     |
|2023-02-01 00:00:00|BEER     |2                  |5                    |1                     |
+-------------------+---------+-------------------+---------------------+----------------------+
🧠 Tech Stack
Apache Spark Structured Streaming

Python

JupyterLab

🧩 Project Structure
Folder/File	Description
data/	Incoming CSVs to be streamed
modules/	Custom ETL logic and Spark functions
scripts/	Preprocessing and simulation scripts
retail_streaming_etl.ipynb	Main notebook streaming demo
split_sales_for_streaming.py	Helper script to simulate real-time ingestion
docker-compose.yml	Container setup for Spark services
🚀 Future Enhancements
Integration with cloud data sources (GCS / AWS S3 / Azure).

Real-time dashboards for analytics.

Kafka or Delta Lake streaming sink.

🧩 License
Distributed under the MIT License.
Use freely for commercial or educational projects.

⭐ Contribute
If you liked this project:

Star the repository ⭐

Share feedback or ideas via Issues

Submit PRs for enhancements

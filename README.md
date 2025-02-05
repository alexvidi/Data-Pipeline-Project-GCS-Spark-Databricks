Data Pipeline: GCS, Spark, and Databricks
This project implements a data pipeline that ingests data from a public API, processes it with Apache Spark in Databricks Community Edition, and stores the results in Google Cloud Storage (GCS). It focuses on optimizing data storage and processing in a scalable environment.

Pipeline Stages
Data Ingestion
The data is ingested from a public API and stored in Google Cloud Storage (GCS). This step uses free-tier GCS storage to store data in formats like Parquet for optimization.

Data Processing with Apache Spark
The data stored in GCS is processed using Apache Spark on Databricks Community Edition. This step focuses on transforming and preparing the data for further analysis.

Technologies Used
Google Cloud Storage (GCS): For storing raw data in the cloud.
Apache Spark (Databricks Community Edition): For processing data at scale.
Python: For coding the data pipeline and managing API requests.
The goal of this project is to demonstrate a scalable and efficient data pipeline that can handle large datasets in a cloud environment. It highlights how cloud storage and distributed computing can be leveraged to process data with minimal cost.


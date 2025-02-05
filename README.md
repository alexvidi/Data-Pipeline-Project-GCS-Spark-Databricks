# Data Pipeline: GCS, Spark, and Databricks

This project demonstrates how to create a scalable data pipeline using Google Cloud Storage (GCS), Apache Spark, and Databricks Community Edition. The pipeline ingests data from a public API, processes it using Spark for transformations, and stores the processed data in GCS. The primary objective is to create a cost-effective, efficient, and scalable data processing pipeline leveraging cloud technologies.

## Pipeline Overview

The pipeline is divided into the following stages:

### 1. Data Ingestion

Data is ingested from a public API (for example, DummyJSON) and uploaded to Google Cloud Storage (GCS). GCS is used to store raw data, and the free tier is utilized to minimize costs. The data is stored in **Parquet format** for optimized storage, ensuring efficient read/write operations. This format is chosen due to its compact size and the ease with which Spark can process it.

Key steps:
- Data is fetched from the public API.
- The data is stored in a **GCS bucket**.
- Files are saved in **Parquet format** to optimize storage space and processing time.

### 2. Data Processing with Apache Spark on Databricks

Once the data is ingested into GCS, Apache Spark is used to process and transform the data. Apache Spark is an open-source unified analytics engine for big data processing, and it allows the handling of large datasets efficiently. The processing happens in **Databricks Community Edition**, which provides a free platform for running Spark workloads.

Key steps:
- Data is read from **GCS** using Spark.
- Transformations and data cleaning are performed using **PySpark**.
- The processed data is stored back in **GCS**.

### 3. Data Storage in GCS

After processing, the transformed data is saved back to Google Cloud Storage in the **processed_data** folder, ready for further analysis or use by other systems. The data is kept in Parquet format to continue optimizing storage space.

### 4. (Optional) Future Steps

The pipeline can be extended in the future with the following features:
- **Data Transformation with dbt**: dbt can be used for advanced data transformations in the pipeline.
- **Big Data Analysis with Google BigQuery**: BigQuery can be integrated to perform scalable SQL-based analysis on the data.
- **Orchestration with Apache Airflow**: Apache Airflow can be used for orchestrating and scheduling the pipeline, enabling automated data workflows.

## Technologies Used

- **Google Cloud Storage (GCS)**: GCS is used for storing the raw and processed data. The free-tier storage in GCS is utilized to minimize costs.
- **Apache Spark (Databricks Community Edition)**: Spark is used for processing large-scale datasets in a distributed environment. Databricks Community Edition is used to run Spark jobs without incurring additional costs.
- **Python & PySpark**: Python is used to script the data pipeline, with PySpark being utilized for distributed data processing.
- **Parquet**: Parquet is the format used to store the data in GCS due to its columnar storage format and compression efficiency, making it well-suited for analytical workloads.

## Project Structure

The project is structured as follows:

- `ingest_data.py`: A Python script that handles the ingestion of data from the public API and uploads it to GCS.
- `process_data.py`: A Python script that reads the raw data from GCS, processes it with Spark, and writes the processed data back to GCS.
- `README.md`: This file, containing details about the project and how to use it.
- `/data`: A folder containing the raw data files (for local testing).
- `/notebooks`: Databricks notebooks containing Spark code for data processing.

## Setup and Usage

1. **Google Cloud Storage Setup**: Create a GCS bucket to store the raw and processed data. Update the script with your GCS bucket name.
2. **Databricks Setup**: Use Databricks Community Edition to process the data with Apache Spark. You can use the Databricks notebooks for running Spark jobs.
3. **Run the Python Scripts**: 
   - Run `ingest_data.py` to fetch data from the public API and store it in GCS.
   - Run `process_data.py` to read, process, and store the data back in GCS.
4. **Optional**: Add dbt and Google BigQuery for advanced transformations and data analysis.

## Conclusion

This project showcases how to build a simple yet scalable data pipeline that ingests, processes, and stores data in a cloud environment using open-source tools. The focus is on cost-effective solutions, using free-tier resources like Google Cloud Storage and Databricks Community Edition. The project can easily be extended with more advanced features like orchestration, advanced data transformation, and big data analysis.



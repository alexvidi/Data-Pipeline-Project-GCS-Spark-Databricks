import os
from google.cloud import storage

# Set bucket name (replace with your actual bucket name)
BUCKET_NAME = "data-engineering-bucket-alexvidi"

def upload_to_gcs(bucket_name, source_folder):
    """Uploads all Parquet files from the source folder to the specified GCS bucket."""
    
    # Initialize Google Cloud Storage client
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    
    # Loop through all files in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith(".parquet"):  # Only upload Parquet files
            file_path = os.path.join(source_folder, filename)
            blob = bucket.blob(filename)

            # Upload file to GCS
            blob.upload_from_filename(file_path)
            print(f" Uploaded {filename} to gs://{bucket_name}/{filename}")

def main():
    """Main function to execute the upload process."""
    source_folder = "data"  # Local folder where Parquet files are stored
    upload_to_gcs(BUCKET_NAME, source_folder)

if __name__ == "__main__":
    main()

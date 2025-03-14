import os
import json
from google.cloud import storage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load configuration from JSON
CONFIG_PATH = "config/config.json"
with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)

# Define constants
BUCKET_NAME = config.get("gcs_bucket", "")
DATA_FOLDER = config.get("data_folder", "data")

def upload_to_gcs(bucket_name, source_folder):
    """Uploads all Parquet files from the source folder to the specified GCS bucket."""
    if not bucket_name:
        print("ERROR: GCS bucket name is missing in config.json.")
        return
    
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    
    for filename in os.listdir(source_folder):
        if filename.endswith(".parquet"):  # Only upload Parquet files
            file_path = os.path.join(source_folder, filename)
            blob = bucket.blob(filename)
            try:
                blob.upload_from_filename(file_path)
                print(f"Uploaded {filename} to gs://{bucket_name}/{filename}")
            except Exception as e:
                print(f"ERROR: Failed to upload {filename} to GCS: {e}")

def main():
    """Main function to execute the upload process."""
    print("Starting upload process to GCS...")
    if not os.path.exists(DATA_FOLDER):
        print(f"ERROR: Data folder {DATA_FOLDER} does not exist. Aborting upload.")
        return
    upload_to_gcs(BUCKET_NAME, DATA_FOLDER)
    print("Upload process completed.")

if __name__ == "__main__":
    main()



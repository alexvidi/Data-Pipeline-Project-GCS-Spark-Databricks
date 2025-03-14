import os
import requests
import pandas as pd
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load configuration from JSON
CONFIG_PATH = "config/config.json"
with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)

# Define constants
DATA_FOLDER = config.get("data_folder", "data")
API_URLS = config.get("api_urls", {})

def create_data_folder():
    """Creates the data directory if it does not exist."""
    os.makedirs(DATA_FOLDER, exist_ok=True)
    print(f"Data folder checked/created: {DATA_FOLDER}")

def fetch_data(url):
    """Fetches data from the given API URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Fetching data from {url}: {e}")
        return None

def save_to_parquet(data, filename):
    """Saves data to a Parquet file."""
    if data:
        df = pd.DataFrame(data)
        file_path = os.path.join(DATA_FOLDER, f"{filename}.parquet")
        df.to_parquet(file_path, engine="pyarrow", index=False)
        print(f"Data saved to: {file_path}")
    else:
        print(f"WARNING: No data to save for {filename}")

def main():
    """Main execution function."""
    print("Starting data extraction...")
    create_data_folder()
    
    for key, url in API_URLS.items():
        print(f"Fetching data from {url}")
        data = fetch_data(url)
        if data and key in data:
            save_to_parquet(data[key], key)
    
    print("Data extraction and storage completed.")

if __name__ == "__main__":
    main()

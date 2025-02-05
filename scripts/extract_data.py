import os
import requests
import pandas as pd

def create_data_folder():
    """Creates the 'data' directory if it does not exist."""
    os.makedirs("data", exist_ok=True)

def fetch_data(url):
    """Makes a GET request to the given URL and returns the JSON response."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data from {url}: {response.status_code}")
        return None

def save_to_parquet(data, filename):
    """Saves the given data as a Parquet file in the 'data' directory."""
    df = pd.DataFrame(data)
    file_path = f"data/{filename}.parquet"
    df.to_parquet(file_path, engine="pyarrow", index=False)
    print(f" Data saved to: {file_path}")

def main():
    """Orchestrates the extraction and storage of data."""
    print(" Starting data extraction...")
    
    create_data_folder()
    
    urls = {
        "products": "https://dummyjson.com/products",
        "users": "https://dummyjson.com/users",
        "carts": "https://dummyjson.com/carts"
    }
    
    for key, url in urls.items():
        data = fetch_data(url)
        if data:
            save_to_parquet(data[key], key)
    
    print(" Data extraction and storage completed.")

if __name__ == "__main__":
    main()
import pandas as pd
import requests
from datetime import datetime
from sqlalchemy import create_engine

# --- 1. EXTRACT ---
def extract_data():
    print("Fetching data from API...")
    # Free Crypto API (CoinGecko)
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API Request failed with status code {response.status_code}")

# --- 2. TRANSFORM ---
def transform_data(raw_data):
    print("Transforming & Cleaning data...")
    df = pd.DataFrame(raw_data)
    
    cols = ['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume', 'last_updated']
    df = df[cols]

    df = df.dropna(subset=['current_price'])

    df['processed_at'] = datetime.now()
    
    # Data Formatting
    df['symbol'] = df['symbol'].str.upper()
    
    return df

# --- 3. LOAD ---
def load_data(df):
    print("Loading data to PostgreSQL / Storage...")
    
    df.to_csv("cleaned_crypto_data.csv", index=False)
    print("Data successfully processed and loaded!")

if __name__ == "__main__":
    try:
        raw = extract_data()
        transformed_df = transform_data(raw)
        load_data(transformed_df)
        print(f"ETL Execution Successful! Processed {len(transformed_df)} records.")
    except Exception as e:
        print(f"ETL Pipeline Error: {e}")
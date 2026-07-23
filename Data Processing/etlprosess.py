import pandas as pd
from sqlalchemy import create_engine

print("========= Extract Data =========")
# Create dummy data 
data = {
    'Crypto_Name': ['Bitcoin', 'Ethereum', 'Cardano', None, 'Solana'],
    'Price_USD': [65000.0, 35000.0, 0.45, 100.0, None],
    'Volume': [1000, 2000, 5000, None, 1500]
}

# Create Pandas DataFrame
df = pd.DataFrame(data)
print(df)

print("========= Transforme Data =========")
# Missing / Null value clearing
df_cleaned = df.dropna()
print(df_cleaned)

print("========= Load Data =========")
# PostgreSQL Connection string
db_user = "postgres"
db_password = "12345" 
db_host = "localhost"
db_port = "5432"
db_name = "crypto_db"

try: 
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    
    # Save DataFrame in PostgreSQL
    df_cleaned.to_sql('crypto_table', con=engine, if_exists='replace', index=False)
    print("Sucsessfuly Data tranfer to DB!")

except Exception as e:
    print("Error to Loading data!")
    print(e)
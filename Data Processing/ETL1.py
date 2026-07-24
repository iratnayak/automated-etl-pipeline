import pandas as pd
from sqlalchemy import create_engine

print("========= Extract ==========")
df = pd.read_csv('sales_data.csv')
print(df)

print("========= Tranceforme Data ==========")
# 1. Quantity එකේ හිස්තැන් (NaN) තියෙනවා නම්, ඒක '1' විදිහට හදනවා
df['Quantity'] = df ['Quantity'].fillna(1)

# 2. Price එකේ හිස්තැන් තියෙනවා නම්, ඒ සම්පූර්ණ පේළියම අයින් කරනවා
df = df.dropna(subset= ['Price'])

# 3. Date එකේ හිස්තැන් තියෙනවා නම්, ඒකට '2023-01-01' දානවා
df['Date'] = df ['Date'].fillna('2023-01-01')

# 4. අලුත් Column එකක් හදනවා: Total_Sales = Quantity * Price
df['Total_Sale'] = df['Quantity'] * df['Price']

print("--- Cleaned Data (Total_Sales එකත් සමග) ---")
print(df)

print("========= Load Data ==========")
db_user = "postgres"
db_password = "12345" 
db_host = "localhost"
db_port = "5432"
db_name = "crypto_db"

try: 
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

    # 'sales_table' කියලා අලුත් Table එකකට Data ටික Save කරනවා
    df.to_sql('sales_table', con=engine, if_exists='replace', index=False)
    print("✅ Successfully Loaded Data to PostgreSQL 'sales_table'!")

except Exception as e:
    print("⚠️ Error Loading data!")
    print(e)
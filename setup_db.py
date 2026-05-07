import pandas as pd
import sqlite3

print("Reading Excel files...")

# Read Table 1 - Assets
df_assets = pd.read_excel(
    'Monthly authorised deposit-taking institution statistics March 2026.xlsx',
    sheet_name='Table 1', skiprows=2)

# Check actual column count
print("Actual columns:", df_assets.shape[1])
print("Column names:", df_assets.columns.tolist())

# Rename based on actual 8 columns
df_assets.columns = ['bank_name', 'cash_deposits', 'trading_securities', 
                      'investment_securities', 'net_acceptances', 
                      'total_loans', 'total_assets', 'total_securitised_assets']

df_assets = df_assets.dropna(subset=['bank_name'])
df_assets['date'] = '2026-03-31'

# Create SQLite database
conn = sqlite3.connect('apra_banking.db')
df_assets.to_sql('bank_assets', conn, if_exists='replace', index=False)

print("\nDatabase created successfully!")
print("\nTop 5 banks by total assets:")
result = pd.read_sql_query("""
    SELECT bank_name, total_assets 
    FROM bank_assets 
    WHERE total_assets IS NOT NULL 
    AND total_assets > 0
    ORDER BY total_assets DESC 
    LIMIT 5
""", conn)
print(result)
conn.close()
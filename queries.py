import pandas as pd
import sqlite3

conn = sqlite3.connect('apra_banking.db')

print("=" * 60)
print("APRA BANKING ANALYSIS — MARCH 2026")
print("=" * 60)

# Query 1: Top 10 banks by total assets
print("\n1. TOP 10 BANKS BY TOTAL ASSETS (AUD millions)")
print("-" * 60)
q1 = pd.read_sql_query("""
    SELECT 
        bank_name,
        ROUND(total_assets, 1) as total_assets_m,
        ROUND(total_assets * 100.0 / SUM(total_assets) OVER(), 2) as market_share_pct
    FROM bank_assets
    WHERE total_assets > 0
    AND bank_name != 'TOTAL'
    ORDER BY total_assets DESC
    LIMIT 10
""", conn)
print(q1.to_string(index=False))

# Query 2: Loan to asset ratio
print("\n2. LOAN TO ASSET RATIO — TOP 10 BANKS")
print("-" * 60)
q2 = pd.read_sql_query("""
    SELECT 
        bank_name,
        ROUND(total_loans, 1) as total_loans_m,
        ROUND(total_assets, 1) as total_assets_m,
        ROUND(total_loans * 100.0 / total_assets, 1) as loan_to_asset_ratio
    FROM bank_assets
    WHERE total_assets > 0
    AND total_loans > 0
    AND bank_name != 'TOTAL'
    ORDER BY total_assets DESC
    LIMIT 10
""", conn)
print(q2.to_string(index=False))

# Query 3: Investment securities analysis
print("\n3. INVESTMENT SECURITIES — TOP 10 BANKS")
print("-" * 60)
q3 = pd.read_sql_query("""
    SELECT 
        bank_name,
        ROUND(investment_securities, 1) as investment_securities_m,
        ROUND(investment_securities * 100.0 / total_assets, 1) as inv_to_asset_pct
    FROM bank_assets
    WHERE total_assets > 0
    AND investment_securities > 0
    AND bank_name != 'TOTAL'
    ORDER BY investment_securities DESC
    LIMIT 10
""", conn)
print(q3.to_string(index=False))

# Query 4: Big 4 vs rest of market
print("\n4. BIG 4 vs REST OF MARKET")
print("-" * 60)
q4 = pd.read_sql_query("""
    SELECT 
        CASE 
            WHEN bank_name IN (
                'Commonwealth Bank of Australia',
                'Westpac Banking Corporation', 
                'National Australia Bank Limited',
                'Australia and New Zealand Banking Group Limited'
            ) THEN 'Big 4'
            ELSE 'Other Banks'
        END as bank_group,
        COUNT(*) as num_banks,
        ROUND(SUM(total_assets), 1) as total_assets_m,
        ROUND(SUM(total_loans), 1) as total_loans_m
    FROM bank_assets
    WHERE total_assets > 0
    AND bank_name != 'TOTAL'
    GROUP BY bank_group
    ORDER BY total_assets_m DESC
""", conn)
print(q4.to_string(index=False))

conn.close()
print("\nAnalysis complete!")
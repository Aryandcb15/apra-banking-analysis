# APRA Banking Sector Analysis

## Overview
SQL-based analysis of the Australian banking sector using real regulatory 
data published by the Australian Prudential Regulation Authority (APRA). 
This project was chosen deliberately — after speaking with an industry 
professional at ANZ who confirmed SQL is used daily in corporate finance 
teams, and after my own job market analysis showed SQL appears in 60%+ 
of Australian finance analyst job listings.

## Tools Used
- Python (pandas, sqlite3, sqlalchemy) — data extraction and loading
- SQL (SQLite) — analytical queries
- APRA MADIS Dataset — official Australian banking regulatory data (March 2026)

## Key Findings
- The Big 4 banks (CBA, Westpac, NAB, ANZ) control 70% of total Australian 
  banking assets — just 4 institutions out of 119
- Commonwealth Bank leads with 20.52% market share and $1.2 trillion in assets
- Norfina has the highest loan-to-asset ratio at 77.2%, indicating aggressive 
  lending relative to its asset base
- HSBC Australia holds 22.9% of its assets in investment securities — 
  significantly higher than the Big 4 average of ~8%
- United Overseas Bank holds 44.5% of assets in investment securities, 
  suggesting a highly conservative lending strategy

## SQL Concepts Demonstrated
- Window functions (market share % using SUM OVER())
- CASE WHEN statements for bank segmentation
- Aggregate functions (SUM, COUNT, ROUND)
- Filtering and sorting with WHERE and ORDER BY
- GROUP BY for Big 4 vs market comparison

## Results
The following CSV files contain the query outputs and can be viewed directly on GitHub:

- `results_top10_banks_by_assets.csv` — Top 10 Australian banks ranked by total assets with market share %
- `results_loan_to_asset_ratio.csv` — Loan to asset ratios across the top 10 banks
- `results_investment_securities.csv` — Investment securities holdings and % of total assets
- `results_big4_vs_market.csv` — Big 4 banks vs rest of market comparison

## Files
- `setup_db.py` — loads APRA Excel data into a SQLite database
- `queries.py` — analytical SQL queries with business insights
- `apra_banking.db` — SQLite database
- Excel files — raw APRA MADIS data (March 2026 + back-series 2019–2026)
- Glossary PDF — APRA data dictionary

## Data Source
Australian Prudential Regulation Authority (APRA) — Monthly Authorised 
Deposit-taking Institution Statistics (MADIS), March 2026
https://www.apra.gov.au/monthly-authorised-deposit-taking-institution-statistics

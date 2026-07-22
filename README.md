# Automated Data Integration & ETL Pipeline

An automated Python-based ETL (Extract, Transform, Load) pipeline designed to extract real-time market data via REST APIs, apply data validation and cleansing using Pandas, and structure data for database ingestion and analytical reporting.

## 🚀 Key Features
- **Extract:** Fetches live multi-source datasets via REST APIs.
- **Transform:** Cleans missing values, standardizes schemas, and adds audit timestamps using Pandas.
- **Data Validation:** Implements automated null checks and datatype assertions.
- **Load:** Ingests cleaned datasets into PostgreSQL for downstream analytics.

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Pandas, Requests, SQLAlchemy
- **Database:** PostgreSQL
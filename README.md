# E-Commerce Analytics Platform

An end-to-end data pipeline and AI-driven analytics platform analyzing 100K+ real orders from Olist, Brazil's largest e-commerce marketplace.

## 🛠️ Tech Stack

- **Data Engineering:** Python (Pandas, SQLAlchemy), Azure Blob Storage
- **Data Warehouse:** Azure SQL Database (Star Schema)
- **Business Intelligence:** Power BI, Tableau Public
- **AI/NLP:** Claude API (Haiku) for multilingual sentiment classification

## 🏗️ Architecture

The project follows the **Medallion Architecture**:

1. **Raw (Bronze):** Ingestion of 9 Kaggle datasets into Azure Blob Storage.
2. **Transform (Silver):** Data cleaning and feature engineering using Python.
3. **Warehouse (Gold):** Star Schema modeling (1 Fact, 4 Dimensions) in Azure SQL.
4. **Presentation:** Interactive dashboards in Power BI and Tableau.

## 📈 Key Insights

- **The 3-Day Rule:** 1-star review rates jump from **19% to 54%** once a delivery is over 3 days late.
- **AI Discovery:** Text analysis revealed **"Wrong/Missing Item" (37%)** as the top complaint, a fulfillment issue invisible in structured data.
- **Logistics Gap:** Northern states (e.g., RR) average **29-day delivery** vs. the 12-day national average.

## 🔗 Links

- **[Live Dashboard](https://public.tableau.com/app/profile/jo.f5042/viz/eCommerceAnalysis_17784694679280/OlistE-CommerceAnalytics)**
- **[Dataset Source](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)**

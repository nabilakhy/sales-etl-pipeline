# End-to-End Sales ETL Pipeline

A beginner-friendly end-to-end Data Engineering project that extracts, transforms, and loads retail sales data into PostgreSQL using Python and Pandas.

## Project Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using the Sample Superstore dataset.

The pipeline processes raw sales data, performs data cleaning and transformation, loads the processed data into PostgreSQL, and validates the results to ensure data quality.

## Architecture

```text
Raw CSV Dataset
      |
      v
   EXTRACT
   (Pandas)
      |
      v
  TRANSFORM
  - Remove duplicates
  - Convert date columns
  - Convert numeric columns
  - Calculate delivery_days
  - Calculate profit_margin
      |
      v
  Processed CSV
      |
      v
    LOAD
  (SQLAlchemy)
      |
      v
  PostgreSQL
  clean_transactions
      |
      v
  VALIDATE
  - Row count
  - Empty IDs
  - NULL values
  - Invalid quantity
```

## Dataset

- **Source:** [Sample Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Original records:** 9,994 rows
- **Original columns:** 21
- **Processed columns:** 23

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- psycopg2
- python-dotenv
- SQL

## Project Structure

```text
sales-etl-pipeline/
├── data/
│   ├── raw/
│   │   └── Sample - Superstore.csv
│   └── processed/
│       └── clean_sales.csv
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── validate.py
│   ├── main.py
│   └── inspect_data.py
├── sql/
│   ├── create_tables.sql
│   └── sales_analysis.sql
├── logs/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Data Transformation

The transformation process includes:

1. Removing duplicate records.
2. Converting Order Date and Ship Date into datetime format.
3. Ensuring numeric columns use appropriate data types.
4. Calculating delivery duration in days.
5. Calculating row-level profit margin.

Two additional columns are created:

- `delivery_days`: Number of days between order and shipment.
- `profit_margin`: Profit divided by sales, multiplied by 100.

Negative profit values are retained because they represent business losses and are meaningful for sales analysis.

## Data Loading

The processed dataset is loaded into PostgreSQL.

- **Database:** sales_etl_db
- **Table:** clean_transactions
- **Loaded records:** 9,994

SQLAlchemy is used to establish the database connection and load the processed data.

## Data Validation

The pipeline performs the following validation checks:

| Validation | Result |
|---|---|
| Row count matches expected records | PASS |
| No empty Order ID | PASS |
| No empty Product ID | PASS |
| No NULL Sales | PASS |
| No NULL Profit | PASS |
| No invalid Quantity | PASS |

**Final validation result: 6/6 checks passed.**

## SQL Analytics

The project also includes SQL queries to explore:

1. Overall sales performance.
2. Monthly sales and profit trends.
3. Sales and profit by product category.
4. Top 10 products by sales.
5. Sales performance by region.
6. Loss-making product subcategories.

All analytical queries are available in `sql/sales_analysis.sql`.

## Business Insights

Based on the analysis of 9,994 sales transaction records, several business insights were identified:

### 1. Overall Business Performance

- Total sales reached **$2,297,200.86**.
- Total profit reached **$286,397.02**.
- Overall profit margin was **12.47%**.

The business generated positive overall profit, although profitability varied across product categories and regions.

### 2. Monthly Sales and Profit Trends

- **November 2017** recorded the highest monthly sales, reaching **$118,447.83**.
- **December 2016** recorded the highest monthly profit at **$17,885.31**.
- **January 2015** recorded the lowest monthly profit at **-$3,281.01**.

This indicates that the month with the highest sales does not necessarily generate the highest profit.

### 3. Product Category Performance

| Category | Sales | Profit | Profit Margin |
|---|---:|---:|---:|
| Technology | $836,154.03 | $145,454.95 | 17.40% |
| Office Supplies | $719,047.03 | $122,490.80 | 17.04% |
| Furniture | $741,999.80 | $18,451.27 | 2.49% |

**Key insight:** Technology generated the highest sales and profit, while Furniture had the lowest profit margin despite contributing substantial sales.

### 4. Regional Performance

| Region | Sales | Profit | Profit Margin |
|---|---:|---:|---:|
| West | $725,457.82 | $108,418.45 | 14.94% |
| East | $678,781.24 | $91,522.78 | 13.48% |
| Central | $501,239.89 | $39,706.36 | 7.92% |
| South | $391,721.91 | $46,749.43 | 11.93% |

**Key insight:** The West region contributed the highest sales and profit, while Central had the lowest profit margin.

### 5. Top-Selling Products

The Canon imageCLASS 2200 Advanced Copier was the highest-selling product, generating **$61,599.82** in sales and **$25,199.93** in profit.

However, high sales do not always guarantee positive profit. For example, the Cisco TelePresence System EX90 generated $22,638.48 in sales but recorded a loss of $1,811.08.

### 6. Loss-Making Product Subcategories

Three product subcategories recorded negative total profit:

| Subcategory | Sales | Profit |
|---|---:|---:|
| Tables | $206,965.53 | -$17,725.48 |
| Bookcases | $114,880.00 | -$3,472.56 |
| Supplies | $46,673.54 | -$1,189.10 |

Combined, these three subcategories generated a loss of **$22,387.14**.

**Key insight:** Tables represented the largest loss among the identified subcategories and may require further investigation into pricing, discount strategies, and operating costs.

### Business Recommendations

Based on these findings:

1. Review Furniture pricing and discount strategies to improve profitability.
2. Investigate the Central region's lower profit margin.
3. Evaluate loss-making products and subcategories to identify potential causes.
4. Analyze monthly sales patterns to support inventory and promotional planning.
5. Monitor profit alongside revenue when evaluating product performance.

*Note: These findings are based on the provided Sample Superstore dataset and represent exploratory analysis rather than verified real-world business performance.*

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/sales-etl-pipeline.git
cd sales-etl-pipeline
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file based on `.env.example` and configure your local PostgreSQL credentials.

### 5. Create the PostgreSQL database

Create a database named `sales_etl_db` in PostgreSQL.

### 6. Run the pipeline

```bash
python src/main.py
```

## Project Status

**Completed — MVP**

This project was developed as a practical learning project to understand fundamental Data Engineering concepts, including ETL processes, data transformation, relational database loading, and data validation.

## Author

**Nabila Khyarotunnisa**

Aspiring Data Engineer | Informatics Engineering Graduate

- GitHub: [github.com/nabilakhyarotunnisa](https://github.com/nabilakhyarotunnisa)
- Portfolio: [nabilakhy.my.id](https://nabilakhy.my.id)

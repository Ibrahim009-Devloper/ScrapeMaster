# 🛒 Multi website Data Scraping & Automation Pipeline

This is a professional, modular data scraping and processing framework built with **Python** and **Playwright**. It automates the extraction of product data from Amazon, cleans it, and exports it into structured formats.

---

## 🏗 Project Structure

```text
├── config/
│   └── setting.py             # Global configurations & constants
├── Data/
│   ├── Row_data/              # Raw extracted data (Unprocessed)
│   ├── proceced_data/         # Cleaned and structured data
│   └── export_data/           # Final CSV/Excel files for delivery
├── Data_cleaner/
│   └── amazon_product_data_cleaner.py  # Data cleaning logic
├── logs/                      # Runtime execution logs
├── pipline/
│   └── run_amazon.py          # Main Execution Script (Entry Point)
├── scrapers/
│   └── amazon/
│       ├── product_link_scraper.py # Stage 1: Collect product URLs
│       └── product_info_scraper.py # Stage 2: Extract details from URLs
├── utils/
│   ├── browser.py             # Browser driver factory
│   ├── parser.py              # HTML Parsing logic
│   ├── server.py              # Proxy/Server configurations
│   └── logger.py              # Custom logging setup
├── requirements.txt           # Project dependencies
└── README.md
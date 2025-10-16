# Remote Work Tracker BI Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project%20Status-Active-success)
![Power BI](https://img.shields.io/badge/BI%20Tool-Power%20BI-yellow)
![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange)

## Project Overview

This project demonstrates a comprehensive Business Intelligence (BI) solution for tracking remote job postings. It encompasses web scraping (or API data collection), Extract, Transform, Load (ETL) processes, database management, and utility scripts, culminating in a dataset suitable for trend analysis and dashboard creation (e.g., in Power BI). The goal is to provide data-driven insights into the remote job market.

## Project Components

The project is organized into several key components:

1. **Web Scraping/API Data Collection**: Python script to gather remote job data.
2. **ETL Process**: Python script to clean, transform, and load the collected data.
3. **Database Management**: Python script for interacting with a SQLite database.
4. **Utility Functions**: Python script for common helper functions like logging.
5. **Jupyter Notebooks**: Interactive notebooks for demonstrating and explaining the code.

## Setup and Installation

To set up and run this project locally, follow these steps:

### Prerequisites

* Python 3.8+
* `pip` (Python package installer)

### 1. Clone the Repository

```bash
git clone <repository_url>
cd remote-work-tracker-bi
```

### 2. Install Dependencies

Install the required Python libraries using `pip`:

```bash
pip install pandas requests beautifulsoup4 ipython
```

### 3. Data Acquisition (Web Scraping/API)

Run the API scraper to collect the initial dataset. This will generate `remotive_jobs_extended.csv`.

```bash
python3.11 remotive_api_scraper.py
```

### 4. Run the ETL Process

Execute the ETL script to process the `remotive_jobs_extended.csv` file and load the data into the SQLite database (`remote_jobs.db`).

```bash
python3.11 etl_script.py
```

## Usage

### Exploring the Project with Jupyter Notebooks

Jupyter Notebooks are provided to walk through the code and demonstrate each component:

* **`remotive_api_scraper_notebook.ipynb`**: Explains the API data collection process.
* **`etl_db_utils_notebook.ipynb`**: Details the ETL process, database interaction, and utility functions.

To open and run the notebooks:

```bash
jupyter notebook
```

Then, navigate to the `.ipynb` files in your browser.

### Database Exploration

The `remote_jobs.db` SQLite database will be created after running the ETL process. You can explore its contents using any SQLite browser or by using the `DBConnector` class in a Python script.

## Detailed Component Descriptions

### 1. Web Scraping/API Data Collection (`remotive_api_scraper.py`)

* **Purpose**: Fetches remote job postings from the Remotive.com Public API.
* **Methodology**: Utilizes the `requests` library to make HTTP GET requests to the API endpoint. It iterates through various job categories to gather a comprehensive dataset.
* **Output**: Saves the collected data into `remotive_jobs_extended.csv`.
* **Best Practices Demonstrated**: API usage, handling JSON responses, iterating through categories, and respecting API rate limits with `time.sleep()`.

### 2. ETL Process (`etl_script.py`)

* **Purpose**: Extracts raw job data, transforms it into a clean and consistent format, and loads it into the database.
* **Extract**: Reads `remotive_jobs_extended.csv` into a Pandas DataFrame.
* **Transform**: Renames columns, handles missing values (e.g., `NaN` to `None`), converts `publication_date` to ISO format, and adds an `ingestion_timestamp`.
* **Load**: Uses the `DBConnector` to insert the transformed data into the `remote_jobs` table in `remote_jobs.db`.
* **Best Practices Demonstrated**: Data cleaning, standardization, handling missing values, and integration with a database layer.

### 3. Database Management (`db_connector.py`)

* **Purpose**: Provides an interface for connecting to and managing the SQLite database.
* **Key Features**:
  * `DBConnector` class for connection management.
  * `create_table()` to define the `remote_jobs` schema.
  * `insert_jobs()` for efficient data insertion, using `INSERT OR IGNORE` to prevent duplicates.
  * `fetch_all_jobs()` to retrieve data for analysis.
* **Best Practices Demonstrated**: Modular database interaction, schema definition, and duplicate handling.

### 4. Utility Functions (`utils.py`)

* **Purpose**: Contains reusable helper functions for common tasks.
* **Key Functions**:
  * `setup_logging()`: Configures a robust logging system to monitor script execution and debug issues.
  * `get_current_timestamp()`: Provides a consistent method for generating ISO-formatted timestamps.
* **Best Practices Demonstrated**: Centralized utility functions, effective logging for monitoring and debugging.

## Future Enhancements

* **Advanced Data Transformation**: Implement more sophisticated data cleaning and enrichment, such as natural language processing (NLP) for job descriptions to extract skills or sentiment.
* **Scheduling**: Automate the scraping and ETL process using tools like Apache Airflow or cron jobs.
* **Power BI Integration**: Develop a Power BI dashboard to visualize job trends, salary insights, and other key metrics from the `remote_jobs.db` database.
* **Error Reporting**: Implement more advanced error reporting and alerting mechanisms.
* **Multiple Job Boards**: Extend the scraper to collect data from additional remote job boards to provide a broader market view.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contact

For any questions or feedback, please contact

<div align="center">
  <a href="mailto:sohilakhaled811@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://linkedin.com/in/sohilakabbas">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://sohilakhaledportfolio.vercel.app/">
    <img src="https://img.shields.io/badge/Portfolio-FF5722?style=for-the-badge&logo=todoist&logoColor=white" alt="Portfolio" />
  </a>
</div>

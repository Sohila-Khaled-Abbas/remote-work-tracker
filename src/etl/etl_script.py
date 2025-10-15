import pandas as pd
import numpy as np
from datetime import datetime
from db_connector import DBConnector # Import the DBConnector

def extract_data(file_path):
    """Extracts data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully extracted {len(df)} records from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error during data extraction: {e}")
        return pd.DataFrame()

def transform_data(df):
    """Transforms the extracted job data."""
    if df.empty:
        print("No data to transform.")
        return pd.DataFrame()

    print("Starting data transformation...")

    # Rename columns for consistency with DB schema
    df = df.rename(columns={
        'Job ID': 'id',
        'Job Title': 'job_title',
        'Company Name': 'company_name',
        'Publication Date': 'publication_date',
        'Job Type': 'job_type',
        'Category': 'category',
        'Candidate Required Location': 'candidate_required_location',
        'Salary Range': 'salary_range',
        'Job Description': 'job_description',
        'Source URL': 'source_url',
        'Company Logo': 'company_logo',
        'Job Board': 'job_board'
    })

    # Handle missing values: Replace NaN with None for database insertion
    df = df.replace({np.nan: None})

    # Convert publication_date to datetime objects and then to ISO format string
    # This ensures consistency and handles potential mixed types during conversion
    def parse_date(date_str):
        if pd.isna(date_str) or date_str is None:
            return None
        try:
            # Attempt to parse as ISO format first
            dt_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return dt_obj.isoformat()
        except ValueError:
            # Fallback for other formats if necessary, or return None
            return None

    df['publication_date'] = df['publication_date'].apply(parse_date)

    # Add ingestion timestamp
    df['ingestion_timestamp'] = datetime.now().isoformat()

    # Ensure all required columns are present, fill with None if missing
    required_cols = [
        'id', 'job_title', 'company_name', 'publication_date', 'job_type',
        'category', 'candidate_required_location', 'salary_range', 'job_description',
        'source_url', 'company_logo', 'job_board', 'ingestion_timestamp'
    ]
    for col in required_cols:
        if col not in df.columns:
            df[col] = None

    # Select and reorder columns to match the database schema
    df = df[required_cols]

    print("Data transformation complete.")
    return df

def load_data(df, db_connector):
    """Loads the transformed data into the database using a DB connector."""
    if df.empty:
        print("No data to load.")
        return

    print(f"Starting data loading for {len(df)} records...")
    db_connector.insert_jobs(df)
    print("Data loading complete.")

if __name__ == "__main__":
    # This part is for demonstration/testing the ETL script independently.
    # In a real scenario, db_connector would be passed from the main application.
    print("Running ETL script in standalone mode.")
    
    csv_file = "remotive_jobs_extended.csv"
    extracted_df = extract_data(csv_file)
    transformed_df = transform_data(extracted_df)

    if not transformed_df.empty:
        db = DBConnector()
        db.connect()
        db.create_table()
        load_data(transformed_df, db)
        db.disconnect()
    else:
        print("ETL process completed with no data to load.")


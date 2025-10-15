import sqlite3
import pandas as pd
from datetime import datetime

class DBConnector:
    def __init__(self, db_name="remote_jobs.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        """Establishes a connection to the SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f"Connected to database: {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        """Closes the database connection."""
        if self.conn:
            self.conn.close()
            print("Disconnected from database.")

    def create_table(self):
        """Creates the remote_jobs table if it doesn't exist."""
        if not self.conn:
            self.connect()
        
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS remote_jobs (
            id INTEGER PRIMARY KEY,
            job_title TEXT NOT NULL,
            company_name TEXT NOT NULL,
            publication_date TEXT NOT NULL,
            job_type TEXT,
            category TEXT,
            candidate_required_location TEXT,
            salary_range TEXT,
            job_description TEXT,
            source_url TEXT UNIQUE NOT NULL,
            company_logo TEXT,
            job_board TEXT NOT NULL,
            ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        try:
            self.cursor.execute(create_table_sql)
            self.conn.commit()
            print("Table 'remote_jobs' ensured to exist.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def insert_jobs(self, df: pd.DataFrame):
        """Inserts job data from a Pandas DataFrame into the remote_jobs table.
           Handles duplicates by ignoring entries with existing source_url.
        """
        if df.empty:
            print("No data to insert.")
            return

        if not self.conn:
            self.connect()
            self.create_table() # Ensure table exists before inserting

        # Prepare data for insertion
        # Convert DataFrame rows to a list of tuples, ensuring order matches SQL INSERT statement
        # And handle potential None values for columns that can be null
        data_to_insert = []
        for index, row in df.iterrows():
            data_to_insert.append((
                row.get("id"),
                row.get("job_title"),
                row.get("company_name"),
                row.get("publication_date"),
                row.get("job_type"),
                row.get("category"),
                row.get("candidate_required_location"),
                row.get("salary_range"),
                row.get("job_description"),
                row.get("source_url"),
                row.get("company_logo"),
                row.get("job_board"),
                row.get("ingestion_timestamp", datetime.now().isoformat()) # Default if not set by ETL
            ))

        insert_sql = """
        INSERT OR IGNORE INTO remote_jobs (
            id, job_title, company_name, publication_date, job_type, category,
            candidate_required_location, salary_range, job_description, source_url,
            company_logo, job_board, ingestion_timestamp
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        try:
            self.cursor.executemany(insert_sql, data_to_insert)
            self.conn.commit()
            print(f"Successfully inserted/ignored {len(data_to_insert)} records into 'remote_jobs'.")
        except sqlite3.Error as e:
            print(f"Error inserting data: {e}")

    def fetch_all_jobs(self):
        """Fetches all job records from the database."""
        if not self.conn:
            self.connect()

        try:
            self.cursor.execute("SELECT * FROM remote_jobs;")
            columns = [description[0] for description in self.cursor.description]
            rows = self.cursor.fetchall()
            df = pd.DataFrame(rows, columns=columns)
            return df
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()

if __name__ == "__main__":
    db = DBConnector()
    db.connect()
    db.create_table()

    # Example of inserting dummy data
    dummy_data = pd.DataFrame([
        {
            "id": 1,
            "job_title": "Software Engineer",
            "company_name": "Tech Corp",
            "publication_date": "2025-10-15T10:00:00",
            "job_type": "full_time",
            "category": "Software Development",
            "candidate_required_location": "Worldwide",
            "salary_range": "$80,000 - $120,000",
            "job_description": "Develop and maintain software.",
            "source_url": "http://example.com/job1",
            "company_logo": "http://example.com/logo1.png",
            "job_board": "ExampleJobs",
            "ingestion_timestamp": datetime.now().isoformat()
        },
        {
            "id": 2,
            "job_title": "Data Analyst",
            "company_name": "Data Insights Inc.",
            "publication_date": "2025-10-14T11:30:00",
            "job_type": "contract",
            "category": "Data Analysis",
            "candidate_required_location": "Remote US",
            "salary_range": "$50/hr - $70/hr",
            "job_description": "Analyze large datasets.",
            "source_url": "http://example.com/job2",
            "company_logo": "http://example.com/logo2.png",
            "job_board": "ExampleJobs",
            "ingestion_timestamp": datetime.now().isoformat()
        }
    ])
    db.insert_jobs(dummy_data)

    # Fetch and display data
    all_jobs = db.fetch_all_jobs()
    print("\nAll jobs in DB:")
    print(all_jobs.head())

    db.disconnect()


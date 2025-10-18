"""
Export Data Script - Remote Work Tracker
==========================================
This script exports cleaned job data from the SQLite database to CSV files.
Supports various export options including full export, filtered export, and summary statistics.

Author: Sohia Khaled Abbas
Date: 2025-10-18
"""

import pandas as pd
import argparse
import logging
from datetime import datetime
from pathlib import Path
from db_connector import DBConnector
from utils import setup_logging

# Initialize logger
setup_logging("export_data.log", logging.INFO)
logger = logging.getLogger(__name__)


class DataExporter:
    """
    Handles exporting data from the database to CSV files.
    
    Attributes:
        db (DBConnector): Database connector instance.
        output_dir (Path): Directory for output files.
    """
    
    def __init__(self, db_name="remote_jobs.db", output_dir="exports"):
        """
        Initialize the DataExporter.
        
        Args:
            db_name: Name of the SQLite database file.
            output_dir: Directory to save exported CSV files.
        """
        self.db = DBConnector(db_name)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        logger.info(f"DataExporter initialized. Output directory: {self.output_dir}")
    
    def export_all_jobs(self, filename=None):
        """
        Export all jobs from the database to a CSV file.
        
        Args:
            filename: Custom filename for the export. If None, generates timestamp-based name.
        
        Returns:
            Path to the exported CSV file.
        """
        logger.info("Starting full data export...")
        
        # Connect to database and fetch all jobs
        self.db.connect()
        df = self.db.fetch_all_jobs()
        self.db.disconnect()
        
        if df.empty:
            logger.warning("No data found in database. Export aborted.")
            return None
        
        # Generate filename if not provided
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"remote_jobs_export_{timestamp}.csv"
        
        # Ensure .csv extension
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        # Export to CSV
        output_path = self.output_dir / filename
        df.to_csv(output_path, index=False, encoding='utf-8')
        
        logger.info(f"Successfully exported {len(df)} records to {output_path}")
        print(f"✅ Exported {len(df)} jobs to: {output_path}")
        
        return output_path
    
    def export_by_category(self, category, filename=None):
        """
        Export jobs filtered by category.
        
        Args:
            category: Job category to filter by.
            filename: Custom filename for the export.
        
        Returns:
            Path to the exported CSV file.
        """
        logger.info(f"Exporting jobs for category: {category}")
        
        # Connect to database and fetch all jobs
        self.db.connect()
        df = self.db.fetch_all_jobs()
        self.db.disconnect()
        
        if df.empty:
            logger.warning("No data found in database. Export aborted.")
            return None
        
        # Filter by category
        df_filtered = df[df['category'] == category]
        
        if df_filtered.empty:
            logger.warning(f"No jobs found for category: {category}")
            print(f"⚠️ No jobs found for category: {category}")
            return None
        
        # Generate filename if not provided
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            category_safe = category.replace(' ', '_').replace('/', '_')
            filename = f"remote_jobs_{category_safe}_{timestamp}.csv"
        
        # Ensure .csv extension
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        # Export to CSV
        output_path = self.output_dir / filename
        df_filtered.to_csv(output_path, index=False, encoding='utf-8')
        
        logger.info(f"Successfully exported {len(df_filtered)} records for category '{category}' to {output_path}")
        print(f"✅ Exported {len(df_filtered)} jobs for '{category}' to: {output_path}")
        
        return output_path
    
    def export_by_date_range(self, start_date, end_date, filename=None):
        """
        Export jobs within a specific date range.
        
        Args:
            start_date: Start date (YYYY-MM-DD format).
            end_date: End date (YYYY-MM-DD format).
            filename: Custom filename for the export.
        
        Returns:
            Path to the exported CSV file.
        """
        logger.info(f"Exporting jobs from {start_date} to {end_date}")
        
        # Connect to database and fetch all jobs
        self.db.connect()
        df = self.db.fetch_all_jobs()
        self.db.disconnect()
        
        if df.empty:
            logger.warning("No data found in database. Export aborted.")
            return None
        
        # Convert publication_date to datetime
        df['publication_date'] = pd.to_datetime(df['publication_date'])
        
        # Filter by date range
        df_filtered = df[
            (df['publication_date'] >= start_date) & 
            (df['publication_date'] <= end_date)
        ]
        
        if df_filtered.empty:
            logger.warning(f"No jobs found between {start_date} and {end_date}")
            print(f"⚠️ No jobs found between {start_date} and {end_date}")
            return None
        
        # Generate filename if not provided
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"remote_jobs_{start_date}_to_{end_date}_{timestamp}.csv"
        
        # Ensure .csv extension
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        # Export to CSV
        output_path = self.output_dir / filename
        df_filtered.to_csv(output_path, index=False, encoding='utf-8')
        
        logger.info(f"Successfully exported {len(df_filtered)} records for date range to {output_path}")
        print(f"✅ Exported {len(df_filtered)} jobs from {start_date} to {end_date} to: {output_path}")
        
        return output_path
    
    def export_summary_statistics(self, filename=None):
        """
        Export summary statistics about the job data.
        
        Args:
            filename: Custom filename for the export.
        
        Returns:
            Path to the exported CSV file.
        """
        logger.info("Generating summary statistics...")
        
        # Connect to database and fetch all jobs
        self.db.connect()
        df = self.db.fetch_all_jobs()
        self.db.disconnect()
        
        if df.empty:
            logger.warning("No data found in database. Export aborted.")
            return None
        
        # Generate summary statistics
        summary_data = []
        
        # Overall statistics
        summary_data.append({
            'Metric': 'Total Jobs',
            'Value': len(df),
            'Category': 'Overall'
        })
        
        summary_data.append({
            'Metric': 'Unique Companies',
            'Value': df['company_name'].nunique(),
            'Category': 'Overall'
        })
        
        summary_data.append({
            'Metric': 'Unique Categories',
            'Value': df['category'].nunique(),
            'Category': 'Overall'
        })
        
        # Jobs by category
        category_counts = df['category'].value_counts()
        for category, count in category_counts.items():
            summary_data.append({
                'Metric': 'Jobs Count',
                'Value': count,
                'Category': category
            })
        
        # Jobs by location
        location_counts = df['candidate_required_location'].value_counts().head(10)
        for location, count in location_counts.items():
            summary_data.append({
                'Metric': 'Jobs by Location',
                'Value': count,
                'Category': location
            })
        
        # Jobs by type
        type_counts = df['job_type'].value_counts()
        for job_type, count in type_counts.items():
            summary_data.append({
                'Metric': 'Jobs by Type',
                'Value': count,
                'Category': job_type
            })
        
        # Create DataFrame
        summary_df = pd.DataFrame(summary_data)
        
        # Generate filename if not provided
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"remote_jobs_summary_{timestamp}.csv"
        
        # Ensure .csv extension
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        # Export to CSV
        output_path = self.output_dir / filename
        summary_df.to_csv(output_path, index=False, encoding='utf-8')
        
        logger.info(f"Successfully exported summary statistics to {output_path}")
        print(f"✅ Exported summary statistics to: {output_path}")
        
        return output_path
    
    def export_for_powerbi(self, filename=None):
        """
        Export data optimized for Power BI import.
        Includes data type conversions and formatting.
        
        Args:
            filename: Custom filename for the export.
        
        Returns:
            Path to the exported CSV file.
        """
        logger.info("Exporting data optimized for Power BI...")
        
        # Connect to database and fetch all jobs
        self.db.connect()
        df = self.db.fetch_all_jobs()
        self.db.disconnect()
        
        if df.empty:
            logger.warning("No data found in database. Export aborted.")
            return None
        
        # Optimize for Power BI
        df_powerbi = df.copy()
        
        # Convert publication_date to datetime
        df_powerbi['publication_date'] = pd.to_datetime(df_powerbi['publication_date'])
        
        # Extract year, month, and day for easier filtering in Power BI
        df_powerbi['year'] = df_powerbi['publication_date'].dt.year
        df_powerbi['month'] = df_powerbi['publication_date'].dt.month
        df_powerbi['month_name'] = df_powerbi['publication_date'].dt.strftime('%B')
        df_powerbi['day'] = df_powerbi['publication_date'].dt.day
        df_powerbi['day_of_week'] = df_powerbi['publication_date'].dt.day_name()
        df_powerbi['quarter'] = df_powerbi['publication_date'].dt.quarter
        
        # Parse salary range into min and max (if available)
        def parse_salary(salary_str):
            """Parse salary string into min and max values."""
            if pd.isna(salary_str) or salary_str == '':
                return None, None
            
            try:
                # Handle various salary formats
                salary_str = str(salary_str).replace('$', '').replace(',', '').replace('k', '000')
                
                if '-' in salary_str:
                    parts = salary_str.split('-')
                    min_sal = float(parts[0].strip())
                    max_sal = float(parts[1].strip())
                    return min_sal, max_sal
                else:
                    # Single value
                    sal = float(salary_str.strip())
                    return sal, sal
            except:
                return None, None
        
        # Apply salary parsing
        df_powerbi[['salary_min', 'salary_max']] = df_powerbi['salary_range'].apply(
            lambda x: pd.Series(parse_salary(x))
        )
        
        # Calculate average salary
        df_powerbi['salary_avg'] = (df_powerbi['salary_min'] + df_powerbi['salary_max']) / 2
        
        # Generate filename if not provided
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"remote_jobs_powerbi_{timestamp}.csv"
        
        # Ensure .csv extension
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        # Export to CSV
        output_path = self.output_dir / filename
        df_powerbi.to_csv(output_path, index=False, encoding='utf-8')
        
        logger.info(f"Successfully exported {len(df_powerbi)} records optimized for Power BI to {output_path}")
        print(f"✅ Exported {len(df_powerbi)} jobs (Power BI optimized) to: {output_path}")
        
        return output_path


def main():
    """
    Main function to handle command-line interface for data export.
    """
    parser = argparse.ArgumentParser(
        description='Export cleaned job data from database to CSV files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Export all jobs
  python export_data.py --all
  
  # Export jobs by category
  python export_data.py --category "Software Development"
  
  # Export jobs by date range
  python export_data.py --date-range 2025-01-01 2025-03-31
  
  # Export summary statistics
  python export_data.py --summary
  
  # Export optimized for Power BI
  python export_data.py --powerbi
  
  # Export with custom filename
  python export_data.py --all --output my_jobs.csv
        """
    )
    
    parser.add_argument('--all', action='store_true',
                        help='Export all jobs from database')
    parser.add_argument('--category', type=str,
                        help='Export jobs for a specific category')
    parser.add_argument('--date-range', nargs=2, metavar=('START', 'END'),
                        help='Export jobs within date range (YYYY-MM-DD format)')
    parser.add_argument('--summary', action='store_true',
                        help='Export summary statistics')
    parser.add_argument('--powerbi', action='store_true',
                        help='Export data optimized for Power BI')
    parser.add_argument('--output', '-o', type=str,
                        help='Custom output filename')
    parser.add_argument('--db', type=str, default='remote_jobs.db',
                        help='Database file name (default: remote_jobs.db)')
    parser.add_argument('--output-dir', type=str, default='exports',
                        help='Output directory (default: exports)')
    
    args = parser.parse_args()
    
    # Create exporter instance
    exporter = DataExporter(db_name=args.db, output_dir=args.output_dir)
    
    # Execute export based on arguments
    if args.all:
        exporter.export_all_jobs(filename=args.output)
    elif args.category:
        exporter.export_by_category(category=args.category, filename=args.output)
    elif args.date_range:
        start_date, end_date = args.date_range
        exporter.export_by_date_range(start_date=start_date, end_date=end_date, filename=args.output)
    elif args.summary:
        exporter.export_summary_statistics(filename=args.output)
    elif args.powerbi:
        exporter.export_for_powerbi(filename=args.output)
    else:
        print("⚠️ No export option specified. Use --help for usage information.")
        parser.print_help()


if __name__ == "__main__":
    main()


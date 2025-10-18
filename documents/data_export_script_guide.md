# Data Export Script - User Guide

## Overview

The `export_data.py` script provides a comprehensive solution for exporting cleaned job data from the SQLite database to CSV files. It supports multiple export formats and filtering options, making it easy to prepare data for analysis, reporting, or importing into Business Intelligence tools like Power BI.

---

## Features

✅ **Full Data Export** - Export all jobs from the database  
✅ **Category Filtering** - Export jobs for specific categories  
✅ **Date Range Filtering** - Export jobs within a date range  
✅ **Summary Statistics** - Generate aggregated statistics  
✅ **Power BI Optimization** - Export with additional calculated fields for BI analysis  
✅ **Custom Filenames** - Specify custom output filenames  
✅ **Automatic Timestamps** - Auto-generated filenames with timestamps  
✅ **Logging** - Comprehensive logging for tracking exports  

---

## Installation

No additional installation required. The script uses standard libraries included with the project:

```bash
# Ensure you have the required dependencies
pip install pandas
```

---

## Usage

### Basic Syntax

```bash
python export_data.py [OPTIONS]
```

### Command-Line Options

| Option | Description |
|--------|-------------|
| `--all` | Export all jobs from the database |
| `--category CATEGORY` | Export jobs for a specific category |
| `--date-range START END` | Export jobs within date range (YYYY-MM-DD) |
| `--summary` | Export summary statistics |
| `--powerbi` | Export data optimized for Power BI |
| `--output FILENAME` | Custom output filename |
| `--db DATABASE` | Database file name (default: remote_jobs.db) |
| `--output-dir DIR` | Output directory (default: exports) |
| `--help` | Show help message |

---

## Examples

### 1. Export All Jobs

Export all jobs from the database to a timestamped CSV file:

```bash
python export_data.py --all
```

**Output:**
```
✅ Exported 1292 jobs to: exports/remote_jobs_export_20251018_130828.csv
```

---

### 2. Export with Custom Filename

Export all jobs with a custom filename:

```bash
python export_data.py --all --output my_remote_jobs.csv
```

**Output:**
```
✅ Exported 1292 jobs to: exports/my_remote_jobs.csv
```

---

### 3. Export by Category

Export jobs for a specific category (e.g., Software Development):

```bash
python export_data.py --category "Software Development"
```

**Output:**
```
✅ Exported 100 jobs for 'Software Development' to: exports/remote_jobs_Software_Development_20251018_130839.csv
```

**Available Categories:**
- Software Development
- Customer Service
- Design
- Marketing
- Sales / Business
- Project Management
- Data Analysis
- DevOps / Sysadmin
- Finance / Legal
- Product
- QA
- Writing
- Human Resources

---

### 4. Export by Date Range

Export jobs posted between specific dates:

```bash
python export_data.py --date-range 2025-01-01 2025-03-31
```

**Output:**
```
✅ Exported 245 jobs from 2025-01-01 to 2025-03-31 to: exports/remote_jobs_2025-01-01_to_2025-03-31_20251018_130900.csv
```

---

### 5. Export Summary Statistics

Generate a summary statistics CSV with aggregated data:

```bash
python export_data.py --summary
```

**Output:**
```
✅ Exported summary statistics to: exports/remote_jobs_summary_20251018_130836.csv
```

**Summary includes:**
- Total jobs count
- Unique companies count
- Unique categories count
- Jobs by category breakdown
- Jobs by location (top 10)
- Jobs by type breakdown

---

### 6. Export for Power BI (Recommended for BI Analysis)

Export data with additional calculated fields optimized for Power BI:

```bash
python export_data.py --powerbi
```

**Output:**
```
✅ Exported 1292 jobs (Power BI optimized) to: exports/remote_jobs_powerbi_20251018_130832.csv
```

**Additional Fields in Power BI Export:**
- `year` - Extracted year from publication date
- `month` - Month number (1-12)
- `month_name` - Month name (January, February, etc.)
- `day` - Day of month
- `day_of_week` - Day name (Monday, Tuesday, etc.)
- `quarter` - Quarter number (1-4)
- `salary_min` - Parsed minimum salary
- `salary_max` - Parsed maximum salary
- `salary_avg` - Average salary (calculated)

---

### 7. Custom Output Directory

Export to a custom directory:

```bash
python export_data.py --all --output-dir my_exports
```

**Output:**
```
✅ Exported 1292 jobs to: my_exports/remote_jobs_export_20251018_130828.csv
```

---

### 8. Use Different Database

Export from a different database file:

```bash
python export_data.py --all --db backup_jobs.db
```

---

## Output File Structure

### Standard Export

All standard exports include these columns:

| Column | Description |
|--------|-------------|
| `id` | Unique job ID (auto-generated) |
| `job_title` | Job title |
| `company_name` | Company name |
| `publication_date` | Date job was posted |
| `job_type` | Employment type (full_time, contract, etc.) |
| `category` | Job category |
| `candidate_required_location` | Location requirements |
| `salary_range` | Salary range (if available) |
| `job_description` | Full job description |
| `source_url` | URL to original job posting |
| `company_logo` | URL to company logo |
| `job_board` | Source job board (e.g., Remotive.com) |
| `ingestion_timestamp` | When the job was added to database |

### Power BI Export

Includes all standard columns PLUS:

| Additional Column | Description |
|-------------------|-------------|
| `year` | Year extracted from publication_date |
| `month` | Month number (1-12) |
| `month_name` | Month name (January, February, etc.) |
| `day` | Day of month |
| `day_of_week` | Day name (Monday, Tuesday, etc.) |
| `quarter` | Quarter (Q1, Q2, Q3, Q4) |
| `salary_min` | Minimum salary (parsed from salary_range) |
| `salary_max` | Maximum salary (parsed from salary_range) |
| `salary_avg` | Average salary ((min + max) / 2) |

---

## Programmatic Usage

You can also use the `DataExporter` class in your own Python scripts:

```python
from export_data import DataExporter

# Create exporter instance
exporter = DataExporter(db_name="remote_jobs.db", output_dir="exports")

# Export all jobs
exporter.export_all_jobs()

# Export by category
exporter.export_by_category("Software Development")

# Export for Power BI
exporter.export_for_powerbi()

# Export summary statistics
exporter.export_summary_statistics()

# Export by date range
exporter.export_by_date_range("2025-01-01", "2025-03-31")
```

---

## Logging

All export operations are logged to `export_data.log` in the current directory. The log includes:

- Export start and completion times
- Number of records exported
- Output file paths
- Any errors or warnings

**Example log entry:**
```
2025-10-18 13:08:28,782 - INFO - DataExporter initialized. Output directory: exports
2025-10-18 13:08:28,782 - INFO - Starting full data export...
2025-10-18 13:08:28,989 - INFO - Successfully exported 1292 records to exports/remote_jobs_export_20251018_130828.csv
```

---

## Best Practices

### For Power BI Import

1. **Use the `--powerbi` option** for the most complete dataset with pre-calculated fields
2. **Import as CSV** in Power BI Desktop
3. **Set data types** correctly:
   - `publication_date` → Date
   - `salary_min`, `salary_max`, `salary_avg` → Decimal Number
   - `year`, `month`, `day`, `quarter` → Whole Number

### For Data Analysis

1. **Export by category** to focus on specific job markets
2. **Use date ranges** to analyze trends over time
3. **Export summary statistics** for quick insights

### For Backups

1. **Export all data regularly** with timestamped filenames
2. **Store in version control** or cloud storage
3. **Verify exports** by checking row counts

---

## Troubleshooting

### No Data Exported

**Issue:** Export completes but shows 0 records

**Solution:**
- Check if the database has data: `python db_connector.py`
- Verify the database file exists: `ls -l remote_jobs.db`
- Run the ETL script to populate data: `python etl_script.py`

### Import Error

**Issue:** `ImportError: cannot import name 'setup_logger'`

**Solution:**
- Ensure `utils.py` is in the same directory
- Check that `utils.py` contains the `setup_logging` function

### Category Not Found

**Issue:** `⚠️ No jobs found for category: [CATEGORY]`

**Solution:**
- Check available categories: `python export_data.py --summary`
- Ensure category name matches exactly (case-sensitive)

### Permission Denied

**Issue:** Cannot write to output directory

**Solution:**
- Create the directory: `mkdir exports`
- Check write permissions: `chmod 755 exports`

---

## File Sizes

Approximate file sizes for reference:

| Export Type | Rows | File Size |
|-------------|------|-----------|
| Full Export (1,292 jobs) | 1,292 | ~8.7 MB |
| Power BI Export (1,292 jobs) | 1,292 | ~8.7 MB |
| Category Export (100 jobs) | 100 | ~760 KB |
| Summary Statistics | ~50 | ~1 KB |

---

## Integration with Power BI

### Step-by-Step Import Guide

1. **Export the data:**
   ```bash
   python export_data.py --powerbi
   ```

2. **Open Power BI Desktop**

3. **Get Data → Text/CSV**

4. **Navigate to the exported file:**
   ```
   exports/remote_jobs_powerbi_[timestamp].csv
   ```

5. **Load the data**

6. **Transform data types:**
   - Go to Transform Data
   - Set `publication_date` to Date type
   - Set salary fields to Decimal Number
   - Set year, month, day, quarter to Whole Number

7. **Create relationships** (if using multiple tables)

8. **Build your dashboard!**

---

## Support

For issues or questions:
- Check the main project README.md
- Review the CONTRIBUTING.md guidelines
- Open an issue on GitHub

---

## License

This script is part of the Remote Work Tracker project and is licensed under the MIT License.

---

**Last Updated:** October 18, 2025  
**Version:** 1.0.0


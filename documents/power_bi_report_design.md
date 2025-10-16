# Power BI Report Design: Remote Job Trend Analysis

This document outlines the design for a Power BI report that visualizes trends in the remote job market, based on the data collected from the Remotive.com API and stored in the `remote_jobs.db` database. The report is designed for HR leaders, talent acquisition specialists, and business decision-makers.

## 1. Report Objectives

*   Provide a high-level overview of the remote job market.
*   Analyze job trends by category, location, and job type.
*   Identify top hiring companies and in-demand skills.
*   Offer insights into salary trends and geographical distribution of remote work.

## 2. Report Structure and Pages

The report will consist of four main pages, each with a specific focus:

### Page 1: Executive Summary Dashboard

*   **Purpose**: A high-level, at-a-glance view of the remote job market.
*   **Layout**: Clean and modern, with key performance indicators (KPIs) at the top.
*   **Visualizations**:
    *   **KPI Cards**: Total Jobs, Number of Companies Hiring, Average Salary (if available), and Number of Job Categories.
    *   **Donut Chart**: Job Postings by Category (Top 5 + "Others").
    *   **Bar Chart**: Top 10 Companies by Number of Job Postings.
    *   **Map**: Job Postings by Candidate Required Location (Worldwide, US, etc.).
    *   **Line Chart**: Job Postings Over Time (by publication date).
*   **Interactivity**: Slicers for `publication_date` (last 30/60/90 days) and `category`.

### Page 2: Job Category Deep Dive

*   **Purpose**: Detailed analysis of specific job categories.
*   **Layout**: A main chart with supporting visuals and a table for detailed data.
*   **Visualizations**:
    *   **Clustered Bar Chart**: Number of Jobs per Category.
    *   **Treemap**: Job Postings by `job_type` (full_time, contract, etc.) within a selected category.
    *   **Table**: Detailed job listings for the selected category, including `job_title`, `company_name`, `publication_date`, and `salary_range`.
*   **Interactivity**: Slicer for `category` to filter the entire page. The table will be filterable and sortable.

### Page 3: Company and Location Analysis

*   **Purpose**: Insights into which companies are hiring and where candidates are sought.
*   **Layout**: Two main sections, one for company analysis and one for location analysis.
*   **Visualizations**:
    *   **Company Analysis**:
        *   **Bar Chart**: Top 20 Companies by Number of Job Postings.
        *   **Table**: Company details, including `company_name`, number of jobs, and categories they are hiring in.
    *   **Location Analysis**:
        *   **Map**: Geographical distribution of `candidate_required_location`.
        *   **Donut Chart**: Breakdown of jobs by location (e.g., Worldwide, USA, Europe).
*   **Interactivity**: Slicers for `company_name` and `candidate_required_location`.

### Page 4: Salary and Skills Insights (Future Enhancement)

*   **Purpose**: Analysis of salary trends and required skills (requires more advanced data extraction).
*   **Layout**: Visuals for salary distribution and skill frequency.
*   **Visualizations**:
    *   **Box and Whisker Plot**: Salary distribution by job category (requires parsing `salary_range`).
    *   **Word Cloud**: Most frequent keywords from `job_description` and `job_title` to identify in-demand skills.
*   **Interactivity**: Slicers for `category` and `job_title` keywords.

## 3. Data Model and DAX Measures

*   **Data Source**: The `remote_jobs` table in the `remote_jobs.db` SQLite database.
*   **Relationships**: A single-table model is sufficient for this initial design.
*   **DAX Measures**:
    *   `Total Jobs = COUNT(remote_jobs[id])`
    *   `Number of Companies = DISTINCTCOUNT(remote_jobs[company_name])`
    *   `Average Salary = AVERAGE(remote_jobs[parsed_salary])` (requires a calculated column to parse the `salary_range` field).

## 4. UI/UX and Design Principles

*   **Theme**: A custom JSON theme will be used for consistent colors, fonts, and visual styling, reflecting a professional and modern aesthetic.
*   **Navigation**: Clear navigation buttons to move between pages.
*   **Storytelling**: Each page will have a title and a brief introductory text to guide the user.
*   **Metadata**: A footer on each page will display "Last Updated," "Data Source: Remotive.com," and a contact for questions.
*   **Tooltips**: Custom tooltips will be designed to provide additional context when hovering over visuals.


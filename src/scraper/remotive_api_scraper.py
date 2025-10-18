import requests
import pandas as pd
import time

def get_remotive_categories():
    categories_url = "https://remotive.com/api/remote-jobs/categories"
    try:
        response = requests.get(categories_url)
        response.raise_for_status()
        data = response.json()
        if 'jobs' in data:
            return [job['slug'] for job in data['jobs']]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching categories from Remotive API: {e}")
    except ValueError as e:
        print(f"Error decoding JSON response for categories: {e}")
    return []

def scrape_remotive_api(category=None, search=None, limit=None):
    base_api_url = "https://remotive.com/api/remote-jobs"
    params = {}
    if category:
        params['category'] = category
    if search:
        params['search'] = search
    if limit:
        params['limit'] = limit

    job_listings = []
    print(f"Starting to fetch jobs from Remotive API with parameters: {params}")

    try:
        response = requests.get(base_api_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        if 'jobs' in data:
            for job in data['jobs']:
                job_data = {
                    "Job ID": job.get("id"),
                    "Job Title": job.get("title"),
                    "Company Name": job.get("company_name"),
                    "Publication Date": job.get("publication_date"),
                    "Job Type": job.get("job_type"),
                    "Category": job.get("category"),
                    "Candidate Required Location": job.get("candidate_required_location"),
                    "Salary Range": job.get("salary"),
                    "Job Description": job.get("description"),
                    "Source URL": job.get("url"),
                    "Company Logo": job.get("company_logo"),
                    "Job Board": "Remotive.com"
                }
                job_listings.append(job_data)
        else:
            print("No 'jobs' key found in the API response.")

    except requests.exceptions.RequestException as e:
        print(f"Error during request to Remotive API: {e}")
    except ValueError as e:
        print(f"Error decoding JSON response from Remotive API: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    df = pd.DataFrame(job_listings)
    return df

if __name__ == "__main__":
    all_categories = get_remotive_categories()
    if not all_categories:
        print("Could not retrieve categories. Exiting.")
    else:
        print(f"Found categories: {', '.join(all_categories)}")
        all_scraped_data = pd.DataFrame()
        for category_slug in all_categories:
            print(f"Scraping category: {category_slug}")
            # Fetch a larger limit for each category, respecting API rate limits
            # Remotive API advises max 4 requests a day, so we'll fetch a reasonable amount per category.
            # For demonstration, let's try to get up to 100 jobs per category if available.
            category_data = scrape_remotive_api(category=category_slug, limit=5000)
            if not category_data.empty:
                all_scraped_data = pd.concat([all_scraped_data, category_data], ignore_index=True)
            time.sleep(2) # Pause between category requests to be polite

        if not all_scraped_data.empty:
            output_filename = "remotive_jobs_extended.csv"
            all_scraped_data.to_csv(output_filename, index=False)
            print(f"Successfully fetched {len(all_scraped_data)} jobs from Remotive API across all categories and saved to {output_filename}")
        else:
            print("No job listings were fetched from Remotive API across all categories.")


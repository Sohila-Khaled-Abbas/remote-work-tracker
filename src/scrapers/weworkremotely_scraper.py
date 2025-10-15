import os
import json
import time
import logging
from bs4 import BeautifulSoup
from datetime import datetime
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.scrapers.base_scraper import BaseScraper

# ---------------------------------------------------------
# Logger setup
# ---------------------------------------------------------
os.makedirs("../../data/logs", exist_ok=True)
logging.basicConfig(
    filename="../../data/logs/weworkremotely.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class WeWorkRemotelyScraper(BaseScraper):
    BASE_URL = "https://weworkremotely.com/remote-jobs"

    def scrape_jobs(self, pages=3, include_description=False):
        """Scrape job listings from We Work Remotely."""
        all_jobs = []
        for page in range(1, pages + 1):
            url = f"{self.BASE_URL}?page={page}"
            logging.info(f"Scraping page {page}: {url}")

            try:
                self.load_page(url)
                soup = BeautifulSoup(self.driver.page_source, "html.parser")
                sections = soup.find_all("section", class_="jobs")

                for section in sections:
                    for li in section.find_all("li", class_="feature"):
                        try:
                            anchor = li.find("a", href=True)
                            if not anchor:
                                continue

                            job_url = "https://weworkremotely.com" + anchor["href"]

                            company_tag = li.find("span", class_="company")
                            title_tag = li.find("span", class_="title")
                            region_tag = li.find("span", class_="region company")

                            if not company_tag or not title_tag:
                                continue  # skip incomplete cards

                            company = company_tag.get_text(strip=True)
                            title = title_tag.get_text(strip=True)
                            region = region_tag.get_text(strip=True) if region_tag else "Remote"
                            tags = [t.get_text(strip=True) for t in li.find_all("span", class_="tooltip")]

                            # Optional: scrape detailed job description
                            job_description = ""
                            if include_description:
                                job_description = self.get_job_description(job_url)

                            all_jobs.append({
                                "company": company,
                                "title": title,
                                "region": region,
                                "tags": tags,
                                "url": job_url,
                                "source": "WeWorkRemotely",
                                "scraped_at": datetime.today().strftime("%Y-%m-%d"),
                                "description": job_description
                            })

                        except Exception as e:
                            logging.error(f"Error parsing job listing: {e}")

                time.sleep(2)

            except Exception as e:
                logging.error(f"Error scraping page {page}: {e}")
                continue

        return all_jobs

    # ---------------------------------------------------------
    # Detail page extractor
    # ---------------------------------------------------------
    def get_job_description(self, job_url):
        """Extract job description text from detail page."""
        try:
            self.load_page(job_url, wait_time=2)
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            desc_section = soup.find("div", class_="listing-container")
            if desc_section:
                return desc_section.get_text(separator=" ", strip=True)
        except Exception as e:
            logging.warning(f"Failed to fetch job description from {job_url}: {e}")
        return ""

    # ---------------------------------------------------------
    # Save to JSON
    # ---------------------------------------------------------
    def save_to_json(self, data, path="../../data/raw/"):
        """Save scraped data to JSON file."""
        os.makedirs(path, exist_ok=True)
        filename = f"{path}weworkremotely_{datetime.today().strftime('%Y%m%d')}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logging.info(f"Data saved to {filename}")
        print(f"[INFO] Data saved to {filename}")

# ---------------------------------------------------------
# Run scraper directly
# ---------------------------------------------------------
if __name__ == "__main__":
    scraper = WeWorkRemotelyScraper()
    jobs = scraper.scrape_jobs(pages=3, include_description=False)  # set True if you want job descriptions
    scraper.save_to_json(jobs)
    scraper.quit()
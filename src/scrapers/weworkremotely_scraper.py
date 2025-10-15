import json
import time
from bs4 import BeautifulSoup
from datetime import datetime
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.scrapers.base_scraper import BaseScraper
import logging


class WeWorkRemotelyScraper(BaseScraper):
    BASE_URL = "https://weworkremotely.com/remote-jobs"

    def scrape_jobs(self, pages=5):
        all_jobs = []
        for page in range(1, pages + 1):
            url = f"{self.BASE_URL}?page={page}"
            logging.info(f"Scraping page {page}: {url}")
            self.load_page(url)
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            sections = soup.find_all("section", class_="jobs")
            for section in sections:
                for li in section.find_all("li", class_="feature"):
                    try:
                        anchor = li.find("a", href=True)
                        if not anchor:
                            continue
                        link = "https://weworkremotely.com" + anchor["href"]
                        company = li.find("span", class_="company").get_text(strip=True)
                        title = li.find("span", class_="title").get_text(strip=True)
                        region = li.find("span", class_="region company").get_text(strip=True) if li.find("span", class_="region company") else "Remote"
                        tags = [t.get_text(strip=True) for t in li.find_all("span", class_="tooltip")]
                        date_posted = datetime.today().strftime("%Y-%m-%d")
                        all_jobs.append({
                            "company": company,
                            "title": title,
                            "region": region,
                            "tags": tags,
                            "url": link,
                            "source": "WeWorkRemotely",
                            "scraped_at": date_posted
                        })
                    except Exception as e:
                        print(f"[ERROR] Skipping job: {e}")
            time.sleep(2)
        return all_jobs

    def save_to_json(self, data, path="../../data/raw/"):
        filename = f"{path}weworkremotely_{datetime.today().strftime('%Y%m%d')}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[INFO] Data saved to {filename}")

if __name__ == "__main__":
    scraper = WeWorkRemotelyScraper()
    jobs = scraper.scrape_jobs(pages=3)
    scraper.save_to_json(jobs)
    scraper.quit()


logging.basicConfig(filename="../../data/logs/weworkremotely.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

from scrapers import pph_scraper, guru_scraper

def run_all_scrapers():
    """print("\n🚀 Starting all scrapers...\n")

    print("🔎 Scraping PeoplePerHour...")
    pph_scraper.scrape()  # ✅ This will run the function inside the file

"""
    print("🔎 Scraping Guru...")
    guru_scraper.scrape()

    print("\n✅ All scraping done. Data saved to /data folder.")

if __name__ == "__main__":
    run_all_scrapers()

from utils.keyword_filter import filter_jobs
"""
filter_jobs("data/pph_jobs.csv", "data/filtered_pph_jobs.csv")"""
filter_jobs("data/guru_jobs.csv", "data/filtered_guru_jobs.csv")


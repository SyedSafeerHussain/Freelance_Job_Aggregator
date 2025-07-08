from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import os
from utils.helpers import save_to_csv
from utils.helpers import load_keywords
import logging
# Logging setup
LOG_DIR="logs"
LOG_FILE=os.path.join(LOG_DIR,"errors.log")
os.makedirs(LOG_DIR,exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def scrape():  # ✅ Wrap everything below inside this function
    try:
        driver=webdriver.Chrome()
        url = "https://www.peopleperhour.com/freelance-jobs"
        driver.get(url)
        time.sleep(2)
    except Exception as e:
        logging.error("🚨 Failed to start WebDriver or load page: %s", str(e))
    # Accept cookies

    try:
        accept = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='cookie-banner']/div/div[2]/a"))
        )
        accept.click()
        logging.info("✅ Cookie accepted")
    except Exception as e:
        logging.warning("⚠️ Cookie button issue: %s", str(e))
        

    keywords = load_keywords()

    all_jobs = []

    for word in keywords:
        try:
            driver.get(url)
            time.sleep(2)
            try:
                search = driver.find_element(By.XPATH, "//*[@id='reactContainer']/div/div[3]/section/main/div/div[1]/div[1]/div[3]/div/div/div[1]/form/div/div/input")
                search.clear()
                search.send_keys(word)
                search.submit()
                time.sleep(2)
            except Exception as e:
                logging.warning("⚠️ Searching issue")
            try:
                accept = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='cookie-banner']/div/div[2]/a"))
            )
                accept.click()
                logging.info("✅ Cookie accepted")
            except Exception as e:
                logging.warning("⚠️ Cookie button issue: %s", str(e))
        

            posts = driver.find_elements(By.XPATH, "//*[@id='reactContainer']/div/div[3]/section/main/div/div[3]/div/div[2]/ul/li")
            for post in posts:
                try:
                    title = post.find_element(By.XPATH, ".//h6").text
                    desc = post.find_element(By.XPATH, ".//p[2]").text
                    link = post.find_element(By.XPATH, './/h6/a').get_attribute('href')
                    price = post.find_element(By.XPATH, ".//span[contains(@class, 'title-nano')]").text
                except Exception as e:
                    logging.error("❌ Failed to extract job data: %s", str(e))
                    title = desc = link = price = 'N/A'
                all_jobs.append({
                    "Job Title": title,
                    "Job Description": desc,
                    "link": link,
                    "price": price
                })
        except Exception as e:
            logging.error(f"❌ Error during keyword '{word}' scraping: {str(e)}")
    driver.quit()

    try:
        save_to_csv(all_jobs,"pph_jobs.csv")
        logging.info("✅ Scraping complete and saved to data/pph_job.csv")

    except Exception as e:
        logging.error("❌ Failed to save CSV: %s", str(e))

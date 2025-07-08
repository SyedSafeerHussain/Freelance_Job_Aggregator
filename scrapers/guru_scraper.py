from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from utils.helpers import load_keywords
from utils.helpers import save_to_csv
import os
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
def scrape():  # ✅ Wrap in function
    try:
        driver=webdriver.Chrome()
        url="https://www.guru.com/d/jobs/"
        driver.get(url)
        time.sleep(2)
    except Exception as e:
        logging.error("🚨 Failed to start WebDriver or load page: %s", str(e))

    # Accept cookies
    try:
        accept = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-accept-btn-handler']"))
        )
        accept.click()
        logging.info("✅ Cookie accepted")
    except Exception as e:
        logging.warning("⚠️ Cookie button issue: %s", str(e))

    keywords=load_keywords()

    all_jobs = []

    for word in keywords:
        try:
            driver.get(url)
            time.sleep(2)
            search=driver.find_element(By.XPATH, "//*[@id='typeahead-33']")
            search.clear()
            search.send_keys(word)
            try:
                key = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='search-app']/div/section/div/div[1]/div[2]/div[1]/span[1]/label/ul/li"))
                )
                key.click()
                logging.info(f"🔍 Keyword clicked: {word}")
            except Exception as e:
                logging.warning(f"⚠️ Dropdown issue for keyword '{word}': {str(e)}")
            time.sleep(2)

            posts = driver.find_elements(By.XPATH, "//*[@id='search-app']/div/section/div/div[2]/div/ul/li")
            
            for post in posts:
                try:
                    title = post.find_element(By.XPATH, './/h2').text
                    price = post.find_element(By.XPATH, ".//div[contains(@class,'jobRecord__budget')]").text
                    desc = post.find_element(By.XPATH, ".//p[contains(@class,'jobRecord__desc')]").text
                    link = post.find_element(By.XPATH, ".//h2/a").get_attribute('href')
                except Exception as e:
                    logging.error("❌ Failed to extract job data: %s", str(e))
                    title=desc=link=price='n/a'
                
                all_jobs.append({
                    'Job Title':title,
                    "Job Description":desc,
                    "link":link,
                    "price":price
                })
        except Exception as e:
            logging.error(f"❌ Error during keyword '{word}' scraping: {str(e)}")

    driver.quit()

    try:
        save_to_csv(all_jobs,"guru_jobs.csv")
        logging.info("✅ Scraping complete and saved to data/guru_jobs.csv")
    except Exception as e:
        logging.error("❌ Failed to save CSV: %s", str(e))


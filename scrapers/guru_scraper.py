from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from utils.helpers import load_keywords
from utils.helpers import save_to_csv
import os

def scrape():  # ✅ Wrap in function
    driver = webdriver.Chrome()
    url = "https://www.guru.com/d/jobs/"
    driver.get(url)
    time.sleep(3)

    # Accept cookie banner
    try:
        accept = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-accept-btn-handler']"))
        )
        accept.click()
        print("✅ Cookie accepted using direct XPath")
    except:
        print("❌ Cookie accept button not found or not clickable.")

    keywords=load_keywords()

    all_jobs = []

    for word in keywords:
        driver.get(url)
        time.sleep(2)
        try:
            search = driver.find_element(By.XPATH, "//*[@id='typeahead-32']")
            search.clear()
            search.send_keys(word)
            try:
                key = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='search-app']/div/section/div/div[1]/div[2]/div[1]/span[1]/label/ul/li"))
                )
                key.click()
                print(f"🔍 Keyword clicked: {word}")
            except:
                print(f"⚠️ No dropdown found for: {word}")
            time.sleep(2)
        except:
            print(f"❌ Search bar issue with keyword: {word}")

        # Try cookie accept again just in case
        try:
            accept = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-accept-btn-handler']"))
            )
            accept.click()
        except:
            pass

        posts = driver.find_elements(By.XPATH, "//*[@id='search-app']/div/section/div/div[2]/div/ul/li")
        for post in posts:
            try:
                title = post.find_element(By.XPATH, './/h2').text
                price = post.find_element(By.XPATH, ".//div[contains(@class,'jobRecord__budget')]").text
                desc = post.find_element(By.XPATH, ".//p[contains(@class,'jobRecord__desc')]").text
                link = post.find_element(By.XPATH, ".//h2/a").get_attribute('href')
            except:
                title = desc = link = price = 'n/a'

            all_jobs.append({
                "Job Title": title,
                "Job Description": desc,
                "link": link,
                "price": price
            })

    driver.quit()
    save_to_csv(all_jobs, "guru_jobs.csv")  # ✅ Correct file name
    print("✅ Scraping complete and saved to data/guru_jobs.csv")

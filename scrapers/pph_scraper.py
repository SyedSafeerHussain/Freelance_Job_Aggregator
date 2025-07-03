from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import csv
import os
driver=webdriver.Chrome()
url="https://www.peopleperhour.com/freelance-jobs"
driver.get(url)
WebDriverWait(driver,5)
#----------------------------------------------------check-cookie-banner-----------------------------------

try:
    accept = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='cookie-banner']/div/div[2]/a"))
    )
    accept.click()
    print("✅ Cookie accepted using direct XPath")
except:
    print("❌ Cookie accept button not found or not clickable.")
keywords = [
    "web scraping",
    "selenium",
    "python",
    "automation",
    "data extraction",
    "api integration",
    "data mining",
    "beautifulsoup",
    "scrapy",
    "pdf scraping",
    "bot",
    "crawler",
    "email automation",
    "data scraping",
    "chrome extension",
    "twilio",
    "telegram bot",
    "freelancing bot",
    "job scraper",
    "keyword filter"
]
folder_path=os.path.dirname(os.path.abspath(__file__))
csv_path=os.path.join(folder_path,'Jobs.csv')
for word in keywords:
    driver.get(url)
    time.sleep(2)
    try:
        search=driver.find_element(By.XPATH,"//*[@id='reactContainer']/div/div[3]/section/main/div/div[1]/div[1]/div[3]/div/div/div[1]/form/div/div/input")
        search.clear()
        search.send_keys(word)
        search.submit()
        time.sleep(10)
    except:
        print("something wrong")
    #--------------------------------------------------check-cookie-banner---------------------------------------
    try:
        accept = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='cookie-banner']/div/div[2]/a"))
    )
        accept.click()
        print("✅ Cookie accepted using direct XPath")
    except:
        print("❌ Cookie accept button not found or not clickable.")

    time.sleep(5)
    #-----------------------------------------------Get current file's directory------------------------------
    
    #-----------------------------------------------Scrape data and save in file -----------------------------------------
    with open('jobs.csv','a',newline='')as file:
        writer=csv.writer(file)
        writer.writerow(["Job Title",'Job Description','link','price'])
        posts=driver.find_elements(By.XPATH,"//*[@id='reactContainer']/div/div[3]/section/main/div/div[3]/div/div[2]/ul/li")
        for post in posts:
            try:
                title=post.find_element(By.XPATH,".//h6").text
                desc=post.find_element(By.XPATH,".//p[2]").text
                link=post.find_element(By.XPATH,'.//h6/a').get_attribute('href')
                price=post.find_element(By.XPATH,".//span[contains(@class, 'title-nano')]").text
            except:
                title='N/A'
                desc='N/A'
                link='N/A'
                price='N/A'
            writer.writerow([title,desc,link,price])
print("Done")

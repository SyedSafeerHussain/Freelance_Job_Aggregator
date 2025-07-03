from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv
import os
driver=webdriver.Chrome()
url="https://www.guru.com/d/jobs/"
driver.get(url)
time.sleep(3)
#----------------------------------------------------check-cookie-banner-----------------------------------
try:
    accept=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"//*[@id='onetrust-accept-btn-handler']"))
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
csv_path=os.path.join(folder_path,'guru.csv')


for words in keywords:
    driver.get(url)
    time.sleep(2)
    try:
        search=driver.find_element(By.XPATH,"//*[@id='typeahead-32']")
        search.clear()
        search.send_keys(words)
        try:
            key=WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.XPATH,"//*[@id='search-app']/div/section/div/div[1]/div[2]/div[1]/span[1]/label/ul/li"))
            )
            key.click()
            print("Key found")
        except:
            print("Not found")
        time.sleep(2)
    except:
        print('lora')
    #----------------------------------------------------check-cookie-banner-----------------------------------

    try:
        accept=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"//*[@id='onetrust-accept-btn-handler']"))
    )
        accept.click()
        print("✅ Cookie accepted using direct XPath")
    except:
        print("❌ Cookie accept button not found or not clickable.")
        #-----------------------------------------------Scrape data and save in file -----------------------------------------
    with open("guru.csv",'a',newline='')as file:
        writer=csv.writer(file)
        writer.writerow(['title','description','link','price'])
        posts=driver.find_elements(By.XPATH,"//*[@id='search-app']/div/section/div/div[2]/div/ul/li")
        for post in posts:
            try:
                title=post.find_element(By.XPATH,'.//h2').text
                price=post.find_element(By.XPATH,".//div[contains(@class,'jobRecord__budget')]").text
                desc=post.find_element(By.XPATH,".//p[contains(@class,'jobRecord__desc')]").text
                link=post.find_element(By.XPATH,".//h2/a").get_attribute('href')
            except:
                title='n/a'
                price='n/a'
                link='n/a'
                desc='n/a'
            writer.writerow([title,desc,link,price])
driver.quit()
print("Done")
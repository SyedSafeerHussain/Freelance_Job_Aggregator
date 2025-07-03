"""from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
import time
import os
driver=webdriver.Chrome()
url="https://remoteok.com/"
driver.get(url)
Keywords=[
    "Engineer",
    "Developer",
    "JavaScript",
    "Full Stack",
    "Ops"
]
folder_path=os.path.dirname(os.path.abspath(__file__))
csv_path=os.path.join(folder_path,'remote.csv')

for word in Keywords:
    driver.get(url)
    time.sleep(2)
    try:
        search=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/input")
        search.clear()
        search.send_keys(word)
        try:
            key=WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.XPATH,"/html/body/div[6]/div/div[4]/div[1]"))
            )
            key.click()
            print("Key found")
        except:
            print('Key not found')
    except:
        print("Search selector no working at all")
    
    with open("remote.csv",'a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(['title','desc','price','link'])
        posts=driver.find_elements(By.CSS_SELECTOR,"tr[data-offset]")"""
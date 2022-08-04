import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# some JSON:
data =  '{ "url":"https://opensea.io/", "imageNFT":"r\"C:\Users\NANOTEK\Desktop\244978232_3008896996054968_2504149158620241149_n.jpg\"", "name":"EMI-NFT", "desc":"NFT description" }'
data= json.loads(data)

os.system('chrome.exe -remote-debugging-port=9014 --user-data-dir="C:\selenium\session1"')
time.sleep(3)

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:1111")
driver = webdriver.Chrome('C:\\selenium\\chromedriver.exe',options=chrome_options)

driver.maximize_window()
driver.get(data['url'])

driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div[1]/nav/ul/div[1]/li[4]').click()
time.sleep(3)
try:
    driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div/div/div[2]/ul/li[1]/button').click()
    time.sleep(3)
except:
    print("Connecté")



try:
    driver.switch_to.window(driver.window_handles[1])
    try:
        driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div[2]/div[4]/div[2]/button[2]').click()
        time.sleep(5)
        driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
        time.sleep(5)
    except:
        print("->")
    try:
        if(len(driver.window_handles)==2):
            driver.switch_to.window(driver.window_handles[1])
            driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]').click()
            time.sleep(5)
    except:
        driver.refresh()
        print("-->")
except:
    print("Deja inscrit")
try:
    driver.switch_to.window(driver.window_handles[0])
except:
    print("--->")

try:
    driver.find_element(By.ID,"media").send_keys(dat['imageNFT'])
except:
    driver.refresh()
    time.sleep(5)
    if(len(driver.window_handles)==2):
            driver.switch_to.window(driver.window_handles[1])
            driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]').click()
            time.sleep(5)
    driver.find_element(By.ID,"media").send_keys(r"C:\Users\NANOTEK\Desktop\244978232_3008896996054968_2504149158620241149_n.jpg")

driver.find_element(By.ID,"name").send_keys(data['name'])
driver.find_element(By.ID,"description").send_keys(data['desc'])
driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div/section/div/form/div[9]/div[1]/span/button').click()
time.sleep(5)


driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[2]/button/i').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div/div[1]/div/span[2]/a').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[2]/div/div[2]/div/div/div[2]/input').send_keys("70")

time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[6]/button').click()

print("sample test case successfully completed")
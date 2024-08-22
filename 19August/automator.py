from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://google.co.in')
x=driver.find_element(By.TAG_NAME,"textarea")
x.click()
x.send_keys("nfl")
x.send_keys(Keys.ENTER)
y=driver.find_element(By.XPATH,'//*[@id="sports-app"]/div/div[4]/div[2]/div/g-immersive-footer/g-fab')
y.click()
time.sleep(5)
n=driver.find_elements(By.XPATH,"//div[contains(@class, 'ellipsisize')]//span")
titles=driver.find_elements(By.XPATH,"//td[contains(@class,'BAX2sc')]//div")
print(len(n))
for i in n:
    print(i.text)
print(len(titles))
for i in titles:
    print(i.text)
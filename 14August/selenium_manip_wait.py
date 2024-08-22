import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#Importing these two libraries to provide for waiting till loading time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#No required path specification when using latest selenium for chromedriver
driver=webdriver.Chrome()
driver.get("https://google.co.in")
print(driver.title)
elem=driver.find_element(By.NAME,"q")
elem.send_keys("Germany")
elem.submit()
time.sleep(5)


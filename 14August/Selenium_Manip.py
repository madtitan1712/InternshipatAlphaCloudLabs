import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#No required path specification when using latest selenium for chromedriver
driver=webdriver.Chrome()
driver.get("https://python.org")
print(driver.title)
searchbar=driver.find_element(By.NAME,"q")
searchbar.clear()
searchbar.send_keys("getting started with python")
searchbar.send_keys(Keys.RETURN)
print(driver.current_url)
time.sleep(5)
driver.close()

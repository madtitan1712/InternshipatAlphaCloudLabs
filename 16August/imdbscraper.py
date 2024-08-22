from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
imdburl="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
driver.get(imdburl)
wait=WebDriverWait(driver,10)
textelem=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul li h3")))
x=open("Top250Flims.txt","a")
for i in textelem:
    print(i.text)

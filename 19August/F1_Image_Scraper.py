#This thing can scrape any of the main article images from https://autosport.com
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from PIL import Image
import io
import os

driver=webdriver.Chrome()
driver.get("https://www.autosport.com/motogp/news/martin-bagnaia-is-not-faster-than-me-despite-austria-motogp-domination/10645573/")
wait=WebDriverWait(driver,10)
print("Done connecting..")
carousel=driver.find_element(By.CLASS_NAME,"ms-article_detail")
images=carousel.find_elements(By.TAG_NAME,"picture")
savedir="D:/Programming/Python/Intern/19August"
if not os.path.exists(savedir):
    os.makedirs(savedir)
cnt=0
print(len(images))
for x in images:
    y=x.find_element(By.TAG_NAME,"img")
    imagedata=y.get_attribute("src")
    resp=requests.get(imagedata)
    image=io.BytesIO(resp.content)
    saver=Image.open(image)
    imagepath=os.path.join(savedir,f"image{cnt+1}.jpg")
    saver.save(imagepath)
    cnt+=1
print("Done")
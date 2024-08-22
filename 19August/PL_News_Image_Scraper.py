#This can scrape any images in the articles from the Premier League website 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import requests
from PIL import Image 
import io

driver=webdriver.Chrome()
url="https://www.premierleague.com/news/4082473"
driver.get(url)
wait=WebDriverWait(driver,10)
x=wait.until(EC.presence_of_element_located((By.XPATH,"//section[contains(@class, 'standardArticle article')]")))
image_elements=x.find_elements(By.CSS_SELECTOR,"picture img[src]")
savedir="D:/Programming/Python/Intern/19August/Premier League"
print(f"Found {len(image_elements)} Images")
if not os.path.exists(savedir):
    os.makedirs(savedir)
cnt=0
for i in image_elements:
    try:
        y=i.get_attribute("src")
        resp=requests.get(y)
        imagedata=io.BytesIO(resp.content)
        saver=Image.open(imagedata)
        saver=saver.convert("RGB")
        imagepath=os.path.join(savedir,f"image{cnt+1}.jpg")
        saver.save(imagepath)
        cnt+=1
    except:
        print(f"Unable to process the image {cnt+1}")                
driver.close()
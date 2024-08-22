from selenium import webdriver
from selenium.webdriver.common.by import By
import io
import requests
from PIL import Image
from pathlib import Path
import time
driver=webdriver.Chrome()
driver.get("https://www.thehindu.com/entertainment/music/")
images=driver.find_elements(By.CLASS_NAME,"media-object adaptive placeholder")
namer=0
for i in images:
    z=i.get_attribute("src")
    print(f"fetching: {z}\n")
    x=requests.get(z).content
    v=io.BytesIO(z)
    sendout=Image.open(v).convert("RGB")
    pathout=Path("D:/Programming/Python/Intern/14August",namer+".jpeg")
    sendout.save(pathout,"JPEG",quality=100)
    print("Done\n")
    time.sleep(2)
driver.close()
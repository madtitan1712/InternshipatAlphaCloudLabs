#imports
import requests
import time
import hashlib
from pathlib import Path
from PIL import Image
import io
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
options=webdriver.ChromeOptions()
options.add_argument('--headless')
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
try:
    url=input("Enter your URL")
    wait=WebDriverWait(driver,10)
    driver.get(url)
    get_url=driver.current_url
    wait.until(EC.url_to_be(url))
    if get_url==url:
        page_source=driver.page_source
    soup=BeautifulSoup(page_source,features="html.parser")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight,)")
    text_matches=soup.body.find_all("p")
    title=soup.title.text
    f=open(f"{soup.title.text}.txt",'a',encoding="utf-8")
    f.write(soup.title.text)
    for i in text_matches:
        for j in i(['sup','sub']):
            j.decompose()
        f.write(i.text)
    print("Writing done... Farming for Images")
    h=soup.find_all("a",class_="mw-file-description")
    images=[]
    for tag in h:
        img_tags=tag.find_all("img",class_="mw-file-element")
        images.extend(img_tags)
    imageslist=[]
    for i in images:
        if i not in imageslist:
            imageslist.append(i.get("src"))
    for x in imageslist:
        z=requests.get('http:' + x).content
        imagefile=io.BytesIO(z)
        sendout=Image.open(imagefile).convert("RGB")
        filepath=Path("D:/Programming/Python/Intern/13August/ResultImages/",hashlib.sha1(z).hexdigest()[:10]+".png")
        print("Now Fetching : ",filepath,"\n")
        sendout.save(filepath,"PNG",quality=80)
        time.sleep(2)
        print("Fetch Done for",filepath,"\n")

except KeyboardInterrupt:
    print("You have stopped the session")
except TimeoutError:
    print("Time out for the webpage to load")
except FileNotFoundError:
    print("File is not found or file path is wrong")

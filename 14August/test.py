from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from PIL import Image
import io
driver = webdriver.Chrome()
base_url = "https://www.instagram.com/p/CJmFNIOBSRn/"
image_urls = []
# Loop through possible images in the carousel (adjust range as needed)
for i in range(1, 9):
    url = f"{base_url}?img_index={i}"
    driver.get(url)
    driver.implicitly_wait(5)
    try:
        img = driver.find_element(By.CSS_SELECTOR, "article img[src]")
        img_src = img.get_attribute("src")
        image_urls.append(img_src)
    except Exception as e:
        print(f"Image {i}: Not found. {e}")
        break
driver.quit()
for idx, img_url in enumerate(image_urls):
    response = requests.get(img_url)
    img = Image.open(io.BytesIO(response.content))
    img.save(f"image_{idx + 1}.jpg")

print("All images saved.")

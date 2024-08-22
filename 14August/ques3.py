from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from PIL import Image
import io
driver = webdriver.Chrome()
post_url = "https://www.instagram.com/p/CJl5PG4A5MB/"
driver.get(post_url)
wait = WebDriverWait(driver, 10)
image_element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "article img[src]"))
)
image_url = image_element.get_attribute("src")
response = requests.get(image_url)
image_data = io.BytesIO(response.content)
image = Image.open(image_data)
image.save("instagram_post_image.jpg")
driver.quit()
print("Done")

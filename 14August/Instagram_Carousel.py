from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from PIL import Image
import io
import os
driver = webdriver.Chrome()
post_url = "https://www.instagram.com/p/CJmFNIOBSRn/"
driver.get(post_url)
wait = WebDriverWait(driver, 10)
image_elements = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article img[src]"))
)
save_directory = "D:/Programming/Python/Intern/14August"
os.makedirs(save_directory, exist_ok=True)
for idx, image_element in enumerate(image_elements):
    image_url = image_element.get_attribute("src")
    print(f"Fetching Image {idx + 1}: {image_url}")

    
    response = requests.get(image_url)
    image_data = io.BytesIO(response.content)
    image = Image.open(image_data)

    
    image_path = os.path.join(save_directory, f"instagram_post_image_{idx + 1}.jpg")
    image.save(image_path)

print("All images downloaded and saved.")
driver.quit()

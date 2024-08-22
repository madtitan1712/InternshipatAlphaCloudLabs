from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Open Google and perform the search
driver.get('https://google.co.in')
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "textarea"))
)
search_box.click()
search_box.send_keys("nfl")
search_box.send_keys(Keys.ENTER)

# Wait until the sports section loads and click the desired element
try:
    element_to_click = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="sports-app"]/div/div[4]/div[2]/div/g-immersive-footer/g-fab'))
    )
    element_to_click.click()
except Exception as e:
    print("Button not found or clickable:", e)
    driver.quit()

time.sleep(5)  # Give some time for the schedule to load

# Scroll in smaller increments to ensure content loads
scroll_pause_time = 2

while True:
    # Scroll down by a small amount
    driver.execute_script("window.scrollBy(0, 500);")
    
    # Wait for new content to load
    time.sleep(scroll_pause_time)
    
    # Check for new scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    # Scroll again and check if new content loaded
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(scroll_pause_time)
    
    # Calculate new scroll height and compare with the last height
    if new_height == driver.execute_script("return document.body.scrollHeight"):
        break

time.sleep(5)

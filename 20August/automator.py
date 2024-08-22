from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def scroll_within_element(driver, element, delay=2):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", element)
    time.sleep(delay)

def load_all_content_within_element(driver, element, max_scrolls=10, delay=2):
    last_height = driver.execute_script("return arguments[0].scrollHeight;", element)
    scroll_count = 0
    
    while scroll_count < max_scrolls:
        scroll_within_element(driver, element, delay)
        new_height = driver.execute_script("return arguments[0].scrollHeight;", element)
        
        if new_height == last_height:
            break
        
        last_height = new_height
        scroll_count += 1

driver = webdriver.Chrome()
driver.get('https://google.co.in')
x = driver.find_element(By.TAG_NAME, "textarea")
x.click()
x.send_keys("nfl")
x.send_keys(Keys.ENTER)

y = driver.find_element(By.XPATH, '//*[@id="sports-app"]/div/div[4]/div[2]/div/g-immersive-footer/g-fab')
y.click()
time.sleep(5)

l = driver.find_element(By.XPATH, "//div[@class='JNVNDd imso-fpm']")
wait = WebDriverWait(driver, 20)
load_all_content_within_element(driver, l)

n = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'ellipsisize')]//span")))
date = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='imspo_mt__cmd']//span | //div[@class='imspo_mt__pm-inf imspo_mt__pm-infc imspo_mt__date']")))
weeklist = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='GVj7ae imso-medium-font qJnhT imso-ani']")))

namelist = [i.text for i in n if i.text!='']
datelist = [i.text for i in date if i.text != '']
weeklistz = [i.text for i in weeklist][:-4] #removing the last 4 weeks as they're TBD


matches = []
for i in range(0, len(namelist) - 1, 2):
    matches.append([namelist[i], namelist[i + 1]])
df = pd.DataFrame(matches, columns=["Home", "Away"])
df=df.dropna()
df["Date"] = datelist[:-13]  # Removing last 13 dates as they are TBD and Couldn't be deselected 

# Insert week numbers
result_rows = []
week_index = 0

for i in range(len(df)):
    if i == 0 or (i % 16 == 1 and i > 0):
        result_rows.append([weeklistz[week_index], '', ''])
        week_index += 1
        week_index = min(week_index, len(weeklistz) - 1)
    result_rows.append(df.iloc[i].tolist())

df_result = pd.DataFrame(result_rows, columns=['Home', 'Away', 'Date'])

# Save the DataFrame directly to a CSV file
df_result.to_csv("result.csv", index=False)

print(df_result)

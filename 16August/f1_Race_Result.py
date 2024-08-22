from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
driver=webdriver.Chrome()
url="https://www.formula1.com/en/results/2024/races/"
driver.get(url)
wait=WebDriverWait(driver,10)
header=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//th")))
table=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//tr")))
titles=[]
values=[]
for i in header:
    titles.append(i.text)
for i in table:
    tdlist=[]
    td=i.find_elements(By.TAG_NAME,"td")
    for j in td:
        tdlist.append(j.text)
    values.append(tdlist)
with open("race_result.csv","w") as filz:
    writer=csv.writer(filz)
    writer.writerow(titles)
    for i in values:
        writer.writerow(i)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
driver=webdriver.Chrome()
page_url="https://www.formula1.com/en/results/2024/drivers"
driver.get(page_url)
wait=WebDriverWait(driver,10)
head=table=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//th")))
table=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//tr")))
titles=[]
values=[]
for i in head:
    titles.append(i.text)
for i in table:
    tdlist=[]
    td=i.find_elements(By.TAG_NAME,"td")
    for i in td:
        tdlist.append(i.text)
    values.append(tdlist)
with open("rankings.csv",'w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(titles)
    for i in values:
        writer.writerow(i)

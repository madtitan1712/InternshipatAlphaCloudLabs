from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://www.thehindu.com/entertainment/movies/")
h3tags=driver.find_elements(By.CLASS_NAME,'title')
h3small=driver.find_elements(By.CLASS_NAME,'title big')
textlist=[]
for i in h3tags:
    if(i.text not in textlist):
        textlist.append(i.text.replace("\n"," "))
for j in h3small:
    if(j.text not in textlist):
        textlist.append(j.text.replace("\n"," "))
print(textlist)
from bs4 import BeautifulSoup
import requests
x=requests.get("https://realpython.github.io/fake-jobs/")
n=open("result.txt",'a')
soup=BeautifulSoup(x.content,features='html.parser')
main_itr=soup.find_all("div",class_="card-content")
for itr in main_itr:
    title=itr.find("h2",class_="title is-5")
    company=itr.find("h3",class_="subtitle is-6 company")
    location=itr.find("p",class_="location")
    print(f"Job title: {title.text.strip()}")
    print(f"Job provider: {company.text.strip()}")
    print(f"Location:{location.text.strip()}")
    print("\n")
    n.write(f"{title.text.strip()}")
    n.write(f"\n{company.text.strip()}")
    n.write(f"\n{location.text.strip()}")
    n.write("\n\n")
if(n.close()):
    print("File write complete")



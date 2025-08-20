import os
from bs4 import BeautifulSoup

for file in os.listdir("HTML"):
     with open(f"HTML/{file}", "r",encoding='utf-8') as f:
         html_content=f.read()
         soup=BeautifulSoup(html_content,"html.parser")
         print(soup.title)
         for link in soup.findAll("a"):
             print(link.get("href"))


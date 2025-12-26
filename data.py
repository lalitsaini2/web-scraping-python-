from bs4 import BeautifulSoup
import os
import pandas as pd
d = {'tittle': [], 'price': [], 'link':[]}
for file in os.listdir("data"):
 
     with open(f"/{file}",encoding="utf-8-" ) as f :
      html_doc= f.read()
      soup = BeautifulSoup(html_doc, 'html.parser')

     t= soup.find("div", class_='RG5Slk')
     tittle = t.get_text()
  
     l= soup.find('a')
     link = 'https://www.flipkart.com'+l['href']
  
     p= soup.find("div", class_='hZ3P6w DeU9vF')
     price =p.get_text()
     print(tittle,link,price)

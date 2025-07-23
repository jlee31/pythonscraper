from bs4 import BeautifulSoup
import requests
import re 

# ! Main Info
product = input("Enter product that you are looking for: ")
url = f"https://www.newegg.ca/p/pl?d={product}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

# Nitty Gritty
page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split('>')[-1][:-1])
# print(pages)

items_found = {}


for page in range(1, pages+1):
    url = f"https://www.newegg.ca/p/pl?d={product}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find(class_="list-wrap")
    items = div.find_all(text=re.compile(product))
    
    for item in items:
        parent = item.parent
        if parent.name != 'a':
            continue
        link = parent['href']
        next_parent = item.find_parent(class_="item_container")
        price = next_parent.find(class_="price-current").strong.string

        items_found[item] = {"price": price, "link": link}

print(items_found)
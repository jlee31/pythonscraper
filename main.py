#  import selenium 
from bs4 import BeautifulSoup

with open("index.html", "r") as file:
    doc = BeautifulSoup(file, "html.parser") 

print(doc.prettify())
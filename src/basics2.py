from bs4 import BeautifulSoup

with open("public/index2.html", 'r') as file:
    doc = BeautifulSoup(file, "html.parser")

result = doc.find("option")
print(result)
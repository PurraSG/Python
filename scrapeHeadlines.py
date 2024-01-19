import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

myLinks = soup.find_all("span", {"class":"titleline"})

keywords = ["ai", "microsoft", "python", "apple"]

for link in myLinks:
  text = link.text
  textWords = text.split()
  hasKeyword = False
  for word in textWords:
    if word.lower() in keywords:
      hasKeyword = True
  if hasKeyword:
    print(text)
    print()
    
  
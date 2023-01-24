from bs4 import BeautifulSoup
import requests
website='http://127.0.0.1:5501/results/log.html'
result=requests.get(website)
content=result.text

soup= BeautifulSoup(content,'lxml')
print(soup.prettify())

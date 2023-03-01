from bs4 import BeautifulSoup
import requests
from HTMLLogger import HTMLLogger


website='http://127.0.0.1:5501/results/log.html'
result=requests.get(website)
content=result.text

# soup= BeautifulSoup(content,'lxml')
# print(soup.prettify())


file_name = "console_logs.html"
log_file = "output.xml"


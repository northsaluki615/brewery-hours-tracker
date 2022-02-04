# For scraping brewery hours
#https://opensource.com/article/21/9/web-scraping-python-beautiful-soup

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pprint

url = "https://www.workingdraftbeer.com/" # For testing only
# uses "Footer-business-hours"

soup = BeautifulSoup(requests.get(url).content, 'html.parser')

results = soup.find('div', {'class': 'Footer-business-hours'})

print(results)

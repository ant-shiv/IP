from bs4 import BeautifulSoup #bs4 folder contaning module
import requests
import time


result = requests.get('https://jionews.com/magazines/reader/magazine/The-Caravan/Nov-2020/29108')
src = result.text
soup = BeautifulSoup(src, 'lxml')
jobs = soup.findAll('div',class_='pageSection')
print(jobs)

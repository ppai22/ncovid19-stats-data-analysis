import requests
from bs4 import BeautifulSoup
import json


who_url = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports/'
base_page_source = requests.get(who_url).text

soup = BeautifulSoup(base_page_source, 'lxml')

directory = []
for content_block in [soup.find_all('div', class_='sf-content-block content-block')[-4]]:
    for item in content_block.find_all('p'):
        try:
            directory.append([item.strong.text, 'https://www.who.int' + item.a['href']])
        except:
            pass
directory = directory[::-1]
with open('directory.json', 'w+') as f:
    json.dump(directory, f, indent=4)

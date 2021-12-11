import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
dateAndTitleNews = []
fullNews = []
for elem in root[0].findall('item'):
        dateAndTitleNews.append({'pubDate': elem.findtext('pubDate'), 'title': elem.findtext('title')})

for elem in root[0].findall('item'):
        dictionary = {}
        for child in elem:
            dictionary[child.tag] = child.text
        fullNews.append(dictionary)

with open('dateAndTitleNews.json', 'w', encoding='utf-8') as outFile:
    json.dump(dateAndTitleNews, fp=outFile, ensure_ascii=False, indent=4)

with open('fullNews.json', 'w', encoding='utf-8') as outFile2:
    json.dump(fullNews, fp=outFile2, ensure_ascii=False, indent=4)

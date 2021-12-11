import itertools
from urllib.request import urlopen
from json import loads


url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
data = loads(urlopen(url).read().decode('utf8'))
revisions = data['query']['pages']['183903']['revisions']
groupedRevisions = itertools.groupby(revisions, lambda revision: revision['timestamp'][:10])
for key, group in groupedRevisions:
    print(key, len(list(group)))

print(" ")

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data2 = loads(urlopen(url).read().decode('utf8'))
revisions2 = data2['query']['pages']['192203']['revisions']
groupedRevisions2 = itertools.groupby(revisions2, lambda revision: revision['timestamp'][:10])
maxCount = 0
maxKey = ""
for key, group in groupedRevisions2:
    listOfRevisions = list(group)
    if len(listOfRevisions) > maxCount:
        maxCount = len(listOfRevisions)
        maxKey = key
print(maxKey, maxCount)

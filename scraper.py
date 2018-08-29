import urllib.request as urllib2
from bs4 import BeautifulSoup
import pandas as pd
index_page = 'http://indicators.report/indicators/'
page_main = urllib2.urlopen(index_page)
soup_url = BeautifulSoup(page_main,'html.parser')
arr_url = []
for item in soup_url.find_all(attrs={'class': 'indicators-archive'}):
    for link in item.find_all('a'):
        arr_url.append(link.get('href'))
print(arr_url)

arr_main = []
for i in range(len(arr_url)):
    quote_page = arr_url[i]
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    name_box = soup.find('h1', attrs={'class': 'entry-title'})
    name = name_box.text.strip()
    content_box = soup.find('div', attrs={'class': 'entry-content'}).findAll('p')
    #print(content_box)
    arr = []
    for x in content_box:
        #print(x)
        arr.append(x.text.strip())
    arr_main.append(arr)
df = pd.DataFrame(arr_main)

import pickle
with open('df.pickle', 'wb') as f:
    pickle.dump(df, f)

print(df)
df.to_csv('df.csv')
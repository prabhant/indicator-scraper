html = u""
from bs4 import BeautifulSoup
import urllib.request as urllib2

soup = BeautifulSoup(page, 'html.parser')

for tag in soup.find("h1").next_siblings:
    if tag.name == "h1":
        break
    else:
        html += unicode(tag)
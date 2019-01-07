
# import requests

# from bs4 import BeautifulSoup

# url = 'http://alonhadat.com.vn/2-phong-khep-kin-so-28b-ngo-766-de-la-thanh-quan-dong-da-hn-1811622.html'

# a = requests.get(url).text

# soup = BeautifulSoup(a, 'lxml').text
# b = soup.findAll('div', {'class':'fone'})
# print(b.text)

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import requests
import pickle
"""
# df = pd.read_csv('data/url.csv')
result = []
url = pickle.load(open('url_user', 'rb'))

for i in url :
    a = requests.get(i)
    if a.status_code == 200 :
        response = urlopen(i)
        html = response.read()
        parsed_html = BeautifulSoup(html)
        result.append(parsed_html.body.find('div', attrs={'class':'fone'}).text)

import pickle
pickle.dump(result, open('sdt', 'wb'))



# # get the contents
# response = urlopen('http://alonhadat.com.vn/2-phong-khep-kin-so-28b-ngo-766-de-la-thanh-quan-dong-da-hn-1811622.html')
# html = response.read()
 
# parsed_html = BeautifulSoup(html)
# print (parsed_html.body.find('div', attrs={'class':'fone'}).text)
"""
a = pickle.load(open('sdt', 'rb'))
print(len(a))
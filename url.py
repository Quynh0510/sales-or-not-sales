
import pickle 
import pandas as pd 


df = pd.read_csv('data/alonhadat.csv')
url = []

user = pickle.load(open('user', 'rb'))

index = []

for i in user :
    index.append(list(df['Author']).index(i))
for i in index :
    url.append(df['Url'][i] if 'http' in df['Url'][i] else 'http://' + df['Url'][i])
pickle.dump(url, open('url_user', 'wb'))

# url = pickle.load(open('url_user', 'rb'))




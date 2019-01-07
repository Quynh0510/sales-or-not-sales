
import pandas as pd 
import pickle

df = pd.read_csv('data/alonhadat.csv')
df = df.fillna(' ')


dic = {}
dic1 = {}
sale = []
url = []

for i in range(len(df['Author'])) :
    if df['Author'][i] == ' ' :
        # print(df['Url'][i])
        url.append(df['Url'][i])
    else :
        if df['Author'][i] not in dic :
            dic[df['Author'][i]] = 1
        else :
            dic[df['Author'][i]] += 1



for i in dic.keys() :
    if dic[i] > 7 :
        dic1[i] = dic[i]
        sale.append(i)

pickle.dump(dic1, open('fre', 'wb'))
pickle.dump(sale, open('user', 'wb'))
pickle.dump(url, open('url_alo', 'wb'))








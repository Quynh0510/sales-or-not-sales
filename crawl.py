


from pymongo import MongoClient

uri = "mongodb://fbcrawler:VA32MdBzMK2aC5a7@10.5.36.107:2017/"
client = MongoClient(uri)


database = client["forumsdb"]
collection = database["Articles"]


query = {}
query["Domain"] = u"alonhadat.com.vn"

cursor = collection.find(query)
try:
    for doc in cursor:
        print(doc)
finally:
    client.close()


from pymongo import MongoClient

url= "mongodb+srv://admin:admin@atlascluster.p6ajt.mongodb.net/pytech"

client = MongoClient(url)

db = client.pytech

print((db.list_collection_names))


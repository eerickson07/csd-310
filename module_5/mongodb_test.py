from pymongo import MongoClient

import certifi

url = "mongodb+srv://admin:admin@cluster0.l7o1z.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url,tlsCAFile=certifi.where())

db = client.pytech

print("\n--Pytech Collection List--")

print(db.list_collection_names())

input("\n\n\ End of program, press any key to exit..." )
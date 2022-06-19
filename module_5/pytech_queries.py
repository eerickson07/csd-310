from pymongo import MongoClient

url = "mongodb+srv://admin:admin@atlascluster.p6ajt.mongodb.net/pytech"

client = MongoClient(url)

db = client.pytech

students = db.students

student_list = students.find()


print ("Displaying Students Documents")

for doc in student_list:
    print(" Student ID: + doc["student_id"] + "First Name:" + doc["first_name" + "Last Name" + doc ["last name"])

student_1 = students.find_one({"student_id": "1007"})

student_2 = students.find_one({"student_id": "1008"})

student_3 = students.find_one({"student_id": "1009"})

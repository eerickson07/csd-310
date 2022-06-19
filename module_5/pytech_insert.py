from pymongo import MongoClient

url = "mongodb+srv://admin:admin@atlascluster.p6ajt.mongodb.net/pytech"

client = MongoClient

db = client.pytech


john = {
    "student_id": "1007"
    "first_name":"John"
    "last_name": "Smith"
            }

william = {
    "student_id": "1008"
    "first_name": "William"
    "last_name": "Johnson"
    }
 jessica = {
    "student_id": "1009"
    "first_name": "Jessica"
    "last_name": "Ford"
}
john_student_id = students.insert_one(john).inserted_id

william_student_id = stuents.insert_one(john).inserted_id

jessica_student_id = stuents.insert_one(john).inserted_id

students = db.students

print ("student list")

print(john)

print(william)

print(jessica)
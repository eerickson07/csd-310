from pymongo import MongoClient

import certifi

url = "mongodb+srv://admin:admin@cluster0.l7o1z.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url,tlsCAFile=certifi.where())

db = client.pytech

students = db.students

student_list = students.find({})


print ("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "Last Name:" + doc ["last name"] + "\n")

john = students.find_one({"student_id": "1007"})

print("\n -- DISPLAYING STUDENT DOCUMENT FROM fine_one() QUERY --")
print("  Student ID: " + john["student_id"] + "\n First Name: " + john ["first_name"] + "\n Last Name: " + john["last_name"] + "\n")

input("\n\n End of program, press any key to continue...")
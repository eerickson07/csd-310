from pymongo import MongoClient

import certifi

url = "mongodb+srv://admin:admin@cluster0.l7o1z.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url,tlsCAFile=certifi.where())

db = client.pytech


john = {
    "student_id": "1007",
    "first_name": "John",
    "last_name": "Smith",
    "enrollment":[     
        {
            "term" : "Summer",
            "gpa": "3.8",
            "start_date": "June 1, 2022",
            "end_date": "August 31, 2022",
            "course": [
                {
            "course_id": "410",
            "description": "Data/Database Security",
            "instructor": "Henry Le",
            "grade": "A"
                }
        ]
        }
    ]
 }

william = {
    "student_id": "1008",
    "first_name": "William",
    "last_name": "Johnson",
    "enrollment": [
        {
            "term" : "Summer",
            "gpa": "3.2",
            "start_date": "June 1, 2022",
            "end_date": "August 31, 2022",
            "course": [
                {
            "course_id": "410",
            "description": "Data/Database Security",
            "instructor": "Henry Le",
            "grade": "A"
        }
        ]
    }
    ]
}
jessica = {
    "student_id": "1009",
    "first_name": "Jessica",
    "last_name": "Ford",
    "enrollment":  [
        {
            "term" : "Summer",
            "gpa": "3.4",
            "start_date": "June 1, 2022",
            "end_date": "August 31, 2022",
            "course": [
                {
            "course_id": "410",
            "description": "Data/Database Security",
            "instructor": "Henry Le",
            "grade": "A"
        }
        ]
    }
    ]
    }

students = db.students

print("\n -- INSERT STATEMENTS")
john_student_id = students.insert_one(john).inserted_id
print(" Inserted student record John Smith into the students collection with document_id" + str(john_student_id))

william_student_id = students.insert_one(william).inserted_id
print(" Inserted student record William Johnson into the students collection with document_id" + str(william_student_id))

jessica_student_id = students.insert_one(jessica).inserted_id
print(" Inserted student record Jessica Ford into the students collection with document_id" + str(jessica_student_id))



input("\n\n End of program, press any key to exit... ")
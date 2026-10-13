
from flask import Flask
from routes.users import users


client = MongoClient("")
db = client[""]
#may ilalagay pako dito


#session ID


def record_attendance():
    data = request.get_json(silent=True) or {}

    student_id = data.get("student_id", "").strip()
    name = data.get("name", "").strip()



#statement operation

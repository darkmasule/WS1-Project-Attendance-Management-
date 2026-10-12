
from flask import Flask
from routes.users import users



#may ilalagay pako dito





def record_attendance():
    data = request.get_json(silent=True) or {}

    student_id = data.get("student_id", "").strip()
    name = data.get("name", "").strip()

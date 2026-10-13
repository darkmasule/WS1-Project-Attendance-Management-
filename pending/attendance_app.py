from flask import Flask, request, jsonify

from collections import deque

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

client = MongoClient("")
db = client[""]
attendance_records.create_index(
    [("student_id", 1), ("session_id", 1)],
    unique=True
)


#session ID


def record_attendance():
    data = request.get_json(silent=True) or {}

    student_id = data.get("student_id", "").strip()
    name = data.get("name", "").strip()



#statement operation

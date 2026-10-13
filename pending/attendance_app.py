from flask import Flask, request, jsonify

from collections import deque

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

client = MongoClient("mongodb+srv://felipejrnoriel_db_user:aqwkTLilxErXraRO@fp-db.8nhcswv.mongodb.net/")
db = client[""]
attendance_records.create_index(
    [("student_id", 1), ("session_id", 1)],
    unique=True
)

attendance_queue = deque()
SESSION_ID = ""
#need pa to i complete

#session ID


def record_attendance():
    data = request.get_json(silent=True) or {}

    student_id = data.get("student_id", "").strip()
    name = data.get("name", "").strip()



#statement operation
while attendance_queue:
    student = attendance_queue.popleft()

try:
    #di pa tapos need pa ng return except return blocks

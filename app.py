import os

from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# TODO Enter this first in terminal if not set yet:
# $env:MONGO_URI = "mongodb+srv://felipejrnoriel_db_user:aqwkTLilxErXraRO@fp-db.8nhcswv.mongodb.net/"
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

db = client["testing"]
collection = db["users"]


@app.route("/")
def home():
    return render_template("index_test.html")


@app.route("/submit", methods=["POST"])
def submit():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    user = {"first_name": first_name, "last_name": last_name, "email": email}

    collection.insert_one(user)

    return f""" <h1>Submitted Successfully!</h1> <p>Name: {first_name} {last_name}</p> <p>Email: {email}</p> <a href="/">Back to Form</a> """


if __name__ == "__main__":
    app.run(debug=True)

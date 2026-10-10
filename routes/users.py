from flask import Blueprint, render_template, request
from database.db import collection

users = Blueprint("users", __name__)


@users.route("/")
def home():
    return render_template("index_test.html")


@users.route("/submit", methods=["POST"])
def submit():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    user = {"first_name": first_name, "last_name": last_name, "email": email}

    collection.insert_one(user)

    return f""" <h1>Submitted Successfully!</h1>
    <p>Name: {first_name} {last_name}</p>
    <p>Email: {email}</p> 
    <a href="/">Back to Form</a> """

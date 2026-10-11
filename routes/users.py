from flask import Blueprint, render_template, request
from database.db import collection
from werkzeug.security import generate_password_hash, check_password_hash

users = Blueprint("users", __name__)


@users.route("/")
def home():
    return render_template("index.html")


@users.route("/submit", methods=["POST"])
def submit():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    id_number = request.form.get("id_number")
    program = request.form.get("program")
    year_level = request.form.get("year_level")
    section = request.form.get("section")
    email = request.form.get("email")
    password = generate_password_hash(request.form.get("password"))
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "id_number": id_number,
        "program": program,
        "year_level": year_level,
        "section": section,
        "email": email,
        "password": password,
    }

    collection.insert_one(user)

    return """ <h1>Submitted Successfully!</h1>
    <a href="/">Back to Form</a> """

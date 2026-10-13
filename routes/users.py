from flask import Blueprint, render_template, request, session, redirect, url_for
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


@users.route("/login", methods=["POST"])
def login():
    id_number = request.form.get("id_number")
    password = request.form.get("password")

    user = collection.find_one({"id_number": id_number})

    if user and check_password_hash(user["password"], password):
        session["user_id"] = str(user["_id"])
        session["id_number"] = user["id_number"]

        return redirect(url_for("users.test"))

    return "Invalid ID number or password"


@users.route("/testing")
def test():
    if "user_id" not in session:
        return redirect(url_for("users.home"))

    return render_template("index_test.html")


@users.route("/student/profile")
def student_profile():
    return render_template("student_profile.html")

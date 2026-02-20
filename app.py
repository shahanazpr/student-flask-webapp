from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
FILENAME = "students.json"

def load_students():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_students(students):
    with open(FILENAME, "w") as file:
        json.dump(students, file, indent=4)

@app.route("/")
def index():
    students = load_students()
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"]
    roll = request.form["roll"]
    course = request.form["course"]

    students = load_students()
    students.append({"name": name, "roll": roll, "course": course})
    save_students(students)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
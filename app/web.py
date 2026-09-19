from flask import Flask, render_template, request
from app.database.database import (save_applicant, create_student_table)
app = Flask(__name__, template_folder="../templates",  static_folder="../static")

@app.route("/")
def admission_form():
    return render_template("admission_form.html")
@app.route("/save", methods=["POST"])
def save():
     # get data from HTML form and insert into applicant
    create_student_table()
    
    # create applicant dictionary
    
    applicant = {
    "First Name": request.form["first_name"],
    "Last Name": request.form["last_name"],
    "Date of Birth" : request.form["date_of_birth"],
    "Gender": request.form["gender"],
    "VSN" : None,
    "Year Level" : None,
    "Class Name" : None
}
    save_applicant(applicant)

    return "Applicant received successfully!"
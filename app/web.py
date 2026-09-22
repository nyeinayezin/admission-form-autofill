from flask import Flask, render_template, send_file, request
from app.database.database import (save_applicant, create_tables, view_applicants, get_current_applicant)
from app.pdf_generator import generate_application_pdf
app = Flask(__name__, template_folder="../templates",  static_folder="../static")
create_tables()
@app.route("/")
def admission_form():
    return render_template("admission_form.html")

@app.route("/save", methods=["POST"])
def save():
     # get data from HTML form and insert into students 
    applicant = {
    "First Name": request.form["first_name"],
    "Last Name": request.form["last_name"],
    "Date of Birth" : request.form["date_of_birth"],
    "Gender": request.form["gender"]
    }
    guardian1 = {
    "guardian1_first_name": request.form["guardian1_first_name"],
    "guardian1_last_name": request.form["guardian1_last_name"],
    "guardian1_phone": request.form["guardian1_phone"],
    "guardian1_email" : request.form["guardian1_email"],
    "guardian1_address" : request.form["guardian1_address"],
    "guardian1_relationship" : request.form["guardian1_relationship"],
    "guardian1_primary" : 1 if request.form["primary_contact"] == "guardian1" else 0
    }
    guardian2 = {
    "guardian2_first_name": request.form["guardian2_first_name"],
    "guardian2_last_name": request.form["guardian2_last_name"],
    "guardian2_phone": request.form["guardian2_phone"],
    "guardian2_email" : request.form["guardian2_email"],
    "guardian2_address" : request.form["guardian2_address"],
    "guardian2_relationship" : request.form["guardian2_relationship"],
    "guardian2_primary" : 1 if request.form["primary_contact"] == "guardian2" else 0

    }
    student_id = save_applicant(applicant,guardian1,guardian2)
    applicant = get_current_applicant(student_id)
    if applicant is None:
        return "Student not found", 404
    generate_application_pdf(applicant)
    #applicants = view_applicants()
    #print("VIEW RESULTS:", applicants)
    #return view_applicants()
    
    return render_template("view_current_student.html", applicant = applicant)

@app.route("/generate-pdf/<int:student_id>")

def generate_pdf(student_id):

    applicant = get_current_applicant(student_id)

    if applicant is None:
        return "Student not found", 404

    pdf_path = generate_application_pdf(applicant)

    return send_file(
        pdf_path,
        as_attachment=True
    )
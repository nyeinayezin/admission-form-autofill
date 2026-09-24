# admission-form-autofill
A DEMO web application that automatically fills admission forms using applicant information.
This repository contains a sample small project demo showcasing selected working functions of the application. It is not the fully developed web application. The implementation is intended to demonstrate the project concept, core functionality, and development approach.
web.py is the entry point, not main.py
git clone <repository>
cd admission-form-autofill
pip install -r requirements.txt
python -m flask --app app.web run
py -m pip install pymupdf #autogenerate .pdf file from submission of web_form
py -m pip install matplotlib
py -m pip install numpy
Future Development
A planned enhancement is to automate the process of converting scanned application documents into structured database records. The workflow will include document scanning, OCR/data extraction, data validation, and automatic insertion of the extracted information into the database.
Planned workflow:
Scanned Document → OCR/Data Extraction → Validation → Database → Web Application

import sqlite3
from app.config import (DATABASE_NAME, SQL_DIR)
def get_connection():
    return sqlite3.connect(DATABASE_NAME)
def load_sql(sql_file_name):
    sql_file = SQL_DIR/sql_file_name
    with open(sql_file, "r", encoding="utf-8") as file:
        return file.read()

#creates the students table        
def create_tables():
    connection = get_connection()
    sql = load_sql("schema.sql")
    connection.executescript(sql)
    connection.commit()
    connection.close()
    print("Tables are created successfully!")
#saves a student/applicant record
def save_applicant(applicant,guardian1,guardian2):
    connection = get_connection()
    cursor = connection.cursor()
    sql = load_sql("insert_applicant.sql")
    cursor.execute(
       sql,
        (
            applicant["First Name"],
            applicant["Last Name"],
            applicant["Date of Birth"],
            applicant["Gender"]           
        )
    )
    #get id for the row just inserted and set student_id for students_guardians 
    student_id = cursor.lastrowid
    print("applicant saved successfully")
    cursor.execute("""SELECT * FROM students """)
    #print(cursor.fetchall())
    sql_guardian = load_sql("insert_guardians.sql")
    cursor.execute(
       sql_guardian,
        (
            guardian1["guardian1_first_name"],
            guardian1["guardian1_last_name"],
            guardian1["guardian1_phone"],
            guardian1["guardian1_email"],
            guardian1["guardian1_address"]
           
        )
    )
    #get id for the row just inserted and set guardian_id for students_guardians 
    guardian1_id = cursor.lastrowid
    cursor.execute(
       sql_guardian,
        (
            guardian2["guardian2_first_name"],
            guardian2["guardian2_last_name"],
            guardian2["guardian2_phone"],
            guardian2["guardian2_email"],
            guardian2["guardian2_address"]
           
        )
    )
    #get id for the row just inserted and set guardian_id for students_guardians 
    guardian2_id = cursor.lastrowid
    cursor.execute("""SELECT * FROM Guardians""")
    sql_students_guardians = load_sql("insert_students_guardians.sql")
    cursor.execute(
        sql_students_guardians,
        (
            student_id,
            guardian1_id,
            guardian1["guardian1_relationship"],
            guardian1["guardian1_primary"]
        )
    )
    cursor.execute(
        sql_students_guardians,
        (
            student_id,
            guardian2_id,
            guardian2["guardian2_relationship"],
            guardian2["guardian2_primary"]
        )
    )
    connection.commit()
    connection.close()
    return student_id
    print("guardians saved successfully!")

def view_applicants():
    connection = get_connection()
    cursor = connection.cursor()

    view_sql = load_sql("view_result.sql")

    cursor.execute(view_sql)

    rows = cursor.fetchall()
    print("NUMBER OF RAW ROWS:", len(rows))

    
    applicants = []

    for row in rows:
        print("PROCESSING ROW:", row)

        student_id = row[0]
        student = None

        for applicant in applicants:
            if applicant["student_id"] == student_id:
                student = applicant
                break

        if student is None:
            student = {
                "student_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "date_of_birth": row[3],
                "gender": row[4],
                "guardians": []
            }

            applicants.append(student)

        print("BEFORE APPEND:", student["guardians"])

        student["guardians"].append({
            "guardian_id": row[5],
            "first_name": row[6],
            "last_name": row[7],
            "phone": row[8],
            "email": row[9],
            "address": row[10],
            "relationship": row[11],
            "is_primary_contact": row[12]
        })

        print("AFTER APPEND:", student["guardians"])

    connection.close()

    return applicants

def get_current_applicant(student_id):
    connection = get_connection()
    cursor = connection.cursor()

    view_sql = load_sql("view_current_student.sql")

    cursor.execute(view_sql, (student_id,))

    rows = cursor.fetchall()

    applicant = None

    for row in rows:

        if applicant is None:
            applicant = {
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "date_of_birth": row[3],
                "gender": row[4],
                "guardians": []
            }

        applicant["guardians"].append({
            "id": row[5],
            "first_name": row[6],
            "last_name": row[7],
            "phone": row[8],
            "email": row[9],
            "address": row[10],
            "relationship": row[11],
            "is_primary_contact": row[12]
        })

    connection.close()

    return applicant
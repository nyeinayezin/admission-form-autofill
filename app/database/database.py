import sqlite3
from app.config import (DATABASE_NAME, SQL_DIR)
def get_connection():
    return sqlite3.connect(DATABASE_NAME)
def load_sql(sql_file_name):
    sql_file = SQL_DIR/sql_file_name
    with open(sql_file, "r", encoding="utf-8") as file:
        return file.read()
#creates the students table        
def create_student_table():
    connection = get_connection()
    sql = load_sql("schema.sql")
    connection.executescript(sql)
    connection.commit()
    connection.close()
    print("Table created successfully!")
#saves a student/applicant record
def save_applicant(applicant):
    connection = get_connection()
    sql = load_sql("insert_applicant.sql")
    cursor = connection.cursor()
    cursor.execute(
       sql,
        (
            applicant["First Name"],
            applicant["Last Name"],
            applicant["Date of Birth"],
            applicant["Gender"],
            applicant["VSN"],
            applicant["Year Level"],
            applicant["Class Name"]

        )
    )
    cursor.execute("""SELECT * FROM students """)
    print(cursor.fetchall())
    connection.commit()
    connection.close()

    print("Applicant saved successfully!")
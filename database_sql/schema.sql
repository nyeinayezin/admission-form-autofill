-- Create the students table
/*
    This table stores
    student information.
*/
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth TEXT,
    gender TEXT,
    vsn TEXT,
    year_level TEXT,
    class_name TEXT
);
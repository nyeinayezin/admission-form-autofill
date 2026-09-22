-- Create the students table
/*
    This table stores
    student information.
*/
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth TEXT,
    gender TEXT
);

CREATE TABLE IF NOT EXISTS guardians (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    address TEXT
);

CREATE TABLE IF NOT EXISTS students_guardians (
    student_id INTEGER NOT NULL,
    guardian_id INTEGER NOT NULL,
    relationship TEXT NOT NULL,
    is_primary_contact INTEGER DEFAULT 0,

    PRIMARY KEY (student_id, guardian_id),

    FOREIGN KEY (student_id)
        REFERENCES students(id),

    FOREIGN KEY (guardian_id)
        REFERENCES guardians(id)
);
CREATE TABLE IF NOT EXISTS addresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    address_line TEXT,
    suburb TEXT,
    state TEXT,
    postcode TEXT,
    country TEXT,

    FOREIGN KEY (student_id)
        REFERENCES students(id)
);
CREATE TABLE IF NOT EXISTS enrollments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    vsn TEXT,
    year_level TEXT,
    class_name TEXT,
    enrollment_date TEXT,
    approval_date TEXT,
    start_date TEXT,
    withdrawal_date TEXT,
    status TEXT,

    FOREIGN KEY (student_id)
        REFERENCES students(id)
);
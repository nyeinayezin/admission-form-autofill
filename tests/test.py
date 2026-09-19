"""import sqlite3
def create_database():
    conn = sqlite3.connect("test5.db")
    cursor = conn.cursor()
    cursor.execute ("CREATE TABLE IF NOT EXISTS student (id INTEGER, name TEXT)")
    conn.commit()
    conn.close()
    print("Table created successfully!")
create_database()
CREATE TABLE IF NOT EXISTS applicants(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    dad_name TEXT,
    mom_name TEXT,
    address TEXT
)"""

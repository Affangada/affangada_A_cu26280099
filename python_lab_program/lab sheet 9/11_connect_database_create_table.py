"""Python CRUD Operations Lab Sheet 09 solution."""
# Connect to SQLite database and create the students table.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll_no TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            marks REAL NOT NULL
        )
    """)
    connection.commit()
    print("Connected to database and students table is ready.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

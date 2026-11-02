"""Python CRUD Operations Lab Sheet 09 solution."""
# Read and display all student records from SQLite.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll_no TEXT PRIMARY KEY, name TEXT NOT NULL, marks REAL NOT NULL
        )
    """)
    cursor.execute("SELECT roll_no, name, marks FROM students")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print("Roll:", row[0], "| Name:", row[1], "| Marks:", row[2])
    else:
        print("No student records found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

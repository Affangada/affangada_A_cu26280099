"""Python CRUD Operations Lab Sheet 09 solution."""
# Find the student with the highest marks.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT roll_no, name, marks FROM students
        ORDER BY marks DESC LIMIT 1
    """)
    row = cursor.fetchone()
    if row:
        print("Student with highest marks:", row)
    else:
        print("No student records found.")
except sqlite3.Error as error:
    print("Database error (create the table first):", error)
finally:
    if connection is not None:
        connection.close()

"""Python CRUD Operations Lab Sheet 09 solution."""
# Search for a specific student using roll number.
import sqlite3

connection = None
try:
    roll = input("Enter roll number to search: ").strip()
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll,))
    row = cursor.fetchone()
    if row:
        print("Student found:", row)
    else:
        print("Student not found.")
except sqlite3.Error as error:
    print("Database error (create the table first):", error)
finally:
    if connection is not None:
        connection.close()

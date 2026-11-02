"""Python CRUD Operations Lab Sheet 09 solution."""
# Display all student records sorted by student name.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("SELECT roll_no, name, marks FROM students ORDER BY name ASC")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No student records found.")
except sqlite3.Error as error:
    print("Database error (create the table first):", error)
finally:
    if connection is not None:
        connection.close()

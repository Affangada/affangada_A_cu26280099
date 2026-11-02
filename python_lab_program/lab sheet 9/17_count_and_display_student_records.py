"""Python CRUD Operations Lab Sheet 09 solution."""
# Count and display the number of student records.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]
    print("Total number of student records:", count)
except sqlite3.Error as error:
    print("Database error (create the table first):", error)
finally:
    if connection is not None:
        connection.close()

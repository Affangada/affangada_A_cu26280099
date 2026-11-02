"""Python Database Management Lab Sheet 08 solution."""
# Find the average marks of all students.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("SELECT AVG(marks) FROM students")
    average = cursor.fetchone()[0]
    if average is None:
        print("No student marks available.")
    else:
        print("Average marks:", round(average, 2))
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

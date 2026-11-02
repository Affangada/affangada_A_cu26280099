"""Python Database Management Lab Sheet 08 solution."""
# Update the marks of a student using their ID.
import sqlite3

connection = None
try:
    student_id = int(input("Enter student ID: "))
    new_marks = float(input("Enter new marks: "))

    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE students SET marks=? WHERE id=?",
        (new_marks, student_id)
    )
    connection.commit()
    print("Marks updated." if cursor.rowcount else "Student ID not found.")
except ValueError:
    print("ID and marks must be valid numbers.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

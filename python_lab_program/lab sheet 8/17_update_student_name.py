"""Python Database Management Lab Sheet 08 solution."""
# Update the name of a student using their ID.
import sqlite3

connection = None
try:
    student_id = int(input("Enter student ID: "))
    new_name = input("Enter new student name: ").strip()

    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE students SET name=? WHERE id=?",
        (new_name, student_id)
    )
    connection.commit()
    print("Name updated." if cursor.rowcount else "Student ID not found.")
except ValueError:
    print("Student ID must be a valid integer.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

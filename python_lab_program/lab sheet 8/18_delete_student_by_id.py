"""Python Database Management Lab Sheet 08 solution."""
# Delete one student record using the student ID.
import sqlite3

connection = None
try:
    student_id = int(input("Enter student ID to delete: "))
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    connection.commit()
    print("Student deleted." if cursor.rowcount else "Student ID not found.")
except ValueError:
    print("Student ID must be a valid integer.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

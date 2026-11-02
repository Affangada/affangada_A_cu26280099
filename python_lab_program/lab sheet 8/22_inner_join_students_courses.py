"""Python Database Management Lab Sheet 08 solution."""
# Perform an INNER JOIN between students and courses.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT students.name, courses.course_name
        FROM students
        INNER JOIN courses ON students.id = courses.student_id
    """)
    rows = cursor.fetchall()
    for row in rows:
        print("Student:", row[0], "| Course:", row[1])
    if not rows:
        print("No matching student-course records found.")
except sqlite3.Error as error:
    print("Database error (run Program 21 first):", error)
finally:
    if connection is not None:
        connection.close()

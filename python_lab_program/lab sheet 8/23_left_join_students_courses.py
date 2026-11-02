"""Python Database Management Lab Sheet 08 solution."""
# Perform a LEFT JOIN between students and courses.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT students.name, courses.course_name
        FROM students
        LEFT JOIN courses ON students.id = courses.student_id
        ORDER BY students.name
    """)
    rows = cursor.fetchall()
    for row in rows:
        print("Student:", row[0], "| Course:", row[1] or "No course assigned")
except sqlite3.Error as error:
    print("Database error (run Program 21 first):", error)
finally:
    if connection is not None:
        connection.close()

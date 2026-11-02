"""Python Database Management Lab Sheet 08 solution."""
# Display students grouped by age and count students in each age group.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT age, COUNT(*) AS student_count
        FROM students
        GROUP BY age
        ORDER BY age
    """)
    rows = cursor.fetchall()
    print("Age | Number of students")
    for age, count in rows:
        print(age, "|", count)
    if not rows:
        print("No student records found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

"""Python Database Management Lab Sheet 08 solution."""
# Create a courses table and insert course data.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY,
            course_name TEXT NOT NULL,
            student_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)
    courses = [
        (101, "Python", 1),
        (102, "DBMS", 2),
        (103, "Java", 3),
        (104, "Cloud Computing", 4)
    ]
    cursor.executemany("""
        INSERT OR REPLACE INTO courses (course_id, course_name, student_id)
        VALUES (?, ?, ?)
    """, courses)
    connection.commit()
    print("Courses table created and course data inserted.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

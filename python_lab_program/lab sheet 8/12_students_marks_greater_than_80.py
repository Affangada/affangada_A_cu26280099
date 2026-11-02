"""Python Database Management Lab Sheet 08 solution."""
# Retrieve students whose marks are greater than 80.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, name, marks FROM students
        WHERE marks > ?
    """, (80,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    if not rows:
        print("No students scored above 80.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

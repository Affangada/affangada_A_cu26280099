"""Python Database Management Lab Sheet 08 solution."""
# Retrieve student data sorted by marks in descending order.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, name, marks FROM students
        ORDER BY marks DESC
    """)
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

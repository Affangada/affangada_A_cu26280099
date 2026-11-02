"""Python Database Management Lab Sheet 08 solution."""
# Display only the name and marks columns.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("SELECT name, marks FROM students")
    rows = cursor.fetchall()

    print("Name | Marks")
    for row in rows:
        print(row[0], "|", row[1])
    if not rows:
        print("No student records found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

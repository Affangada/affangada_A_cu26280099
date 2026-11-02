"""Python Database Management Lab Sheet 08 solution."""
# Delete all student records where marks are below 40.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE marks < ?", (40,))
    connection.commit()
    print("Number of student records deleted:", cursor.rowcount)
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

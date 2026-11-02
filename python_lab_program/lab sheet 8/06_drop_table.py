"""Python Database Management Lab Sheet 08 solution."""
# Drop (delete) the students table from the database.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS students")
    connection.commit()
    print("Students table dropped successfully (if it existed).")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

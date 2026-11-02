"""Python CRUD Operations Lab Sheet 09 solution."""
# Delete a student record using roll number.
import sqlite3

connection = None
try:
    roll = input("Enter roll number to delete: ").strip()
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE roll_no = ?", (roll,))
    connection.commit()
    if cursor.rowcount:
        print("Student record deleted.")
    else:
        print("Student not found.")
except sqlite3.Error as error:
    print("Database error (create the table first):", error)
finally:
    if connection is not None:
        connection.close()

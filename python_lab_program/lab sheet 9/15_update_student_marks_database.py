"""Python CRUD Operations Lab Sheet 09 solution."""
# Update student marks using roll number.
import sqlite3

connection = None
try:
    roll = input("Enter roll number: ").strip()
    marks = float(input("Enter new marks: "))
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE students SET marks = ? WHERE roll_no = ?", (marks, roll))
    connection.commit()
    if cursor.rowcount:
        print("Student marks updated.")
    else:
        print("Student not found.")
except ValueError:
    print("Marks must be a valid number.")
except sqlite3.Error as error:
    print("Database error (create the table first):", error)
finally:
    if connection is not None:
        connection.close()

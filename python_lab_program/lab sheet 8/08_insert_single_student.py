"""Python Database Management Lab Sheet 08 solution."""
# Insert a single student record into the students table.
import sqlite3

connection = None
try:
    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ").strip()
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO students (id, name, age, marks)
        VALUES (?, ?, ?, ?)
    """, (student_id, name, age, marks))
    connection.commit()
    print("Student record inserted successfully.")
except ValueError:
    print("ID, age, and marks must be valid numbers.")
except sqlite3.IntegrityError:
    print("That student ID already exists.")
except sqlite3.Error as error:
    print("Database error (check that Program 03 was run):", error)
finally:
    if connection is not None:
        connection.close()

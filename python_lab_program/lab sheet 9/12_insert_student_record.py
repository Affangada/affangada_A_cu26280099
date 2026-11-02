"""Python CRUD Operations Lab Sheet 09 solution."""
# Insert a new student record into the SQLite table.
import sqlite3

connection = None
try:
    roll = input("Roll number: ").strip()
    name = input("Student name: ").strip()
    marks = float(input("Marks: "))
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll_no TEXT PRIMARY KEY, name TEXT NOT NULL, marks REAL NOT NULL
        )
    """)
    cursor.execute("INSERT INTO students VALUES (?, ?, ?)", (roll, name, marks))
    connection.commit()
    print("Student record inserted successfully.")
except ValueError:
    print("Marks must be a valid number.")
except sqlite3.IntegrityError:
    print("This roll number already exists.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

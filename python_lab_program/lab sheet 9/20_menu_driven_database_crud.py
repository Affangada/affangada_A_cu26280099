"""Python CRUD Operations Lab Sheet 09 solution."""
# Menu-driven application for all student CRUD operations using SQLite.
import sqlite3

DB_NAME = "college.db"

def create_table(connection):
    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll_no TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            marks REAL NOT NULL
        )
    """)
    connection.commit()

def add_student(connection):
    roll = input("Roll number: ").strip()
    name = input("Name: ").strip()
    marks = float(input("Marks: "))
    connection.execute(
        "INSERT INTO students (roll_no, name, marks) VALUES (?, ?, ?)",
        (roll, name, marks)
    )
    connection.commit()
    print("Student added.")

def view_students(connection):
    rows = connection.execute(
        "SELECT roll_no, name, marks FROM students ORDER BY roll_no"
    ).fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No student records found.")

def update_student(connection):
    roll = input("Roll number to update: ").strip()
    marks = float(input("New marks: "))
    cursor = connection.execute(
        "UPDATE students SET marks = ? WHERE roll_no = ?", (marks, roll)
    )
    connection.commit()
    print("Student updated." if cursor.rowcount else "Student not found.")

def delete_student(connection):
    roll = input("Roll number to delete: ").strip()
    cursor = connection.execute(
        "DELETE FROM students WHERE roll_no = ?", (roll,)
    )
    connection.commit()
    print("Student deleted." if cursor.rowcount else "Student not found.")

connection = None
try:
    connection = sqlite3.connect(DB_NAME)
    create_table(connection)
    while True:
        print("\\n1.Create 2.Read 3.Update 4.Delete 5.Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                add_student(connection)
            elif choice == "2":
                view_students(connection)
            elif choice == "3":
                update_student(connection)
            elif choice == "4":
                delete_student(connection)
            elif choice == "5":
                print("Exiting application.")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter marks as a valid number.")
        except sqlite3.IntegrityError:
            print("That roll number already exists.")
        except sqlite3.Error as error:
            print("Database operation failed:", error)
            connection.rollback()
except sqlite3.Error as error:
    print("Could not open database:", error)
finally:
    if connection is not None:
        connection.close()

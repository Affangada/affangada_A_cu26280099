"""Python Database Management Lab Sheet 08 solution."""
# Insert multiple student records using executemany().
import sqlite3

connection = None
try:
    students = [
        (1, "Aman", 20, 85.5),
        (2, "Sara", 21, 92.0),
        (3, "Rahul", 20, 74.0),
        (4, "Priya", 22, 88.5),
        (5, "John", 21, 39.0)
    ]

    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.executemany("""
        INSERT OR REPLACE INTO students (id, name, age, marks)
        VALUES (?, ?, ?, ?)
    """, students)
    connection.commit()
    print("Multiple student records inserted successfully.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

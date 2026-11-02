"""Python Database Management Lab Sheet 08 solution."""
# Read and display all records from the students table.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, age, marks FROM students")
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print("ID:", row[0], "| Name:", row[1],
                  "| Age:", row[2], "| Marks:", row[3])
    else:
        print("No student records found.")
except sqlite3.Error as error:
    print("Database error (check that the table exists):", error)
finally:
    if connection is not None:
        connection.close()

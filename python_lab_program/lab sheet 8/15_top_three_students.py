"""Python Database Management Lab Sheet 08 solution."""
# Display the top three students with the highest marks.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, name, marks FROM students
        ORDER BY marks DESC LIMIT 3
    """)
    rows = cursor.fetchall()

    print("Top 3 students:")
    for row in rows:
        print(row)
    if not rows:
        print("No student records found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

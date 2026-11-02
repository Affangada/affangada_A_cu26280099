"""Python Database Management Lab Sheet 08 solution."""
# Empty the students table while keeping its structure intact.
# SQLite does not support TRUNCATE TABLE; DELETE without WHERE has the same
# effect on table rows while preserving the table definition.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students")
    connection.commit()
    print("All student records deleted; table structure is unchanged.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

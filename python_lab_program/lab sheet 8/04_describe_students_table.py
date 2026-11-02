"""Python Database Management Lab Sheet 08 solution."""
# Display the structure of the students table.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info(students)")
    columns = cursor.fetchall()

    if columns:
        print("Students table structure:")
        print("CID | Name | Data Type | Not Null | Default | Primary Key")
        for column in columns:
            print(column)
    else:
        print("Table does not exist. Run Program 03 first.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

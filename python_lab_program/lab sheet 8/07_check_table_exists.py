"""Python Database Management Lab Sheet 08 solution."""
# Check whether a specific table exists in the database.
import sqlite3

table_name = "students"
connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
        (table_name,)
    )
    if cursor.fetchone():
        print(table_name, "table exists.")
    else:
        print(table_name, "table does not exist.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

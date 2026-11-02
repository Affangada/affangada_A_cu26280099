"""Python Database Management Lab Sheet 08 solution."""
# Connect to an SQLite database and display a success message.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    print("Successfully connected to the SQLite database.")
except sqlite3.Error as error:
    print("Database connection failed:", error)
finally:
    if connection is not None:
        connection.close()
        print("Database connection closed.")

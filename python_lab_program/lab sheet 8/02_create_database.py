"""Python Database Management Lab Sheet 08 solution."""
# Create a new SQLite database.
# SQLite creates the database file automatically when it does not exist.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("new_college.db")
    print("Database 'new_college.db' created/opened successfully.")
except sqlite3.Error as error:
    print("Error creating database:", error)
finally:
    if connection is not None:
        connection.close()

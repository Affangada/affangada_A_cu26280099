"""Python Database Management Lab Sheet 08 solution."""
# List all tables available in the connected SQLite database.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type = 'table' AND name NOT LIKE 'sqlite_%'
        ORDER BY name
    """)
    tables = cursor.fetchall()

    if tables:
        print("Tables in database:")
        for table in tables:
            print(table[0])
    else:
        print("No tables found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()

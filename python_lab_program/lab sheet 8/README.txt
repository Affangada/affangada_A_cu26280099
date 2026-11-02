COER UNIVERSITY — MCA I Semester (Session 2026-2027)
Lab Sheet-08: Python Programming Lab — Database Management using Python

This folder contains 25 solved Python programs, each in its own numbered .py file.

DATABASE USED
- SQLite via Python's built-in sqlite3 module.
- No separate database server or pip installation is required.
- All database programs use the file college.db in the current working directory.

RECOMMENDED RUN ORDER
1. Run Program 01 to test the connection.
2. Run Program 02 to see how a separate SQLite database file is created.
3. Run Program 03 to create the students table in college.db.
4. Run Program 04 and 05 to inspect the table and list tables.
5. Run Program 09 to insert sample student records (IDs 1–5).
   Alternatively, use Program 08 to insert one record manually.
6. Run Programs 10–19 and 24–25 to practise SELECT, UPDATE, DELETE,
   sorting, aggregate functions and GROUP BY.
7. Run Program 21 to create and populate the courses table.
8. Run Programs 22–23 to practise INNER JOIN and LEFT JOIN.

IMPORTANT
- Program 06 drops the students table. Run it only when you intend to delete
  the table definition and its data.
- Program 20 empties the students table but keeps its structure. SQLite does
  not have TRUNCATE TABLE; DELETE FROM students provides the equivalent result.
- Program 19 permanently deletes records with marks below 40.
- Program 21 uses sample course rows linked to student IDs 1–4.
- Programs 22 and 23 require both students and courses tables.
- Run Program 03 again if the students table was dropped.
- Programs 08, 16, 17 and 18 request input from the user.
- Database operations use parameterized SQL queries where values are supplied.

HOW TO RUN
1. Extract the ZIP file.
2. Open the folder in VS Code, IDLE, or PyCharm.
3. Run each .py file with Python 3.

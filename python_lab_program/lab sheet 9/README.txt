COER UNIVERSITY — MCA I Semester (Session 2026-2027)
Lab Sheet-09: Python Programming Lab — CRUD Operations using Python

This folder contains all 20 solved programs in separate numbered .py files.

PROGRAMS 01–10
List/dictionary CRUD, menu-driven books and products, and file-based CRUD.
The file-based examples create their data files in the current working directory.

PROGRAMS 11–20
SQLite database CRUD programs. SQLite is included with standard Python, so no
MySQL server or third-party package is required. The programs use a database
file named college.db, created in the folder from which you run them.

RECOMMENDED DATABASE RUN ORDER
1. Run 11_connect_database_create_table.py once to create the table.
2. Run 12_insert_student_record.py to add sample records.
3. Run 13–19 to read, search, update, delete, count, sort, and find top marks.
4. Run 20_menu_driven_database_crud.py for the complete menu-driven application.

HOW TO RUN
1. Extract the ZIP file.
2. Open the folder in VS Code, IDLE, or PyCharm.
3. Run each .py file using Python 3.

NOTES
- Database examples use Python's built-in sqlite3 module.
- SQL values are passed with placeholders (?) to avoid unsafe query construction.
- File and database resources are closed using context managers or finally blocks.
- Each program is independent. Programs 13–20 expect the students table created
  by Program 11 (Program 12 and Program 20 also create it if needed).

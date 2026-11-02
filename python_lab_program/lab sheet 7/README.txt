COER UNIVERSITY — MCA I Semester (Session 2026-2027)
Lab Sheet-07: Python Programming Lab — File Handling (Read and Write)

This folder contains all 30 solved programs in separate numbered Python files.

TEXT FILE PROGRAMS (01–20)
- Most programs use sample.txt as the default input file.
- Run Program 01 first to create sample.txt.
- Program 13 reads numbers.txt; create this file with numeric values separated
  by spaces or new lines.
- Program 20 merges file1.txt and file2.txt; create these two files first.

CSV PROGRAMS (21–30)
- Run Program 21 first to create students.csv with sample student data.
- Programs 22–29 read or process students.csv.
- Program 25 appends a record to students.csv.
- Program 30 asks for one or more CSV file names separated by commas. The
  input CSV files must have matching column headers.

HOW TO RUN
1. Extract this ZIP file.
2. Open the folder in VS Code, IDLE, or PyCharm.
3. Run any numbered .py file with Python 3.
4. Use relative file names when prompted, or press Enter to use the default.

NOTES
- All files are opened with context managers (with open) so they close safely.
- CSV programs use Python's built-in csv module; no pip installation is needed.
- Output files are created in the current working directory.
- Programs include basic exception handling for missing files and invalid input.

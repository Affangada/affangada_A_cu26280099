"""Python File Handling Lab Sheet 07 solution."""
# Count the number of data rows and columns in a CSV file.
import csv

filename = input("CSV file (default students.csv): ").strip() or "students.csv"
try:
    with open(filename, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))
    if rows:
        print("Number of columns:", len(rows[0]))
        print("Number of data rows:", max(0, len(rows) - 1))
    else:
        print("CSV file is empty.")
except FileNotFoundError:
    print("CSV file not found.")
except OSError as error:
    print("File error:", error)

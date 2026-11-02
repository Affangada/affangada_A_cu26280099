"""Python File Handling Lab Sheet 07 solution."""
# Search for a student record in a CSV file using student name.
import csv

filename = input("CSV file (default students.csv): ").strip() or "students.csv"
search_name = input("Enter student name to search: ").strip().lower()
try:
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        found = False
        for row in reader:
            if row.get("Name", "").strip().lower() == search_name:
                print("Record found:", row)
                found = True
        if not found:
            print("Student not found.")
except FileNotFoundError:
    print("CSV file not found. Run Program 21 first.")
except OSError as error:
    print("File error:", error)

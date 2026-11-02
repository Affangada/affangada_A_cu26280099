"""Python File Handling Lab Sheet 07 solution."""
# Find and display the student with the highest marks in a CSV file.
import csv

filename = input("CSV file (default students.csv): ").strip() or "students.csv"
try:
    with open(filename, "r", newline="", encoding="utf-8") as file:
        students = list(csv.DictReader(file))
    valid_students = []
    for student in students:
        try:
            student["Marks"] = float(student["Marks"])
            valid_students.append(student)
        except (ValueError, KeyError, TypeError):
            continue

    if valid_students:
        top_student = max(valid_students, key=lambda student: student["Marks"])
        print("Highest scoring student:", top_student["Name"])
        print("Marks:", top_student["Marks"])
    else:
        print("No valid student marks found.")
except FileNotFoundError:
    print("CSV file not found. Run Program 21 first.")
except OSError as error:
    print("File error:", error)

"""Python File Handling Lab Sheet 07 solution."""
# Append a new student record to an existing CSV file.
import csv
import os

filename = "students.csv"
try:
    file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0
    name = input("Student name: ").strip()
    age = int(input("Age: "))
    marks = float(input("Marks: "))

    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Age", "Marks"])
        writer.writerow([name, age, marks])
    print("New record appended to", filename)
except ValueError:
    print("Age and marks must be numeric.")
except OSError as error:
    print("File error:", error)

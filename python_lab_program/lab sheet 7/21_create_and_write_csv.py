"""Python File Handling Lab Sheet 07 solution."""
# Create a CSV file and write student records into it.
import csv

filename = "students.csv"
students = [
    ["Name", "Age", "Marks"],
    ["Aman", 20, 85],
    ["Sara", 21, 92],
    ["Rahul", 20, 74],
    ["Priya", 22, 88]
]
try:
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(students)
    print("CSV data written to", filename)
except OSError as error:
    print("File error:", error)

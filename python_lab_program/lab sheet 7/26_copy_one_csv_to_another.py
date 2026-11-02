"""Python File Handling Lab Sheet 07 solution."""
# Copy all rows from one CSV file to another CSV file.
import csv

source = input("Source CSV (default students.csv): ").strip() or "students.csv"
destination = input("Destination CSV (default students_copy.csv): ").strip() or "students_copy.csv"
try:
    with open(source, "r", newline="", encoding="utf-8") as src:
        rows = list(csv.reader(src))
    with open(destination, "w", newline="", encoding="utf-8") as dest:
        writer = csv.writer(dest)
        writer.writerows(rows)
    print("CSV data copied to", destination)
except FileNotFoundError:
    print("Source CSV file not found.")
except OSError as error:
    print("File error:", error)

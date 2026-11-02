"""Python File Handling Lab Sheet 07 solution."""
# Read data from a CSV file and display it.
import csv

filename = input("CSV file (default students.csv): ").strip() or "students.csv"
try:
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found. Run Program 21 first.")
except OSError as error:
    print("File error:", error)

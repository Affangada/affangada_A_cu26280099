"""Python File Handling Lab Sheet 07 solution."""
# Read a CSV file and calculate the average of numeric columns.
import csv

filename = input("CSV file (default students.csv): ").strip() or "students.csv"
try:
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        totals = {}
        counts = {}
        for row in reader:
            for column, value in row.items():
                try:
                    number = float(value)
                except (ValueError, TypeError):
                    continue
                totals[column] = totals.get(column, 0) + number
                counts[column] = counts.get(column, 0) + 1

    if totals:
        for column in totals:
            print(f"Average {column}: {totals[column] / counts[column]:.2f}")
    else:
        print("No numeric columns found.")
except FileNotFoundError:
    print("CSV file not found. Run Program 21 first.")
except OSError as error:
    print("File error:", error)

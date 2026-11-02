"""Python File Handling Lab Sheet 07 solution."""
# Display specific columns (Name and Marks) from a CSV file.
import csv

filename = input("CSV file (default students.csv): ").strip() or "students.csv"
try:
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or "Name" not in reader.fieldnames or "Marks" not in reader.fieldnames:
            print("CSV must contain Name and Marks columns.")
        else:
            for row in reader:
                print("Name:", row["Name"], "| Marks:", row["Marks"])
except FileNotFoundError:
    print("CSV file not found. Run Program 21 first.")
except OSError as error:
    print("File error:", error)

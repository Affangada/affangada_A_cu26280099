"""Python File Handling Lab Sheet 07 solution."""
# Combine multiple CSV files into one CSV file, keeping one header row.
import csv

filenames = input("Enter CSV file names separated by commas: ").split(",")
filenames = [name.strip() for name in filenames if name.strip()]
destination = input("Output CSV (default combined.csv): ").strip() or "combined.csv"

try:
    combined_rows = []
    header = None
    for filename in filenames:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            current_header = next(reader, None)
            if current_header is None:
                continue
            if header is None:
                header = current_header
            elif current_header != header:
                print("Skipped", filename, "- its columns do not match.")
                continue
            combined_rows.extend(reader)

    if header is None:
        print("No readable CSV data found.")
    else:
        with open(destination, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(combined_rows)
        print("Combined", len(combined_rows), "records into", destination)
except FileNotFoundError as error:
    print("CSV file not found:", error.filename)
except OSError as error:
    print("File error:", error)

"""Python File Handling Lab Sheet 07 solution."""
# Read a text file one line at a time.
filename = input("Enter file name (default sample.txt): ").strip() or "sample.txt"
try:
    with open(filename, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.rstrip()}")
except FileNotFoundError:
    print("File not found. Run Program 01 first.")
except OSError as error:
    print("File error:", error)

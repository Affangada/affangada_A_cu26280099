"""Python File Handling Lab Sheet 07 solution."""
# Display the first and last lines of a text file.
filename = input("File name (default sample.txt): ").strip() or "sample.txt"
try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    if lines:
        print("First line:", lines[0].rstrip())
        print("Last line:", lines[-1].rstrip())
    else:
        print("The file is empty.")
except FileNotFoundError:
    print("File not found.")
except OSError as error:
    print("File error:", error)

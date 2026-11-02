"""Python File Handling Lab Sheet 07 solution."""
# Count the number of lines and characters in a text file.
filename = input("Enter file name (default sample.txt): ").strip() or "sample.txt"
try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    print("Number of lines:", len(content.splitlines()))
    print("Number of characters:", len(content))
except FileNotFoundError:
    print("File not found. Run Program 01 first.")
except OSError as error:
    print("File error:", error)

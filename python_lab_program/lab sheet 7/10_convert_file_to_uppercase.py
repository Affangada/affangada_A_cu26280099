"""Python File Handling Lab Sheet 07 solution."""
# Read a file and write its contents in uppercase to another file.
source = input("Source file (default sample.txt): ").strip() or "sample.txt"
destination = input("Output file (default uppercase.txt): ").strip() or "uppercase.txt"
try:
    with open(source, "r", encoding="utf-8") as file:
        content = file.read()
    with open(destination, "w", encoding="utf-8") as file:
        file.write(content.upper())
    print("Uppercase content saved in", destination)
except FileNotFoundError:
    print("Source file not found.")
except OSError as error:
    print("File error:", error)

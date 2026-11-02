"""Python File Handling Lab Sheet 07 solution."""
# Copy the contents of one file into another file.
source = input("Source file (default sample.txt): ").strip() or "sample.txt"
destination = input("Destination file (default copy.txt): ").strip() or "copy.txt"
try:
    with open(source, "r", encoding="utf-8") as src:
        content = src.read()
    with open(destination, "w", encoding="utf-8") as dest:
        dest.write(content)
    print("Contents copied to", destination)
except FileNotFoundError:
    print("Source file not found.")
except OSError as error:
    print("File error:", error)

"""Python File Handling Lab Sheet 07 solution."""
# Merge the contents of two text files into a third file.
first = input("First file (default file1.txt): ").strip() or "file1.txt"
second = input("Second file (default file2.txt): ").strip() or "file2.txt"
destination = input("Merged file (default merged.txt): ").strip() or "merged.txt"
try:
    with open(first, "r", encoding="utf-8") as file:
        content1 = file.read()
    with open(second, "r", encoding="utf-8") as file:
        content2 = file.read()
    with open(destination, "w", encoding="utf-8") as file:
        file.write(content1)
        file.write("\\n")
        file.write(content2)
    print("Files merged into", destination)
except FileNotFoundError:
    print("One of the input files was not found.")
except OSError as error:
    print("File error:", error)

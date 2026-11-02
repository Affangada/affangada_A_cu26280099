"""Python File Handling Lab Sheet 07 solution."""
# Append new content to an existing text file.
filename = input("Enter file name (default sample.txt): ").strip() or "sample.txt"
new_text = input("Enter text to append: ")
try:
    with open(filename, "a", encoding="utf-8") as file:
        file.write(new_text + "\\n")
    print("Content appended successfully.")
except OSError as error:
    print("File error:", error)

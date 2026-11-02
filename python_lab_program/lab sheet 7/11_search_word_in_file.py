"""Python File Handling Lab Sheet 07 solution."""
# Search for a particular word in a text file.
filename = input("File name (default sample.txt): ").strip() or "sample.txt"
word = input("Enter word to search: ").strip()
try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    if word.lower() in content.lower().split():
        print("Word found in the file.")
    else:
        print("Word not found.")
except FileNotFoundError:
    print("File not found.")
except OSError as error:
    print("File error:", error)

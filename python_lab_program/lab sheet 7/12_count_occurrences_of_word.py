"""Python File Handling Lab Sheet 07 solution."""
# Count how many times a word occurs in a text file.
filename = input("File name (default sample.txt): ").strip() or "sample.txt"
word = input("Enter word to count: ").strip().lower()
try:
    with open(filename, "r", encoding="utf-8") as file:
        words = file.read().lower().split()
    print("Occurrences:", words.count(word))
except FileNotFoundError:
    print("File not found.")
except OSError as error:
    print("File error:", error)

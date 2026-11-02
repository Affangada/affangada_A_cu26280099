"""Python File Handling Lab Sheet 07 solution."""
# Count the total number of words in a text file.
filename = input("Enter file name (default sample.txt): ").strip() or "sample.txt"
try:
    with open(filename, "r", encoding="utf-8") as file:
        word_count = len(file.read().split())
    print("Total words:", word_count)
except FileNotFoundError:
    print("File not found. Run Program 01 first.")
except OSError as error:
    print("File error:", error)

"""Python File Handling Lab Sheet 07 solution."""
# Replace one word with another word in a text file.
filename = input("File name (default sample.txt): ").strip() or "sample.txt"
old_word = input("Word to replace: ")
new_word = input("Replacement word: ")
try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    updated = content.replace(old_word, new_word)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(updated)
    print("Word replacement completed.")
except FileNotFoundError:
    print("File not found.")
except OSError as error:
    print("File error:", error)

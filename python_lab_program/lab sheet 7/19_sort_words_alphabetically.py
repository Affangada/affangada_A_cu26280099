"""Python File Handling Lab Sheet 07 solution."""
# Sort all words in a file alphabetically and save them to a new file.
source = input("Input file (default sample.txt): ").strip() or "sample.txt"
destination = input("Output file (default sorted_words.txt): ").strip() or "sorted_words.txt"
try:
    with open(source, "r", encoding="utf-8") as file:
        words = file.read().split()
    words.sort(key=str.lower)
    with open(destination, "w", encoding="utf-8") as file:
        file.write("\\n".join(words))
    print("Sorted words saved in", destination)
except FileNotFoundError:
    print("Input file not found.")
except OSError as error:
    print("File error:", error)

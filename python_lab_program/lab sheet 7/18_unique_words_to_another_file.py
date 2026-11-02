"""Python File Handling Lab Sheet 07 solution."""
# Read a file and save its unique words into another file.
source = input("Input file (default sample.txt): ").strip() or "sample.txt"
destination = input("Output file (default unique_words.txt): ").strip() or "unique_words.txt"
try:
    with open(source, "r", encoding="utf-8") as file:
        words = file.read().split()
    unique_words = sorted(set(words), key=str.lower)
    with open(destination, "w", encoding="utf-8") as file:
        file.write("\\n".join(unique_words))
    print("Unique words saved in", destination)
except FileNotFoundError:
    print("Input file not found.")
except OSError as error:
    print("File error:", error)

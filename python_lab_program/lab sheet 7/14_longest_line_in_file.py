"""Python File Handling Lab Sheet 07 solution."""
# Display the longest line in a text file.
filename = input("File name (default sample.txt): ").strip() or "sample.txt"
try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()
    if lines:
        longest = max(lines, key=len)
        print("Longest line:", longest)
        print("Length:", len(longest))
    else:
        print("The file is empty.")
except FileNotFoundError:
    print("File not found.")
except OSError as error:
    print("File error:", error)

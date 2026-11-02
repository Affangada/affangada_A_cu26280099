"""Python File Handling Lab Sheet 07 solution."""
# Read and display the complete contents of a text file.
filename = input("Enter file name (default sample.txt): ").strip() or "sample.txt"
try:
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Run Program 01 first or check the file name.")
except OSError as error:
    print("File error:", error)

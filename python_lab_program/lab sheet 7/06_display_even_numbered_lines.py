"""Python File Handling Lab Sheet 07 solution."""
# Display only even-numbered lines from a text file.
filename = input("Enter file name (default sample.txt): ").strip() or "sample.txt"
try:
    with open(filename, "r", encoding="utf-8") as file:
        for number, line in enumerate(file, start=1):
            if number % 2 == 0:
                print(f"{number}: {line.rstrip()}")
except FileNotFoundError:
    print("File not found. Run Program 01 first.")
except OSError as error:
    print("File error:", error)

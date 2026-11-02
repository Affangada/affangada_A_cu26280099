"""Python File Handling Lab Sheet 07 solution."""
# Remove blank lines from a file and save the cleaned content.
source = input("Input file (default sample.txt): ").strip() or "sample.txt"
destination = input("Output file (default no_blank_lines.txt): ").strip() or "no_blank_lines.txt"
try:
    with open(source, "r", encoding="utf-8") as file:
        lines = file.readlines()
    non_blank = [line for line in lines if line.strip()]
    with open(destination, "w", encoding="utf-8") as file:
        file.writelines(non_blank)
    print("Blank lines removed. Clean file:", destination)
except FileNotFoundError:
    print("Input file not found.")
except OSError as error:
    print("File error:", error)

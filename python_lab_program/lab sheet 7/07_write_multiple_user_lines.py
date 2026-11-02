"""Python File Handling Lab Sheet 07 solution."""
# Write multiple lines entered by the user into a file.
filename = "multiple_lines.txt"
try:
    count = int(input("How many lines do you want to enter? "))
    with open(filename, "w", encoding="utf-8") as file:
        for i in range(count):
            line = input(f"Enter line {i + 1}: ")
            file.write(line + "\\n")
    print("Lines saved in", filename)
except ValueError:
    print("Please enter a valid whole number.")
except OSError as error:
    print("File error:", error)

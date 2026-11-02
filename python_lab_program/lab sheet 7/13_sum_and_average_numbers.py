"""Python File Handling Lab Sheet 07 solution."""
# Read numbers from a file and display their sum and average.
filename = input("Numbers file (default numbers.txt): ").strip() or "numbers.txt"
try:
    with open(filename, "r", encoding="utf-8") as file:
        numbers = [float(value) for value in file.read().split()]
    if numbers:
        print("Sum:", sum(numbers))
        print("Average:", sum(numbers) / len(numbers))
    else:
        print("The file contains no numbers.")
except FileNotFoundError:
    print("File not found. Create numbers.txt with one or more numbers.")
except ValueError:
    print("The file contains a value that is not numeric.")
except OSError as error:
    print("File error:", error)

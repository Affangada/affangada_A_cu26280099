"""Python CRUD Operations Lab Sheet 09 solution."""
# Save student data to a text file and read it back.
filename = "students.txt"

try:
    n = int(input("How many students to save? "))
    with open(filename, "w", encoding="utf-8") as file:
        for i in range(n):
            print("Student", i + 1)
            roll = input("Roll number: ").strip()
            name = input("Name: ").strip()
            marks = float(input("Marks: "))
            # Store each record as comma-separated values.
            file.write(f"{roll},{name},{marks}\\n")

    print("\\nSaved student records:")
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            roll, name, marks = line.strip().split(",", 2)
            print("Roll:", roll, "| Name:", name, "| Marks:", marks)
except ValueError:
    print("Please enter a valid number for count and marks.")
except OSError as error:
    print("File error:", error)

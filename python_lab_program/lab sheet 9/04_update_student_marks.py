"""Python CRUD Operations Lab Sheet 09 solution."""
# Update a student's marks in a list using roll number.
students = [
    {"roll": "101", "name": "Aman", "marks": 82.5},
    {"roll": "102", "name": "Sara", "marks": 91.0}
]

roll = input("Enter roll number to update: ").strip()
try:
    new_marks = float(input("Enter new marks: "))
    for student in students:
        if student["roll"] == roll:
            student["marks"] = new_marks
            print("Student marks updated successfully.")
            print(student)
            break
    else:
        print("Student record not found.")
except ValueError:
    print("Please enter marks as a valid number.")

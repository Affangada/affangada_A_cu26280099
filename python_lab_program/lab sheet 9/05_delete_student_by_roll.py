"""Python CRUD Operations Lab Sheet 09 solution."""
# Delete a student record using roll number.
students = [
    {"roll": "101", "name": "Aman", "marks": 82.5},
    {"roll": "102", "name": "Sara", "marks": 91.0},
    {"roll": "103", "name": "Rahul", "marks": 76.5}
]

roll = input("Enter roll number to delete: ").strip()
for student in students:
    if student["roll"] == roll:
        students.remove(student)
        print("Student record deleted successfully.")
        break
else:
    print("Student record not found.")

print("Remaining records:", students)

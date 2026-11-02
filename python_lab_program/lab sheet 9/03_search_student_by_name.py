"""Python CRUD Operations Lab Sheet 09 solution."""
# Search for a student by name in a list.
students = [
    {"roll": "101", "name": "Aman", "marks": 82.5},
    {"roll": "102", "name": "Sara", "marks": 91.0},
    {"roll": "103", "name": "Rahul", "marks": 76.5}
]

search_name = input("Enter student name to search: ").strip().lower()
matches = [s for s in students if s["name"].lower() == search_name]

if matches:
    for student in matches:
        print("Record found:", student)
else:
    print("Student not found.")

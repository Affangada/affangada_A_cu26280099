"""Python CRUD Operations Lab Sheet 09 solution."""
# Read and display all student records from a list.
students = [
    {"roll": "101", "name": "Aman", "marks": 82.5},
    {"roll": "102", "name": "Sara", "marks": 91.0},
    {"roll": "103", "name": "Rahul", "marks": 76.5}
]

if students:
    print("Student Records:")
    for student in students:
        print("Roll:", student["roll"], "| Name:", student["name"],
              "| Marks:", student["marks"])
else:
    print("No student records found.")

"""Python CRUD Operations Lab Sheet 09 solution."""
# Create a list of student records.
students = []
n = int(input("How many students do you want to add? "))

for i in range(n):
    print("\\nEnter details for student", i + 1)
    roll = input("Roll number: ").strip()
    name = input("Name: ").strip()
    marks = float(input("Marks: "))
    students.append({"roll": roll, "name": name, "marks": marks})

print("\\nCreated student records:")
for student in students:
    print(student)

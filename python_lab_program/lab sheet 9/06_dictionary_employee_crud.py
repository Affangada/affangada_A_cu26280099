"""Python CRUD Operations Lab Sheet 09 solution."""
# Perform Create, Read, Update and Delete on employee dictionary.
employees = {}

def create_employee():
    emp_id = input("Employee ID: ").strip()
    if emp_id in employees:
        print("Employee ID already exists.")
        return
    name = input("Employee name: ").strip()
    salary = float(input("Salary: "))
    employees[emp_id] = {"name": name, "salary": salary}
    print("Employee added.")

def read_employees():
    if not employees:
        print("No employee records.")
    for emp_id, details in employees.items():
        print(emp_id, details)

def update_employee():
    emp_id = input("Employee ID to update: ").strip()
    if emp_id not in employees:
        print("Employee not found.")
        return
    employees[emp_id]["name"] = input("New name: ").strip()
    employees[emp_id]["salary"] = float(input("New salary: "))
    print("Employee updated.")

def delete_employee():
    emp_id = input("Employee ID to delete: ").strip()
    if employees.pop(emp_id, None) is None:
        print("Employee not found.")
    else:
        print("Employee deleted.")

while True:
    print("\\n1.Create 2.Read 3.Update 4.Delete 5.Exit")
    choice = input("Choose: ").strip()
    try:
        if choice == "1":
            create_employee()
        elif choice == "2":
            read_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid numeric input.")

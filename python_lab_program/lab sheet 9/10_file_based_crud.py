"""Python CRUD Operations Lab Sheet 09 solution."""
# File-based CRUD: add, view, modify and delete student records.
import json

FILENAME = "student_records.json"

def load_records():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, OSError) as error:
        print("Could not read file:", error)
        return []

def save_records(records):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)

records = load_records()
while True:
    print("\\n1.Add 2.View 3.Modify 4.Delete 5.Exit")
    choice = input("Choose: ").strip()
    try:
        if choice == "1":
            roll = input("Roll number: ").strip()
            if any(r["roll"] == roll for r in records):
                print("Roll number already exists.")
                continue
            name = input("Name: ").strip()
            marks = float(input("Marks: "))
            records.append({"roll": roll, "name": name, "marks": marks})
            save_records(records)
            print("Record added.")
        elif choice == "2":
            if records:
                for record in records:
                    print(record)
            else:
                print("No records found.")
        elif choice == "3":
            roll = input("Roll number to modify: ").strip()
            for record in records:
                if record["roll"] == roll:
                    record["name"] = input("New name: ").strip()
                    record["marks"] = float(input("New marks: "))
                    save_records(records)
                    print("Record modified.")
                    break
            else:
                print("Record not found.")
        elif choice == "4":
            roll = input("Roll number to delete: ").strip()
            new_records = [r for r in records if r["roll"] != roll]
            if len(new_records) == len(records):
                print("Record not found.")
            else:
                records = new_records
                save_records(records)
                print("Record deleted.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter marks as a valid number.")
    except OSError as error:
        print("File error:", error)

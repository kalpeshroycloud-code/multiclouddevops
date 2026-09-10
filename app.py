employees = []


def add_employee():
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)
    print("Employee added successfully.")


def display_employees():
    if not employees:
        print("No employees found.")
    print("-" * 50)

    for employee in employees:
        print("ID:", employee["id"])
        print("Name:", employee["name"])
        print("Department:", employee["department"])
        print("Salary:", employee["salary"])
        print("-" * 50)


def search_employee():
    emp_id = input("Enter employee ID to search: ")

    for employee in employees:
        if employee["id"] == emp_id:
            print("\nEmployee Found")
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print("Salary:", employee["salary"])
            return

    print("Employee not found.")


def delete_employee():
    emp_id = input("Enter employee ID to delete: ")

    for employee in employees:
        if employee["id"] == emp_id:
            employees.remove(employee)
            print("Employee deleted successfully.")
            return

    print("Employee not found.")


def update_salary():
    emp_id = input("Enter employee ID: ")
    new_salary = float(input("Enter new salary: "))

    for employee in employees:
        if employee["id"] == emp_id:
            employee["salary"] = new_salary
            print("Salary updated successfully.")
            return

    print("Employee not found.")


def show_total_employees():
    total = len(employees)
    print("Total employees:", total)


def main():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Update Salary")
        print("6. Total Employees")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            display_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            delete_employee()

        elif choice == "5":
            update_salary()

        elif choice == "6":
            show_total_employees()

        elif choice == "7":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

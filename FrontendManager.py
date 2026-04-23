from Employee import Employee
from Manager import EmployeeManager

class FrontendManager:
    def __init__(self):
        self.manager = EmployeeManager()

    def run(self):
        while True:
            print("\n==============================")
            print("   Employee Management System")
            print("==============================")
            print("1. Add Employee")
            print("2. List Employees")
            print("3. Delete Employee by Name")
            print("4. Delete Employees by Age Range")
            print("5. Find Employee by Name")
            print("6. Update Employee Salary")
            print("7. Exit")
            print("==============================")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                name = input("Enter employee name: ").strip()
                try:
                    age    = int(input("Enter employee age: "))
                    salary = float(input("Enter employee salary: "))
                except ValueError:
                    print("❌ Invalid input! Age must be a number, salary must be a number.")
                    continue
                self.manager.add_employee(name, age, salary)
                print(f"✅ {name} added successfully.")

            elif choice == '2':
                self.manager.list_employees()

            elif choice == '3':
                name = input("Enter employee name to delete: ").strip()
                self.manager.delete_by_name(name)

            elif choice == '4':
                try:
                    min_age = int(input("Enter minimum age: "))
                    max_age = int(input("Enter maximum age: "))
                except ValueError:
                    print("❌ Invalid age! Numbers only please.")
                    continue
                deleted = self.manager.delete_by_age_range(min_age, max_age)
                print(f"✅ Deleted {deleted} employee(s) in age range {min_age}-{max_age}.")

            elif choice == '5':
                name     = input("Enter employee name to find: ").strip()
                employee = self.find_employee(name)

            elif choice == '6':
                name = input("Enter employee name to update salary: ").strip()
                try:
                    new_salary = float(input("Enter new salary: "))
                except ValueError:
                    print("❌ Invalid salary! Numbers only please.")
                    continue
                self.manager.update_salary(name, new_salary)

            elif choice == '7':
                print("👋 Goodbye!")
                break

            else:
                print("❌ Invalid choice. Please enter 1-7.")

    def find_employee(self, name):
        employee = self.manager.find_by_name(name)
        if employee:
            print(employee)
        else:
            print(f"❌ No employee found with name: {name}")
        return employee

if __name__ == "__main__":
    app = FrontendManager()
    app.run()
    
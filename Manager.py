import csv
from Employee import Employee

class EmployeeManager:
    def __init__(self):
        self.employees = []  # This list will hold instances of Employee
        self.filename  = "employees.csv"    
        self.load_from_csv() 
    
    def add_employee(self, name, age, salary):
        employee = Employee(name, age, salary)
        self.employees.append(employee)  # Add an Employee instance to the list
        self.save_to_csv()  # Save the updated list to CSV after adding a new employee
        return employee  # Return the newly created Employee instance
    
     # ── CSV SAVE ──────────────────────────────────────────────
    def save_to_csv(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "age", "salary"])
            for emp in self.employees:
                writer.writerow([emp.name, emp.age, emp.salary])

    # ── CSV LOAD ──────────────────────────────────────────────
    def load_from_csv(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employee = Employee(
                        row["name"],
                        int(row["age"]),
                        float(row["salary"])
                    )
                    self.employees.append(employee)
            print(f"✅ Loaded {len(self.employees)} employee(s) from file.")
        except FileNotFoundError:
            print("Starting fresh — no saved data found.")
    
    
    def list_employees(self):
        if not self.employees:
            print("No employees found.")
        else:
            for employee in self.employees:
                print(employee)  # This wil0l call the __str__ method of Employee
    
    def delete_by_name(self, name):
        for employee in self.employees:
            if employee.name.lower() == name.lower():
                self.employees.remove(employee)
                self.save_to_csv()
                print(f"Employee deleted: {employee.name}")
                return
        print(f"Employee not found: {name}")

    def delete_by_age_range(self, min_age, max_age):
        deleted_count = 0
        kept_employees = []
        
        for employee in self.employees:
            if min_age <= employee.age <= max_age:
                deleted_count += 1  # Increment the count of deleted employees
            else:
                kept_employees.append(employee) # Keep employees that do not fall within the age range  
   
        self.employees = kept_employees  # Update the employees list with the filtered list
        return deleted_count  # Return the count of deleted employees

    def update_salary(self,name,new_salary):
        employee=self.find_by_name(name) # Use the find_by_name method to locate the employee
        if employee is None:
            print(f"No employee found with the name: {name}")
        else:
            employee.salary=new_salary  # Update the salary of the found employee
            self.save_to_csv()  # Save the updated employee list to CSV
            print(f"Updated salary for {employee.name} to {employee.salary}")


EmployeesManager = EmployeeManager
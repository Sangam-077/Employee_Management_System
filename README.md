# Employee Management System 🏢

A Python OOP project to manage employee records with persistent CSV storage.
Built as part of learning Object-Oriented Programming concepts in Python.

---

## 📸 Preview

```
==============================
   Employee Management System
==============================
1. Add Employee
2. List Employees
3. Delete Employee by Name
4. Delete Employees by Age Range
5. Find Employee by Name
6. Update Employee Salary
7. Exit
==============================
Enter your choice:
```

---

## ✨ Features

- ✅ Add new employees
- ✅ List all employees
- ✅ Delete employee by name
- ✅ Delete employees by age range
- ✅ Find employee by name
- ✅ Update employee salary
- ✅ Auto-saves to CSV — data persists between sessions
- ✅ Input validation & error handling

---

## 📁 Project Structure

```
Employee-Management-System/
│
├── Employee.py           → Employee class (data model)
├── Manager.py            → EmployeeManager class (business logic)
├── FrontendManager.py    → FrontendManager class (user interface)
└── employees.csv         → Auto-generated data file (created on first run)
```

---

## 🚀 How to Run

Make sure you have Python 3 installed, then run:

```bash
python FrontendManager.py
```

That's it! The program will:
- Auto-load existing employees from `employees.csv` on startup
- Auto-save any changes immediately to `employees.csv`

---

## 💡 OOP Concepts Used

| Concept | Where Used |
|---|---|
| Classes & Objects | Employee, EmployeeManager, FrontendManager |
| Constructors (`__init__`) | All 3 classes |
| Encapsulation | Data and methods bundled inside classes |
| Composition | FrontendManager uses EmployeeManager uses Employee |
| `__str__` & `__repr__` | Employee class for clean output |
| File Handling | CSV auto-save and auto-load in EmployeeManager |
| Input Validation | try/except in FrontendManager |

---

## 🏗️ Architecture

```
FrontendManager        EmployeeManager         Employee
─────────────────      ─────────────────       ────────────
Handles user      →    Handles business   →    Holds data
input/output           logic                   (name, age, salary)
(Layer 3)              (Layer 2)               (Layer 1)
```

This 3-layer architecture keeps the code clean and easy to maintain.
Each class has one job and does it well.

---

## 📝 Example Usage

```
Enter your choice: 1
Enter employee name: Sangam
Enter employee age: 20
Enter employee salary: 30000
✅ Sangam added successfully.

Enter your choice: 2
Employee(Name: Sangam has an Age: 20 with Salary: 30000)

Enter your choice: 6
Enter employee name to update salary: Sangam
Enter new salary: 35000
✅ Updated salary for Sangam to 35000

Enter your choice: 7
👋 Goodbye!
```

---

## 🛠️ Requirements

- Python 3.x
- No external libraries needed — uses only built-in `csv` module

---

## 👨‍💻 Author

**Sangam**
- GitHub: [@Sangam-077](https://github.com/Sangam-077)

---

## 📚 What I Learned

This project was built while learning Python OOP from scratch.
Key takeaways:
- How to structure a real project using multiple classes
- How to separate concerns across different layers
- How to persist data using CSV files
- How to handle user input safely with validation

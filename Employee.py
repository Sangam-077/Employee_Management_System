class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self): # This method is used to provide a human-readable string representation of the object. It is called when you use the print() function or str() on an instance of the class.
        return f"Employee(Name: {self.name} has an  Age: {self.age} with Salary: {self.salary})"
        
    def __repr__(self): # This method is used to provide a string representation of the object for debugging and development purposes. It should ideally return a string that can be used to recreate the object.
        return f"Employee(Name: {self.name} has an  Age: {self.age} with Salary: {self.salary})"
# Parent class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        return self.salary


# Child class
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_pay(self):
        return self.salary + self.bonus


# ---- Testing the program ----
emp = Employee("Rose", 200000)
mgr = Manager("Jackson", 900000, 300000)

print("Employee Pay:", emp.calculate_pay())
print("Manager Pay:", mgr.calculate_pay())
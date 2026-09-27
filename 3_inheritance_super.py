# Concept: inheritance and super()
# Example: Employee -> Manager / Developer

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def describe(self):
        print(f"{self.name} (ID: {self.emp_id}) - Employee, salary Rs. {self.salary}")


class Manager(Employee):
    def __init__(self, name, emp_id, salary, team_size):
        super().__init__(name, emp_id, salary)  # reuse parent's constructor
        self.team_size = team_size              # new attribute just for managers

    # override the parent method, but still use it via super()
    def describe(self):
        super().describe()
        print(f"  Role: Manager, leads a team of {self.team_size} people")


class Developer(Employee):
    def __init__(self, name, emp_id, salary, language):
        super().__init__(name, emp_id, salary)
        self.language = language

    def describe(self):
        super().describe()
        print(f"  Role: Developer, works in {self.language}")

    # brand new method that only developers have
    def commit_code(self):
        print(f"  {self.name} committed new {self.language} code to the repo!")


if __name__ == '__main__':
    # parent object still works on its own
    boss = Employee("Sir Ahmed", "E-100", 300000)

    mgr = Manager("Hina Noor", "M-201", 180000, team_size=7)
    dev = Developer("Bilal Khan", "D-302", 120000, language="Python")

    print("--- Employee (parent) ---")
    boss.describe()

    print("\n--- Manager (child) ---")
    mgr.describe()

    print("\n--- Developer (child) ---")
    dev.describe()
    dev.commit_code()

    # isinstance() proves inheritance really happened
    print("\nIs mgr an Employee?", isinstance(mgr, Employee))
    print("Is dev a Manager?  ", isinstance(dev, Manager))

class Person:
    country = "India"

    def __init__(self):
        super().__init__()      # Object class is parent of all the Class
        print("Initializing Person...")

    def takeBreath(self):
        print("I am breathing...")


class Employee(Person):
    company = "Honda"

    def __init__(self):
        print("Initializing Employee...")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing..")


class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        print("Initializing Programmer...")

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        super().takeBreath()            # Try uncommenting
        print("I am a Progarmmer so I am breathing++..")
        print(super().country)
        print(super().company)
        print(self.company)


# NOTE: the difference in constructors
# In Java, child class constructor automatically calls parent class constructors
# But in Python this does happens if constructors are not specifically defined. (Default constructors present)
# If constructors are defined by us, we have to call super().__init__() in the constructor of child class

p = Person()
p.takeBreath()
print()

e = Employee()
# e.getSalary()
e.takeBreath()
print()

pr = Programmer()
pr.takeBreath()

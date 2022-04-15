class Person:
    def __init__(self, personCountry: str) -> None:
        self.country = personCountry

    def takeBreath(self):
        print("I am breathing...")

    def eat(self):
        print('Person Eating..')


class Employee(Person):
    def __init__(self, employeeCompany: str, country: str) -> None:
        super().__init__(personCountry=country)
        self.company = employeeCompany

    def getSalary(self):
        print("Salary is Rs. 500000")

    def takeBreath(self):
        print("I am an Employee so I am luckily breathing..")


class Programmer(Employee):
    def __init__(self, programmerCompany: str, personCountry: str) -> None:
        super().__init__(programmerCompany, country=personCountry)
        # self.company = 'Google'               # uncomment this & see

    def getSalary(self):
        print(f"Salary is Rs. 3000000 ")

    def takeBreath(self):
        print("I am a Progarmmer so I am breathing++..")


p = Person('India')
p.takeBreath()
print(p.country)
# print(p.company) # throws an error
print()

e = Employee('Honda', 'India')
e.takeBreath()
e.getSalary()
e.eat()
print(e.company)
print(e.country)
print()

pr = Programmer('Amazon', 'India')
pr.takeBreath()
pr.getSalary()
pr.eat()
print(pr.company)
print(pr.country)

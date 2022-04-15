class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing...")

    def eat(self):
        print('Person Eating..')


class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print("Salary is Rs. 500000")

    def takeBreath(self):
        print("I am an Employee so I am luckily breathing..")


class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"Salary is Rs. 3000000 ")

    def takeBreath(self):
        print("I am a Progarmmer so I am breathing++..")


p = Person()
p.takeBreath()
print(p.country)
# print(p.company) # throws an error
print()

e = Employee()
e.takeBreath()
e.getSalary()
e.eat()
print(e.company)
print(e.country)
print()

pr = Programmer()
pr.takeBreath()
pr.getSalary()
pr.eat()
print(pr.company)
print(pr.country)

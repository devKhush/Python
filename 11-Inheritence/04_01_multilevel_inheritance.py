class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing...")

    def eat(self):
        print('Person Eating..')


class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print("Salary is Rs.500000")

    def takeBreath(self):
        print("I am an Employee so I am luckily breathing..")


class Programmer(Employee):
    # company = "Fiverr"

    def getSalary(self):
        print("Salary is Rs.3000000")

    # def takeBreath(self):
    #     print("I am a Progarmmer so I am breathing++..")


# Employee inherits everything from Person class
# Programemr class inherits everything from Employee class (including that of Person class too)

# FUNDA of Inheritence: Agar apne pass hai attribute/methods toh apna use kro, agar nhi hai toh papa ka use kro
# Here Inheritence happens from Nearest parent

p = Person()
p.takeBreath()
# print(p.company) # throws an error
print()

e = Employee()
e.takeBreath()
e.getSalary()
e.eat()
print(e.company)
print()

pr = Programmer()
pr.getSalary()
pr.takeBreath()
pr.eat()
print(pr.company)
print(pr.country)

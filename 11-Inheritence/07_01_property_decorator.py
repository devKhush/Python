# https://www.sololearn.com/learning/1073/2472/5144/1

class Employee:

    def __init__(self, salary, salaryBonus) -> None:
        self.salary = salary
        self.salarybonus = salaryBonus
        # self.totalSalary = self.salary + self.salarybonus

    # getter func with name must be same name as object attribute
    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    # setter func with name must be same name as object attribute
    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary


# Change variables that depends upon each other inside getters and setters

e = Employee(5600, 400)

# Behind the scene getter will be called
print(e.totalSalary)
print()

# Behind the scene setter will be called with value as parameter assigned to it
e.totalSalary = 5800

print(e.salary)
print(e.salarybonus)
print(e.totalSalary)

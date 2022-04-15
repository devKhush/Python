class Employee:
    def __init__(self, salary, increment) -> None:
        self.salary = salary
        self.increment = increment
        # self.salaryAfterIncrement = self.salary * self.increment

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, newSalary):
        self.increment = newSalary / self.salary


e = Employee(100, 10)
print(e.salary)
print(e.increment)

# this becomes a attribute itself, even though this attribute doesn't exist
print(e.salaryAfterIncrement)
print()

e.salaryAfterIncrement = 950
print(e.salary)
print(e.increment)
print(e.salaryAfterIncrement)
print()

e.salaryAfterIncrement = 910
print(e.salary)
print(e.increment)
print(e.salaryAfterIncrement)

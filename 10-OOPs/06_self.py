class Employee:
    company = "Google"      # static/class attribute

    def getSalary(self):    # Instance method
        print(
            f"Salary for this employee working in {self.company} is {self.salary}")


harry = Employee()
harry.salary = 100000       # instance attribute as per preference

print(Employee.company)     # static/class attribute

harry.getSalary()           # Instance method
Employee.getSalary(harry)   # same as previous call (in above line)
# Internally, it converts into above call

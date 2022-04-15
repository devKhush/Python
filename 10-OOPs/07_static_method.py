class Employee:
    company = "Google"

    def getSalary(self, signature):     # Instance methods
        print(
            f'Salary of this employee working in {self.company} is {self.salary}')

    @staticmethod
    def greet():                        # Class methods
        print("Good Morning, Sir")

    @staticmethod       # @staticmethod is a Decorator
    def time():                         # Class methods
        print("The time is 9AM in the morning")


# Class methods don't need 'self' objects as param
# Recall: that non-static members can't be used inside static methods() in java

harry = Employee()
harry.salary = 100000
harry.getSalary("Thanks!")      # parameter
# Employee.getSalary(harry)

harry.greet()       # Employee.greet()
Employee.greet()    # can be called using class name too
harry.time()
Employee.time()

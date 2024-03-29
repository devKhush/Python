class Employee:
    company = "Google"

    def __init__(self):             # Useless Constructor, Always latest constructor is called
        print('Holaaaa \nHolaaaa \n')

    def __init__(self, name, salary, subunit):      # Always latest constructor is called
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee Object is created!")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    def getSalary(self, signature):
        print(
            f"Salary for {self.name} employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")


harry = Employee("Harry", 100, "YouTube")
# harry = Employee()  # - -> This throws an error (missing 3 required positional arguments:)

harry.getDetails()
print()
harry.getSalary('Thanks!')

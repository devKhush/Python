class Employee:
    company = "Camel"
    salary = 100

    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod                # it is also Decorator
    def changeSalary(cls, sal: int):
        print('Inside class method')
        cls.salary = sal

    # def changeSalary(self, sal):          # This will also do the same work as above
    #     print('Inside instance method')
    #     self.__class__.salary = sal

    # @staticmethod                          # This will also do the same work as above
    # def changeSalary(sal: int):
    #     print('Inside static method')
    #     __class__.salary = sal

    # def changeSalary(self, sal):      # This willn't work bcoz this will create an Instance attribute
    #     self.salary = sal             # Bcoz of Instance variable precedence on assignment


e = Employee('Dev')
x = Employee('Khush')
print(e)
print(type(e))

print(e.salary)
print(Employee.salary)
print()

# How to change class attributes?
# This will also do the same work as above, but can we do this in some methods?
e.changeSalary(455)
# Employee.salary = 455
# Employee.changeSalary(500)

print(e.salary)
print(Employee.salary)
print(x.salary)

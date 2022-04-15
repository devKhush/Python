# https://www.sololearn.com/learning/1073/2469/5129/1

class Freelancer:
    company = "Google"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 5         # Assignment rule, creates instance variable

    @staticmethod                         # Try uncommenting
    def greet():
        print('Greet Freelance')


class Employee:
    company = "Visa"
    eCode = 120

    def employeeFunc(self):
        print('Inside Employee function')

    @staticmethod
    def greet():
        print('Greet Employee')


class Programmer(Freelancer, Employee):
    name = "Rohit"

    # @staticmethod
    # def greet():
    #     print('Greet Programmer')


# FUNDA of Inheritence: Agar apne pass hai attribute/methods toh apna use kro,
# agar nhi hai toh papa ka use kro
# In multiple Inheritence, Parent class which is inherited first gets prefernece
# over the other Parent class
p = Programmer()

print(p.company)
print(p.level)
print(p.eCode)
print(Freelancer.level)
print(p.level == Freelancer.level)
print()

p.upgradeLevel()

print(p.company)
print(p.level)
print(p.eCode)
print(Freelancer.level)
print(p.level == Freelancer.level)
print()

p.employeeFunc()
p.greet()

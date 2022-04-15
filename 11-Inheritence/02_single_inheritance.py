# https://www.sololearn.com/learning/1073/2469/5129/1

class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")


class Programmer(Employee):
    language = "Python"
    company = "Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is an programmer")


# FUNDA of Inheritence: Agar apne pass hai attribute/methods toh apna use kro, agar nhi hai toh papa ka use kro

e = Employee()
e.showDetails()
print(e.company)
print()

p = Programmer()
p.showDetails()
print(p.company)
p.getLanguage()
print(p.language)

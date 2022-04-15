# https://www.sololearn.com/learning/1073/2471/5141/1

class Employee:
    company = "Google"

    def __init__(self, name, age) -> None:
        self.name = name
        self.__age = age

    def _showAge(self) -> None:
        print('Age is {}'.format(self.__age))

    def __otherPrivateMethod(self):
        print('Any method')


e = Employee('Unknown', 19)
print(e.name)
# print(e.__age)                # error as '__age' is a strongly priavte attribute
print(e._Employee__age)
print()

e._showAge()
# e.__otherPrivateMethod()      # error as '__age' is a strongly priavte method
e._Employee__otherPrivateMethod()

# https://www.sololearn.com/learning/1073/2471/5139/1


'''
Weakly private methods and attributes have a single underscore at the beginning.
This signals that they are private, and shouldn't be used by external code. 
However, it is mostly only a convention, and does not stop external code from accessing them.
Its only actual effect is that from module_name import *  won't import variables that start
with a single underscore.
'''

# Encapsulation is feature of preventing Data from direct access


class Employee:
    company = "Google"

    def __init__(self, name, age) -> None:
        self.name = name
        self._age = age

    def _showAge(self) -> None:
        print('Age is {}'.format(self._age))

    def _otherPrivateMethod(self):
        print('Any method')


e = Employee('Unknown', 19)
print(e.name)
print(e._age)

e._showAge()
e._otherPrivateMethod()

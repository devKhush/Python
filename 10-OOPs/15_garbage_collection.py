# https://www.sololearn.com/learning/1073/2468/5137/1

# https://www.geeksforgeeks.org/destructors-in-python/#:~:text=The%20__del__()%20method,an%20object%20is%20garbage%20collected.&text=Note%20%3A%20A%20reference%20to%20objects,or%20when%20the%20program%20ends.

class Employee:
    company = "Google"

    def __init__(self, name) -> None:
        self.name = name

    def __del__(self):
        print('*'*20, 'Deleting the object', '*'*20)


e = Employee('Unknown')
print('e: ', e)
a = b = e

print('Deleting first time....')
del e
# print(e)          # error
print()

print('a: ', a)
print('Deleting second time....')
del a
print()

print('b: ', b)
print('Deleting third time....')
# del b
print()


a = 42                  # Create object <42>
b = a                   # Increase ref. count  of <42>
c = [a]                 # Increase ref. count  of <42>
del a                   # Decrease ref. count  of <42>
b = 100                 # Decrease ref. count  of <42>
c[0] = -1               # Decrease ref. count  of <42>

print('Done !')

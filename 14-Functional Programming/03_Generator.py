# https://www.geeksforgeeks.org/generators-in-python/

from re import A


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)
print()


x = simpleGeneratorFun()

print(x)
print(next(x))
print('Call 1..............')
print(x.__next__())
print('Call 2..............')
print(x.__next__())
print('Call 3..............')
print(x.__next__())
print('Call 4..............')
print(x.__next__())

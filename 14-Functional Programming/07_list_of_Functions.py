def func1():
    print('Function 1')


def func2():
    print('Function 2')


def func3():
    print('Function 3')


def func4():
    print('Function 4')


f4 = func4  # add the reference of function with name 'func4' to f4 stored in memory

del func4   # delete the reference of func4 to function stored in memory

# f4 will work as reference of function-4 is still present to f4
listOfFunctions = [func1, func2, func3, f4]

for i in listOfFunctions:
    i()

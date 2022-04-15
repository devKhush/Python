# def func(a):
#     return a+5

# https://www.sololearn.com/learning/1073/2460/5100/1

func = lambda a: a + 5
square = lambda x: x * x
sum = lambda a, b, c: a + b + c
increment = lambda a: a + 1

x = 3
print(func(x))  # Prints 8
print(square(x))  # Prints 9
print(sum(x, 1, 2))  # Prints 6
print(increment(x))
print()


def my_func(anyFunc, arg):
    return anyFunc(arg)


print(my_func(lambda x: 2 * x * x, 5))
print()

# Polynomial func directly calling lambdas function
print(returnValue := (lambda x: x**2 + 5 * x + 4)(-4))

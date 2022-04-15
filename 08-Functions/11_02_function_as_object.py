# Functions can also be used as arguments of other functions.

def add(x, y):
    return x+y


def twice_call(function, a, b):
    return function(function(a, b), function(a, b))


c = 5
d = 10
print(twice_call(add, c, d))

sum = add
print(twice_call(sum, c, d))

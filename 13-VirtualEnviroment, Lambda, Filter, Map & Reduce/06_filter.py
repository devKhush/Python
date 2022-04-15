# Filter Syntax: list(filter(function, list))
'''
Return an iterator yielding those items of iterable for which function(item) is true.
If function is None, return the items that are true.

The function filter filters an iterable by removing items that don't match 
a predicate (a function that returns a Boolean).
'''


def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False


def Greater_than_5(x):
    return x > 5


greater__than__10 = lambda num: num > 10

l = [1, 2, 3, 4, 5, 6, 6, 8, 89, 7, 8, 89, 98]

print(list(filter(greater_than_5, l)))
print(list(filter(Greater_than_5, l)))
print(set(filter(Greater_than_5, l)))
print()

print(result := list(filter(greater__than__10, l)))
print(result := tuple(filter(greater__than__10, l)))
print(result := set(filter(greater__than__10, l)))
print()

print(l)
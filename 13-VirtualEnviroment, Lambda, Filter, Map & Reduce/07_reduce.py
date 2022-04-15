from functools import reduce
'''Apply a function of two arguments cumulatively to the items of a sequence
or iterable, from left to right, so as to reduce the iterable to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ( ( ( (1+2) + 3) + 4) + 5). 
If initial is present, it is placed before the items of the iterable in the calculation, 
and serves as a default when the iterable is empty.'''

sum = lambda a, b: a + b
product = lambda a, b: a * b
divide = lambda a, b: b / a
unknown1 = lambda a, b: b * b
unknown2 = lambda a, b: a * a

l = [1, 2, 3, 4, 5]

print(sum := reduce(sum, l))
print(product := reduce(product, l))
print(divide := reduce(divide, l))
print()

print(reduce(lambda a, b: 2, l))
print(reduce(lambda a, b: (a + b) - b, l))
print(reduce(lambda a, b: (a + b) * b, l))
print()

print(product := reduce(unknown1, l))
print(product := reduce(unknown2, l))

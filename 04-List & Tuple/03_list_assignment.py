import random

l = [1, 2, 3, 4, 5]

# * -> assigns remaining element in list to variable
a, *b = l
print(a)
print(b)
print()

# sequential assignment of elements
a, b, c, *d = l
print(a)
print(b)
print(c)
print(d)
print()

# sequential assignment of elements
a, b, c, *c = l
print(a)
print(b)
print(c)

# trandomly shuffles the list
print()
random.shuffle(l)
print(l)

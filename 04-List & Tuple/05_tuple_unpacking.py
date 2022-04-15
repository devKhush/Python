# string unpacking into tuple
t = tuple('Khushdev Pandit !')
print('\n', t)

# * -> assigns remaining element in tuple to variable, it returns a list
# sequential assignment of elements
a, b, *c = t
print(a)
print(b)
print(c)
print()

num = (1, 2, 3, 4)
num = 1, 2, 3, 4
print(num)

a, b, c, d = num
print(a)
print(b)
print(c)
print(d)
print()

a, *b, c = num
print(a)
print(b)
print(c)
print()

# Tuple is deleted
del num
print(num)

a = [3, 6, 7, 8, 9, 2, 4, 23, 75, 23, 123, 67]

xyz = []
for item in a:
    if item % 2 == 0:
        xyz.append(item)
print(xyz)
print()

# Shortcut to write the same:
b = [i for i in a if i % 2 == 0]
print(b)
print()

t = [1, 4, 2, 4, 1, 2, 3]
s = {i for i in t}
print(s)
print()

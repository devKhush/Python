'''
Sets can be combined using mathematical operations.
The union operator | combines two sets to form a new one containing items in either.
The intersection operator & gets items only in both.
The difference operator - gets items in the first set but not in the second.
The symmetric difference operator ^ gets items in either set, but not both.
'''

# When to use what?
# https://www.sololearn.com/learning/1073/2464/5342/1

a = {1, 2, 3, 4, 5}
b = {1, 8, 4, 5, 9, 10, 11, 12}

print(a.union(b))
print(a | b)
print()

print(a.intersection(b))
print(a & b)
print()

print(a.difference(b))
print(a - b)
print()

print(b - a)
print(b - b)
print(a ^ b)

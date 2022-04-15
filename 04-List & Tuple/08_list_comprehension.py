# Example 1
list = [i**2 for i in range(11) if (i % 2) == 0]
print(list)

# Creates multiple of 3 fron 3 to 20
a = [i for i in range(20) if (i % 3) == 0]
print(a)

b = [i > 5 for i in list]
print(b)

# Trying to create a list in a very extensive range will result in a MemoryError.
# error = [i for i in range(10**100)]
# print(error)

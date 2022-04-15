# Create a list using []
a = [1, 2, 4, 56, 6]
b = [10, 20, 30, 40]

# Print the list using print() function
print(a)
print(b*3)
print()

# Access using index using a[0], a[1], a[2]
print(a[2])

# Change the value of list using
a[0] = 98
print(a)


# We can create a list with items of different types
c = [45, "Harry", False, 6.9]
print(c)

# list concatenation
print('\nConcatenated list:')
print(d := a+b+c[1:3])

# list multiply
print('\nList multiplication:')
print(e := (b[0:2]+c[2:])*3)

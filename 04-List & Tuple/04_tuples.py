# Creating a tuple using ()
t = ()      # empty tuple
print(t)
print(type(t))
t = (1, 2, 4, 5)
print(t)
print()

t1 = ()         # Empty tuple
print(t1)
print(type(t1))
print()

t1 = (1)        # Wrong way to declare a Tuple with Single element
print(t1)
print(type(t1))
print()


t1 = (1,)       # Tuple with Single element
print(t1)
print(type(t1))


# Printing the elements of a tuple
print("\n" + str(t[0]))

# Cannot update the values of a tuple
# t[1] = 34     # throws an error


# Tuples can be created without the parentheses,
# by just separating the values with commas.
my_tuple = 'a', 'b', 'c', 'd'
print(my_tuple)
print(tuple())      # Empty tuple
print()

# Tuple may or may not use () for initialization
t = 1,2,3,4,'kde', 55.5, 100
print(t)
print(type(t))
print()

# Wrong way to declare a Tuple with Single element
repeated_tuple = ('abc')*6
print(repeated_tuple)
repeated_tuple = (4)*6
print(repeated_tuple)
repeated_tuple = ('abc',)*6
print(repeated_tuple)
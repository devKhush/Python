a = None
if (a is None):         #
    print("Yes")
else:
    print("No")
print()


# 'in' operator
print('"in" Operator on lists & strings:')
str = 'dev'
a = [45, 56, 6]
print(45 in a)
print(100 in a)
print('de' in str)
print('d' in str)
print('D' in str)
print()


# 'is' operator on list     , 'is' check addresses
a = [1, 2, 3]       # Lists with same values have different address
b = [1, 2, 3]
print('\'is\' operator on Lists:')
print(a is b)
b = a
print(a is b)
b[0] = 10
print(a)
print(b)
print()


# 'is' operator on tuples
print('\'is\' operator on Tuples:')
a = (1, 2, 3)                # Tuples with same values have same address
b = (1, 2, 3)
print(a is b)
b = a
print(a is b)
print()


# 'is' operator on tuples
print('\'is\' operator on Strings:')
a = "Hello"                  # Strings with same values have same address
b = "Hello"
print(a is b)
a = b
print(a is b)
print()


# 'is' operator on Sets
print('\'is\' operator on Sets:')
a = {1, 2, 3}                # Sets with same values have different address
b = {1, 2, 3}
print(a is b)
a = b
print(a is b)
a.remove(2)
print(a)
print(b)
print()


# 'is' operator on Dictionary
print('\'is\' operator on Dictionary:')
a = {1: 1, 2: 2, 3: 3}       # Dictionary with same values have different address
b = {1: 1, 2: 2, 3: 3}
print(a is b)
b = a
print(a is b)
a[1] = 100
print(a)
print(b)

# For varaibles with diff. values in each cases of List, Set, String, Tuples, Dict, Set,
# their address are always different

x = 'spam '
x *= 10
print(x)


# Walrus Operator
'''Walrus operator := allows you to assign values to variables within an expression,
including variables that do not exist yet.'''
print(x := 40 - 10 * 3)
print(x)
print()

print(age := int(input('Enter age: ')))
print(f'My age is {age}')

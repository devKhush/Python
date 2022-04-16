print('*'*50, 'Demo 1', '*'*50)


def add(a, b):
    print('\n', '*'*20, 'Inside function call', '*'*20)

    # call by reference as values are not passed reference to x & y are passed
    print("Id's of  a & b = %d, %d" % (id(a), id(b)))
    a = 1
    b = 2
    print("Id's of  a & b = %d, %d" % (id(a), id(b)))
    print('Sum is', a+b)

    print('*'*20, 'Exiting function call', '*'*20, '\n')


x, y = 10, 20
print("x & y = %d, %d" % (x, y))
print("Id's of  x & y = %d, %d" % (id(x), id(y)))
add(x, y)
print("x & y = %d, %d" % (x, y))

print('\n\n')


print('*'*50, 'Demo 2', '*'*50)


def add(x, y):
    print('\n', '*'*20, 'Inside function call', '*'*20)

    # call by reference as values are not passed reference to x & y are passed
    print("Id's of  x & y = %d, %d" % (id(x), id(y)))
    x = 1
    y = 2
    print("Id's of  x & y = %d, %d" % (id(x), id(y)))
    print("x & y = %d, %d" % (x, y))
    print('Sum is', x+y)
    print("x & y = %d, %d" % (x, y))

    print('*'*20, 'Exiting function call', '*'*20, '\n')


x, y = 10, 20
print("x & y = %d, %d" % (x, y))
print("Id's of  x & y = %d, %d" % (id(x), id(y)))
add(x, y)
print("x & y = %d, %d" % (x, y))

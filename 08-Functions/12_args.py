def add(*args):
    sum = 0
    for i in args:
        sum += i
    print('Sum is %d' % sum)


add(10, 20, 10, 30)
add(10, 20, 10, 30, 40)
add(10, 20)
add(10)

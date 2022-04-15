# https://www.geeksforgeeks.org/generators-in-python/
# https://www.sololearn.com/learning/1073/2462/5105/1

def fibonacci(n: int):

    a, b = 0, 1
    i = 0
    while i <= n:
        i += 1
        yield a
        a, b = b, a+b


fib = fibonacci(5)
print(fib.__next__(), end=' ')
print(fib.__next__(), end=' ')
print(fib.__next__(), end=' ')
print(fib.__next__(), end=' ')
print(fib.__next__(), end=' ')
print()

for i in fibonacci(10):
    print(i, end=' ')

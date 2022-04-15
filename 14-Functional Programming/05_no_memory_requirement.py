'''
Due to the fact that they yield one item at a time, generators don't have the memory restrictions of lists.
In fact, they can be infinite!
generators allow you to declare a function that behaves like an iterator, 
i.e. it can be used in a for loop.
'''


def infinite_sevens():
    while True:
        yield 7


for i in infinite_sevens():
    print(i)

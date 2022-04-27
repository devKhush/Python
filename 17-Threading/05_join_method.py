# A model where multiple threads within a process execute independently while
# sharing same resources (can be data, files, same call stacks) is called multithreading.

from threading import Thread


class Calculator:

    def num(self):
        for i in range(1, 6):
            print('The number is {}'.format(i))

    def square(self):
        for i in range(1, 6):
            print('The square of number is {}'.format(i*i))

    def double(self):
        for i in range(1, 6):
            print('The double of number is {}'.format(2*i))


calc = Calculator()

t1 = Thread(target=calc.num)
t2 = Thread(target=calc.square)
t3 = Thread(target=calc.double)

t1.start()
t1.join()

t2.start()
t3.start()

for i in range(1, 6):
    print('This is the main thread test 1')

# Wait until the thread terminates.
# This blocks the calling thread until the thread whose join() method is called terminates
# -- either normally or through an unhandled exception or until the optional timeout occurs.
t2.join()
t3.join()

for i in range(1, 6):
    print('This is the main thread test 2')

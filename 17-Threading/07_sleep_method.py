from threading import Thread
import time

# sleep(seconds)
# Delay execution for a given number of seconds. Puts threads into sleep for given time in seconds


class Calculator:

    def num(self):
        for i in range(1, 6):
            print('The number is {}'.format(i))
            time.sleep(1)

    def square(self):
        for i in range(1, 6):
            print('The square of number is {}'.format(i*i))
            time.sleep(1)

    def double(self):
        for i in range(1, 6):
            print('The double of number is {}'.format(2*i))
            time.sleep(1)


calc = Calculator()

t1 = Thread(target=calc.num)
t2 = Thread(target=calc.square)
t3 = Thread(target=calc.double)

t1.start()
t2.start()
t3.start()

for i in range(1, 6):
    print('This is the main thread test 1')

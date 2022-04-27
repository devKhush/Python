from threading import Thread
import time

# sleep(seconds)
# Delay execution for a given number of seconds. Puts threads into sleep for given time in seconds


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

# Each thread starts and get executed completely in duration of 0.2 sec
t1.start()
time.sleep(0.2)

t2.start()
time.sleep(0.2)

t3.start()
# try commenting below line and observe results (both t3 and below for loops can execute simultaneously in this case)
# if time.sleep is not commented, then t3 starts and execute completely before execution of below for loops
time.sleep(0.2)

for i in range(1, 6):
    print('This is the main thread test 1')

for i in range(1, 6):
    print('This is the main thread test 2')

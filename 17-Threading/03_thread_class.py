from threading import *


class Demo:
    def show(self):
        for i in range(1, 11):
            print("\nThis is a child thread")


runnable = Demo()

my_thread1 = Thread(target=runnable.show())     # object of thread class
my_thread1.start()

for i in range(10):
    print('\nThis is a parent thread')

from threading import *


class MyThreadClass1(Thread):

    def run(self):
        for i in range(1, 11):
            print("\nThis is a child thread 1")


class MyThreadClass2(Thread):

    def run(self):
        for i in range(1, 11):
            print("\nThis is a child thread 2")
            if i == 5:
                raise RuntimeError


# Thread class has a blueprint of run function (re-define it in child class for threading)
# By default target is run function
my_thread1 = MyThreadClass1()
my_thread2 = MyThreadClass2()

my_thread1.start()
my_thread2.start()                  # try commenting

for i in range(10):
    print('\nThis is a parent thread')

# Conclusion form this program: All the other threads keeps on running/executing if any exception
# occurs in one of the executing threads.

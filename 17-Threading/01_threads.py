# A process is a executable instance of a computer program
# A thread is a sequence of instructions in a program that can be executed independent of
# the remaining program (thread exists within processes)
import threading


def show():
    for i in range(1, 51):
        print('This is a child thread')


# Default thread is parent thread (when program is runned, parent thread is created)
# Execution of a program happens in parent thread unless we create one thread
for i in range(1, 51):
    print('This is a parent thread')


# the below thread will runs only show() method in separate thread (as target is show())
# Everything else in the program will be runned on parent thread (provided there are no more thread)
# 'Target' is the task that thread will perform
thread = threading.Thread(target=show())
thread.start()

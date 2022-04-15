import time


def timer(AnyFunction):

    def wrapper(*args):

        print('Time before function call : ', tStart := time.time())
        AnyFunction(*args)
        print('Time After function call : ', tEnd := time.time())
        print('Total time s[end in fucntion call :',
              (tEnd - tStart)*1000, 'milli seconds')

    return wrapper


@timer
def run(n) -> None:

    time.sleep(2)
    print('Inside function')
    for i in range(n):
        a = 1


run(100000000)


# Look at last example in video:
# https://www.youtube.com/watch?v=r7Dtus7N4pI

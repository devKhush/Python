from random import randint

i = 2

while i <= 50:
    print(i, end=' ')
    i = i + 2

print('\n')


# 'else' in 'while else' loops executes only when,
# the while loop executes fully/successfully/whole without any breaks
# 'else' is executed in full termination of while loop
# can be used to check whether while loop terminated with or without any breaks

while i != 10:
    i = randint(1, 10)

    print(i)
    if i == 8:
        print('loop break by 8')
        break
else:
    print('10 is recived now')

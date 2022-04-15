print('********************************************Part 1********************************************')

while True:
    print('\nEnter \'q\' to quit ')
    a = input('Enter a number: ')
    if a == 'q':
        break

    try:
        a = int(a)
        if a > 5:
            print('You entered a number greater than 5')
    except Exception as e:
        print('You entered something invalid')
        print(type(e))
        print(f'Error: {e}')

print('\nDone')


print('\n********************************************Part 2********************************************')
while True:
    print('\nEnter \'q\' to quit ')
    a = input('Enter a number: ')
    if a == 'q':
        break

    try:
        a = int(a)
        if a > 5:
            print('You entered a number greater than 5')
    except Exception:
        print('You entered something invalid')
        print(type(Exception))
        print(f'Error: {Exception}')

print('\nDone')

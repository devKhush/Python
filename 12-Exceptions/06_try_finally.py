a = 0       # try to change a to 1
try:
    print('Entered into try..')
    print(c := 1/a)
finally:
    print('\nEntered into finally..')
    print('we are done\n')

print('\nWill not executed')

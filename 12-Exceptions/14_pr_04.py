a = int(input('Enter dividend: '))
b = int(input('Enter divisor: '))

try:
    result = a/b
except ZeroDivisionError:       # Note without 'as e' also works
    print(f'Result of {a}/{b} = Infinity')
else:
    print(f'Result of {a}/{b} = {a/b}')
finally:
    print('Division done sucessfully')

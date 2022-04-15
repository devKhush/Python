
# Try giving '0' as input and '1' as input

print('************Part 1 with exit()************')
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print('\nGot an error...')
    print(e)
else:
    print('Got No error')
finally:
    print("\nWe are done")

print("Thanks for using the program")


print('\n************Part 2 without exit()************')
try:
    c = 1/i
except:
    print('\nGot an error...')
    exit()
else:
    print('Got no error')
finally:
    print("\nWe are done")

print("Thanks for using the program")
print("Will not execute if '0' is given as input")

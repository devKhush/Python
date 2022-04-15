try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print('\nGot an Exception...')
    print(e)
else:
    print("We were successful")

print('Done')

# If there is no error in try block
# 1) except clause is not executed
# 2) else part is executed (else without except clause isn't possible)
# 3) finally too if it is present

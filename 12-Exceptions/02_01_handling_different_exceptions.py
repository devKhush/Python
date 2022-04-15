'''
A try statement can have multiple different except blocks to handle different exceptions.
Multiple exceptions can also be put into a single except block using parentheses, 
to have the except block handle all of them.'''

try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)

# No statement allowed b/w try and except block/clause other than comments
# print()


except ValueError as e:
    print()
    print(f'Error: {e}')
    print("Please Enter a valid Integer value")

except ZeroDivisionError as e:
    print()
    print(f'Error: {e}')
    print("Make sure you are not dividing by 0")

# Multiple exception can be grouped together like this
except (IndexError, SyntaxError, MemoryError):
    print('Some Error occured')

# This is a general Exception except clause/block block as in JAVA
# It can catch/handle any error not handled by previous except clause
# Note Exception here, but even though just 'except:' works, see 02_02_nested_try_except.py
except Exception as e:
    print()
    print(e)
    print('Any other Error found')

# This will execute bcoz exception is already handled
print("\nThanks for using this code!")

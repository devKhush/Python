a = None

try:
    a = input("Enter a number: ")
    c = 1/a

# Here only TypeError will be thrown as a is a string always (given by input())
except TypeError as e:
    print(f'\nGot a Type error as \'{a}\' is a str & is not converted to int')
    print(f'Error: {e}')

    try:
        a = int(a)
        print(c := 1/a)

    except ValueError as e:
        print("\nPlease Enter a valid Integer value")
        print('Got a ValueError')
        print(f'Error: {e}')

    except ZeroDivisionError as e:
        print('Got a ZeroDivisionError')
        print("\nMake sure you are not dividing by 0")
        print(f'Error: {e}')

    except:
        print('\nAny other Error found')
        print(e)


# An except statement without any exception specified will catch all errors.
# These should be used sparingly, as they can catch unexpected errors and hide programming mistakes.

# This will execute bcoz exception is already handled
print("\nThanks for using this code!")

def reciprocal(num):
    try:
        convertedToInt = False
        num = int(num)
        convertedToInt = True
        return 1/num
    except:           # This shows that both 'except Exception as anyName' and 'except' can eb used
        if not convertedToInt:
            raise ValueError(
                "Only Integer value allowed \nGot a ValueError in Reciprocal()")
        if int(num) == 0:
            raise ZeroDivisionError(
                "Division by 0 not allowed\nGot a ZeroDivisionError in Reciprocal()")


def increment(x):
    if type(x) != int:                    # Try commenting this part (if block)
        raise TypeError('Only Integer values allowed in Increment()')
    return x+1


def strToInt(x):
    if type(x) != int and type(x) != str and type(x) != float:
        raise TypeError(
            'Only Integer, Float or String values allowed in strToInt()')
    try:
        return int(x)
    except Exception as e:
        raise ValueError(
            "Only Integer values as String are allowed \nGot a ValueError in strToInt()")


num = '23'
# If a error is thrown, then after this line statement willn't execeute as program flow will terminate
a = reciprocal(num)

print(a)

print()
num = 4
b = increment(num)
print(b)

print()
num = None
print(strToInt(num))

# This will execute bcoz exception is already handled
print("\nThanks for using this code!")

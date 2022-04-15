def maximum(num1, num2, num3):
    print('Complex maximum()')

    if (num1 > num2):
        if(num1 > num3):
            return num1
        else:
            return num3
    else:
        if(num2 > num3):
            return num2
        else:
            return num3


def maximum(a, b, c):
    print('Easy maximum()')

    max1 = a
    max2 = b if b > c else c
    return max1 if max1 > max2 else max2


# If there are multiple func with same name, then recent written function will be called

m = maximum(13, 55, 2)
print("The value of the maximum is " + str(m))

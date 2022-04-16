# https://www.geeksforgeeks.org/args-kwargs-python/

# *********************************************** Example 1 ***********************************************

def myFun1(*args, **kwargs):
    # args[1] = 1         # args is received as tuple

    print("args: ", args)
    print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun1('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
print('\n')

# *********************************************** Example 2 ***********************************************


# Python program to illustrate **kwargs for
# variable number of keyword arguments with
# one extra argument.

def myFun2(arg1, **kwargs):
    print(arg1)
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun2("Hi", first='Geeks', mid='for', last='Geeks')

def greet(name):        # returns None by default
    a = 200             # local 'a' variable to func greet()
    print("Good Day, " + name)


def mySum(num1: int, num2) -> int:
    print('Sum func called')
    # a = 999           # error -> same variable can't be assigned before global variable
    global a            # change global 'a' variable
    a = 500
    # a = 1
    return num1 + num2


# works even different parameters & return types are specified || Try out
def mySum2(num1: list, num2: str) -> str:
    print('Sum 2 func called')
    return num1 + num2


a = 100
print(a)

greet("Harry")
print(a)
print()

s = mySum(7, 3)
print('Sum is:', s)
print(a)

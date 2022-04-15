a = 54  # Global variable


def func1():
    print('Inside Func2')

    # a = 0         # Error can't use same variable before global variable
    global a

    print(f"Print statement 2: {a}")
    a = 8                # Local Variable if global keyword is not used, scope is not used
    print(f"Print statement 3: {a}")


def func2():
    a = 1
    print('Inside Func2')
    print(f"Print statement 5: {a}")


print(f"Print statement 1: {a}")
func1()
print(f"Print statement 4: {a}")

func2()
print(f"Print statement 6: {a}")

x, y, z = 1, 2, 3
a = 1
b = 2

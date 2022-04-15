# Python program to illustrate functions
# can be passed as arguments to other functions

# ********************************************EXAMPLE 1********************************************

def shout(text, message):
    return text.upper() + f'{message}'


def whisper(text, message):
    return text.lower() + f'{message}'


def greet(func, m):
    # storing the function in a variable
    greeting = func(
        """Hi, I am created by a function passed as an argument""", m)
    print(greeting)


a = greet

print(a)
print(type(a), '\n')

info = '...'
a(shout, info)
a(whisper, info)
my_print = print
my_print()


# ********************************************EXAMPLE 2********************************************

# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
    def adder(y):
        return x+y

    return adder


add_15 = create_adder(15)
print(sum := add_15(10))
print(create_adder(100)(50))

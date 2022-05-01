def adder(anyFunction):

    def wrapperFunction(*args):

        print('*'*100)
        print('\t'*4, 'Welcome to Adder Calculator!')
        print('*'*100)
        sum = anyFunction(*args)
        return sum

    return wrapperFunction


@adder
def add(a, b, *args):
    return a + b + sum(args)


print('Sum is :', add(1, 2, 3, 4, 5))

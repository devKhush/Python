# https://www.geeksforgeeks.org/decorators-in-python/
# https://www.youtube.com/watch?v=_zTyBMFD4yY
# https://www.geeksforgeeks.org/args-kwargs-python/


# takes in decorated function as parameter show_content() here
# this happens same as 10_Decorators_3.py

def myDecorator(anyFunction):
    print('Step 1')
    print(anyFunction)

    def boundary(content: str, *args, **kwargs):
        print('Step 3')
        print(anyFunction)

        print(args[0]*args[1])
        anyFunction(content, *args, **kwargs)
        print(args[0]*args[1])

        print('Step 7')

    print('Step 2')

    return boundary


@myDecorator
def show_content(string_: str, *args):
    print('Step 5')
    print('\t'*5, 'Hello,', string_, '!!!')
    print('Step 6')


show_content('Khushdev', '*', 100)

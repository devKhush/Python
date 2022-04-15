# https://www.geeksforgeeks.org/decorators-in-python/
# https://www.youtube.com/watch?v=_zTyBMFD4yY
# https://www.geeksforgeeks.org/args-kwargs-python/


# takes in decorated function as parameter show_content() here
# this happens same as 10_Decorators_3.py

def myDecorator(anyFunction):

    def boundary(*args, **kwargs):

        print('*'*100)
        anyFunction(*args, **kwargs)
        print('*'*100)

    return boundary


@myDecorator
def show_content(string_: str):
    print('\t'*5, 'Hello,', string_, '!!!')


show_content('Khushdev')

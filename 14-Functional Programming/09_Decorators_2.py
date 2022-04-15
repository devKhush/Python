# https://www.geeksforgeeks.org/decorators-in-python/
# https://www.geeksforgeeks.org/args-kwargs-python/
# https://www.sololearn.com/learning/1073/2463/5109/1
# https://www.youtube.com/watch?v=r7Dtus7N4pI

def myDecorator(content: str):

    def boundary(border: str, times=100):       # default parameter
        print(border*times)
        show_content(content)
        print(border*times)

    return boundary


def show_content(string_: str):
    print('\t'*5, 'Hello,', string_, '!!!')


decorator = myDecorator('Khushdev')
print(decorator)
print(type(decorator))
print()

decorator('~')

print()

myDecorator('Khushdev Pandit')('$')

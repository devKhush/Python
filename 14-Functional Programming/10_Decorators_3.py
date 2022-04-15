# https://www.geeksforgeeks.org/decorators-in-python/
# https://www.sololearn.com/learning/1073/2463/5109/1
# https://www.youtube.com/watch?v=r7Dtus7N4pI

def myDecorator(functionAny):

    def boundary(content: str, border: str, times=1):       # default parameter
        print(border*times)
        functionAny(content)
        print(border*times)

    return boundary


def show_content(string_: str):
    print('\t'*5, 'Hello,', string_, '!!!')


show_content = myDecorator(show_content)

show_content('Khushdev', '-', 100)
print()
show_content('Khushdev', '>', 100)

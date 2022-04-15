def methodDecorator(func):

    def wrapper(*args, **kwargs):
        print('.......................Start.......................')
        item = func(*args)
        print('.......................End.......................')
        return item

    return wrapper


class Test:
    def __init__(self):
        self.info = '\t\tObject of Test class'

    @methodDecorator
    def getInfo(self):
        print(self.info)


test = Test()
test.getInfo()

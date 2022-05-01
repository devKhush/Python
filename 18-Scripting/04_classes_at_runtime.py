# Fatory method

class A:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def run(self):
        pass


class B(A):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def run(self):
        print('B class')


class C(A):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def run(self):
        print('C class')


def getObject(boolean, a, b) -> A:
    if boolean:
        return B(a, b)
    else:
        return C(a, b)


obj1 = getObject(True, 2, 4)
obj2 = getObject(False, 4, 5)

print(obj1, obj2)

obj1.run()
obj2.run()

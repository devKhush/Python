class A:
    def __init__(self) -> None:
        pass

    def set(self, a):
        self.a = a

    def show(self):
        print(self.a)


obj = A()
# obj.show()            # error as self.a is still not defined for objs
obj.set(100)
obj.show()

obj = A()
# obj.show()            # error as self.a is still not defined for objs

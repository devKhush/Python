class Calculator:
    def __init__(self, a: int) -> None:
        self.number = a
        self.greet()

    def square(self) -> None:
        print(f"The value of {self.number} square is {self.number **2}")

    def sqrt(self) -> None:
        # python formatting ways
        print(
            f"The value of {self.number} square root is {round(self.number**0.5, 4)}")
        print("The value of {num} square root is {sqrt:.4f}".format(num=self.number,
                                                                    sqrt=(self.number**0.5)))
        print(
            f"The value of {self.number} square root is %.4f" % (self.number**0.5))

    def cube(self) -> None:
        print(f"The value of {self.number} cube is {self.number**3}")

    def cubeRoot(self) -> None:
        pass

    @staticmethod
    def greet() -> None:
        print('Hello, user! Welcome to the calculator!!!')


calculator = Calculator(6)
calculator.greet()
print()

calculator.sqrt()
print()
calculator.cube()
print()
calculator.square()
print()

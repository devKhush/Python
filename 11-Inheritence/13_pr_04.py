class ComplexNumber:
    def __init__(self, Real, Imag) -> None:
        self.real = Real
        self.imag = Imag

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(Real=real, Imag=imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(Real=real, Imag=imag)

    def __str__(self) -> str:
        if self.imag > 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"


a = ComplexNumber(1, 2)
print(a)

b = ComplexNumber(4, -3)
print(b)

print(a+b)
print(a*b)

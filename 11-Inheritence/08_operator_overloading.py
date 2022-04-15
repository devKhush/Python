# https://www.sololearn.com/learning/1073/2470/5133/1
# https://www.sololearn.com/learning/1073/2470/5136/1
# https://www.sololearn.com/learning/1073/2470/5135/1

class Number:
    # Dunder methods are names that are preceded and succeeded by double underscores
    # eg: __init__(), __add__(), __mul__()

    def __init__(self, num):
        self.num = num
        self.waste = 1000

    # Method overloading aka Operator overloadings
    def __add__(self, num2) -> int:
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num

    def __sub__(self, num2) -> int:
        print('Subracting...')
        return self.num - num2.num


# See Harry Notes OP 🔥🔥🔥
n1 = Number(10)
n2 = Number(6)

# Operators on Objects, need some operators methods called decorators method
sum = n1 + n2
mul = n1 * n2
sub = n1 - n2

print(sum)
print(mul)
print(sub)
print(type(sum))
print(type(mul))
print(type(sub))

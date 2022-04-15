# https://www.sololearn.com/learning/1073/2470/5133/1
# https://www.sololearn.com/learning/1073/2470/5136/1

class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num

    def __str__(self) -> str:       # toString() method in JAVA
        return f'Decimal number : {self.num}'

    def __len__(self) -> int:
        return 1


n = Number(9)
print(n)        # toString() method in JAVA
print(len(n))

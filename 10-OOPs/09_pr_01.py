class Programmer:

    company = 'Google'

    def __init__(self, name: str, age: int, favLang: str) -> None:
        self.name = name
        self.age = age
        self.favLang = favLang

    def introduce(self) -> None:
        print(
            f"Hello, \nMy name is {self.name} \nMy age is {self.age} \nMy favoriate language is {self.favLang} \nAnd I work in {self.company}")


dev = Programmer('Khushdev', 19, 'Java and Python')
dev.introduce()

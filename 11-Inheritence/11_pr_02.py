# Example of Multi-level Inheritence

class Animal:
    def __init__(self, leg, gender) -> None:
        self.legs = leg
        self.gender = gender


class Pet(Animal):
    def __init__(self, leg, gender, height) -> None:
        super().__init__(leg, gender)
        self.height = height


class Dog(Pet):
    def __init__(self, leg, gender, height, colour) -> None:
        super().__init__(leg, gender, height)
        self.colour = colour

    def bark(self):
        print('Dog is barking...')

    def getDogDetails(self):
        print(f'Dog num of Legs: {self.legs}')
        print(f'Dog num of Gender: {self.gender}')
        print(f'Dog num of Height: {self.height}')
        print(f'Dog num of Colour: {self.colour}')


dog = Dog(4, 'Male', '1 metre', 'White')
print(dog.legs)
print(dog.gender)
print(dog.height)
print(dog.colour)

dog.getDogDetails()

dog.bark()

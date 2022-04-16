class Car:
    def __init__(self, name) -> None:
        self.name = name

    def accelerate(self):
        print('Accelerating...')


class BMW(Car):
    def accelerate(self, speed):
        print('Accelerating to', speed, 'kmph')
        return super().accelerate()


class Audi(Car):
    def accelerate(self, speed):
        print('Accelerating to', speed, 'kmph')
        return super().accelerate()


cars = [BMW('My BMW'), Audi('My Audi')]

for car in cars:
    print(car.name, end=' ')
    car.accelerate(100)
    print()
    # car.accelerate()      # method has been overidden, so throws error (this doesn't happens in Java)

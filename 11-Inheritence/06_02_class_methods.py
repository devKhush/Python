# https://www.sololearn.com/learning/1073/2473/5142/1


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        print('Area of this rectangle is {} \n'.format(self.height*self.width))

    @classmethod
    def getRectangle(cls, height, width):
        return cls(width, height)

    @classmethod
    def getSquare(cls, width):
        return cls(width, width)


r1 = Rectangle(3, 4)
r1.getArea()

r2 = Rectangle.getRectangle(10, 20)
r2.getArea()

square = Rectangle.getSquare(5)
square.getArea()

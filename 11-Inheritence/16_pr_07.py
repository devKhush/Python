class Vector:
    def __init__(self, vector: list) -> None:
        self.vector = vector

    def __add__(self, other):
        sumVector = Vector([])
        for i in range(0, len(self.vector)):
            sumVector.vector.append(self.vector[i] + other.vector[i])
        return sumVector

    def __mul__(self, other) -> int:
        dotProduct = 0
        for i in range(0, len(self.vector)):
            dotProduct += self.vector[i] * other.vector[i]
        return dotProduct

    def __str__(self) -> str:
        return str(self.vector)

    def __len__(self) -> int:
        return len(self.vector)


vector1 = Vector([2, 3, 4])
vector2 = Vector([1, 6, 5])

print(vector1)
print(vector2)
print(len(vector1))
print(len(vector2))
print()

print(vector1+vector2)
print(vector1*vector2)

class Vector:
    def __init__(self, vector: list):
        self.vector = vector

    def __str__(self):
        return f"{self.vector[0]}i + {self.vector[1]}j + {self.vector[2]}k"


v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])
print(v1)
print(v2)

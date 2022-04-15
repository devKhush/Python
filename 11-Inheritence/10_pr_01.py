# Example of Single Inheritence

class Vector2D:
    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j

    def __str__(self) -> str:
        return f'{self.i}i + {self.j}j'


class Vector3D(Vector2D):
    def __init__(self, i, j, k) -> None:
        super().__init__(i, j)
        self.k = k

    def __str__(self) -> str:
        return f'{self.i}i + {self.j}j + {self.k}k'


vec2D = Vector2D(3, 4)
vec3D = Vector3D(6, 9, 1)

print(vec2D)
print(vec3D)

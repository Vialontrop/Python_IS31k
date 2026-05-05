# Практическая работа 21 – Задача 14
# Vector со слотами и методом сложения векторов

class Vector:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __add__(self, other):
        return self.add(other)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1.add(v2)
print(v3)           # Vector(4, 6)

v4 = v1 + v2        # через __add__
print(v4)           # Vector(4, 6)

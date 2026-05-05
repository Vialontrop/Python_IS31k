# Практическая работа 21 – Задача 7
# Point со слотами и методом строкового представления координат

class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coords(self):
        return f"({self.x}, {self.y})"

    def __str__(self):
        return self.coords()


p1 = Point(3, 7)
p2 = Point(-1, 0)

print(p1.coords())   # (3, 7)
print(p2.coords())   # (-1, 0)
print(p1)            # (3, 7)

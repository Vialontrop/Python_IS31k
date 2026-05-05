# Практическая работа 21 – Задача 9
# Circle со слотами и методом вычисления площади

import math

class Circle:
    __slots__ = ('radius',)

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


c = Circle(5)
print(f"Радиус: {c.radius}")
print(f"Площадь: {c.area():.4f}")           # 78.5398
print(f"Длина окружности: {c.circumference():.4f}")  # 31.4159

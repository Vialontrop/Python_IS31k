# Практическая работа 21 – Задача 8
# Rectangle со слотами и методом вычисления площади

class Rectangle:
    __slots__ = ('width', 'height')

    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


r = Rectangle(5, 3)
print(f"Ширина: {r.width}, Высота: {r.height}")
print(f"Площадь: {r.area()}")        # 15
print(f"Периметр: {r.perimeter()}")  # 16

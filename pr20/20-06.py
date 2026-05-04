# Практическая работа 20 – Задача 6
# Положительные числа: только > 0

class Positive:
    def __set_name__(self, owner, name):
        self._name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self._name)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Ожидается число")
        if value <= 0:
            raise ValueError(f"Значение должно быть положительным, получено: {value}")
        obj.__dict__[self._name] = value


class Product:
    price = Positive()
    quantity = Positive()


p = Product()
p.price = 99.9
p.quantity = 5
print(p.price, p.quantity)   # 99.9 5

try:
    p.price = -10
except ValueError as e:
    print(e)

try:
    p.quantity = 0
except ValueError as e:
    print(e)

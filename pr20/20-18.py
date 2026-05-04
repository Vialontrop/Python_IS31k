# Практическая работа 20 – Задача 18
# Список чисел: разрешены только list, все элементы — числа

class NumberList:
    def __set_name__(self, owner, name):
        self._name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self._name)

    def __set__(self, obj, value):
        if not isinstance(value, list):
            raise TypeError("Ожидается список (list)")
        for item in value:
            if not isinstance(item, (int, float)):
                raise ValueError(f"Все элементы должны быть числами, найдено: {item!r}")
        obj.__dict__[self._name] = value


class Statistics:
    values = NumberList()


s = Statistics()
s.values = [1, 2.5, 3, 4.0, 5]
print(s.values)   # [1, 2.5, 3, 4.0, 5]
print(sum(s.values))

try:
    s.values = [1, "два", 3]
except ValueError as e:
    print(e)

try:
    s.values = (1, 2, 3)
except TypeError as e:
    print(e)

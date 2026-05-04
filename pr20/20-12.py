# Практическая работа 20 – Задача 12
# Возраст: только значения от 0 до 120

class Age:
    def __set_name__(self, owner, name):
        self._name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self._name)

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError("Возраст должен быть целым числом")
        if not (0 <= value <= 120):
            raise ValueError(f"Возраст должен быть от 0 до 120, получено: {value}")
        obj.__dict__[self._name] = value


class Person:
    age = Age()


p = Person()
p.age = 25
print(p.age)   # 25

try:
    p.age = -5
except ValueError as e:
    print(e)

try:
    p.age = 150
except ValueError as e:
    print(e)

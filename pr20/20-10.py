# Практическая работа 20 – Задача 10
# Ограничение длины: строки не длиннее 10 символов

class MaxLength:
    def __init__(self, max_len=10):
        self.max_len = max_len

    def __set_name__(self, owner, name):
        self._name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self._name)

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("Ожидается строка")
        if len(value) > self.max_len:
            raise ValueError(f"Строка слишком длинная: {len(value)} > {self.max_len}")
        obj.__dict__[self._name] = value


class Tag:
    label = MaxLength(10)


t = Tag()
t.label = "Python"
print(t.label)   # Python

try:
    t.label = "очень длинная строка"
except ValueError as e:
    print(e)

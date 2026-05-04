# Практическая работа 20 – Задача 17
# Кэширование: значение вычисляется один раз

import time

class CachedProperty:
    def __init__(self, func):
        self.func = func
        self._name = None

    def __set_name__(self, owner, name):
        self._name = f"_cached_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self._name not in obj.__dict__:
            print(f"[Cache] Вычисляю '{self.func.__name__}'...")
            obj.__dict__[self._name] = self.func(obj)
        else:
            print(f"[Cache] Возвращаю из кэша '{self.func.__name__}'")
        return obj.__dict__[self._name]


class Report:
    def __init__(self, data):
        self.data = data

    @CachedProperty
    def result(self):
        time.sleep(0.3)   # имитация долгого вычисления
        return sum(self.data) * 2


r = Report([1, 2, 3, 4, 5])
print(r.result)   # вычисляет
print(r.result)   # берёт из кэша
print(r.result)   # берёт из кэша

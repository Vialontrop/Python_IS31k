# Практическая работа 20 – Задача 9
# Счётчик обращений к атрибуту

class CountedAccess:
    def __set_name__(self, owner, name):
        self._name   = f"_{name}"
        self._count  = f"_{name}_count"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        obj.__dict__[self._count] = obj.__dict__.get(self._count, 0) + 1
        return obj.__dict__.get(self._name)

    def __set__(self, obj, value):
        obj.__dict__[self._name] = value

    def get_count(self, obj):
        return obj.__dict__.get(self._count, 0)


class DataModel:
    value = CountedAccess()


d = DataModel()
d.value = 42
_ = d.value
_ = d.value
_ = d.value

print(f"Значение: {d.value}")
print(f"Обращений: {DataModel.value.get_count(d)}")  # 4

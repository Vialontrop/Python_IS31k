# Практическая работа 20 – Задача 5
# Ограничение типа: только int

class IntOnly:
    def __set_name__(self, owner, name):
        self._name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self._name)

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError(f"Ожидается int, получено {type(value).__name__}")
        obj.__dict__[self._name] = value


class Config:
    count = IntOnly()


cfg = Config()
cfg.count = 10
print(cfg.count)   # 10

try:
    cfg.count = "abc"
except TypeError as e:
    print(e)   # Ожидается int, получено str

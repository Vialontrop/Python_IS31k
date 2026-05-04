# Практическая работа 20 – Задача 14
# Только одно присваивание: после первого изменение запрещено

class WriteOnce:
    def __set_name__(self, owner, name):
        self._name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self._name)

    def __set__(self, obj, value):
        if self._name in obj.__dict__:
            raise AttributeError(f"Атрибут '{self._name[1:]}' уже установлен и не может быть изменён")
        obj.__dict__[self._name] = value


class ImmutableConfig:
    api_key = WriteOnce()
    version = WriteOnce()


cfg = ImmutableConfig()
cfg.api_key = "SECRET-123"
cfg.version = "1.0.0"

print(cfg.api_key)   # SECRET-123
print(cfg.version)   # 1.0.0

try:
    cfg.api_key = "NEW-KEY"
except AttributeError as e:
    print(e)

try:
    cfg.version = "2.0.0"
except AttributeError as e:
    print(e)

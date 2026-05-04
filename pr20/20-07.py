# Практическая работа 20 – Задача 7
# Строковый дескриптор: только str

class StringOnly:
    def __set_name__(self, owner, name):
        self._name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self._name)

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError(f"Ожидается str, получено {type(value).__name__}")
        obj.__dict__[self._name] = value


class User:
    username = StringOnly()
    email    = StringOnly()


u = User()
u.username = "alice"
u.email    = "alice@example.com"
print(u.username, u.email)

try:
    u.username = 123
except TypeError as e:
    print(e)   # Ожидается str, получено int

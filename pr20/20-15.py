# Практическая работа 20 – Задача 15
# Лог изменений: выводит старое и новое значение

class ChangeLog:
    _MISSING = object()   # sentinel для «значение ещё не задано»

    def __set_name__(self, owner, name):
        self._name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self._name, self._MISSING)

    def __set__(self, obj, value):
        old = obj.__dict__.get(self._name, self._MISSING)
        if old is self._MISSING:
            print(f"[LOG] '{self._name[1:]}' инициализирован: → {value!r}")
        else:
            print(f"[LOG] '{self._name[1:]}': {old!r} → {value!r}")
        obj.__dict__[self._name] = value


class Profile:
    name  = ChangeLog()
    score = ChangeLog()


p = Profile()
p.name  = "Алиса"
p.score = 0
p.name  = "Alice"
p.score = 42

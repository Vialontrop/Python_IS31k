# Практическая работа 20 – Задача 13
# Округление: сохраняет числа до 2 знаков после запятой

class Rounded:
    def __init__(self, digits=2):
        self.digits = digits

    def __set_name__(self, owner, name):
        self._name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self._name)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Ожидается число")
        obj.__dict__[self._name] = round(value, self.digits)


class Invoice:
    amount = Rounded(2)
    tax    = Rounded(2)


inv = Invoice()
inv.amount = 99.9999
inv.tax    = 15.555555

print(inv.amount)   # 100.0
print(inv.tax)      # 15.56

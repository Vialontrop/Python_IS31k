# Практическая работа 20 – Задача 11
# Email-дескриптор: проверяет наличие '@'

class EmailField:
    def __set_name__(self, owner, name):
        self._name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self._name)

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("Email должен быть строкой")
        if "@" not in value:
            raise ValueError(f"Некорректный email: '{value}' — нет символа '@'")
        obj.__dict__[self._name] = value


class Account:
    email = EmailField()


a = Account()
a.email = "user@example.com"
print(a.email)   # user@example.com

try:
    a.email = "notanemail"
except ValueError as e:
    print(e)

try:
    a.email = "also@bad@email"
    print(a.email)   # допустимо — '@' присутствует
except ValueError as e:
    print(e)

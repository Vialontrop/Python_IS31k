# Практическая работа 21 – Задача 3
# Сравнение класса со слотами и без

class WithSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y


ws  = WithSlots(1, 2)
wos = WithoutSlots(1, 2)

# Попытка добавить новый атрибут
print("=== WithSlots ===")
try:
    ws.z = 3
    print(f"z = {ws.z}")
except AttributeError as e:
    print(f"Ошибка: {e}")

print("\n=== WithoutSlots ===")
wos.z = 3
print(f"z = {wos.z}")          # без проблем
print(f"__dict__: {wos.__dict__}")

# Вывод:
# - WithSlots    → AttributeError; нет __dict__, меньше памяти.
# - WithoutSlots → динамическое добавление атрибутов разрешено.

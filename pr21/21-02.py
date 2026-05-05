# Практическая работа 21 – Задача 2
# Animal со слотами: попытка добавить новый атрибут

class Animal:
    __slots__ = ('type', 'weight')

    def __init__(self, type_, weight):
        self.type   = type_
        self.weight = weight


a = Animal("Кот", 4.5)
print(a.type, a.weight)

# Попытка добавить атрибут, которого нет в __slots__
try:
    a.color = "рыжий"
except AttributeError as e:
    print(f"Ошибка: {e}")

# Вывод: AttributeError — __slots__ запрещает создание
# любых атрибутов, не перечисленных в нём.
# Объект не имеет __dict__, поэтому динамическое добавление невозможно.

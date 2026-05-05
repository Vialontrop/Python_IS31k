# Практическая работа 21 – Задача 1
# Класс Person со слотами, создание объекта и вывод атрибутов

class Person:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age  = age


p = Person("Алиса", 25)
print(p.name)   # Алиса
print(p.age)    # 25

# Практическая работа 21 – Задача 13
# Наследование со слотами: Person → Student

class Person:
    __slots__ = ('name',)

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Привет, меня зовут {self.name}"


class Student(Person):
    # Указываем ТОЛЬКО новые слоты (родительские наследуются)
    __slots__ = ('grade',)

    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def info(self):
        return f"{self.greet()}, мой балл: {self.grade}"


p = Person("Иван")
print(p.greet())

s = Student("Маша", 5)
print(s.info())
print(s.name)    # унаследован из Person
print(s.grade)   # собственный слот

# Новые атрибуты по-прежнему запрещены
try:
    s.extra = "запрещено"
except AttributeError as e:
    print(e)

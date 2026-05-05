# Практическая работа 21 – Задача 6
# Student со слотами и методом изменения оценки

class Student:
    __slots__ = ('name', 'grade')

    def __init__(self, name, grade):
        self.name  = name
        self.grade = grade

    def set_grade(self, new_grade):
        if not (1 <= new_grade <= 5):
            raise ValueError(f"Оценка должна быть от 1 до 5, получено: {new_grade}")
        print(f"[{self.name}] оценка изменена: {self.grade} → {new_grade}")
        self.grade = new_grade


s = Student("Иван", 3)
print(f"{s.name}: {s.grade}")
s.set_grade(5)
print(f"{s.name}: {s.grade}")

try:
    s.set_grade(6)
except ValueError as e:
    print(e)

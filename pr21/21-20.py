# Практическая работа 21 – Задача 20
# Student со слотами: grades, add_grade(), average(), запрет новых атрибутов

class Student:
    __slots__ = ('name', 'age', 'grades')

    def __init__(self, name, age):
        self.name   = name
        self.age    = age
        self.grades = []

    def add_grade(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Оценка должна быть числом")
        if not (1 <= value <= 5):
            raise ValueError(f"Оценка должна быть от 1 до 5, получено: {value}")
        self.grades.append(value)

    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return (f"Student(name={self.name!r}, age={self.age}, "
                f"grades={self.grades}, avg={self.average():.2f})")


# Создаём несколько объектов
s1 = Student("Алиса", 19)
s1.add_grade(5)
s1.add_grade(4)
s1.add_grade(5)

s2 = Student("Боб", 20)
s2.add_grade(3)
s2.add_grade(3)
s2.add_grade(4)

s3 = Student("Карлос", 18)
s3.add_grade(5)
s3.add_grade(5)
s3.add_grade(5)

for student in (s1, s2, s3):
    print(student)
    print(f"  Средний балл: {student.average():.2f}\n")

# Убеждаемся, что новые атрибуты запрещены
try:
    s1.nickname = "Аля"
except AttributeError as e:
    print(f"Ошибка: {e}")

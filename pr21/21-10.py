# Практическая работа 21 – Задача 10
# Employee со слотами и методом повышения зарплаты

class Employee:
    __slots__ = ('name', 'salary')

    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

    def raise_salary(self, percent):
        if percent <= 0:
            raise ValueError("Процент должен быть положительным")
        increase = self.salary * percent / 100
        self.salary += increase
        print(f"[{self.name}] зарплата повышена на {percent}%: +{increase:.2f} → {self.salary:.2f}")


e = Employee("Мария", 50_000)
print(f"{e.name}: {e.salary}")
e.raise_salary(10)   # +10%
e.raise_salary(5)    # +5%

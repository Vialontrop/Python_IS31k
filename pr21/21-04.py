# Практическая работа 21 – Задача 4
# Car со слотами и конструктором __init__

class Car:
    __slots__ = ('brand', 'model', 'year')

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year  = year


car = Car("Toyota", "Camry", 2022)
print(f"Марка: {car.brand}")
print(f"Модель: {car.model}")
print(f"Год: {car.year}")

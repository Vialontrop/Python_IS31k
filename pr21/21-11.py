# Практическая работа 21 – Задача 11
# Product со слотами и проверкой: цена не отрицательная

class Product:
    __slots__ = ('name', 'price')

    def __init__(self, name, price):
        self.name  = name
        self.price = price   # вызовет сеттер через свойство — см. ниже

    # Слоты не поддерживают property напрямую;
    # используем явную валидацию в __init__ и set_price
    def set_price(self, value):
        if value < 0:
            raise ValueError(f"Цена не может быть отрицательной: {value}")
        self.price = value


p = Product("Ноутбук", 45_000)
print(f"{p.name}: {p.price} руб.")

p.set_price(50_000)
print(f"Новая цена: {p.price} руб.")

try:
    p.set_price(-100)
except ValueError as e:
    print(e)

try:
    Product("Мышь", -200)
    # Прямое присваивание в __init__ — без проверки;
    # для защиты используйте set_price или свойства через отдельный базовый класс
except Exception as e:
    print(e)

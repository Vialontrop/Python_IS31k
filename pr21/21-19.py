# Практическая работа 21 – Задача 19
# Order со слотами, items — список цен, метод total()

class Order:
    __slots__ = ('items',)

    def __init__(self):
        self.items = []   # список цен (float/int)

    def add_item(self, price):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.items.append(price)

    def total(self):
        return sum(self.items)

    def __str__(self):
        return f"Order({self.items}) → итого: {self.total():.2f}"


o = Order()
o.add_item(199.99)
o.add_item(49.50)
o.add_item(350.00)

print(o)
print(f"Позиций: {len(o.items)}, Сумма: {o.total():.2f} руб.")

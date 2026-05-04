# Практическая работа 20 – Задача 16
# Связанные поля: изменение одного обновляет другое

class LinkedField:
    def __set_name__(self, owner, name):
        self._name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self._name)

    def __set__(self, obj, value):
        obj.__dict__[self._name] = value
        self._on_change(obj, value)

    def _on_change(self, obj, value):
        pass   # переопределяется в подклассах


class PriceField(LinkedField):
    """При изменении цены пересчитывает total."""
    def _on_change(self, obj, value):
        qty = obj.__dict__.get("_quantity", 0)
        obj.__dict__["_total"] = round(value * qty, 2)


class QuantityField(LinkedField):
    """При изменении количества пересчитывает total."""
    def _on_change(self, obj, value):
        price = obj.__dict__.get("_price", 0)
        obj.__dict__["_total"] = round(price * value, 2)


class Order:
    price    = PriceField()
    quantity = QuantityField()

    @property
    def total(self):
        return self.__dict__.get("_total", 0)


o = Order()
o.price    = 9.99
o.quantity = 3
print(f"Цена: {o.price}, Кол-во: {o.quantity}, Итого: {o.total}")   # 29.97

o.price = 5.0
print(f"Цена: {o.price}, Кол-во: {o.quantity}, Итого: {o.total}")   # 15.0

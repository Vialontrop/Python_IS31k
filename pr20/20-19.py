# Практическая работа 20 – Задача 19
# Счётчик объектов: подсчёт количества экземпляров класса

class InstanceCounter:
    """Дескриптор-счётчик, хранит данные на уровне класса."""

    def __set_name__(self, owner, name):
        self._name = name
        # Счётчик живёт в классе, а не в экземпляре
        setattr(owner, f"_{name}_count", 0)

    def __get__(self, obj, objtype=None):
        if obj is None:
            # Обращение через класс — возвращаем текущий счёт
            return getattr(objtype, f"_{self._name}_count")
        return getattr(type(obj), f"_{self._name}_count")

    def __set__(self, obj, value):
        # Устанавливать значение вручную нельзя
        raise AttributeError("Счётчик нельзя задать вручную")


class Robot:
    count = InstanceCounter()

    def __init__(self, name):
        self.name = name
        Robot._count_count += 1   # увеличиваем счётчик при создании

    def __del__(self):
        Robot._count_count -= 1


r1 = Robot("R2D2")
r2 = Robot("C3PO")
r3 = Robot("BB8")

print(f"Роботов создано: {Robot.count}")   # 3

del r3
print(f"Роботов осталось: {Robot.count}")  # 2

# Практическая работа 20 – Задача 20
# Комплексный дескриптор: тип, диапазон, логирование, запрет удаления

class ValidatedField:
    """
    Дескриптор с:
      - проверкой типа (expected_type)
      - проверкой диапазона (min_val, max_val)
      - логированием каждого обращения
      - запретом удаления атрибута
    """

    def __init__(self, expected_type, min_val=None, max_val=None):
        self.expected_type = expected_type
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self._name    = name
        self._private = f"_{name}"

    # ── GET ──────────────────────────────────────────────
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self._private, None)
        print(f"[GET]  '{self._name}' → {value!r}")
        return value

    # ── SET ──────────────────────────────────────────────
    def __set__(self, obj, value):
        # 1. Проверка типа
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"'{self._name}': ожидается {self.expected_type.__name__}, "
                f"получено {type(value).__name__}"
            )
        # 2. Проверка диапазона
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"'{self._name}': значение {value} < минимума {self.min_val}")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"'{self._name}': значение {value} > максимума {self.max_val}")

        old = obj.__dict__.get(self._private, "—не задано—")
        print(f"[SET]  '{self._name}': {old!r} → {value!r}")
        obj.__dict__[self._private] = value

    # ── DELETE ───────────────────────────────────────────
    def __delete__(self, obj):
        raise AttributeError(f"Атрибут '{self._name}' удалять запрещено")


# ── Пример использования ─────────────────────────────────
class Employee:
    name   = ValidatedField(str)
    age    = ValidatedField(int, min_val=18, max_val=65)
    salary = ValidatedField(float, min_val=0.0)


emp = Employee()
emp.name   = "Иван"
emp.age    = 30
emp.salary = 75_000.0

print(emp.name)
print(emp.age)
print(emp.salary)

# Тест ошибок
print("\n--- Тест ошибок ---")

try:
    emp.age = "тридцать"
except TypeError as e:
    print(e)

try:
    emp.age = 70
except ValueError as e:
    print(e)

try:
    emp.salary = -500.0
except ValueError as e:
    print(e)

try:
    del emp.name
except AttributeError as e:
    print(e)

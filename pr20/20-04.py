# Практическая работа 20 – Задача 4
# Приватное хранение: значение в __dict__ экземпляра

class PrivateStorage:
    def __set_name__(self, owner, name):
        self._name = f"_{name}"   # приватный ключ, уникальный для атрибута

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self._name, None)

    def __set__(self, obj, value):
        obj.__dict__[self._name] = value


class Person:
    name = PrivateStorage()
    age  = PrivateStorage()


p1 = Person()
p2 = Person()

p1.name = "Алиса"
p1.age  = 30
p2.name = "Боб"
p2.age  = 25

print(p1.name, p1.age)   # Алиса 30
print(p2.name, p2.age)   # Боб 25
print(p1.__dict__)        # {'_name': 'Алиса', '_age': 30}

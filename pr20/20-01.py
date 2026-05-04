# Практическая работа 20 – Задача 1
# Простой дескриптор: хранит и возвращает значение

class SimpleDescriptor:
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self._value

    def __set__(self, obj, value):
        self._value = value


class MyClass:
    attr = SimpleDescriptor()


obj = MyClass()
obj.attr = 42
print(obj.attr)   # 42

obj.attr = "hello"
print(obj.attr)   # hello

# Практическая работа 20 – Задача 2
# Дескриптор с логированием при получении значения

class LoggedGet:
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        print("Getting value")
        return self._value

    def __set__(self, obj, value):
        self._value = value


class MyClass:
    attr = LoggedGet()


obj = MyClass()
obj.attr = 100
x = obj.attr   # выведет: Getting value
print(x)       # 100

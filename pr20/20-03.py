# Практическая работа 20 – Задача 3
# Дескриптор с логированием при установке значения

class LoggedSet:
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self._value

    def __set__(self, obj, value):
        print("Setting value")
        self._value = value


class MyClass:
    attr = LoggedSet()


obj = MyClass()
obj.attr = 55    # выведет: Setting value
obj.attr = 99    # выведет: Setting value
print(obj.attr)  # 99

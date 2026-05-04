# Практическая работа 20 – Задача 8
# Значение по умолчанию: возвращает 'default', если не задано

class WithDefault:
    def __init__(self, default="default"):
        self.default = default

    def __set_name__(self, owner, name):
        self._name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self._name, self.default)

    def __set__(self, obj, value):
        obj.__dict__[self._name] = value


class Settings:
    theme    = WithDefault("default")
    language = WithDefault("ru")


s = Settings()
print(s.theme)     # default
print(s.language)  # ru

s.theme = "dark"
print(s.theme)     # dark

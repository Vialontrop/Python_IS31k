class Calculator:
    def __init__(self, value=0):
        self.value = value

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def create_zero(cls):
        return cls(0)

    def square(self, x):
        f = lambda x: x * x
        return f(x)

c = Calculator.create_zero()
print(c.square(5))
print(Calculator.add(2, 3))
class Multiplier:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return Multiplier(self.value * other.value)

    def get_value(self):
        return self.value


a = Multiplier(4)
b = Multiplier(5)
c = a * b
print(c.get_value())

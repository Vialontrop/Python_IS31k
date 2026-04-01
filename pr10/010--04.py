class Divider:
    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        return Divider(self.value / other.value)

    def get_value(self):
        return self.value


a = Divider(20)
b = Divider(4)
c = a / b
print(c.get_value())

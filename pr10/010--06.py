class EqualNumber:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def get_value(self):
        return self.value


a = EqualNumber(5)
b = EqualNumber(5)
c = EqualNumber(3)
print(a == b)
print(a == c)

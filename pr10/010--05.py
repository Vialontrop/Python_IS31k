class ComparableNumber:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def get_value(self):
        return self.value


a = ComparableNumber(5)
b = ComparableNumber(10)
print(a < b)
print(b < a)

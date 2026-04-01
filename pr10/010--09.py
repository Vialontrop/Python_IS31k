class Counter:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other
        return self

    def get_value(self):
        return self.value


c = Counter(5)
c += 3
print(c.get_value())

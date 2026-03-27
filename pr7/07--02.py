class PositiveNumber:
    def __init__(self):
        self._number = 0

    def set_number(self, n):
        if n > 0:
            self._number = n

    def get_number(self):
        return self._number

pn = PositiveNumber()
pn.set_number(10)
print(pn.get_number())
pn.set_number(-5)
print(pn.get_number())

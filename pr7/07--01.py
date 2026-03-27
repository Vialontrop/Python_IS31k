class SecretNumber:
    def __init__(self):
        self._number = 0

    def set_number(self, n):
        self._number = n

    def get_number(self):
        return self._number

sn = SecretNumber()
sn.set_number(42)
print(sn.get_number())

class Temperature:
    def __init__(self):
        self._celsius = 0

    def set_celsius(self, c):
        self._celsius = c

    def get_celsius(self):
        return self._celsius

    def get_fahrenheit(self):
        return self._celsius * 9 / 5 + 32

temp = Temperature()
temp.set_celsius(0)
print(temp.get_celsius())
print(temp.get_fahrenheit())

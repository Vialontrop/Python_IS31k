# Практическая работа 21 – Задача 16
# Temperature со слотами и конвертацией °C → °F

class Temperature:
    __slots__ = ('value',)

    def __init__(self, value):
        self.value = value   # температура в Цельсиях

    def to_fahrenheit(self):
        return self.value * 9 / 5 + 32

    def to_kelvin(self):
        return self.value + 273.15

    def __str__(self):
        return f"{self.value}°C"


temps = [Temperature(0), Temperature(100), Temperature(-40), Temperature(37)]

for t in temps:
    print(f"{t} = {t.to_fahrenheit():.2f}°F = {t.to_kelvin():.2f} K")

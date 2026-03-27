class NumberDivider:
    def __init__(self):
        self.divisible_numbers = []
        self.not_divisible_numbers = []

    def add_number(self, number):
        if number % 3 == 0:
            self.divisible_numbers.append(number)
        else:
            self.not_divisible_numbers.append(number)

    def divisible(self):
        return self.divisible_numbers

    def not_divisible(self):
        return self.not_divisible_numbers
nd = NumberDivider()
nd.add_number(3)
nd.add_number(4)
nd.add_number(6)
nd.add_number(7)
print("Кратные 3:", nd.divisible())
print("Не кратные 3:", nd.not_divisible())
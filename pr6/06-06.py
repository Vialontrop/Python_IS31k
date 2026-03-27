class MinMaxNumberFinder:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def min_numbers(self):
        minimum = min(self.numbers)
        result = []

        for number in self.numbers:
            if number == minimum:
                result.append(number)

        return result

    def max_numbers(self):
        minimum = min(self.numbers)
        result = []

        for number in self.numbers:
            if number != minimum and number not in result:
                result.append(number)

        result.sort()
        return result
finder = MinMaxNumberFinder()
finder.add_number(5)
finder.add_number(1)
finder.add_number(9)
finder.add_number(1)
finder.add_number(7)
print("Минимальные:", finder.min_numbers())
print("Максимальные:", finder.max_numbers())
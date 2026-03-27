class EvenOddSumTracker:
    def __init__(self):
        self.even_total = 0
        self.odd_total = 0

    def add_number(self, number):
        if number % 2 == 0:
            self.even_total += number
        else:
            self.odd_total += number

    def even_sum(self):
        return self.even_total

    def odd_sum(self):
        return self.odd_total
tracker = EvenOddSumTracker()
tracker.add_number(2)
tracker.add_number(3)
tracker.add_number(4)
tracker.add_number(5)
print("Сумма чётных:", tracker.even_sum())
print("Сумма нечётных:", tracker.odd_sum())
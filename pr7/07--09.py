class LimitedCounter:
    def __init__(self, limit):
        self._value = 0
        self._limit = limit

    def increment(self):
        if self._value < self._limit:
            self._value += 1

    def decrement(self):
        if self._value > 0:
            self._value -= 1

    def get_value(self):
        return self._value

counter = LimitedCounter(3)
counter.increment()
counter.increment()
counter.increment()
counter.increment()
print(counter.get_value())
counter.decrement()
print(counter.get_value())

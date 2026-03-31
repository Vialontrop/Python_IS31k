from abc import ABC, abstractmethod


class NumberProcessor(ABC):
    @abstractmethod
    def process(self, number):
        pass


class SquareProcessor(NumberProcessor):
    def process(self, number):
        return number ** 2


class DoubleProcessor(NumberProcessor):
    def process(self, number):
        return number * 2


processors = [SquareProcessor(), DoubleProcessor()]
for p in processors:
    print(p.process(5))

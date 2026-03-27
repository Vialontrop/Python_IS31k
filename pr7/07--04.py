class StepCounter:
    def __init__(self):
        self._steps = 0

    def walk(self, steps):
        self._steps += steps

    def reset(self):
        self._steps = 0

    def get_steps(self):
        return self._steps

counter = StepCounter()
counter.walk(5)
counter.walk(3)
print(counter.get_steps())
counter.reset()
print(counter.get_steps())

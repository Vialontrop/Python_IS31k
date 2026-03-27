class AlternatingCounter:
    def __init__(self):
        self.first = 0
        self.second = 0
        self.first_turn = True

    def count(self):
        if self.first_turn:
            self.first += 1
        else:
            self.second += 1

        self.first_turn = not self.first_turn
        return self.first, self.second

    def reset(self):
        self.first = 0
        self.second = 0
        self.first_turn = True
ac = AlternatingCounter()
print(ac.count())
print(ac.count())
print(ac.count())
ac.reset()
print("После сброса:", ac.count())
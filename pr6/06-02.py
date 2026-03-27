class CounterButton:
    def __init__(self):
        self.presses = 0

    def press(self):
        self.presses += 1

    def count(self):
        return self.presses

    def reset(self):
        self.presses = 0
btn = CounterButton()
btn.press()
btn.press()
print("Нажатий:", btn.count())
btn.reset()
print("После сброса:", btn.count())
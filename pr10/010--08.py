class BooleanWrapper:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return self.value


b = BooleanWrapper(True)
print(not b)
c = BooleanWrapper(False)
print(not c)

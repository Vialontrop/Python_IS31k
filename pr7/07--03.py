class UserName:
    def __init__(self):
        self._name = ""

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name.upper()

user = UserName()
user.set_name('alex')
print(user.get_name())

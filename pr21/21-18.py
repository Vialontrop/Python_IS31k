# Практическая работа 21 – Задача 18
# Message со слотами и форматированным выводом

class Message:
    __slots__ = ('text', 'author')

    def __init__(self, author, text):
        self.author = author
        self.text   = text

    def format(self):
        return f"{self.author}: {self.text}"

    def __str__(self):
        return self.format()


messages = [
    Message("Алиса", "Привет!"),
    Message("Боб",   "Как дела?"),
    Message("Алиса", "Всё отлично, спасибо!"),
]

for m in messages:
    print(m)

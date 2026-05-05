# Практическая работа 21 – Задача 5
# Book со слотами и методом info()

class Book:
    __slots__ = ('title', 'author')

    def __init__(self, title, author):
        self.title  = title
        self.author = author

    def info(self):
        print(f"«{self.title}» — {self.author}")


b1 = Book("Мастер и Маргарита", "Булгаков")
b2 = Book("1984", "Оруэлл")

b1.info()
b2.info()
